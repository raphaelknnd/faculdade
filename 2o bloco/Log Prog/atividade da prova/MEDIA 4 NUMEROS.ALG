Algoritmo "MEDIA 4 NUMEROS"

Var
num: vetor [0..3] de real
count: inteiro
resultado: real
Inicio
enquanto count < 4 faca
         escreva("Informe o numero: ")
         leia(num[count])
         count <- count + 1
fimenquanto

count <- 0

enquanto count < 4 faca
       resultado <- num[count] + resultado
       count <- count + 1
fimenquanto

escreva(resultado / 4)


Fimalgoritmo