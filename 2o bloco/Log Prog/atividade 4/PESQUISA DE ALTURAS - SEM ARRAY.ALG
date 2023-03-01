Algoritmo "PESQUISA DE ALTURAS"
// Autor(a)    : Raphael Kênnedy
// Data atual  : 10/4/2022
Var
sexo, masc, fem: inteiro
altura, alturaH, alturaM: real
media, total, percent: real
alt_Maior, alt_Menor: real
MIN, MAX: inteiro const

Inicio
MIN <- 0
MAX <- 1
alt_Menor <- 10000 //inteiro muito grande

para count de MIN ate MAX faca
     escreva("Informe o sexo da ", count + 1, "ª pessoa (masculino = 0 | feminino = 1: ")
     leia(sexo)
     escreva("Informe a altura da ", count + 1, "ª pessoa: ")
     leia(altura)
     
     //verificando se é masculino ou feminino e guardando os valores
     se sexo = 0 entao
        alturaH <- alturaH + altura
        masc <- masc + 1
     senao
          se sexo = 1 entao
             alturaM <- alturaM + altura
             fem <- fem + 1
          fimse
     fimse
     
     //Encontrando a maior e a menor altura
     se altura > alt_Maior entao
        alt_Maior <- altura
     fimse
     
     se altura < alt_Menor entao
        alt_Menor <- altura
     fimse
     
fimpara

//Encontrando a altura média das mulheres
media <- alturaM / fem


//Encontrando a altura média da população
total <- (alturaM + alturaH) / (MAX + 1)

//Encontrando o percentual de homens
percent <- (masc / (MAX + 1)) * 100
escreval("============================")
escreval("A maior altura é ", alt_Maior, "m e a menor é ", alt_menor, "m.")
escreval("A altura média das mulheres é de ", media, "m.")
escreval("A altura média da população é de ", total, "m.")
escreval("O percentual de homens nessa população é de ", percent, "%.")


Fimalgoritmo