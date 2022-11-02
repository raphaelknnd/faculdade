# 4. Crie um programa que receba uma string com uma frase digitada pelo usuário. Conte quantos
# espaços em branco existem na string e quantas vezes aparecem cada uma das vogais A, E, I, O e U.

def contador(frase):
  a = 0
  e = 0
  i = 0 
  o = 0
  u = 0
  espaco = 0
  
  frase = frase.lower()

  for count in frase:
    if count == "a":
      a += 1
    elif count == "e":
      e += 1
    elif count == "i":
      i += 1
    elif count == "o":
      o += 1
    elif count == "u":
      u += 1
    elif count == " ":
      espaco += 1

  print("A = {}\nE = {}\nI = {}\nO = {}\nU = {}\nESPAÇOS = {}".format(a, e, i, o, u, espaco))




frase = input("Insira uma frase: ")

contador(frase)