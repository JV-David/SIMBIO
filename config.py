class Config:
    PAGE_CONFIG = {
        "page_title": "SIMBIO - Simulador de Dinâmica de Sistemas",
        "page_icon": "🧬",
        "layout": "wide"
    }
    
    MODEL_DEFAULTS = {
        "SIR": {
            "beta": 0.3,
            "gamma": 0.1,
            "S0": 999,
            "I0": 1,
            "R0": 0
        },
        "Lotka-Volterra": {
            "alpha": 1.1,
            "beta": 0.4,
            "delta": 0.1,
            "gamma": 0.4,
            "x0": 10,
            "y0": 5
        }
    }