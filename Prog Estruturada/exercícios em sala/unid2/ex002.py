# 2. Construa um programa em Python que solicite uma idade entre 0 e 130 anos. Imprima uma
# mensagem se o valor for inválido e continue solicitando até que o usuário digite um valor válido.
aux = 0

while aux == 0:
  idade = int(input("Insira uma idade entre 0 e 130: "))

  if idade < 0 or idade > 130:
    print("Idade inválida! ")

  aux = 1
  
print("Fim da execução.")