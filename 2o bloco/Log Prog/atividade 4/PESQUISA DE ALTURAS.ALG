Algoritmo "PESQUISA DE ALTURAS"
// Autor(a)    : Raphael Kênnedy
// Data atual  : 10/4/2022
Var
sexo: vetor [0..9] de inteiro
altura: vetor [0..9] de real
media, total, percent: real
count, aux: inteiro
alt_Maior, alt_Menor: real
MIN, MAX: inteiro const

Inicio
MIN <- 0
MAX <- 9

para count de MIN ate MAX faca
     escreva("Informe o sexo da ", count + 1, "ª pessoa (masculino = 0 | feminino = 1: ")
     leia(sexo[count])
     escreva("Informe a altura da ", count + 1, "ª pessoa: ")
     leia(altura[count])
fimpara


//Encontrando a maior e a menor altura
alt_Maior <- altura[0]
alt_Menor <- altura[0]

para count de MIN ate MAX faca
     se altura[count] < alt_Menor entao
        alt_Menor <- altura[count]
     fimse
     
     se altura[count] > alt_Maior entao
        alt_Maior <- altura[count]
     fimse
fimpara


//Encontrando a altura média das mulheres
media <- 0
aux <- 0
para count de MIN ate MAX faca
     se sexo[count] = 1 entao
        media <- altura[count] + media
        aux <- aux + 1
     fimse
fimpara

media <- media / aux


//Encontrando a altura média da população
total <- 0
para count de MIN ate MAX faca
     total <- total + altura[count]
fimpara

total <- total / (MAX + 1)

//Encontrando o percentual de homens
percent <- 0
para count de MIN ate MAX faca
     se sexo[count] = 0 entao
        percent <- percent + 1
     fimse
fimpara

percent <- (percent / (MAX + 1)) * 100
escreval("============================")
escreval("A maior altura é ", alt_Maior, "m e a menor é ", alt_menor, "m.")
escreval("A altura média das mulheres é de ", media, "m.")
escreval("A altura média da população é de ", total, "m.")
escreval("O percentual de homens nessa população é de ", percent, "%.")


Fimalgoritmo