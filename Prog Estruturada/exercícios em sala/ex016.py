#16. Crie um programa que recebe como entrada dois números inteiros, divida o primeiro número
#pelo segundo e imprima na tela, separadamente, a parte inteira da divisão e o resto.

n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))

result = n1 // n2
resto = n1 % n2

print("O resultado da divisão inteira é {0} e o resto da divisão é {1}.".format(result, resto))