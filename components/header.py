import streamlit as st

def show_header():
    st.markdown("""
    <div class="main-header">
        <h1>🧬 SIMBIO - Simulador de Dinâmica de Sistemas Biológicos</h1>
        <p>Modelagem Matemática Computacional com Equações Diferenciais</p>
    </div>
    """, unsafe_allow_html=True)