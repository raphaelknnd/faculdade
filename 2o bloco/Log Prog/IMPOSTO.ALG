Algoritmo "Imposto"


Var
salBruto, salLiquido, al: REAL

Inicio
escreva("Informe o salario base: ")
leia(salBruto)

//Calcula o caso do sal�rio ser menor que a borda inferior
SE (salBruto < 1903.98) ENTAO
   salLiquido <- salBruto
   al <- 0
FIMSE

//Caso do sal�rio ser maior que a borda inferior e a primeira borda superior
SE ((salBruto >= 1903.90) E (salBruto < 2826.65)) ENTAO
   salLiquido <- salBruto - ((salBruto * 7.5) / 100)
   al <- 7.5
FIMSE

//Caso do sal�rio estar entre a primeira borda superior e a �ltima
SE ((salBruto >= 2826.65) E (salBruto < 3751.06)) ENTAO
   salLiquido <- salBruto - ((salBruto * 22.5) / 100)
   al <- 22.5
FIMSE

//Caso do sal�rio ser maior que a �ltima borda superior
SE (salBruto >= 3751.06) ENTAO
   salLiquido <- salBruto - ((salBruto * 27.5) / 100)
   al <- 27.5
FIMSE

escreva("O sal�rio l�quido � R$", salLiquido, " e o AL � de", al,  "%.")

Fimalgoritmo