# Problema de Transporte com o Método do Canto Noroeste em Python

## 📖 Introdução

O Problema de Transporte na logística visa otimizar a distribuição de mercadorias entre diversos pontos de origem e destinos, minimizando os custos totais de transporte. Comum em cenários de distribuição e redes de suprimento, o Método do Canto Noroeste é uma heurística empregada para encontrar uma solução inicial. Inicia-se a alocação no canto noroeste da tabela de custos, progredindo de maneira a otimizar o transporte considerando as restrições de oferta e demanda, sendo uma abordagem eficaz na resolução desse desafio logístico.

## 🚚 Problema 

Uma empresa chamada "GreenLife" que se especializa no fornecimento de produtos orgânicos frescos para diversos estados do Brasil. A GreenLife estabeleceu parcerias com as 100 cidades mais populosas para atuarem como fornecedores, e elas visam distribuir seus produtos de forma eficiente para 27 estados. A empresa busca maximizar seus lucros no transporte determinando as rotas de envio mais econômicas.

A GreenLife busca maximizar seus lucros, considerando as quantidades ótimas a serem enviadas de cada fornecedor para cada estado. A função objetivo reflete a maximização do lucro total, considerando os lucros por unidade em cada rota. As restrições garantem que a demanda de cada estado seja atendida e que cada fornecedor não envie mais do que sua oferta.

