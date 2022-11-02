# 3. Faça um programa que descubra se uma palavra é ou não um palíndromo. Um palíndromo é
# uma sequência de caracteres que, quando lidos do fim para o começo, são idênticos à palavra original.
# Exemplos: Ana, ovo, osso, ama e arara são palíndromos.

def palindromo(palavra):
  return palavra[::-1] # [::-1] retorna a string ao contrário por conta do terceiro parâmetro "-1"

palavra = input("Informe uma palavra: ")

aux = palindromo(palavra)

print("Sua palavra foi {}".format(palavra))
print("A palavra invertida é {}".format(aux))

if aux == palavra:
  print("É um palíndromo")
else:
  print("Não é")