Algoritmo "Formas de pagamento"
//
//
// Elabore um algoritmo que calcule o que deve ser pago por um produto,
// considerando o preço normal de etiqueta e a escolha da condição de pagamento.
// Utilize os códigos da tabela a seguir para ler qual a condição de pagamento
// escolhida e efetuar o cálculo adequado.
// Código Condição de pagamento
// À vista em dinheiro ou cheque, recebe 15% de desconto
// À vista no cartão de crédito, recebe 10% de desconto
// Em duas vezes, preço normal de etiqueta sem juros
// Em duas vezes, preço normal de etiqueta mais juros de 10%
Var
   preco: REAL
   pagamento: INTEIRO

Inicio
   escreva("Informe o valor do produto: R$")
   leia(preco)

   escreval("================ FORMA DE PAGAMENTO ==================")
   escreval("| 1. À vista no dinheiro ou cheque |  15% de desconto|")
   escreval("| 2. À vista no cartão de crédito  |  10% de desconto|")
   escreval("| 3. Em duas vezes                 | Sem juros       |")
   escreval("| 4. Três ou mais vezes            | 10% de juros    |")
   escreval("======================================================")

   escreva("Forma de pagamento: ")
   leia(pagamento)

   SE pagamento = 1 ENTAO
      preco <- preco - (preco * 0.15)
      escreva("Deverá ser pago R$", preco)
   SENAO
      SE pagamento = 2 ENTAO
         preco <- preco - (preco * 0.10)
         escreva("Deverá ser pago R$", preco)
      SENAO
         SE pagamento = 3 ENTAO
            preco <- preco
            escreva("Deverá ser pago R$", preco)
         SENAO
            SE pagamento = 4 ENTAO
               preco <- preco + (preco * 0.10)
               escreva("Deverá ser pago R$", preco)
            SENAO
               escreval("Informe uma forma de pagamento válida")
            FIMSE
         FIMSE
      FIMSE
   FIMSE

Fimalgoritmo