# 1. Construa um programa com a função ‘soma3’ que recebe como argumento três inteiros e
# retorna a soma desses três números. Imprima na tela o resultado.

def soma3(n1, n2, n3):
  soma = n1 + n2 + n3
  return soma

num =  input("Insira os numeros separados por espaço: ")

num = num.split(" ")

soma = soma3(int(num[0]), int(num[1]), int(num[2]))

print("A soma é ", soma)


