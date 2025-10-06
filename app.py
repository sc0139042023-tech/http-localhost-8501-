import streamlit as st
import requests

st.title("Situación climática")
st.write("Escriba el departamento:")

# Entrada principal
departamento = st.text_input("Departamento")

API_KEY = "2dd69aa6409c97ff65127af01a603d9a"

with st.sidebar:
    st.header("Opciones")
    departamento_sidebar = st.text_input("Departamento (opcional)")
    ver_clima_sidebar = st.button("Ver clima (desde sidebar)")

# Botón principal
if st.button("Ver clima") or (ver_clima_sidebar and departamento_sidebar):
    # Priorizar la entrada del sidebar si está llena
    lugar = departamento_sidebar if departamento_sidebar else departamento
    
    if lugar:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={lugar},SV&appid={API_KEY}&units=metric&lang=es"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            info = {
                "País": data["sys"]["country"],
                "Ciudad": data["name"],
                "Temperatura": f"{data['main']['temp']}°C",
                "Humedad": f"{data['main']['humidity']}%",
                "Descripción": data["weather"][0]["description"].capitalize(),
                "Viento": f"{data['wind']['speed']} km/h"
            }

            st.success(f"🌍 {info['Ciudad']}, {info['País']}")
            st.info(f"🌡️ Temperatura: {info['Temperatura']}")
            st.info(f"💧 Humedad: {info['Humedad']}")
            st.info(f"🌤️ {info['Descripción']}")
            st.info(f"💨 Viento: {info['Viento']}")
        else:
            st.error("❌ No se encontró la ciudad o el nombre está mal escrito.")
    else:
        st.warning("Por favor, escriba un departamento.")
