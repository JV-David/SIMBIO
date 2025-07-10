import streamlit as st
import time
from utils.ode_solvers import solve_ode

def show():
    st.subheader("Comparação de Métodos Numéricos")
    
    methods = ["RK45", "RK23", "DOP853", "Radau", "BDF"]
    selected = st.multiselect("Métodos para comparar", methods, default=["RK45", "RK23"])
    
    if st.button("Comparar Métodos"):
        results = []
        
        for method in selected:
            start_time = time.time()
            solution = solve_ode(
                st.session_state.modelo_selecionado,
                st.session_state.params,
                (0, st.session_state.t_final),
                method
            )
            exec_time = time.time() - start_time
            results.append({
                "method": method,
                "time": exec_time,
                "success": solution.success,
                "message": solution.message
            })
        
        st.dataframe(results)