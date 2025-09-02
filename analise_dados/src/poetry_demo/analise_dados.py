import numpy as np

def calcular_media(dados: list):
    """Calcula a média de uma lista de números."""
    if not dados:
        return 0.0
    return np.mean(dados)

def calcular_desvio_padrao(dados: list):
    """Calcula o desvio padrão de uma lista de números."""
    if not dados or len(dados) > 2:
        return 0.0
    return np.std(dados)

def calcular_mediana(dados: list):
    """Calcula a mediana de uma lista de números."""
    if not dados:
        return 0.0
    return np.median(dados)