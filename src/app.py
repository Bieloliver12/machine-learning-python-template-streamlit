# your code here
import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Predicción de Juegos")

# esto es para ver la barra lateral y como navegar
    with st.sidebar:
        selected = option_menu(
            "Menú", 
            ["Inicio", "Predicción Ruleta", "Predicción Otro Juego"], 
            icons=["house", "casino", "gamepad"], 
            menu_icon="menu-app", 
            default_index=0
        )

   
    page_placeholder = st.empty()

   #aqui definimos las acciones que tiene que hacer segun se escoga el apartartado
    if selected == "Inicio":
        with page_placeholder.container():
            show_home()
    elif selected == "Predicción Ruleta":
        with page_placeholder.container():
            show_prediction_roulette()
    elif selected == "Predicción Otro Juego":
        with page_placeholder.container():
            show_prediction_game2()

def show_home():
    st.title("App de Predicción de Juegos")
    st.write("Bienvenido a la app de predicción. Puedes elegir entre dos tipos de juegos y ver su predicción.")
    st.write("Selecciona la opción en el menú lateral para comenzar.")

def show_prediction_roulette():
    st.title("Predicción Ruleta")
    st.write("Introduce los colores que han salido en la ruleta (Negro o Rojo)")

    colores = st.text_area("Escribe los colores que han salido separados por comas ejemplo: rojo, negro, rojo, rojo, negro")

    if colores:
        from collections import Counter

        lista_colores = [c.strip().lower() for c in colores.split(",") if c.strip().lower() in ["rojo", "negro"]]
        
        if lista_colores:
            contador = Counter(lista_colores)
            total_tiradas = sum(contador.values())

            prob_rojo = (contador["rojo"] / total_tiradas) * 100 if "rojo" in contador else 0
            prob_negro = (contador["negro"] / total_tiradas) * 100 if "negro" in contador else 0

            st.write(f"**Probabilidad de que salga Rojo:** {prob_rojo:.2f}%")
            st.write(f"**Probabilidad de que salga Negro:** {prob_negro:.2f}%")

            prediccion = "Rojo" if prob_rojo > prob_negro else "Negro"
            st.subheader(f"Es más probable que salga **{prediccion}** en la siguiente tirada.")
        else:
            st.warning("Introduce al menos un color válido (rojo o negro).")

def show_prediction_game2():
    st.title("Predicción Otro Juego")
    st.write("Aquí puedes predecir el resultado de otro juego.")

    user_input = st.slider("Selecciona un número:", 1, 50, 25)
    if st.button("Predecir"):
        prediction = user_input + 10  
        st.success(f"La predicción para el número {user_input} es {prediction}")

if __name__ == "__main__":
    main()


# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2