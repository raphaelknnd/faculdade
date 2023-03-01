# 10. Crie um programa que solicite três números aos usuários e imprima na tela o menor deles.

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if num1 < num2 and num1 < num3:
  res = num1
elif num2 < num1 and num2 < num3:
  res = num2
elif num3 < num1 and num3 < num2:
  res = num3
else:
  res = "equal"

if res == "equal":
  print("Os números são iguais.")
else:
  print(str(res) + " é o menor deles.")