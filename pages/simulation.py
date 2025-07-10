import streamlit as st
import numpy as np
from utils.ode_solvers import solve_ode
from components.plots import plot_results, plot_reaction_diffusion
from components.metrics import show_metrics
from components.data_handlers import export_data

def show():
    st.subheader("Simulação Principal")
    
    if st.button("🚀 Executar Simulação", type="primary"):
        with st.spinner("Calculando..."):
            try:
                # Verificar se os parâmetros foram carregados
                if 'params' not in st.session_state:
                    st.session_state.params = None
                
                t_span = (0, st.session_state.t_final)
                t_eval = np.linspace(0, st.session_state.t_final, st.session_state.n_pontos)
                
                solution = solve_ode(
                    st.session_state.modelo_selecionado,
                    st.session_state.params,
                    t_span,
                    st.session_state.metodo
                )
                
                if solution.success:
                    st.success("✅ Simulação concluída com sucesso!")
                    show_metrics(solution, t_eval)
                    
                    if st.session_state.modelo_selecionado == "Reação-Difusão":
                        fig = plot_reaction_diffusion(
                            solution, 
                            t_eval, 
                            st.session_state.params['n_points']
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        plot_results(solution, t_eval)
                    
                    export_data(solution, t_eval)
                else:
                    st.error(f"❌ Falha na simulação: {solution.message}")
                    
            except Exception as e:
                st.error(f"❌ Erro durante a simulação: {str(e)}")
                st.error("Verifique os parâmetros na barra lateral e tente novamente")