Algoritmo "Formas de pagamento"
//
//
// Elabore um algoritmo que calcule o que deve ser pago por um produto,
// considerando o pre�o normal de etiqueta e a escolha da condi��o de pagamento.
// Utilize os c�digos da tabela a seguir para ler qual a condi��o de pagamento
// escolhida e efetuar o c�lculo adequado.
// C�digo Condi��o de pagamento
// � vista em dinheiro ou cheque, recebe 15% de desconto
// � vista no cart�o de cr�dito, recebe 10% de desconto
// Em duas vezes, pre�o normal de etiqueta sem juros
// Em duas vezes, pre�o normal de etiqueta mais juros de 10%
Var
   preco: REAL
   pagamento: INTEIRO

Inicio
   escreva("Informe o valor do produto: R$")
   leia(preco)

   escreval("================ FORMA DE PAGAMENTO ==================")
   escreval("| 1. � vista no dinheiro ou cheque |  15% de desconto|")
   escreval("| 2. � vista no cart�o de cr�dito  |  10% de desconto|")
   escreval("| 3. Em duas vezes                 | Sem juros       |")
   escreval("| 4. Tr�s ou mais vezes            | 10% de juros    |")
   escreval("======================================================")

   escreva("Forma de pagamento: ")
   leia(pagamento)

   SE pagamento = 1 ENTAO
      preco <- preco - (preco * 0.15)
      escreva("Dever� ser pago R$", preco)
   SENAO
      SE pagamento = 2 ENTAO
         preco <- preco - (preco * 0.10)
         escreva("Dever� ser pago R$", preco)
      SENAO
         SE pagamento = 3 ENTAO
            preco <- preco
            escreva("Dever� ser pago R$", preco)
         SENAO
            SE pagamento = 4 ENTAO
               preco <- preco + (preco * 0.10)
               escreva("Dever� ser pago R$", preco)
            SENAO
               escreval("Informe uma forma de pagamento v�lida")
            FIMSE
         FIMSE
      FIMSE
   FIMSE

Fimalgoritmo