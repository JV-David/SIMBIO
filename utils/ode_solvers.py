from scipy.integrate import solve_ivp
from models import get_model_class

def solve_ode(model_name, params, t_span, method='RK45'):
    try:
        model_class = get_model_class(model_name)
        if model_class is None:
            raise ValueError(f"Modelo {model_name} não encontrado")
        
        if params is None:
            params = model_class.get_parameters()
        
        y0 = model_class.get_initial_conditions(params)
        args = model_class.get_arguments(params)
        
        if model_name == "Reação-Difusão":
            method = 'LSODA'
        
        solution = solve_ivp(
            lambda t, y: model_class.equations(t, y, *args),
            t_span,
            y0,
            method=method,
            dense_output=True
        )
        
        return solution
        
    except Exception as e:
        # Retorna um objeto simulado com falha
        from types import SimpleNamespace
        return SimpleNamespace(
            success=False,
            message=str(e),
            sol=None
        )