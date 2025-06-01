#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contiene dos funciones para calcular n!:
1. factorial_iterativo(n): versión iterativa.
2. factorial_recursivo(n): versión recursiva.
"""

def factorial_iterativo(n):
    """Retorna n! usando un bucle. Error si n < 0."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    """Retorna n! usando recursión. Error si n < 0."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n <= 1:
        return 1
    return n * factorial_recursivo(n - 1)

if __name__ == "__main__":
    # Ejemplos breves
    for i in range(6):
        print(f"Iterativo {i}! = {factorial_iterativo(i)}")
    print()
    for i in range(6):
        print(f"Recursivo {i}! = {factorial_recursivo(i)}")
