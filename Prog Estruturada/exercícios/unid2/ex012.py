# 12. Construa um programa que mostre na tela os números ímpares de 1 a 30, um por linha. Depois
# mostre os mesmos números impressos na mesma linha.

for num in range(1, 30):
  if num % 2 != 0:
    print(str(num))

print(list(range(1,30,1)))



