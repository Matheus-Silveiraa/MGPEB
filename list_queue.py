from collections import deque

modulos = [
    {"nome": "Habitacao", "pouso": 2, "n_comb": 9500, "massa": 18000, "criticidade": 10, "hora": 10},
    {"nome": "Energia", "pouso": 1, "n_comb": 7000, "massa": 12000, "criticidade": 10, "hora": 8},
    {"nome": "Medico", "pouso": 3, "n_comb": 3000, "massa": 5000, "criticidade": 9, "hora": 12},
    {"nome": "Logistica", "pouso": 4, "n_comb": 8000, "massa": 15000, "criticidade": 8, "hora": 14},
    {"nome": "Pesquisa", "pouso": 5, "n_comb": 4000, "massa": 7000, "criticidade": 7, "hora": 16}
]

# acessar primeiro módulo
print(modulos[1])

# percorrer lista
for m in modulos:
    print(m["pouso"])

fila_pouso = deque()

for m in sorted(modulos, key=lambda x: x["pouso"]):
    fila_pouso.append(m)

while fila_pouso:
    modulo = fila_pouso.popleft()
    print("Pousando:", modulo["nome"])

#Busca linear combustivel
menor_comb = modulos[0]

for m in modulos:
    if m["n_comb"] < menor_comb["n_comb"]:
        menor_comb = m 

print("Menor combustível:", menor_comb["nome"])






