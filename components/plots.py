import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import numpy as np

def plot_results(solution, t_eval):
    y_eval = solution.sol(t_eval)
    
    fig = go.Figure()
    for i, label in enumerate(['Suscetíveis', 'Infectados', 'Recuperados'][:len(y_eval)]):
        fig.add_trace(go.Scatter(
            x=t_eval, y=y_eval[i],
            name=label,
            mode='lines'
        ))
    
    fig.update_layout(
        title="Resultados da Simulação",
        xaxis_title="Tempo",
        hovermode="x unified"
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_reaction_diffusion(solution, t_eval, n_points):
    """Visualização especializada para o modelo de reação-difusão"""
    y_eval = solution.sol(t_eval)
    n = n_points
    
    # Selecionar tempos específicos para visualização
    time_indices = [0, len(t_eval)//4, len(t_eval)//2, -1]
    x_space = np.linspace(0, 1, n)
    
    fig = make_subplots(rows=2, cols=2, 
                       subplot_titles=[f"t={t_eval[i]:.2f}" for i in time_indices])
    
    for i, idx in enumerate(time_indices):
        row = (i // 2) + 1
        col = (i % 2) + 1
        
        u = y_eval[:n, idx]
        v = y_eval[n:, idx]
        
        fig.add_trace(go.Scatter(
            x=x_space, y=u,
            name=f'u (t={t_eval[idx]:.2f})',
            line=dict(color='blue')
        ), row=row, col=col)
        
        fig.add_trace(go.Scatter(
            x=x_space, y=v,
            name=f'v (t={t_eval[idx]:.2f})',
            line=dict(color='red', dash='dash')
        ), row=row, col=col)
    
    fig.update_layout(
        title="Evolução do Padrão de Reação-Difusão",
        height=600,
        showlegend=False
    )
    
    return fig

def plot_sensitivity_results(results, param_name, t_final):
    """Plota resultados da análise de sensibilidade"""
    t_eval = np.linspace(0, t_final, 100)
    fig = go.Figure()
    
    for result in results:
        if not result['success']:
            continue
            
        y_eval = result['solution'].sol(t_eval)
        # Assumindo que queremos plotar a primeira variável (ajuste conforme necessário)
        fig.add_trace(go.Scatter(
            x=t_eval,
            y=y_eval[0],
            name=f"{param_name}={result['value']:.2f}",
            mode='lines'
        ))
    
    fig.update_layout(
        title=f"Sensibilidade ao parâmetro {param_name}",
        xaxis_title="Tempo",
        yaxis_title="Valor",
        hovermode="x unified"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar erros se houver
    for result in results:
        if not result['success']:
            st.error(f"Falha com {param_name}={result['value']:.2f}: {result['message']}")