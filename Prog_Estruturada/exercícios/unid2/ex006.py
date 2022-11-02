# 6. Construa um programa que leia do teclado e valide os seguintes dados sobre funcionários de
# uma empresa:
# a) Nome: maior que três caracteres.
# b) Idade: entre 0 e 130.
# c) Salário: maior que zero.
# d) CEP: tamanho 8.
# e) Departamento: ‘Administrativo’ ou ‘Fabrica’.

aux = False

while aux == False:
  name = input("Informe o nome do funcionário: ")
  count = 0
  for x in name:
    count += 1
  
  if count <= 3:
    print("Nome menor que 4 caracteres. Informe um nome válido.")
  else:
    aux = True

aux = False

while aux == False:
  idade = int(input("Informe a idade do funcionário: "))
  
  if idade < 0 or idade > 130:
    print("Idade inválida. Informe uma idade válida.")
  else:
    aux = True

aux = False

while aux == False:
  salario = float(input("Informe o salário do funcionário: "))

  if salario < 0:
    print("Salário inválido! Insira um valor acima de 0(zero).")
  else:
    aux = True

aux = False

while aux == False:
  cep = input("Informe o CEP: ")
  count = 0
  for x in cep:
    count += 1
  
  if count != 8:
    print("Cep deve conter 8 caracteres.")
  else:
    aux = True

aux = False

while aux== False:
  depart = input("Informe o departamento: ").lower()

  if depart in ['administrativo', 'fabrica']:
    aux = True
  else:
    print("Departamento inexistente.")

print("\n\nFIM DA EXECUÇÃO.")