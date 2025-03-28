# your code here
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def main():
    st.title('Bienvenido al portal predictivo de la empresa XYZ')
    st.write('**Por favor seleccione el servicio predictivo que desea utilizar**')
    
    opcion = st.radio('Seleccione el servicio:', 
                      ('Predicción del tipo de flor (con CSV)','Predicción de imagen'), 
                      index=0, 
                      key='option')
    
    if st.button('Empezar!'):
        route_prediction(opcion)

def route_prediction(opcion):
    if opcion == 'Predicción del tipo de flor (con CSV)':
        switch_page("pred_iris_csv")
    elif opcion == 'Predicción de imagen':
        switch_page("pred_imagen")

if __name__ == "__main__":
    main()

# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2