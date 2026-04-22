from collections import deque

modulos = [
    {"nome": "Habitacao", "pouso": 2, "massa": 18000, "criticidade": 10, "hora": 10,
     "combustivel": 30, "cond_atmosferica": 9, "area_pouso": True, "integridade": 95},

    {"nome": "Energia", "pouso": 1, "massa": 12000, "criticidade": 10, "hora": 8,
     "combustivel": 60, "cond_atmosferica": 8, "area_pouso": True, "integridade": 70},

    {"nome": "Medico", "pouso": 3, "massa": 5000, "criticidade": 9, "hora": 12,
     "combustivel": 40, "cond_atmosferica": 7, "area_pouso": True, "integridade": 85},

    {"nome": "Logistica", "pouso": 4, "massa": 15000, "criticidade": 8, "hora": 14,
     "combustivel": 50, "cond_atmosferica": 6, "area_pouso": True, "integridade": 80},

    {"nome": "Pesquisa", "pouso": 5, "massa": 7000, "criticidade": 7, "hora": 16,
     "combustivel": 50, "cond_atmosferica": 7, "area_pouso": True, "integridade": 88}
]

# Busca
menor_comb = min(modulos, key=lambda x: x["combustivel"])
print("Menor combustível:", menor_comb["nome"])

maior_crit = max(m["criticidade"] for m in modulos)
mais_criticos = [m for m in modulos if m["criticidade"] == maior_crit]

for m in mais_criticos:
    print("Maior criticidade:", m["nome"])

# Fila
fila_pouso = deque(sorted(modulos, key=lambda x: x["pouso"]))

# Listas auxiliares
pousados = []
alerta = []

# Condições
while fila_pouso:
    m = fila_pouso.popleft()

    autorizado = (
        m["combustivel"] > 30 and
        m["cond_atmosferica"] > 5 and
        m["area_pouso"] and
        m["integridade"] > 60
    )

    if autorizado:
        print(f"Modulo de {m['nome']} autorizado para pouso")
        pousados.append(m)
    else:
        print(f"Modulo de {m['nome']} pouso BLOQUEADO")
        alerta.append(m)

# Pilha (revisão)
pilha_revisao = []

for m in alerta:
    pilha_revisao.append(m)

while pilha_revisao:
    print("Revisando modulo:", pilha_revisao.pop()["nome"])
