# 9. Altere o programa anterior permitindo ao usuário informar o capital inicial e as taxas de juros.
# Os capitais devem ser positivos e o juros do primeiro devem ser maiores que os do segundo.

count = 0
verify = False

while verify == False:
  jose = int(input("Informe o capital de Jose: "))
  joao = int(input("Informe o capital de João: "))

  if joao > 0 or jose > 0:
    verify = True
  else:
    print("Valor inválido.")

verify = False

while verify == False:
  taxa1 = float(input("Informe a taxa atribuída a José(sem o %): "))
  taxa2 = float(input("Informe a taxa atribuída a João(sem o %): "))

  if taxa1 > taxa2:
    verify = True
  else:
    print("Juros do primeiro não podem ser menores que os do segundo.")


while jose < joao:
  jose *= (1 + (taxa1/100))
  joao *= (1 + (taxa2/100))
  count += 1

print("Levará " + str(count) + " anos.")