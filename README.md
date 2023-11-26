# Problema de Transporte com o Método do Canto Noroeste em Python

## Introdução

O Problema de Transporte na logística visa otimizar a distribuição de mercadorias entre diversos pontos de origem e destinos, minimizando os custos totais de transporte. Comum em cenários de distribuição e redes de suprimento, o Método do Canto Noroeste é uma heurística empregada para encontrar uma solução inicial. Inicia-se a alocação no canto noroeste da tabela de custos, progredindo de maneira a otimizar o transporte considerando as restrições de oferta e demanda, sendo uma abordagem eficaz na resolução desse desafio logístico.

## Problema 

Uma empresa chamada "GreenLife" que se especializa no fornecimento de produtos orgânicos frescos para diversos estados do Brasil. A GreenLife estabeleceu parcerias com as 100 cidades mais populosas para atuarem como fornecedores, e elas visam distribuir seus produtos de forma eficiente para 27 estados. A empresa busca otimizar seus custos de transporte determinando as rotas de envio mais econômicas

A GreenLife precisa determinar as quantidades de envio ideais de cada cidade fornecedora para cada estado para minimizar o custo total de transporte, atendendo à demanda de todos os estados e garantindo que nenhum fornecedor superforneça.

## Codigo

```Python
import csv
```
`import csv:` Importa o módulo csv, que fornece funcionalidades para trabalhar com arquivos CSV.

```Python
def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        dados = [linha for linha in leitor]
    return dados
```
`def ler_csv(nome_arquivo):` Define uma função chamada ler_csv que recebe o nome de um arquivo CSV como argumento.

`with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:` Abre o arquivo CSV no modo de leitura ('r') e usa um bloco with para garantir que o arquivo seja fechado corretamente após o uso. Usa o encoding "utf-8" para lidar com caracteres especiais.

`leitor = csv.reader(arquivo):` Cria um objeto leitor de CSV para iterar sobre as linhas do arquivo.

`dados = [linha for linha in leitor]:` Lê todas as linhas do arquivo e armazena em uma lista chamada dados.

`return dados:` Retorna a lista de listas contendo os dados do arquivo CSV.


```Python
def north_west_corner(supply, demand):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    i = 0
    j = 0
    bfs = []
    while len(bfs) < len(supply) + len(demand) - 1:
        s = supply_copy[i]
        d = demand_copy[j]
        v = min(s, d)
        supply_copy[i] -= v
        demand_copy[j] -= v
        bfs.append(((i, j), v))
        if supply_copy[i] == 0 and i < len(supply) - 1:
            i += 1
        elif demand_copy[j] == 0 and j < len(demand) - 1:
            j += 1
    return bfs
```

`def north_west_corner(supply, demand):` Define uma função chamada north_west_corner que implementa o método "North-West Corner" para resolver problemas de transporte.

`Variáveis locais:` supply_copy e demand_copy são cópias das listas de oferta (supply) e demanda (demand), respectivamente. i e j são índices para percorrer essas listas.

`Loop while:` Itera enquanto o número de alocações na lista bfs for menor do que a soma do comprimento da oferta e da demanda menos 1.

`Alocação e atualização:` Calcula a quantidade alocada (v) como o mínimo entre a oferta e a demanda disponíveis. Atualiza as cópias da oferta e da demanda, adiciona a alocação à lista bfs.

`Atualização de índices:` Atualiza os índices i e j com base nas condições especificadas.

`return bfs:` Retorna a lista de tuplas representando as alocações.

```Python
def calculate_total_cost(bfs, weights):
    total_cost = 0
    print("Multiplications:")
    for (i, j), v in bfs:
        weight = weights[i][j]
        print(f"  {v} * {weight} = {v * weight}")
        total_cost += v * weight
    return total_cost
```
`def calculate_total_cost(bfs, weights):` Define uma função chamada calculate_total_cost que calcula o custo total das alocações multiplicado pelos pesos associados.

`Variável local:` total_cost é inicializada como zero.

`Loop for:` Itera sobre as alocações na lista bfs e calcula o custo total multiplicando as quantidades alocadas pelos pesos associados.

`print("Multiplications:"):` Imprime uma mensagem indicando que as próximas linhas mostrarão as multiplicações realizadas.

`print(f" {v} * {weight} = {v * weight}"):` Imprime cada multiplicação realizada.

`return total_cost:` Retorna o custo total calculado.

