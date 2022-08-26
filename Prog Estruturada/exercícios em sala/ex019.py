# 19. Construa um programa que solicite o tamanho em megabytes de um arquivo para transferência,
# e a velocidade do link de internet em megabits por segundo. Compute o tempo de transferência do
# arquivo, passando por esse link em minutos. Imprima o resultado na tela. Dica: 1 MB são 1000000 de
# bytes e 1 byte são 8 bits.

arq = float(input("Insira o tamanho do aruivo em MB: "))
band = float(input("Insira a valocidade de transferência em Mbps: "))

convert = (arq * 1000000 * 8) / 1024

tempo = convert / band

print("O tempo de transferência será de {0} segundos.".format(tempo))



