import pytest
from agente_ucv.agent import calcular_promedio

def test_calcular_promedio_exito():
    # Prueba con notas normales de la UCV
    resultado = calcular_promedio([14.0, 18.0, 16.0])
    assert resultado["status"] == "success"
    assert "16.00" in resultado["resultado"]

def test_calcular_promedio_vacio():
    # Prueba la validación de seguridad si la lista llega vacía
    resultado = calcular_promedio([])
    assert resultado["status"] == "error"
    assert "no puede estar vacía" in resultado["resultado"]

def test_calcular_promedio_nota_invalida():
    # Prueba la validación si se ingresa una nota fuera del rango 0-20
    resultado = calcular_promedio([15, 25, 11])  # 25 es inválido
    assert resultado["status"] == "error"
    assert "Debe estar entre 0 y 20" in resultado["resultado"]