# 20. Crie um programa que receba três palavra e as imprima na tela na ordem inversa que as recebeu.

palavra = input("Insira a primeira palavra: ")
palavra2 = input("Insira a segunda palavra: ")
palavra3 = input("Insira a terceira palavra: ")

print("{2}, {1}, {0}.".format(palavra, palavra2, palavra3))