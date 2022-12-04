Algoritmo "maior e menor"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/29/2022
Var
numero, maior, menor, count: inteiro


Inicio
maior <- -1000000
menor <- 100000
enquanto count < 10 faca
         escreva("Informe um numero: ")
         leia(numero)
         
         se numero < menor entao
            menor <- numero
         fimse
         
         se numero > maior entao
            maior <- numero
         fimse
         
         count <- count + 1
            
fimenquanto

escreval("Maior: ", maior)
escreval("Menor: ", menor)

Fimalgoritmo