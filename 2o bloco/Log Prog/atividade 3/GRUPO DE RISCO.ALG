Algoritmo "grupo de risco"
//
//
//
//
Var
   idade, x,  y: inteiro
   peso: real
   grupo: caractere

Inicio
   escreva("Informe sua idade")
   leia(idade)
   escreva("Informe seu peso(em kg)")
   leia(peso)

   // Verificação da faixa etária

   se (idade >= 0) e (idade <= 17) entao
      x <- 1
   senao
      se (idade > 17) e (idade <= 60) entao
         x <- 2
      senao
         se idade > 60 entao
            x <- 3
         fimse
      fimse
   fimse

   // Verificação da faixa de peso

   se peso <= 60 entao
      y <- 1
   senao
      se (peso > 60) e (peso <= 90) entao
         y <- 2
      senao
         se peso > 90 entao
            y <- 3
         fimse
      fimse
   fimse

   // Identificação do grupo de risco

   escolha x
   caso 1
      escolha y
      caso 1
         grupo <- "A"
      caso 2
         grupo <- "B"
      caso 3
         grupo <- "C"
      fimescolha
   caso 2
      escolha y
      caso 1
         grupo <- "D"
      caso 2
         grupo <- "E"
      caso 3
         grupo <- "F"
      fimescolha
   caso 3
      escolha y
      caso 1
         grupo <- "G"
      caso 2
         grupo <- "H"
      caso 3
         grupo <- "I"
      fimescolha
   fimescolha



   escreval("O usuário pertence ao grupo ", grupo)



Fimalgoritmo