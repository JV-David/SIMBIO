import streamlit as st
import numpy as np

def show_metrics(solution, t_eval):
    """Exibe métricas da simulação"""
    st.subheader("📊 Métricas da Simulação")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Status", "Sucesso" if solution.success else "Falhou")
    
    with col2:
        st.metric("Tempo Final", f"{st.session_state.t_final:.2f}")
    
    with col3:
        st.metric("Pontos Calculados", st.session_state.n_pontos)
    
    # Métricas específicas por modelo
    if st.session_state.modelo_selecionado == "SIR":
        show_sir_metrics(solution, t_eval)
    elif st.session_state.modelo_selecionado == "Lotka-Volterra":
        show_lotka_volterra_metrics(solution, t_eval)

def show_sir_metrics(solution, t_eval):
    """Métricas específicas para o modelo SIR"""
    y_eval = solution.sol(t_eval)
    beta = st.session_state.params['beta']
    gamma = st.session_state.params['gamma']
    
    col1, col2 = st.columns(2)
    
    with col1:
        R0 = beta / gamma
        st.metric("Número Básico de Reprodução (R₀)", f"{R0:.2f}")
    
    with col2:
        peak_infected = np.max(y_eval[1])
        st.metric("Pico de Infectados", f"{peak_infected:.0f}")

def show_lotka_volterra_metrics(solution, t_eval):
    """Métricas específicas para o modelo Lotka-Volterra"""
    y_eval = solution.sol(t_eval)
    
    col1, col2 = st.columns(2)
    
    with col1:
        avg_prey = np.mean(y_eval[0])
        st.metric("Média de Presas", f"{avg_prey:.2f}")
    
    with col2:
        avg_predator = np.mean(y_eval[1])
        st.metric("Média de Predadores", f"{avg_predator:.2f}")