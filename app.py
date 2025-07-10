import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer
from styles import load_styles
from config import PAGE_CONFIG

def main():
    # Configurações iniciais
    st.set_page_config(**PAGE_CONFIG)
    load_styles()
    show_header()
    
    # Inicialização de variáveis de sessão
    if 'params' not in st.session_state:
        st.session_state.params = {}
    if 'modelo_selecionado' not in st.session_state:
        st.session_state.modelo_selecionado = "SIR"
    if 'historico_simulacoes' not in st.session_state:
        st.session_state.historico_simulacoes = []
    
    # Mostrar sidebar e configurações
    show_sidebar()
    
    # Carregar páginas
    from pages import simulation, sensitivity, comparison, calibration, library
    
    # Layout principal com abas
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🧪 Simulação", 
        "📊 Sensibilidade", 
        "🔄 Comparação", 
        "🎯 Calibração", 
        "📚 Biblioteca"
    ])
    
    with tab1:
        simulation.show()
    with tab2:
        sensitivity.show()
    with tab3:
        comparison.show()
    with tab4:
        calibration.show()
    with tab5:
        library.show()
    
    # Rodapé
    show_footer()

if __name__ == "__main__":
    main()