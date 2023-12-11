# 📃README: Solucionador do Problema do Caixeiro Viajante (TSP)
**ଘ(੭◌ˊ ᵕ ˋ)੭** ★ Trabalho Prático realizado para a disciplina de Algoritmos 2, da Universidade Federal de Minas Gerais (UFMG).
## ｡₊⊹⭒˚｡⋆Execução
Para a execução do programa, deve ser utilizado Python3.

Execução no Windows:
**```python main.py <instance_file.tsp | random> [B|C|T] [B|C|T]```**

Cada parâmetro corresponde:
* **```<instance_file.tsp | random>```**: Especifique o caminho para um arquivo de instância TSP ou use "random" para gerar um grafo completo de tamanho aleatório entre 8 e 16.
* **```[B|C|T] [B|C|T]```**: Opções de algoritmo opcionais para execução. Escolha entre 'B' (Branch and Bound), 'C' (Christofides) e 'T' (Twice Around The Tree). Se nenhuma opção for fornecida, todos os algoritmos serão executados.

## ｡₊⊹⭒˚｡⋆Exemplos de uso
Gera um grafo de tamanho aleatório executa os algoritmos Branch and Bound e Christofides:
```
python main.py random B C
```
Utiliza a instância TSP do arquivo datasets/burma14.tsp e executa os três algoritmos:
```
python main.py datasets/burma14.tsp
```
Utiliza a instância TSP do arquivo datasets/berlin52.tsp e executa o Twice Around The Tree:
```
python main.py datasets/burma14.tsp T
```
## ｡₊⊹⭒˚｡⋆Dependências
Este projeto depende das seguintes bibliotecas Python:
* tsplib95: (http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)
* numpy: (https://numpy.org/)
* NetworkX: (https://networkx.org/)

## ｡₊⊹⭒˚｡⋆Datasets
O arquivo datasets.txt contém informações de limite para instâncias específicas do TSP. Se disponível, o script calcula e exibe a taxa de aproximação.
A pasta 'datasets' contém arquivos de instância TSP no formato TSPLIB.
```
├── datasets
│   ├── instancia1.tsp
│   ├── instancia2.tsp
│   ├── ...
│   └── instanciak.tsp
├── main.py
├── auxiliar.py
├── algoritmos.py
```
