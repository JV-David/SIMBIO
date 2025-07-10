import pandas as pd
from datetime import datetime

def prepare_export_data(solution, t_eval, model_name):
    y_eval = solution.sol(t_eval)
    
    if model_name == "SIR":
        return pd.DataFrame({
            'Tempo': t_eval,
            'Suscetíveis': y_eval[0],
            'Infectados': y_eval[1],
            'Recuperados': y_eval[2]
        })
    elif model_name == "Lotka-Volterra":
        return pd.DataFrame({
            'Tempo': t_eval,
            'Presas': y_eval[0],
            'Predadores': y_eval[1]
        })
    else:
        return pd.DataFrame({
            'Tempo': t_eval,
            'Variável_1': y_eval[0],
            'Variável_2': y_eval[1] if len(y_eval) > 1 else None
        })