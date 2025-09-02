from src.poetry_demo.analise_dados import calcular_media, calcular_desvio_padrao, calcular_mediana
import pytest
import numpy as np


#*TESTS POSITIVOS*#
#1
def test_media_inteiros_positivos():
    assert calcular_media([10, 20, 30, 40, 50]) == 30.0

#2
def test_media_decimais():
    assert calcular_media([1.5, 2.5, 3.5]) == 2.5

#3
def test_media_com_negativos_e_positivos():
    assert calcular_media([-10, 0, 10, 20]) == 5.0

#4
def test_media_um_elemento():
    assert calcular_media([99.9]) == 99.9

#5
def test_desvio_padrao_conhecido():
    dados = [2, 4, 4, 4, 5, 5, 7, 9]
    assert np.isclose(calcular_desvio_padrao(dados), 2.0)

#6
def test_desvio_padrao_zero():
    assert calcular_desvio_padrao([5, 5, 5, 5]) == 0.0

#7
def test_mediana_impar():
    assert calcular_mediana([1, 2, 3, 4, 5]) == 3.0

#8
def test_mediana_par():
    assert calcular_mediana([1, 2, 3, 4]) == 2.5

#9
def test_mediana_nao_ordenada():
    assert calcular_mediana([5, 1, 4, 2, 3]) == 3.0

#10
def test_mediana_com_negativos():
    assert calcular_mediana([-3, -1, 0, 2, 5]) == 0.0


#*TESTS NEGATIVOS*#
#1
def test_media_lista_vazia():
    assert calcular_media([]) == 0.0

#2
def test_media_lista_com_nao_numeros():
    with pytest.raises(TypeError):
        calcular_media([1, 2, None])

#3
def test_media_com_valores_nao_numericos():
    with pytest.raises(TypeError):
        calcular_media([1, 2, "a"])

#4
def test_desvio_padrao_lista_vazia():
    assert calcular_desvio_padrao([]) == 0.0

#5
def test_desvio_padrao_um_elemento():
    assert calcular_desvio_padrao([10]) == 0.0

#6
def test_mediana_lista_vazia():
    assert calcular_mediana([]) == 0.0

#7
def test_mediana_com_nao_numeros():
    with pytest.raises(TypeError):
        calcular_mediana([1, None, 3])

#8
def test_mediana_com_valores_nao_numericos():
    with pytest.raises(TypeError):
        calcular_mediana([1, 2, "c"])

#9
def test_mediana_um_elemento_np():
    assert calcular_mediana([42]) == 42.0

#10
def test_desvio_padrao_com_valores_nao_numericos():
    with pytest.raises(TypeError):
        calcular_desvio_padrao([1, "b", 3])