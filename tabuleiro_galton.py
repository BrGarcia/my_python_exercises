import random
import matplotlib.pyplot as plt

def tabuleiro_galton(d: int)->int:
    b = 10
    for _ in range(d):
        b += random.choice([-1,0,1])
    return b
qtd_bolinhas = 1000 #ou => int(input("Digite o numero de bolinhas: "))
distribuicao = [0] * 21

for _ in range(qtd_bolinhas):
    distribuicao[tabuleiro_galton(10)] += 1

for i,v in enumerate(distribuicao):
    print(f"Indice: {i+1} - Valor {v}")

# Gráfico
legenda = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
plt.bar(legenda, distribuicao)
plt.xlabel(' Posição ')
plt.ylabel('N de Bolinhas')
plt.title('Tabuleiro de Galton')
plt.show()

