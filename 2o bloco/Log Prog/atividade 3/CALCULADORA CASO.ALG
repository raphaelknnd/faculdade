Algoritmo "calculadora caso"
//
//
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 9/20/2022
Var
   operador: caractere
   num1, num2, res: real


Inicio
   escreva("Informe o primeiro numero: ")
   leia(num1)
   escreva("Informe o segundo numero: ")
   leia(num2)

   escreval("| + | Adi��o        |")
   escreval("|-------------------|")
   escreval("| - | Subtra��o     |")
   escreval("|-------------------|")
   escreval("| * | Multiplica��o |")
   escreval("|-------------------|")
   escreval("| / | Divis�o       |")
   escreval("|-------------------|")
   escreva("Informe a opera��o: ")
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
            escreva("Operador inv�lido")
   fimescolha

Fimalgoritmo