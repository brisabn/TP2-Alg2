from heapq import heappop, heappush
from itertools import count
import pandas as pd

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Identicar Limiares dos Datasets  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑
def read_datasets_info(file_path):
    # lê o arquivo pulando o cabeçalho
    df = pd.read_csv(file_path, skiprows=1, delim_whitespace=True, names=["Dataset", "Nodes", "Threshold"])
    df["Nodes"] = df["Nodes"].astype(int)
    df["Threshold"] = df["Threshold"].astype(int)

    # criação do dicionario ✩°｡ ⋆⸜
    datasets_info = df.set_index("Dataset").to_dict(orient="index")
    return datasets_info

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Caminho e Custo  ݁ ˖๋ ࣭ ⭑ ๋࣭ ⭑
def make_hamiltonian(euler_circuit):
    hamiltonian_circuit = []
    visited_nodes = set()

    for edge in euler_circuit:
        if edge[0] not in visited_nodes:
            hamiltonian_circuit.append(edge[0])
            visited_nodes.add(edge[0])

    hamiltonian_circuit.append(hamiltonian_circuit[0])
    return hamiltonian_circuit

def circuit_cost(graph, circuit):
    cost = sum(graph[circuit[i]][circuit[i + 1]]['weight'] for i in range(len(circuit) - 1))
    return cost

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Minimum Spanning Tree  ݁ ˖๋ ࣭ ⭑ ๋࣭ ⭑
def prim_mst_edges(G, weight="weight"):
    # baseado no source do networkx
    push, pop = heappush, heappop
    nodes, c = set(G), count()

    while nodes:
        u = nodes.pop()
        frontier, visited = [], {u}

        for v, data in G.adj[u].items():
            # pega o peso da aresta u-v (ou 1 se não existir) e adiciona no frontier
            wt = data.get(weight, 1)
            push(frontier, (wt, next(c), u, v, data))

        while nodes and frontier:
            W, _, u, v, data = pop(frontier) # tira do frontier
            if v in visited or v not in nodes:
                continue

            yield (u, v, data) if data else (u, v)
            # retorna a aresta (u, v, data) se 'data' existir, caso contrário, retorna apenas (u,v)
            # yield é usada em funções geradoras ٩(ˊᗜˋ*)و

            visited.add(v)
            nodes.discard(v)

            for w, d2 in G.adj[v].items():
                if w not in visited:
                    # pega o peso da aresta v-w (ou 1 se não existir) e adiciona no frontier
                    new_weight = d2.get(weight, 1)
                    push(frontier, (new_weight, next(c), v, w, d2))

def minimum_spanning_tree(G, weight="weight"):
    min_edges = prim_mst_edges(G, weight=weight)
    # cria de maneira esperta um grafo com as arestas geradas ⋆｡⭒˚｡⋆
    T = G.__class__()
    T.graph.update(G.graph)
    T.add_nodes_from(G.nodes.items())
    T.add_edges_from(min_edges)
    return T