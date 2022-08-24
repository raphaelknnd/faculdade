import math

raio = input("Informe o raio: ")

area = math.pi * float(raio) ** 2

print(round(area, 2))

print("{0:.{1}f}".format(area, 2))