Algoritmo "Dobro e triplo"
//
//
// Descri��o   : Encontrar o dobro de um n�mero caso ele seja positivo e o
//               seu triplo caso seja negativo, imprimindo o resultado.
Var
   num: INTEIRO


Inicio
   escreva("Informe um n�mero: ")
   leia(num)

   SE num > 0 ENTAO
      num <- num * 2
   SENAO
      SE num < 0 ENTAO
         num <- num * 3
      FIMSE
   FIMSE
   
   escreva("Numero final =", num)


Fimalgoritmo