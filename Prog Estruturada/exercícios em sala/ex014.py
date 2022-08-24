#14. Crie um programa que receba como a entrada a altura da pessoa e calcule o peso ideal. Utilize
#as fórmulas: para os homens, (72.7*altura) – 58; para as mulheres, (62.1*altura) - 44.7

altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo da pessoa: ")

if sexo == "m":
    peso = round(((72.7 * altura) - 58), 2)
    print("\nA altura ideal é de {0}Kg.".format(peso))
elif sexo == "f":
    peso = round(((62.1 * altura) - 44.7), 2)
    print("\nA altura ideal é de {0}Kg.".format(peso))
else:
    print("\nEntrada inválida")