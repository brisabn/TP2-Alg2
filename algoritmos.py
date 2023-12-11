from auxiliar import make_hamiltonian, circuit_cost, minimum_spanning_tree
import networkx as nx
import time
import numpy as np
import time

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Checar Tempo de Execução  ݁ ˖๋ ࣭ ⭑ ๋࣭ ⭑
def check_time(start_time, timeout=1800):
    elapsed_time = time.time() - start_time
    if elapsed_time > timeout:
        print(f"The execution exceeded the time limit and ran for up to {elapsed_time} seconds")
        raise TimeoutError("The execution exceeded the {} -minute time limit".format(timeout / 60))

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Christofides  ݁ ˖๋ ࣭ ⭑ ๋࣭ ⭑
def tsp_christofides(graph):
    start_time = time.time()
    try:
        T = minimum_spanning_tree(graph)
        # T = nx.minimum_spanning_tree(graph, weight = 'weight', algorithm="prim")
        check_time(start_time)

        odd = [v for v, d in T.degree() if d % 2 == 1]
        M = nx.min_weight_matching(graph.subgraph(odd), maxcardinality=True)

        H = nx.MultiGraph() # combina o MST e o MWM
        H.add_edges_from(T.edges)
        H.add_edges_from(M)

        euler_circuit = list(nx.eulerian_circuit(H, source=1))
        # garantido de encontrar por grau par
        check_time(start_time)
        hamiltonian_circuit = make_hamiltonian(euler_circuit) 
        check_time(start_time)
        cost = circuit_cost(graph, hamiltonian_circuit)

        return cost, hamiltonian_circuit
    except TimeoutError:
        return "NA", "NA"

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Twice Around The Tree  ݁ ˖๋ ࣭ ⭑ ๋࣭ ⭑
def tsp_twice_around(graph):
    start_time = time.time()
    try:
        T = minimum_spanning_tree(graph)
        # dfs_edges = list(nx.dfs_edges(T, 1))
        # hamiltonian_circuit = [start_vertex] + [v for u, v in dfs_edges] + [start_vertex]

        hamiltonian_circuit = list(nx.dfs_preorder_nodes(T, source=1))
        # DFS nos vértices na ordem que foram visitados
        hamiltonian_circuit.append(hamiltonian_circuit[0]) # para voltar
        cost = circuit_cost(graph, hamiltonian_circuit)

        check_time(start_time)
        return cost, hamiltonian_circuit
    except TimeoutError:
        return "NA", "NA"

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Branch and Bound ݁ ˖๋ ࣭ ⭑ ๋࣭ ⭑
def calculate_bound(closest, path, curr_level):
    # estimativa: soma duas arestas de menor peso incidentes em cada vértice e divide por dois
    prev = closest[path[curr_level - 1] - 1]
    curr = closest[path[curr_level] - 1]
    if curr_level == 1:
        return (prev[0] + curr[0]) / 2
    else:
        return (prev[1] + curr[0]) / 2

def update_visited(path, curr_level):
    # track nodes visitados no current path
    visited = [] 
    for i in range(len(path) - 1):
        if i + 1 not in path[:curr_level]:
            visited.append(False)
        else:
            visited.append(True)
    return visited

def tsp_branch_bound_recursive(start_time, graph, num_nodes, curr_bound, curr_weight, curr_level, path, neighbor_edgew, visited, curr_cost, circuit, memo_dict):
    check_time(start_time)
    if curr_level == num_nodes:
        # BOUND: checa se o path forma um circuito válido com custo menor
        first_node, last_node = path[0], path[curr_level - 1]
        if first_node != last_node:
            edge_weight = graph[last_node][first_node]['weight']
            total_cost = curr_weight + edge_weight
            if total_cost < curr_cost:
                curr_cost = total_cost
                circuit = list(path)
        return curr_cost, circuit

    # memoization pra checar se já vimos esse caminho
    memo_key = (tuple(path), tuple(visited))
    if memo_key in memo_dict:
        return memo_dict[memo_key]

    # BRANCH: explora para atualizar o current path
    for neighbor in graph.nodes():
        if path[curr_level-1] != neighbor and not visited[neighbor-1]:
            curr_weight += graph[path[curr_level-1]][neighbor]['weight']
            update_bound = curr_bound
            curr_bound -= calculate_bound(neighbor_edgew, path, curr_level)

            # checa se o current path pode melhorar
            if (curr_bound + curr_weight) < curr_cost:
                path[curr_level], visited[neighbor-1] = neighbor, True
                curr_cost, circuit = tsp_branch_bound_recursive(start_time, graph, num_nodes, curr_bound, curr_weight, curr_level+1, path, neighbor_edgew, update_visited(path, curr_level), curr_cost, circuit, memo_dict)

            # backtrack: undo as mudanças para explorar novo caminho
            curr_weight -= graph[path[curr_level-1]][neighbor]['weight']
            curr_bound = update_bound

    # memoiza o caminho atual
    memo_dict[memo_key] = (curr_cost, circuit)
    check_time(start_time)
    return curr_cost, circuit

def tsp_branch_bound(graph):
    start_time = time.time()
    try:
        num_nodes = graph.number_of_nodes()
        initial_bound = 0
        neighbor_edgew = [] # aretas incidentes

        path = [1] * (num_nodes + 1) # inicializa caminho com nós 
        visited = [False] * num_nodes
        visited[0], path[0] = True, 1

        circuit = []

        for node in graph.nodes():
            check_time(start_time)
            neighbors = graph[node].items()
            # ordenando... !
            sorted_neighbors = sorted(neighbors, key=lambda e: e[1]["weight"] if e[1]["weight"] != 0 else np.inf)[:2]
            weights = [neighbor[1]['weight'] for neighbor in sorted_neighbors]
            neighbor_edgew.append(weights)
            initial_bound += sum(weights) / 2 # calculo do lower bound inicial (੭ˊ꒳​ˋ)੭✧	

        check_time(start_time)
        memo_dict = {}
        cost, circuit = tsp_branch_bound_recursive(start_time, graph, num_nodes, initial_bound, 0, 1, path, neighbor_edgew, visited, np.inf, circuit, memo_dict)
        return cost, circuit
    except TimeoutError:
        return "NA", "NA"