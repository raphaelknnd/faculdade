#15. Construa um programa que receba o tamanho dos catetos de um triângulo retângulo e
#compute sua hipotenusa. Imprima o valor da hipotenusa na tela.
import math

cat1 = float(input("Informe a medida do cateto 'a': "))
cat2 = float(input("Informe a medida do cateto 'b': "))

hip = round(math.sqrt(math.pow(cat1, 2) + math.pow(cat2, 2)), 2)

print("O valor da hipoteunsa é " + str(hip))