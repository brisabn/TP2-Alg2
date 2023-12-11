# 📃README: Solucionador do Problema do Caixeiro Viajante (TSP)
**ଘ(੭◌ˊ ᵕ ˋ)੭** ★ Este trabalho prático foi desenvolvido para a disciplina de Algoritmos 2 na Universidade Federal de Minas Gerais (UFMG). O objetivo era implementar um algoritmo exato (Branch and Bound) e dois aproximativos (Christofides e Twice Around The Tree) para resolver o Problema do Caixeiro Viajante euclidiano. O foco da análise concentrou-se na comparação de desempenho, avaliando métricas de tempo, espaço e otimalidade.

## ｡₊⊹⭒˚｡⋆Execução
Para a execução do programa, deve ser utilizado Python3.

Execução no Windows:
**```python main.py <instance_file.tsp | random> [B|C|T] [B|C|T]```**

Cada parâmetro corresponde:
* **```<instance_file.tsp | random>```**: Especifique o caminho para um arquivo de instância TSP ou use "random" para gerar um grafo completo aleatório de tamanho entre 8 e 16 vértices.
* **```[B|C|T] [B|C|T]```**: Opções de algoritmo opcionais para execução. Escolha entre 'B' (Branch and Bound), 'C' (Christofides) e 'T' (Twice Around The Tree), pode-se escolher 1 ou 2 opções. Se nenhuma opção for fornecida, todos os 3 algoritmos serão executados.

## ｡₊⊹⭒˚｡⋆Exemplos de uso
𖤐 Gera um grafo de tamanho aleatório executa os algoritmos Branch and Bound e Christofides:
```
python main.py random B C
```
𖤐 Utiliza a instância TSP do arquivo datasets/burma14.tsp e executa os três algoritmos:
```
python main.py datasets/burma14.tsp
```
𖤐 Utiliza a instância TSP do arquivo datasets/berlin52.tsp e executa o Twice Around The Tree:
```
python main.py datasets/burma14.tsp T
```
## ｡₊⊹⭒˚｡⋆Dependências
Este projeto depende das seguintes bibliotecas Python:
* **tsplib95**: (http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)
* **numpy**: (https://numpy.org/)
* **NetworkX**: (https://networkx.org/)

## ｡₊⊹⭒˚｡⋆Datasets
O arquivo datasets.txt contém informações de limite para instâncias específicas do TSP. Se disponível, o script calcula e exibe a taxa de aproximação.
A pasta 'datasets' contém arquivos de instância TSP no formato TSPLIB.
```
├── datasets
│   ├── instancia1.tsp
│   ├── instancia2.tsp
│   ├── ...
│   └── instancian.tsp
├── main.py
├── auxiliar.py
├── algoritmos.py
```
