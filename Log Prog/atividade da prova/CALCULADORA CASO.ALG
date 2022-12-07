Algoritmo "calculadora caso"
//
//
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 12/4/2022
Var
   operador: caractere
   num1, num2, res: real


Inicio
   escreva("Informe o primeiro numero: ")
   leia(num1)
   escreva("Informe o segundo numero: ")
   leia(num2)

   escreval("| + | Adição        |")
   escreval("|-------------------|")
   escreval("| - | Subtração     |")
   escreval("|-------------------|")
   escreval("| * | Multiplicação |")
   escreval("|-------------------|")
   escreval("| / | Divisão       |")
   escreval("|-------------------|")
   escreva("Informe a operação: ")
   leia(operador)
   
   //switch case inicia aqui
   escolha operador
   
   caso "+"
        res <- num1 + num2
        escreva(res)
   caso "-"
        res <- num1 - num2
        escreva(res)
   caso "*"
        res <- num1 * num2
        escreva(res)
   caso "/"
        res <- num1 / num2
        escreva(res)
   outrocaso
            escreva("Operador inválido")
   fimescolha

Fimalgoritmo