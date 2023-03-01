Algoritmo "FATORIAL"
// Autor(a)    : Raphael Kênnedy
// Data atual  : 10/4/2022
Var
   num: inteiro
   x, z: inteiro


Inicio

//aqui testamos se o número informado é positivo
   x <- 0
   enquanto x = 0 faca
      escreva("Insira um número: ")
      leia(num)

      se num < 1 entao
         escreva("Entrada inválida.")
      senao
         x <- 1
      fimse
   fimenquanto
   
//aqui calculamos o fatorial. Como a ordem dos fatores não altera o resultado,
//fiz o range crescente ao invés de decrescente.
   para z de 2 ate (num-1) faca
        num <- num * z

   fimpara
   
   escreva(num)


Fimalgoritmo