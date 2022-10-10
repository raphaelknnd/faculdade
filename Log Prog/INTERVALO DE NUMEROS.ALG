Algoritmo "INTERVALO DE NUMEROS"
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/4/2022
Var
start, stop, sair, count, pass: inteiro


Inicio
repita
      pass <- 1
      
      escreva("Informe o valor inicial")
      leia(start)
      escreva("Informe o valor final")
      leia(stop)
      
      se start > stop entao
         pass <- -1
      fimse
      
      para count de start ate stop passo pass faca
           escreva(count, " ,")
      fimpara
      
      escreva("Digite 1 para sair: ")
      leia(sair)
      
ate(sair = 1)


Fimalgoritmo