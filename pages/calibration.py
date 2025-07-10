import streamlit as st
from utils.parameter_calibration import ParameterCalibrator

def show():
    st.subheader("Calibração de Parâmetros")
    
    if 'dados_calibracao' not in st.session_state:
        st.warning("Carregue dados experimentais primeiro")
        return
    
    calibrator = ParameterCalibrator(
        st.session_state.modelo_selecionado,
        st.session_state.t_calibracao,
        st.session_state.dados_calibracao
    )
    
    if st.button("🎯 Calibrar Parâmetros"):
        with st.spinner("Otimizando..."):
            result = calibrator.calibrate()
            if result.success:
                st.success("Calibração concluída!")
                st.json(result.params_optimized)