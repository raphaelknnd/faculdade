Algoritmo "Baskara"

Var
   delta, a, b, c, x1, x2: real

Inicio
   escreva("Informe o valor de a: ")
   leia(a)
   escreva("Informe o valor de b: ")
   leia(b)
   escreva("Informe o valor de c: ")
   leia(c)

   //aqui calcularemos o valor de delta

   delta <- (b^2) - (4 * a * c)

   //testamos se delta � menor que zero

   se (delta < 0) entao
      escreva("A equa��o n�o possui valores reais")
      
   //caso delta seja >= 0, continuamos o c�lculo.
   
   senao
      x1 <- (-b + raizq(delta)) / (2 * a)
      x2 <- (-b - raizq(delta)) / (2 * a)
      escreva("As ra�zes s�o ", x1, " e ",  x2)
   fimse



Fimalgoritmo