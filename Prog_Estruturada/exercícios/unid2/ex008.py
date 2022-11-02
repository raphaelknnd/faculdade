# 8. Supondo que José tenha R$ 75.000,00 investidos a uma taxa anual de 3% de juros e que
# João tenha R$ 215.000,00 investidos com uma taxa de 1,5% de juros anuais, faça um programa que
# calcule e escreva quantos anos seriam necessários para que José ultrapasse ou iguale João, mantidas
# as taxas de juros.

jose = 75000
joao  = 215000
count = 0

while jose < joao:
  jose *= 1.03
  joao *= 1.015
  count += 1

print("Levará " + str(count) + " anos.")