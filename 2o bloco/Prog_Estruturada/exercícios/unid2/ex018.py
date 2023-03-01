# 18. Crie um programa que imprima na tela todos os números pares entre 0 e 100.

for x in range(0, 101, 2):
  print(x)

# Ou podemos escrever o código da seguinte forma, assegurando que mesmo que o start range() seja alterado, os numeros mostrados continuarão sendo pares.
#
# print("="*25)
# for x in range(0, 100):
#   if x % 2 == 0:
#     print(x)


