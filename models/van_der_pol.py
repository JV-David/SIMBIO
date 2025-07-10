from .base_model import BaseModel

class VanDerPolModel(BaseModel):
    @staticmethod
    def equations(t, y, mu):
        x, dx = y
        return [
            dx,
            mu * (1 - x**2) * dx - x
        ]
    
    @classmethod
    def get_parameters(cls):
        return {
            'mu': 1.0,
            'x0': 2.0,
            'dx0': 0.0
        }
    
    @classmethod
    def get_info(cls):
        return {
            'name': '🌊 Van der Pol',
            'equations': [
                'd²x/dt² - μ(1-x²)dx/dt + x = 0'
            ],
            'description': 'Oscilador não-linear'
        }