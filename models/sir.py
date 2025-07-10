from .base_model import BaseModel

class SIRModel(BaseModel):
    @staticmethod
    def equations(t, y, beta, gamma):
        S, I, R = y
        N = S + I + R
        return [
            -beta * S * I / N,  # dS/dt
            beta * S * I / N - gamma * I,  # dI/dt
            gamma * I  # dR/dt
        ]
    
    @classmethod
    def get_parameters(cls):
        return {
            'beta': 0.3,
            'gamma': 0.1,
            'S0': 999,
            'I0': 1,
            'R0': 0
        }
    
    @classmethod
    def get_initial_conditions(cls, params=None):
        if params is None:
            params = cls.get_parameters()
        return [params['S0'], params['I0'], params['R0']]
    
    @classmethod
    def get_arguments(cls, params):
        return (params['beta'], params['gamma'])
    
    @classmethod
    def get_info(cls):
        return {
            'name': '🦠 Modelo SIR',
            'description': 'Modelo epidemiológico para doenças infecciosas',
            'equations': [
                'dS/dt = -βSI/N',
                'dI/dt = βSI/N - γI',
                'dR/dt = γI'
            ],
            'parameters': {
                'beta': 'Taxa de transmissão',
                'gamma': 'Taxa de recuperação',
                'S0': 'População suscetível inicial',
                'I0': 'População infectada inicial',
                'R0': 'População recuperada inicial'
            }
        }