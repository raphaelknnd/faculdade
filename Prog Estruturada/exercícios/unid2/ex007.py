# 7. Crie um programa que verifique se uma letra digitada é “S” para sair do programa. Caso a letra
# digitada for diferente de S, o programa continua perguntando se o usuário deseja sair.

sair = False

while sair != True:
  letra = input("Informe uma letra para sair: ").lower()

  if letra == 's':
    sair = True

