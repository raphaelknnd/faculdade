Algoritmo "Imposto"


Var
salBruto, salLiquido, al: REAL

Inicio
escreva("Informe o salario base: ")
leia(salBruto)

//Calcula o caso do salário ser menor que a borda inferior
SE (salBruto < 1903.98) ENTAO
   salLiquido <- salBruto
   al <- 0
FIMSE

//Caso do salário ser maior que a borda inferior e a primeira borda superior
SE ((salBruto >= 1903.90) E (salBruto < 2826.65)) ENTAO
   salLiquido <- salBruto - ((salBruto * 7.5) / 100)
   al <- 7.5
FIMSE

//Caso do salário estar entre a primeira borda superior e a última
SE ((salBruto >= 2826.65) E (salBruto < 3751.06)) ENTAO
   salLiquido <- salBruto - ((salBruto * 22.5) / 100)
   al <- 22.5
FIMSE

//Caso do salário ser maior que a última borda superior
SE (salBruto >= 3751.06) ENTAO
   salLiquido <- salBruto - ((salBruto * 27.5) / 100)
   al <- 27.5
FIMSE

escreva("O salário líquido é R$", salLiquido, " e o AL é de", al,  "%.")

Fimalgoritmo