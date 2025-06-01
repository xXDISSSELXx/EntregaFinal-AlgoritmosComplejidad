#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""


Este script calcula, en un grafo completo de 10 nodos:
1. Las distancias mínimas entre cada par de nodos usando Dijkstra.
2. Una ruta aproximada para el TSP empleando la heurística del vecino más cercano.

Uso:
    python3 tsp_vecino_mas_cercano.py
"""

import sys

def dijkstra(graph, origen):
    """
    Calcula distancias mínimas desde 'origen' a todos los nodos en 'graph' (matriz NxN).
    Parámetros:
      - graph: lista de listas (NxN) con pesos; 0 indica ausencia de arista directa.
      - origen: índice del nodo inicial.
    Retorna:
      - distancias: lista de tamaño N con la distancia mínima de 'origen' a cada nodo.
    Complejidad: O(N^2) para Dijkstra clásico sobre matriz de adyacencia.
    """
    n = len(graph)
    distancias = [float('inf')] * n
    visitados = [False] * n
    distancias[origen] = 0

    for _ in range(n - 1):
        # Seleccionar el nodo no visitado con distancia mínima
        u = min(
            (d, idx) for idx, (d, v) in enumerate(zip(distancias, visitados)) if not v
        )[1] if any(not v for v in visitados) else -1

        if u == -1 or distancias[u] == float('inf'):
            break
        visitados[u] = True

        for v in range(n):
            peso = graph[u][v]
            if not visitados[v] and peso != 0:
                nueva_dist = distancias[u] + peso
                if nueva_dist < distancias[v]:
                    distancias[v] = nueva_dist

    return distancias

def calcular_distancias_todos_a_nodos(grafo):
    """
    Ejecuta Dijkstra desde cada nodo y devuelve la matriz NxN de distancias mínimas.
    Parámetros:
      - grafo: matriz de adyacencia NxN.
    Retorna:
      - distancias: matriz NxN donde distancias[i][j] es la mínima de i a j.
    Complejidad total: O(N^3).
    """
    n = len(grafo)
    return [dijkstra(grafo, i) for i in range(n)]

def encontrar_vecino_mas_cercano(actual, visitados, mat_dist):
    """
    Devuelve el índice del nodo no visitado más cercano a 'actual'.
    Parámetros:
      - actual: índice del nodo actual.
      - visitados: lista booleana de tamaño N.
      - mat_dist: matriz de distancias mínimas NxN.
    Retorna:
      - vecino: índice del nodo no visitado con menor mat_dist[actual][vecino].
    """
    min_dist = float('inf')
    vecino = -1
    for i, vis in enumerate(visitados):
        if not vis and mat_dist[actual][i] < min_dist:
            min_dist = mat_dist[actual][i]
            vecino = i
    return vecino

def vecino_mas_cercano(mat_dist):
    """
    Heurística Nearest Neighbor para generar un tour TSP.
    Parámetros:
      - mat_dist: matriz NxN de distancias mínimas.
    Retorna:
      - tour: lista de longitud N+1 con el orden de nodos (empieza y termina en 0).
    Complejidad: O(N^2).
    """
    n = len(mat_dist)
    tour = [0] * (n + 1)
    visitados = [False] * n
    actual = 0
    visitados[0] = True

    for i in range(1, n):
        sig = encontrar_vecino_mas_cercano(actual, visitados, mat_dist)
        tour[i] = sig
        visitados[sig] = True
        actual = sig

    tour[n] = 0  # Regreso al inicio
    return tour

def calcular_longitud_tour(tour, mat_dist):
    """
    Suma las distancias entre nodos consecutivos en 'tour'.
    Parámetros:
      - tour: lista de índices de nodos (tamaño N+1).
      - mat_dist: matriz NxN de distancias mínimas.
    Retorna:
      - longitud: entero con la suma total de distancias.
    """
    return sum(
        mat_dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)
    )

if __name__ == "__main__":
    # Definición del grafo (matriz 10x10 de pesos)
    graph = [
        [ 0, 34, 56, 12, 78, 90, 43, 67, 23, 55 ],
        [34,  0, 64, 21, 12, 44, 90, 13, 45, 66 ],
        [56, 64,  0, 50, 34, 33, 76, 82, 28, 59 ],
        [12, 21, 50,  0, 22, 88, 16, 44, 73, 10 ],
        [78, 12, 34, 22,  0, 25, 90, 17, 65, 33 ],
        [90, 44, 33, 88, 25,  0, 14, 56, 32, 71 ],
        [43, 90, 76, 16, 90, 14,  0, 36, 48, 11 ],
        [67, 13, 82, 44, 17, 56, 36,  0, 20, 24 ],
        [23, 45, 28, 73, 65, 32, 48, 20,  0, 60 ],
        [55, 66, 59, 10, 33, 71, 11, 24, 60,  0 ]
    ]

    # 1) Matriz de distancias mínimas
    all_pairs_shortest = calcular_distancias_todos_a_nodos(graph)

    # 2) Tour TSP aproximado
    tour = vecino_mas_cercano(all_pairs_shortest)

    # 3) Mostrar resultados
    print("Tour TSP (vecino más cercano):", tour)
    print("Longitud total:", calcular_longitud_tour(tour, all_pairs_shortest))
