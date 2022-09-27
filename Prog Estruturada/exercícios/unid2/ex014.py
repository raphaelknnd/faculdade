# 14. Crie um programa que pergunte ao usuário 10 números e imprima na tela o maior deles.

numeros = input("Informe 10 numeros: ")
numeros = numeros.split(" ")

numeros = map(int, numeros)
numeros = list(numeros)

i = 0
aux = -1
while i < len(numeros):
  
  if numeros[i] > aux:
    aux = numeros[i]
  
  i+=1

print(numeros)
print(aux)