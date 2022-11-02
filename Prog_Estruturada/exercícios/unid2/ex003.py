# 3. Crie um programa em Python que solicite ao usuário dois números inteiros e imprima o
# maior deles.

num = int(input("Insira um número: "))
num2 = int(input("Insira mais um número: "))

if num > num2:
  print(str(num) + " é maior que " + str(num2))
elif num2 > num:
  print(str(num2) + " é maior que " + str(num))
else:
  print(str(num) + " é igual a " + str(num2))