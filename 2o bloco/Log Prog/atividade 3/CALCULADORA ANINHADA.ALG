Algoritmo "calculadora aninhada"


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

se operador = "+" entao
   res <- num1 + num2
   escreva(res)
senao
     se operador = "-" entao
        res <- num1 - num2
        escreva(res)
     senao
          se operador = "*" entao
             res <- num1 * num2
             escreva(res)
          senao
               se operador = "/" entao
                  res <- num1 / num2
                  escreva(res)
               senao
                    escreva("Operador inv�lido")
               fimse
          fimse
     fimse
fimse


Fimalgoritmo