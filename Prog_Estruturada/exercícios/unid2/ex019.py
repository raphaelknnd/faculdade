# 19. Construa um programa que peça ao usuário quatro números e imprima-os na tela em 
# ordem crescente.
numeros = input("Insira os numeros: ")
numeros = numeros.split(" ")
numeros = map(int, numeros)
numeros = list(numeros)

# Lista de teste:
# numeros = [9, 8, 7, 6, 10, 15, 29, 2]


aux = 0
count = 0

while count < len(numeros):
  i = 0
  while i < len(numeros) - 1:
    if numeros[i] > numeros[i + 1]:
      aux = numeros[i]
      numeros[i] = numeros[i + 1]
      numeros[i + 1] = aux
    i += 1
  count += 1

print(numeros)
