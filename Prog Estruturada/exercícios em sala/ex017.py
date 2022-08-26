#17. Construa um aplicativo para uma loja de pisos. O aplicativo solicita o tamanho em metros
#quadrados da área a ser colocado o piso. Cada piso tem 60 × 60 centímetros; eles são vendidos em
#caixas com 10 pisos, que custam R$ 70,00. Mostre na tela para o cliente a quantidade de caixas que
#ele deve comprar e o preço total do orçamento.

metros = float(input("Informe o tamanho do piso em m²: "))

# Cada piso tem 0,36m^2. Logo, uma caixa com 10 pisos tem 3,6m^2 de piso.
CAIXA = 3.6
quantidade = metros % CAIXA #Variável quantidade recebe a parte inteira de caixas.

if quantidade != 0:
    caixas = (metros // CAIXA) + 1

valor = round((caixas * 70), 2)

print("Serão necessárias {0} caixas de piso, totalizando R${1}.".format(caixas, valor))