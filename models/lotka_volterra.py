from .base_model import BaseModel

class LotkaVolterraModel(BaseModel):
    @staticmethod
    def equations(t, y, alpha, beta, delta, gamma):
        x, y_pred = y
        return [
            alpha * x - beta * x * y_pred,
            delta * x * y_pred - gamma * y_pred
        ]
    
    @classmethod
    def get_parameters(cls):
        return {
            'alpha': 1.1,
            'beta': 0.4,
            'delta': 0.1,
            'gamma': 0.4,
            'x0': 10,
            'y0': 5
        }
    
    @classmethod
    def get_info(cls):
        return {
            'name': '🐺🐰 Lotka-Volterra',
            'equations': [
                'dx/dt = αx - βxy',
                'dy/dt = δxy - γy'
            ],
            'description': 'Modelo predador-presa'
        }