Algoritmo "pares e impares"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/29/2022
Var
par, impar, numero, count: inteiro


Inicio
enquanto count < 150 faca
         escreva("Informe o numero: ")
         leia(numero)
         
         se numero mod 2 = 0 entao
            par <- par + numero
         senao
              impar <- impar + numero
         fimse
         
         count <- count + 1
fimenquanto

escreval("Pares: ", par)
escreval("Impares: ", impar)
escreval("Soma: ", par + impar)

Fimalgoritmo