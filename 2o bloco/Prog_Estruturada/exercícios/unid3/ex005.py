# 5. Construa um programa que permita ao usuário entrar com uma string e mostre a string de trás
# para frente e em letras maiúsculas.

def inverte(string):
  string = string[::-1].upper()
  return string


frase = input("Insira uma frase: ")

inverso = inverte(frase)

print("A nova frase é {}".format(inverso))