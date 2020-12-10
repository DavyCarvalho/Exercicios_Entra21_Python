from random import randint
from collections import Counter

lancamentos = []

for i in range(1, 100):
    dado = randint(1, 6)
    lancamentos.append(dado)

resultado = Counter(lancamentos)

print(resultado)

for jogada, ocorrencia in resultado.items():
    print(f'o lado do dado {jogada} ocorreu {ocorrencia} vezes')