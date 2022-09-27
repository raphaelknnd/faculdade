# 11. Construa um programa para que receba duas notas de um aluno. O programa deve processar
# a média e mostrar a mensagem:
# a) “Aprovado”, para média 7,0 ou maior.
# b) “Reprovado”, para média menor que 7,0.

n1 = int(input("Informe a primeira nota: "))
n2 = int(input("Informe a segunda nota: "))

media = (n1 + n2) / 2

if media >= 7:
  print("Aprovado")
else:
  print("Reprovado")
