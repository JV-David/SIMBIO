import streamlit as st
from models import get_model_classes

def show_sidebar():

    st.markdown("""
    <style>
        .st-emotion-cache-79elbk.edtmxes1 {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.title("⚙️ Configurações do Modelo")
    
    # Seleção do modelo
    model_classes = get_model_classes()
    modelo_selecionado = st.sidebar.selectbox(
        "Escolha o modelo matemático:",
        list(model_classes.keys()),
        key='modelo_selecionado'
    )
    
    # Parâmetros temporais
    st.sidebar.subheader("Parâmetros de Simulação")
    t_final = st.sidebar.slider("Tempo final", 1.0, 100.0, 20.0, 0.5)
    n_pontos = st.sidebar.slider("Número de pontos", 100, 2000, 500, 50)
    
    # Método numérico
    metodo = st.sidebar.selectbox(
        "Método numérico:",
        ["RK45", "RK23", "DOP853", "Radau", "BDF", "LSODA"]
    )
    
    # Configuração de parâmetros específicos do modelo
    st.sidebar.subheader(f"Parâmetros do Modelo {modelo_selecionado}")
    ModelClass = model_classes[modelo_selecionado]
    params = ModelClass.get_parameters()
    
    # Atualizar parâmetros com widgets
    for param_name, param_value in params.items():
        if isinstance(param_value, (int, float)):
            # Garantir que o valor padrão seja float
            default_value = float(param_value)
            
            # Definir limites mínimos e máximos
            min_val = default_value * 0.1  # 10% do valor padrão
            max_val = default_value * 2.0  # 200% do valor padrão
            
            # Garantir que min_val < max_val
            if min_val >= max_val:
                max_val = min_val + 1.0
            
            # Calcular step de forma segura
            step = (max_val - min_val) / 100.0
            step = max(step, 0.001)  # Garantir um step mínimo
            
            params[param_name] = st.sidebar.slider(
                param_name,
                min_value=min_val,
                max_value=max_val,
                value=default_value,
                step=step
            )
        elif isinstance(param_value, list):
            params[param_name] = st.sidebar.selectbox(param_name, param_value)
        elif isinstance(param_value, str):
            params[param_name] = st.sidebar.text_input(param_name, param_value)
        else:
            params[param_name] = param_value
    
    # Atualizar parâmetros na sessão
    st.session_state.params = params
    st.session_state.t_final = t_final
    st.session_state.n_pontos = n_pontos
    st.session_state.metodo = metodo