import random
numeros=[]
num_jogos = int(input("Quantas apostas você vai fazer? "))
for i in range(0,num_jogos):
  while len(numeros) < 6:
    aux=random.randint(1, 60)
    if aux not in numeros:
      numeros.append(aux)
  print(numeros)
  numeros=[]
  