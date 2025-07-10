import streamlit as st
from models import get_model_class

def show_model_card(model_name):
    model = get_model_class(model_name)
    info = model.get_info()
    
    with st.expander(f"📚 {info['name']}"):
        st.markdown(f"**Descrição:** {info['description']}")
        st.markdown("**Equações:**")
        for eq in info['equations']:
            st.code(eq, language='mathematica')