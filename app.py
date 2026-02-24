import streamlit as st
import pycountry
from carta_natal import generar_carta_final # Importamos tu función
from datetime import datetime
import os
import time
from typing import List
from types_config import Fondo

st.set_page_config(page_title="Astrología Artística", page_icon="✨")


FONDOS: List[Fondo] = [
    {"id": "noche_estrellada", "name": "Noche Estrellada", "path": "backgrounds/background.jpg", "color": "white"},
    {"id": "nebulosa", "name": "Nebulosa", "path": "backgrounds/background2.jpg", "color": "white"},
    {"id": "minimal_rosa", "name": "Minimalista rosa", "path": "backgrounds/minimalista-rosa.jpg", "color": "black"},
    {"id": "negro", "name": "Negro", "path": "backgrounds/black.jpg", "color": "white"},
    {"id": "verde", "name": "Verde", "path": "backgrounds/green.jpg", "color": "white"},
    {"id": "azul_estrella", "name": "Azul estrella", "path": "backgrounds/blue-stars.jpg", "color": "white"},
]

def selector_fondos_galeria() -> Fondo:
    st.sidebar.header("🎨 Elige tu Estilo")

   # --- INYECCIÓN DE CSS PARA EL ESTILO ---
    # Esto hará que el botón seleccionado se vea oscuro/destacado
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
        /* Estilo para el botón seleccionado (usando un selector de texto si es posible o simplemente el estado) */
        </style>
    """, unsafe_allow_html=True)
    # Inicializar el estado usando el 'id' del primer fondo
    if 'fondo_id_seleccionado' not in st.session_state:
        st.session_state.fondo_id_seleccionado = FONDOS[0]["id"]

    cols = st.sidebar.columns(2)

    for i, fondo in enumerate(FONDOS):
        with cols[i % 2]:
            if os.path.exists(fondo["path"]):
                st.image(fondo["path"], use_container_width=True)

                es_activo = st.session_state.fondo_id_seleccionado == fondo["id"]
                # Usamos tipo primary para el botón seleccionado
                tipo = "primary" if es_activo else "secondary"
                label = f"◉ {fondo['name']}" if es_activo else f"○ {fondo['name']}"

                if st.button(label, key=f"btn_{fondo['id']}", use_container_width=True, type=tipo):
                    st.session_state.fondo_id_seleccionado = fondo["id"]
                    st.rerun()
            else:
                st.error(f"Falta: {fondo['name']}")

    st.sidebar.markdown("---")

    # Buscamos el objeto completo que coincida con el ID seleccionado
    seleccionado = next(f for f in FONDOS if f["id"] == st.session_state.fondo_id_seleccionado)
    return seleccionado




# --- INTERFAZ ---
st.title("🌙 Generador de Carta Natal")

paises = sorted([p.name for p in pycountry.countries])

with st.sidebar:
    st.header("Datos de Nacimiento")
    nombre = st.text_input("Nombre", "Leo")
    pais = st.selectbox("País", paises, index=paises.index("Argentina"))
    ciudad_txt = st.text_input("Ciudad", "Buenos Aires")

    fecha_minima = datetime(1930, 1, 1)
    fecha_maxima = datetime.now()

    with st.sidebar:
        # ... otros inputs ...

        fecha = st.date_input(
            "Fecha de Nacimiento",
            value=datetime(1994, 9, 19), # Fecha por defecto
            min_value=fecha_minima,
            max_value=fecha_maxima
        )
        # Inputs numéricos para Hora y Minutos
        st.write("Hora de Nacimiento (formato 24hs)")
        col_hr, col_min = st.columns(2)

        with col_hr:
            hora_v = st.number_input("Hora", min_value=0, max_value=23, value=17, step=1)

        with col_min:
            minuto_v = st.number_input("Minutos", min_value=0, max_value=59, value=30, step=1)

    st.markdown("---") # Separador visual
    config_fondo = selector_fondos_galeria()

    btn_generar = st.button("Generar Carta", use_container_width=True, type="primary")

# --- EJECUCIÓN ---
if btn_generar:
    # Combinamos ciudad y país para tu función location
    lugar_completo = f"{ciudad_txt}, {pais}"

    try:
        # Mostramos un mensaje de carga mientras se genera
        with st.spinner("Calculando posiciones planetarias y dibujando..."):
            # Llamamos a tu lógica
            exito = generar_carta_final(
                nombre,
                lugar_completo,
                fecha.year, fecha.month, fecha.day,
                hora_v, minuto_v,
                config_fondo
            )

        if exito:
            # Mostramos la imagen que generó draw_chart_artistic
            # Nota: Asegúrate de que draw_chart_artistic guarde siempre con el mismo nombre
            if os.path.exists("carta_natal.png"):
                st.image("carta_natal.png", caption=f"Carta Natal de {nombre}", width='stretch')

                # Botón de descarga
                with open("carta_natal.png", "rb") as file:
                    st.download_button(
                        label="⬇️ Descargar Imagen",
                        data=file,
                        file_name=f"carta_{nombre}.png",
                        mime="image/png"
                    )
            else:
                st.error("No se encontró el archivo generado.")

    except Exception as e:
        st.error(f"Error al generar la carta: {e}")


