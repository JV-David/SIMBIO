import streamlit as st
import numpy as np
from utils.ode_solvers import solve_ode
from components.plots import plot_sensitivity_results

def show():
    st.subheader("Análise de Sensibilidade")
    
    if 'params' not in st.session_state:
        st.warning("Execute uma simulação principal primeiro")
        return
    
    model_params = st.session_state.params
    param = st.selectbox("Parâmetro para análise", list(model_params.keys()))
    
    col1, col2 = st.columns(2)
    with col1:
        min_val = st.number_input("Valor mínimo", value=float(model_params[param])*0.5)
    with col2:
        max_val = st.number_input("Valor máximo", value=float(model_params[param])*1.5)
    
    steps = st.slider("Número de variações", 2, 10, 3)
    
    if st.button("Analisar Sensibilidade"):
        values = np.linspace(min_val, max_val, steps)
        results = []
        
        for val in values:
            params = st.session_state.params.copy()
            params[param] = val
            
            solution = solve_ode(
                st.session_state.modelo_selecionado,
                params,
                (0, st.session_state.t_final),
                st.session_state.metodo
            )
            
            if solution and solution.success:
                results.append({
                    'value': val,
                    'solution': solution,
                    'success': True
                })
            else:
                results.append({
                    'value': val,
                    'success': False,
                    'message': solution.message if solution else "Erro desconhecido"
                })
        
        plot_sensitivity_results(results, param, st.session_state.t_final)