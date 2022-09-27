#18. Faça um programa que receba a altura e a base de um retângulo e calcule sua área. Mostre na
#tela o resultado.

alt = float(input("Insira a altura do triângulo: "))
base = float(input("Insira a base do triângulo: "))

area = (base * alt) / 2

print("A área do triângulo é de {0}².".format(area))