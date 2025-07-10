from scipy.optimize import minimize
from utils.ode_solvers import solve_ode
import streamlit as st
import numpy as np

class ParameterCalibrator:
    def __init__(self, model_name, t_exp, y_exp):
        self.model_name = model_name
        self.t_exp = t_exp
        self.y_exp = y_exp
    
    def objective_function(self, params):
        solution = solve_ode(self.model_name, params, (self.t_exp[0], self.t_exp[-1]))
        if solution.success:
            y_pred = solution.sol(self.t_exp)
            return np.mean((y_pred - self.y_exp)**2)
        return float('inf')
    
    def calibrate(self):
        initial_params = st.session_state.params
        bounds = [(p*0.5, p*1.5) for p in initial_params.values()]
        
        result = minimize(
            self.objective_function,
            initial_params,
            bounds=bounds,
            method='L-BFGS-B'
        )
        
        return type('Result', (), {
            'success': result.success,
            'params_optimized': result.x,
            'message': result.message
        })