Algoritmo "� PRIMO?"
// Autor(a)    : Raphael K�nnedy
// Data atual  : 10/4/2022
Var
   num, aux, x, y: inteiro
   resto: real


Inicio
   escreva("Informe um n�mero: " )
   leia(num)

   aux <- 2
   y <- 1
   se num = 1 entao
      escreva("N�o � primo!")
   senao
      enquanto (x = 0) faca
         se num % aux = 0 entao
            x <- 1
         senao
            aux <- aux + 1
         fimse

         se aux = num entao
            x <- 1
            y <- 0
         fimse
      fimenquanto
   fimse

   se y = 0 entao
      escreva("� Primo!")
   fimse

   se y = 1 entao
      escreva("N�o � primo")
   fimse

Fimalgoritmo