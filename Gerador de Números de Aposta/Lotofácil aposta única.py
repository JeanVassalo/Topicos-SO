import random
numeros=[]
while len(numeros) < 15:
  aux=random.randint(1, 25)
  if aux not in numeros:
    numeros.append(aux)
numeros