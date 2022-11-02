# 4. Faça um programa que solicite o nome do usuário e a senha, imprimindo uma mensagem de
# erro e voltando a solicitar uma nova senha caso ela seja igual ao nome do usuário.

# variável auxiliar que servirá como contador dentro do laço
aux = False

while aux == 0:
  user = input("Username: ")
  pwrd = input("Password: ")

  if user == pwrd:
    print("ERRO! Usuário e senha não podem ser iguais.")
    continue
  aux = True

print("Login bem sucedido.")