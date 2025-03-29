# your code here
import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Predicción de Juegos", page_icon="🎲", layout="centered")
    
    with st.sidebar:
        selected = option_menu("Menú", ["Inicio", "Predicción Juego 1", "Predicción Juego 2"], 
                               icons=["house", "dice-1", "dice-2"], menu_icon="cast", default_index=0)
    
    if selected == "Inicio":
        show_home()
    elif selected == "Predicción Juego 1":
        show_prediction_game1()
    elif selected == "Predicción Juego 2":
        show_prediction_game2()

def show_home():
    st.title("🎲 App de Predicción de Juegos")
    st.write("Bienvenido a la app de predicción. Puedes elegir entre dos tipos de juegos y ver su predicción.")
    st.write("Selecciona la opción en el menú lateral para comenzar.")

def show_prediction_game1():
    st.title("🔮 Predicción Juego 1")
    st.write("Aquí puedes predecir el resultado del Juego 1.")
    user_input = st.number_input("Introduce un número:", min_value=1, max_value=100)
    if st.button("Predecir"):
        prediction = user_input * 2  # Ejemplo de predicción simple
        st.success(f"La predicción para el número {user_input} es {prediction}")

def show_prediction_game2():
    st.title("🎰 Predicción Juego 2")
    st.write("Aquí puedes predecir el resultado del Juego 2.")
    user_input = st.slider("Selecciona un número:", 1, 50, 25)
    if st.button("Predecir"):
        prediction = user_input + 10  # Ejemplo de predicción simple
        st.success(f"La predicción para el número {user_input} es {prediction}")

if __name__ == "__main__":
    main()


# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2