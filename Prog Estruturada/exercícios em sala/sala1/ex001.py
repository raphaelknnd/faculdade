# 1. Faça um programa que recebe o salário e as despesas. Deverá ser exibido "Gastos dentro do orçamento"
# caso o valor gasto não ultrapasse o salário e "Orçamento estourado" caso os gastos excedam o salário
# recebidio.

salario = float(input("Informe o salário: "))
gastos = float(input("Informe os seus gastos: "))

if gastos <= salario:
  print("Gastos dentro do orçamento!")
else:
  print("Orçamento estourado!")
