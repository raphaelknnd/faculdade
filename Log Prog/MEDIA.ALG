Algoritmo "media"
//
//
// Descrição   : Calcula a media de dois alunos
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 8/23/2022
Var
   nota1, nota2, resultado: REAL
   count: INTEIRO //contador auxiliar dos laços de repetição


Inicio

   //O código inicia fazendo a validação da peimeira nota (PRESENCIAL)
   //A lógica não deixa o usuário sair enquanto não informar uma nota válida.
   count <- 0
   enquanto (count = 0) faca
      escreva("Informe a nota PRESENCIAL: ")
      leia(nota1)
      se (nota1 > 10) ou (nota1 < 0) entao
         escreval("Nota invalida. Insira um valor entre 0 e 10")
      senao
         count <- 1
      fimse
   fimenquanto

   //Aqui segue informando a segunda nota (ONLINE)
   //Assim como no anterior, não sai enquanto não informar uma nota válida.
   count <- 0
   enquanto (count = 0) faca
      escreva("Informe a nota ONLINE: ")
      leia(nota2)
      se (nota2 > 10) ou (nota2 < 0) entao
         escreval("Nota invalida. Insira um valor entre 0 e 10")
      senao
         count <- 1
      fimse
   fimenquanto

   resultado <- (nota1 * 0.6) + (nota2 * 0.4)

   se resultado >= 5 entao
      escreval("Aluno aprovado. Media ", resultado, ".")
   senao
      escreval("Aluno reproado. Media ", resultado, ".")
   fimse


Fimalgoritmo