Algoritmo "FATORIAL"
// Autor(a)    : Raphael K�nnedy
// Data atual  : 10/4/2022
Var
   num: inteiro
   x, z: inteiro


Inicio

//aqui testamos se o n�mero informado � positivo
   x <- 0
   enquanto x = 0 faca
      escreva("Insira um n�mero: ")
      leia(num)

      se num < 1 entao
         escreva("Entrada inv�lida.")
      senao
         x <- 1
      fimse
   fimenquanto
   
//aqui calculamos o fatorial. Como a ordem dos fatores n�o altera o resultado,
//fiz o range crescente ao inv�s de decrescente.
   para z de 2 ate (num-1) faca
        num <- num * z

   fimpara
   
   escreva(num)


Fimalgoritmo