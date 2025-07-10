import streamlit as st
import pandas as pd
from datetime import datetime
from utils.helpers import prepare_export_data

def export_data(solution, t_eval):
    df = prepare_export_data(solution, t_eval, st.session_state.modelo_selecionado)
    
    csv = df.to_csv(index=False)
    st.download_button(
        label="Exportar CSV",
        data=csv,
        file_name=f"simbio_{st.session_state.modelo_selecionado}_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )