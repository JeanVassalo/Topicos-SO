import random
numeros=[]
while len(numeros) < 6:
  aux=random.randint(1, 60)
  if aux not in numeros:
    numeros.append(aux)
numeros
