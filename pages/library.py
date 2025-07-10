import streamlit as st
from models import get_model_classes, get_model_info

def show():
    st.subheader("📚 Biblioteca de Modelos")
    
    model_classes = get_model_classes()
    
    for model_name in model_classes.keys():
        info = get_model_info(model_name)
        
        if info is None:
            st.warning(f"Informações não disponíveis para o modelo {model_name}")
            continue
            
        with st.expander(f"{info.get('name', model_name)}"):
            st.markdown(f"**Descrição:** {info.get('description', 'Sem descrição disponível')}")
            
            if 'equations' in info:
                st.markdown("**Equações:**")
                for eq in info['equations']:
                    st.code(eq, language='mathematica')
            
            if 'parameters' in info:
                st.markdown("**Parâmetros:**")
                for param, desc in info['parameters'].items():
                    st.markdown(f"- `{param}`: {desc}")