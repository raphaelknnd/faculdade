# 13. Crie um programa que pergunte o preço do arroz cateto, agulhinha e jasmim e mostre na tela 
# qual você deve comprar (sempre será o arroz com o menor preço).

print("="*5 +"INFORME O VALOR DO ARROZ:" + "="*5)
cateto = float(input("Cateto: "))
agulhinha = float(input("Agulhinha: "))
jasmim = float(input("Jasmim: "))

aux = cateto
opc = 1

if agulhinha < aux:
  aux = agulhinha
  opc = 2

if jasmim < aux:
  aux = jasmim
  opc = 3

if opc == 1:
  print("Você deve comprar o arroz Cateto")
elif opc == 2:
  print("Você deve comprar o arroz agulhinha")
elif opc == 3:
  print("Você deve comprar o arroz jasmim")

# if cateto < agulhinha and cateto < jasmim:
#   print("Você deve comprar o arroz Cateto")
# elif agulhinha < cateto and agulhinha < jasmim:
#   print("Você deve comprar o arroz agulhinha")
# elif jasmim < agulhinha and jasmim < cateto:
#   print("Você deve comprar o arroz jasmim")

# O código comentado acima funciona para o caso de eu ter todos os valores diferentes, mas vai quebrar a regra de negócio caso ao menos dois valores sejam iguais. Para tratar isso precisaria ainda (talvez exista uma maneira mais prática de fazer isso) fazer cada comparação de dois valores iguais e um diferente e informar ao usuário que ele poderia comprar uma das duas oções.
