Algoritmo "calculadora aninhada"


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
                    escreva("Operador inválido")
               fimse
          fimse
     fimse
fimse


Fimalgoritmo