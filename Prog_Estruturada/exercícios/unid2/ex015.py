# 15. Crie um programa que pergunte ao usuário cinco números e imprima na tela o maior e o menor deles

from asyncio.windows_events import NULL


numeros = input("Informe 5 numeros: ")
numeros = numeros.split(" ")

numeros = map(int, numeros)
numeros = list(numeros)

i = 0
aux = -1

while i < len(numeros):
  
  if numeros[i] > aux:
    aux = numeros[i]
  
  i+=1

i = 0
aux2 =  numeros[0]

while i < len(numeros):
  
  if numeros[i] < aux2:
    aux2 = numeros[i]
  
  i+=1

print(numeros)
print(aux)
print(aux2)