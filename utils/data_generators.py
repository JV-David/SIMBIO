import numpy as np
from utils.ode_solvers import solve_ode

def generate_synthetic_data(model_name, params, t_span, noise_level=0.05):
    t_eval = np.linspace(t_span[0], t_span[1], 20)
    solution = solve_ode(model_name, params, t_span)
    
    if solution.success:
        y_clean = solution.sol(t_eval)
        noise = np.random.normal(0, noise_level * np.max(y_clean), y_clean.shape)
        return t_eval, y_clean + noise
    
    return None, None