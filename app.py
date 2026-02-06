import streamlit as st
import pycountry
from carta_natal import generar_carta_final # Importamos tu función
from datetime import datetime
import os
import time

st.set_page_config(page_title="Astrología Artística", page_icon="✨")

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
    btn_generar = st.button("Generar Carta")

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
                hora_v, minuto_v
            )

        if exito:
            # Mostramos la imagen que generó draw_chart_artistic
            # Nota: Asegúrate de que draw_chart_artistic guarde siempre con el mismo nombre
            if os.path.exists("carta_natal.png"):
                st.image("carta_natal.png", caption=f"Carta Natal de {nombre}", use_container_width=True)

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