Algoritmo "É triangulo?"


Var
   l1, l2,  l3, aux, aux2, aux3: real


Inicio
   escreva("Informe o lado 1: ")
   leia(l1)
   escreva("Informe o lado 2: ")
   leia(l2)
   escreva("Informe o lado 3: ")
   leia(l3)

   //Aqui vamos testar se é um triângulo. Matematicamente, um triângulo só pode
   //existir se a soma dos lados menores for igual ou maior que a soma do lado
   //maior


   //Primeiro encontramos o lado maior
   //as variáveis auxiliares 2 e 3 servem apenas para simplificar o proximo se

   se ((l1 >= l2) e (l1 >= l3)) entao
      aux <- l1
      aux2 <- l2
      aux3 <- l3

   senao
      se ((l2 >= l1) e (l2 >= l3)) entao
         aux <- l2
         aux2 <- l1
         aux3 <- l3

      senao
         se ((l3 >= l2) e (l3 >= l1)) entao
            aux <- l3
            aux2 <- l2
            aux3 <- l1
         fimse
      fimse
   fimse


   aux2 <- aux2 + aux3

   //Em seguida testamos a fórmula A <= B + C e se os lados são negativos
   se((aux > aux2) ou ((l1 <= 0) ou (l2 <= 0) ou (l3 <= 0))) entao
      escreva("Não é um triângulo.")
      //Caso entre no senao, quer dizer que é um triângulo. Nos resta saber qual
   senao
      se((l1 = l2) e (l2 = l3) e (l3 = l1)) entao
         escreva("É um triangulo equilátero.")
      senao
         se (l1 = l2) e (l2 <> l3) e (l1 <> l3) entao
            escreva("É um triangulo isósceles.")
         senao
            se ((l1 <> l2) e (l3 <> l1) e (l2 <> l3)) entao
               escreva("É um triangulo escaleno")

            fimse
         fimse
      fimse
   fimse


Fimalgoritmo
