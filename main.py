from algoritmos import tsp_christofides, tsp_twice_around, tsp_branch_bound
from auxiliar import read_datasets_info
import networkx as nx
import tsplib95
import random
import time
import sys
import os

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Leitura da linha de comando  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑
if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Uso: python main.py <arquivo.tsp|random> [B|C|T] [B|C|T]")
    sys.exit(1)

arg = sys.argv[1]
options = sys.argv[2:] if len(sys.argv) > 2 else []

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Seleção do algoritmo  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑
valid_options = ['B', 'C', 'T']
selected_options = set()
if not options:
    selected_options = set(valid_options)
else:
    for option in options:
        if option.upper() not in valid_options:
            print("Invalid algorithm option.")
            sys.exit(1)
        if option.upper() in selected_options:
            print(f"Error: Option {option.upper()} selected more than once.")
            sys.exit(1)
        selected_options.add(option.upper())

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Instância  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑
file_path = "datasets.txt"
datasets_info = read_datasets_info(file_path) # Lê imiares de cada dataset

def load_instance(arg):
    if arg.lower() != "random":
        problem = tsplib95.load(arg)
        return problem.get_graph()
    else:
        s = 12
        n = random.randint(8, 16)
        print(f"Using the seed {s} to generate a random graph with {n} vertices.")
        return generate_complete_graph(n, s)

def generate_complete_graph(n, s):
    G = nx.complete_graph(n)
    G = nx.relabel_nodes(G, {i: i+1 for i in range(n)})
    random.seed(s)
    for edge in G.edges():
        weight = random.randint(1, 100)
        G[edge[0]][edge[1]]['weight'] = weight
    return G

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Execução dos algoritmos  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑
def execute_algorithm(G, christofides=True, branch_and_bound=True, twice_around_the_three=True):
    algorithms = [
        ("Christofides", christofides, tsp_christofides ),
        ("Twice Around The Tree", twice_around_the_three, tsp_twice_around ),
        ("Branch and Bound", branch_and_bound, tsp_branch_bound),
    ]

    for name, flag, algorithm in algorithms:
        if flag:
            print("---" * 10)
            print(f"[ {name} ]")
            start_time = time.time()
            cost, circuit = algorithm(G)

            # Tempo de Execução
            end_time = time.time()
            execution_time = end_time - start_time
            seconds = execution_time % 60
            print(f"Runtime: {seconds:.6f} seconds")     

            # Tempo de Execução
            if(cost == 'NA'): print(" ! The execution exceeded the time limit")
            print("Approximate cost:", cost)
            
            # Aproximação
            if arg.lower() != "random" and cost != 'NA':
                instance_name = os.path.splitext(os.path.basename(arg))[0]
                threshold = datasets_info.get(instance_name, {}).get("Threshold", None)
                if threshold is not None:
                    approximation_ratio = cost / threshold
                    print(f"Approximation: {approximation_ratio:.2f}")
            print()

#  ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑ Driver Code ๋࣭ ⭑ ݁ ˖๋ ࣭ ⭑
christofides = 'C' in selected_options
branch_and_bound = 'B' in selected_options
twice_around_the_three = 'T' in selected_options

G = load_instance(arg)
execute_algorithm(G, christofides, branch_and_bound, twice_around_the_three)