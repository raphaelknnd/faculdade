Algoritmo "TABUADA DE MULTIPLICAÇÃO"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/4/2022
Var
num, count: inteiro


Inicio
escreva("Informe um numero: ")
leia(num)

para count de 0 ate 10 faca
     escreval(num, " * ", count, " = ", num * count)
fimpara

escreva("==========================")

se num = 0 entao
   escreva("NÂO É POSSÍVEL DIVIDIR")
senao
     para count de 1 ate 10 faca
     escreval(count * num, " / ", num, " = ", (num*count) / num)
fimse
fimpara


Fimalgoritmo
