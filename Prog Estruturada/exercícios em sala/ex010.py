#10. Construa um programa que solicite a temperatura em graus Fahrenheit ao usuário e transforme
#a temperatura em graus Celsius. Imprima na tela. Dica:
#Celsius = 5 * ((Fahrenheit-32) / 9)

fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))

celsius = 5 * ((fahrenheit - 32) / 9)
celsius = round(celsius, 2)

print(str(celsius) + "°C")