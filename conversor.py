import csv

def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        dados = [linha for linha in leitor]
    return dados

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

dados = ler_csv("dados.csv")

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