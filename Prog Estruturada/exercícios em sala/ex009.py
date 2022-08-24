#9. Faça um programa que pergunte ao usuário o valor que ele tem investido e a taxa percentual
#que ele ganha ao mês (juros simples). Calcule e imprima o total ganho com o investimento em 3 meses.

invest =  input("Informe os investimentos: ")
mes = input("Informe a quantidade de meses: ")
juros = input("Informe a taxa de juros: ")

ganho = float(invest) * (float(juros) / 100) * int(mes)

print("O ganho é de R$" + str(ganho))