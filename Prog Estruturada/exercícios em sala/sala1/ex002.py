def reajuste(value):
  if value < 500:
    value = value + ((15/100) * value)
  elif value >= 500 and value <= 1000:
    value = value + ((10/100) * value)
  elif value > 1000:
    value = value + ((5/100) * value)
  print("O salário com reajuste é R$" + str(value))

salario = float(input("Informe o salário: "))

reajuste(salario)
