# 16. Crie um programa que pergunte ao usuário seis números e imprima na tela a soma e a
# média deles.

numeros = input("Informe os seis numeros: ")

numeros = numeros.split(" ")

numeros = list(map(int, numeros))

soma = 0
for aux in numeros:
  soma = soma + aux

soma = soma/6

print("Média = " + str(soma))