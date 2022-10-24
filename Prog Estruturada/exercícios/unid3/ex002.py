# 2. Crie um programa com a função chamada ‘positivo’ que recebe um número e retorne verdadeiro
# se ele for positivo e falso se ele é negativo. Imprima o resultado.

def positivo(num):
  if num >= 0:
    return "Verdadeiro"
  else:
    return "Falso"

numero = int(input("Insira um número: "))

print(positivo(numero))


# Abaixo uma solução para a mesma questão retornando valores booleanos
#
#
# def positivo(num):
#   if num >= 0:
#     return True
#   else:
#     return False
# 
# numero = int(input("Insira um número: "))
# 
# res = positivo(numero)
# 
# if res == True:
#   print("Verdadeiro")
# else: 
#   print("Falso")