- 📗 [Planilha com o Problema](https://docs.google.com/spreadsheets/d/10Eqr6RB5kfVWvIdKsb22g8gDjI9Nlkv6QNh_0cbVwlc/edit?usp=sharing)

Devido ao número de oferta e demanda serem diferentes, foi necessário a inserção de uma linha dummy, com os resultados zerados, e o valor da oferta ajustado para que então oferta e demanda fiquem iguais, podendo então executar o algoritmo do canto noroeste.

## 🔢 Modelagem Matemática
​
Xij: Quantidade de recursos enviados do fornecedor i para o destino j.
​
Si: Quantidade de recursos disponíveis no fornecedor i.

Dj: Quantidade de recursos necessários no destino j.

## 🎯 Objetivo

`Minimizar o custo total de transporte:`

 $`min \sum_{i=1}^{n} \sum_{j=1}^{m} c_{ij} x_{ij}`$ 

 `Restrições`
 * A demanda de cada destino deve ser atendida:
 $`\sum_{i=1}^{n} x_{ij} = d_j \quad \forall j = 1, 2, \ldots, m`$

 * A oferta de cada fornecedor não deve ser superada:
 $`x_{ij} \le s_i \quad \forall i = 1, 2, \ldots, n`$



## 📜 Codigo

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

def getDemand(data):
    return [int(x) for x in data[len(data)-1][1:-1]]

def getSupply(data):
    return [int(x[-1]) for x in data[1:-1]]

def getWeights(data):
    return [[int(value) for value in line[1:-1]] for line in data[1:-1]]

dados = ler_csv("Dados.csv")

demand = getDemand(dados)
supply = getSupply(dados)
weights = getWeights(dados)

bfs = north_west_corner(supply, demand)

total_cost = calculate_total_cost(bfs, weights)

print(weights)

print("\nNorth-West Corner Method Result:")
for (i, j), v in bfs:
    print(f"  ({i}, {j}): {v}")

print("\nTotal Cost after multiplying with weights:")
print(total_cost)
```

`calculate_total_cost(bfs, weights):`
Essa função calcula o custo total do transporte considerando as alocações iniciais (bfs) e os pesos associados a cada rota (weights).
Para cada alocação em bfs, a função multiplica a quantidade alocada pelo peso correspondente, exibindo essas multiplicações na saída padrão.
O custo total é acumulado e retornado ao final.

`getDemand(data), getSupply(data), getWeights(data):`
Estas funções extraem a demanda, oferta e os pesos da matriz de dados lidos do arquivo CSV.
getDemand retorna a demanda a partir da última linha dos dados.
getSupply retorna a oferta a partir das linhas intermediárias dos dados.
getWeights retorna uma matriz bidimensional de pesos a partir das linhas intermediárias dos dados.

`Leitura de Dados:`
Usa a função ler_csv para ler os dados do arquivo CSV chamado "Dados.csv".

`Alocação Inicial com "North-West Corner":`
Utiliza a função north_west_corner para encontrar alocações iniciais usando o método "North-West Corner". Os resultados são armazenados na lista bfs.

`Cálculo do Custo Total:`
Após as alocações, o código chama calculate_total_cost para calcular o custo total multiplicando as alocações pelos pesos associados.

`Impressão dos Resultados:`
Imprime a matriz de pesos, as alocações resultantes do método "North-West Corner" e o custo total após a multiplicação com os pesos.

## 📊 Resultados
`Multiplicações:`

![image](https://github.com/BryanWille/algoritmo-canto-noroeste/assets/84272231/cc4dd90c-0104-48ae-9dc8-df8b35c2dec2)


`Tabela de pesos`
![image](https://github.com/BryanWille/algoritmo-canto-noroeste/assets/84272231/1601fd77-945a-43bc-8b34-a0f07fcf2bc2)

`Resultados do metodo do canto noroeste`

![image](https://github.com/BryanWille/algoritmo-canto-noroeste/assets/84272231/eecf3149-aa33-44ec-b2d0-434f8e9c39f0)

`Resultado da multiplicação Final`

![image](https://github.com/BryanWille/algoritmo-canto-noroeste/assets/84272231/d5a2a92f-db3a-43ba-b412-cbef91c77303)

## 🔄 Complexidade Computacional
No caso de um problema de transporte resolvido por métodos de programação linear, a complexidade pode ser aproximadamente descrita como `O(m*n)` onde `m`  é o número de fornecedores (cidades) e `n` é o número de destinos (estados). Isso se deve ao fato de que, em problemas de programação linear, os métodos de solução eficientes, como o método simplex, têm complexidade proporcional ao número de restrições e variáveis na formulação do problema.

Assim, para um problema de transporte com 100 fornecedores e 27 destinos, a complexidade seria `O(100*27) = O(2700)`. Em termos práticos, essa complexidade é geralmente considerada razoável e eficiente para tamanhos de problemas moderados.

## 🌐  Aplicações do Problema de Transporte na Vida Real:
O Problema de Transporte é uma ferramenta valiosa em diversas aplicações práticas, incluindo:

- Distribuição: o Problema de Transporte pode ser usado para determinar a melhor maneira de distribuir bens de um fabricante para diferentes varejistas.
- Manufatura: o Problema de Transporte pode ser usado para determinar a melhor maneira de transportar matérias-primas de fornecedores para diferentes fábricas.
- Varejo: o Problema de Transporte pode ser usado para determinar a melhor maneira de transportar produtos de um centro de distribuição para diferentes lojas.
- Saúde: o Problema de Transporte pode ser usado para determinar a melhor maneira de transportar sangue ou outros órgãos para diferentes hospitais.
- Energia: o Problema de Transporte pode ser usado para determinar a melhor maneira de transportar energia elétrica de uma usina para diferentes consumidores.
- Logística militar: o Problema de Transporte pode ser usado para determinar a melhor maneira de transportar suprimentos para tropas em campo.


## 🔍 Conclusões:

Em conclusão, o código apresenta uma implementação eficiente do método "Canto Noroeste" para resolver problemas de transporte, demonstrando o processo desde a leitura de dados até a visualização dos resultados. A funcionalidade básica é sólida, oferecendo uma base para abordar problemas práticos de logística e distribuição

Assim, para o problema da empresa GreenLife, o custo mínimo encontrado pelo algoritmo é de 70559, sendo esse valor obtido através do método Canto Noroeste.

## 📚 Referências:

[Radzion: Transportation Problem North West Corner Method with Python
](https://radzion.com/blog/operations/corner)

## 👥 Grupo
- [Bryan Wille](https://github.com/BryanWille)
- [Bernardo Bertouldi](https://github.com/Benkars)
- [Cauã Henrique](https://github.com/CauaHvS)
- [Pedro Augusto](https://github.com/Pdro-Allgusto)
