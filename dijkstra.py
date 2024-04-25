import networkx as nx
import matplotlib.pyplot as plt

def ler_grafo(arquivo):
    grafo = nx.DiGraph()
    with open(arquivo, 'r') as f:
        for linha in f:
            origem, destino, peso = map(int, linha.split())
            grafo.add_edge(origem, destino, weight=peso)
    return grafo

def calcular_distancias_e_rotas_minimas(G, no_inicial):
    distancias = nx.single_source_dijkstra_path_length(G, no_inicial)
    rotas = nx.single_source_dijkstra_path(G, no_inicial)
    return distancias, rotas

arquivo = "grafo.txt"
no_inicial = 1
grafo = ler_grafo(arquivo)
distancias, rotas = calcular_distancias_e_rotas_minimas(grafo, no_inicial)

# Imprimir distâncias e rotas mínimas
print("Distâncias mínimas a partir do vértice", no_inicial)
for no, distancia in distancias.items():
    print("Vértice:", no, "Distância mínima:", distancia)

print("\nCaminhos mínimos a partir do vértice", no_inicial)
for no, rota in rotas.items():
    print("Vértice:", no, "Caminho mínimo:", rota)

