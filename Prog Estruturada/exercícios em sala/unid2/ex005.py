# 5. Crie um programa que verifique se uma letra digitada pelo usuário é uma vogal,
# consoante ou número.

entrada = input("Informe uma letra: ")

entrada = entrada.lower()

if entrada in ['a', 'e', 'i', 'o', 'u']:
  print("É uma vogal!")
elif entrada in ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']:
  print("É um número!")
else:
  print("É uma consoante!")