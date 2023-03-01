# 17. Crie um programa que pergunte a hora ao usuário (0-24). Imprima na tela o texto: “Bom dia.”,
# “Boa tarde.” ou “Boa noite.” ou “Hora Inválida.”, de acordo com a resposta.

hora = int(input("Que horas são?: "))

if hora > 24 or hora < 0:
  print("Hora inválida")
elif hora >= 6 and hora <= 12:
  print("Bom dia")
elif hora > 12 and hora <= 18:
  print("Boa tarde")
else:
  print("Boa noite")

