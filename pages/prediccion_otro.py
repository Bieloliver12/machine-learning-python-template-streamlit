import streamlit as st

st.set_page_config(page_title="Predicción de Otro Juego", page_icon="🎯")

st.title("🎯 Predicción de Otro Juego")
st.write("Introduce algunos datos para hacer la predicción:")

# Otro tipo de entrada
palabra = st.text_input("Escribe una palabra mágica:")

if st.button("Predecir"):
    st.write(f"La predicción para {palabra} es... ¡{palabra[::-1]}! (Ejemplo)")
