import streamlit as st
import pycountry
from carta_natal import generate_final_chart
from datetime import datetime
import os
import time
from config import Background, BACKGROUNDS

st.set_page_config(page_title="Astrología Artística", page_icon="✨")


def background_gallery_selector() -> Background:
    st.sidebar.header("🎨 Elige tu Estilo")

    st.markdown("""
        <style>
        div.stButton > button:first-child {
            border: 1px solid #444;
            border-radius: 20px;
        }
        div.stButton > button[kind="primary"] {
                    background-color: rgb(124, 75, 255);
                    color: white;
                    border: none;
                    border-radius: 20px;
                    transition: all 0.3s ease;
                }
        </style>
    """, unsafe_allow_html=True)

    if 'selected_background_id' not in st.session_state:
        st.session_state.selected_background_id = BACKGROUNDS[0]["id"]

    cols = st.sidebar.columns(4)

    for i, background in enumerate(BACKGROUNDS):
        with cols[i % 4]:
            if os.path.exists(background["path"]):
                st.image(background["path"], width='stretch')

                is_active = st.session_state.selected_background_id == background["id"]
                btn_type = "primary" if is_active else "secondary"
                label = f"◉ {background['name']}" if is_active else f"○ {background['name']}"

                if st.button(label, key=f"btn_{background['id']}", width='stretch', type=btn_type):
                    st.session_state.selected_background_id = background["id"]
                    st.session_state.custom_line_color = None
                    st.rerun()
            else:
                st.error(f"Falta: {background['name']}")

    st.sidebar.markdown("---")

    selected = next(b for b in BACKGROUNDS if b["id"] == st.session_state.selected_background_id)

    import matplotlib.colors as mcolors
    use_custom_line_color = st.sidebar.checkbox("Personalizar color de líneas", key="chk_custom_line_color")
    if use_custom_line_color:
        raw = selected.get("line_color", selected["color"])
        try:
            default = mcolors.to_hex(raw)
        except ValueError:
            default = "#ffffff"
        if st.session_state.get("custom_line_color") is None:
            st.session_state.custom_line_color = default
        picked = st.sidebar.color_picker("Color de líneas", st.session_state.custom_line_color, key="color_picker_line")
        st.session_state.custom_line_color = picked
        selected = {**selected, "line_color": picked}
    else:
        st.session_state.custom_line_color = None

    return selected

import streamlit as st

def check_password():
    """Devuelve True si el usuario introdujo la contraseña correcta."""

    def password_entered():
        """Comprueba si la contraseña coincide."""
        if st.session_state["password"] == "1234":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Eliminar la contraseña del estado por seguridad
        else:
            st.session_state["password_correct"] = False

    # Si ya se autenticó antes, retornar True
    if st.session_state.get("password_correct", False):
        return True

    # Mostrar formulario de entrada de contraseña
    st.title("🔒 Acceso Restringido")
    st.text_input(
        "Introduce la contraseña para acceder al generador:",
        type="password",
        on_change=password_entered,
        key="password"
    )

    if "password_correct" in st.session_state:
        st.error("😕 Contraseña incorrecta")

    return False




# --- EJECUCIÓN PRINCIPAL ---
if check_password():
    st.success("Acceso concedido")
else:
    st.stop() # Detiene la ejecución del resto de la app


# --- INTERFAZ ---
st.title("🌙 Generador de Carta Natal")

countries = sorted([p.name for p in pycountry.countries])

with st.sidebar:
    st.header("Datos de Nacimiento")
    name = st.text_input("Nombre", "Leo")
    country = st.selectbox("País", countries, index=countries.index("Argentina"))
    city_input = st.text_input("Ciudad", "Buenos Aires")

    min_date = datetime(1930, 1, 1)
    max_date = datetime.now()

    with st.sidebar:
        date = st.date_input(
            "Fecha de Nacimiento",
            value=datetime(1994, 9, 19),
            min_value=min_date,
            max_value=max_date
        )
        st.write("Hora de Nacimiento (formato 24hs)")
        col_hr, col_min = st.columns(2)

        with col_hr:
            hour = st.number_input("Hora", min_value=0, max_value=23, value=17, step=1)

        with col_min:
            minute = st.number_input("Minutos", min_value=0, max_value=59, value=30, step=1)

    language = st.radio("Idioma", ["Español", "English"], horizontal=True)
    paper_size = st.radio("Tamaño", ["A5", "A4", "A3"], index=1, horizontal=True)
    st.markdown("---")
    background_config = background_gallery_selector()

    btn_generate = st.button("Generar Carta", width='stretch', type="primary")

# --- EXECUTION ---
if btn_generate:
    full_location = f"{city_input}, {country}"

    try:
        with st.spinner("Calculando posiciones planetarias y dibujando..."):
            success = generate_final_chart(
                name,
                full_location,
                date.year, date.month, date.day,
                hour, minute,
                background_config,
                language=language,
                paper_size=paper_size,
            )

        if success:
            if os.path.exists("carta_natal.png"):
                st.session_state["chart_name"] = name
                with open("carta_natal.png", "rb") as f:
                    st.session_state["chart_png"] = f.read()
                if os.path.exists("carta_natal_cmyk.pdf"):
                    with open("carta_natal_cmyk.pdf", "rb") as f:
                        st.session_state["chart_pdf"] = f.read()
            else:
                st.error("No se encontró el archivo generado.")

    except Exception as e:
        st.error(f"Error al generar la carta: {e}")

if "chart_png" in st.session_state:
    chart_name = st.session_state["chart_name"]
    st.image(st.session_state["chart_png"], caption=f"Carta Natal de {chart_name}", width='stretch')

    st.download_button(
        label="⬇️ Descargar Imagen (PNG)",
        data=st.session_state["chart_png"],
        file_name=f"carta_{chart_name}.png",
        mime="image/png"
    )

    if "chart_pdf" in st.session_state:
        st.download_button(
            label="🖨️ Descargar para Imprimir (PDF CMYK)",
            data=st.session_state["chart_pdf"],
            file_name=f"carta_{chart_name}_cmyk.pdf",
            mime="application/pdf"
        )


