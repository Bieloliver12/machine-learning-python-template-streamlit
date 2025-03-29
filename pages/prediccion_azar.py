import streamlit as st
from collections import Counter

st.set_page_config(page_title="Predicción Ruleta", page_icon="🎰")

st.title("🎰 Predicción de la Ruleta")
st.write("Introduce los colores que han salido en la ruleta (Negro o Rojo) y veremos cuál es más probable que salga ahora.")

# Input del usuario
colores = st.text_area("Escribe los colores que han salido separados por comas (ejemplo: rojo, negro, rojo, rojo, negro)")

if colores:
    # Convertimos la entrada a lista de colores
    lista_colores = [c.strip().lower() for c in colores.split(",") if c.strip().lower() in ["rojo", "negro"]]
    
    if lista_colores:
        # Contamos la frecuencia de cada color
        contador = Counter(lista_colores)
        total_tiradas = sum(contador.values())
        
        # Calculamos probabilidades
        prob_rojo = (contador["rojo"] / total_tiradas) * 100 if "rojo" in contador else 0
        prob_negro = (contador["negro"] / total_tiradas) * 100 if "negro" in contador else 0

        # Mostramos resultados
        st.write(f"🎯 **Probabilidad de que salga Rojo:** {prob_rojo:.2f}%")
        st.write(f"🎯 **Probabilidad de que salga Negro:** {prob_negro:.2f}%")

        # Predicción basada en la mayor probabilidad
        prediccion = "Rojo" if prob_rojo > prob_negro else "Negro"
        st.subheader(f"📢 Es más probable que salga **{prediccion}** en la siguiente tirada.")
    else:
        st.warning("⚠️ Introduce al menos un color válido (rojo o negro).")
