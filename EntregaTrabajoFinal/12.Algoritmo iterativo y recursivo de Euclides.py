
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Contiene dos funciones para calcular el MCD de dos enteros no negativos:
1. gcd_iterativo(a, b)
2. gcd_recursivo(a, b)
"""

def gcd_iterativo(a, b):
    """Retorna el MCD de a y b usando el algoritmo iterativo de Euclides."""
    if a < 0 or b < 0:
        raise ValueError("Los parámetros deben ser >= 0")
    while b:
        a, b = b, a % b
    return a

def gcd_recursivo(a, b):
    """Retorna el MCD de a y b usando el algoritmo recursivo de Euclides."""
    if a < 0 or b < 0:
        raise ValueError("Los parámetros deben ser >= 0")
    return a if b == 0 else gcd_recursivo(b, a % b)

if __name__ == "__main__":
    ejemplos = [(48, 18), (54, 24), (0, 5), (7, 0), (270, 192)]
    print("Pruebas gcd_iterativo:")
    for x, y in ejemplos:
        print(f"gcd_iterativo({x}, {y}) = {gcd_iterativo(x, y)}")
    print("\nPruebas gcd_recursivo:")
    for x, y in ejemplos:
        print(f"gcd_recursivo({x}, {y}) = {gcd_recursivo(x, y)}")