```Python
def getDemand(data):
    return [int(x) for x in data[len(data)-1][1:-1]]
```
`getDemand:` Retorna a demanda a partir dos dados.

```Python
def getSupply(data):
    return [int(x[-1]) for x in data[1:-1]]
```

`getSupply:` Retorna a oferta a partir dos dados.

```Python
def getWeights(data):
    return [[int(value) for value in line[1:-1]] for line in data[1:-1]]
```
`getWeights:` Retorna os pesos a partir dos dados.

```Python
dados = ler_csv("Dados.csv")
```
`Leitura de dados:` Lê os dados do arquivo CSV "Dados.csv" usando a função ler_csv.

```Python
demand = getDemand(dados)
supply = getSupply(dados)
weights = getWeights(dados)
```
`demand = getDemand(dados):` Obtém a demanda associada a cada destino.

`supply = getSupply(dados):` Obtém a oferta associada a cada origem.

`weights = getWeights(dados):` Obtém uma matriz bidimensional de pesos associados ao transporte de mercadorias.

```Python
bfs = north_west_corner(supply, demand)
```
`bfs = north_west_corner(supply, demand):`

`supply` e `demand` são listas que representam a oferta e demanda, respectivamente.

`north_west_corner` é uma função que implementa o método "North-West Corner" para encontrar alocações iniciais.

`bfs` recebe o resultado da aplicação do método, representado como uma lista de tuplas. Cada tupla contém a informação da alocação: índice da oferta, índice da demanda e quantidade alocada.

```Python
total_cost = calculate_total_cost(bfs, weights)
```
`total_cost = calculate_total_cost(bfs, weights):`

`bfs` é a lista de tuplas representando as alocações iniciais obtidas pelo método "North-West Corner".

`weights` é uma matriz bidimensional que contém os pesos associados ao transporte de mercadorias de cada origem para cada destino.

`calculate_total_cost` é uma função que multiplica as quantidades alocadas pelos pesos correspondentes e soma esses valores para calcular o custo total.

`total_cost` armazena o resultado desse cálculo.

```Python
print(weights)
```
`print(weights):`
`weights` é uma matriz bidimensional obtida através da função getWeights, representando os custos ou pesos associados a cada rota de transporte.

`print(weights)` exibe essa matriz na saída padrão, proporcionando uma visualização dos custos de transporte entre origens e destinos.

```Python
print("\nNorth-West Corner Method Result:")
for (i, j), v in bfs:
    print(f"  ({i}, {j}): {v}")
```
`print("\nNorth-West Corner Method Result:"):` Imprime uma mensagem indicando que os resultados seguintes são provenientes do método "North-West Corner".

`for (i, j), v in bfs:` Inicia um loop que percorre cada tupla em bfs, que representa uma alocação inicial.
`(i, j)` são os índices da oferta e demanda.
`v` é a quantidade alocada.

`print(f" ({i}, {j}): {v}"):` Imprime cada alocação no formato "(oferta, demanda): quantidade".

```Python
print("\nTotal Cost after multiplying with weights:")
print(total_cost)
```
`print("\nTotal Cost after multiplying with weights:"):` Imprime uma mensagem indicando que os resultados seguintes representam o custo total após a multiplicação com os pesos.

`print(total_cost):` Imprime o valor da variável `total_cost`, que foi calculada pela função calculate_total_cost. Esse valor representa o custo total do transporte considerando as alocações iniciais multiplicadas pelos pesos associados.

## Resultados

## Aplicações do Problema de Transporte na Vida Real:
O Problema de Transporte é uma ferramenta valiosa em diversas aplicações práticas, incluindo:

- Distribuição: o Problema de Transporte pode ser usado para determinar a melhor maneira de distribuir bens de um fabricante para diferentes varejistas.
- Manufatura: o Problema de Transporte pode ser usado para determinar a melhor maneira de transportar matérias-primas de fornecedores para diferentes fábricas.
- Varejo: o Problema de Transporte pode ser usado para determinar a melhor maneira de transportar produtos de um


## Conclusões e Possíveis Extensões:

Em conclusão, o código apresenta uma implementação eficiente do método "North-West Corner" para resolver problemas de transporte, demonstrando o processo desde a leitura de dados até a visualização dos resultados. A funcionalidade básica é sólida, oferecendo uma base para abordar problemas práticos de logística e distribuição


