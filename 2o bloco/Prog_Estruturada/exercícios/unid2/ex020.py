# 20. Crie um programa que receba dois números inteiros positivos entre 0 e 1000 e imprima na tela 
# todos os números inteiros que estão no intervalo entre eles.

a = False

while a == False:
  start = int(input("Informe o inicio: "))
  stop = int(input("Informe o fim: "))

  if (start < 0 or start > 1000) or (stop < 0 or stop > 1000):
    print("Entrada inválida. ")
  else: 
    a = True

if start < stop:
  for x in range(start, stop):
    print(x)
else:
  for x in range(stop, start):
    print(x)