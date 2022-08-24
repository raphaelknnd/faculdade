#13. Crie um programa que solicite ao usuário três números inteiros. Compute e exiba na tela:
#a) o resto da divisão do primeiro com o segundo;
#b) o segundo exponencial com o terceiro;
#c) o primeiro dividido pelo terceiro, somado com o segundo.

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
n3 = int(input("Informe o terceiro numero: "))

a = n1 % n2
b = n2 ** n3
c = (n1 / n3) + n2

print("a)" + str(a) + "\nb)" + str(b) + "\nc)" + str(c))