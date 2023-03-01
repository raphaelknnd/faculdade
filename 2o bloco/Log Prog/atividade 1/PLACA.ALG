Algoritmo "placa"
//
Var
   placa: inteiro


Inicio
   escreva("Informe o final da placa: ")
   leia(placa)

   se ((placa = 1) ou (placa = 2)) entao
      escreva("Seu veículo não pode rodar  na segunda")

   senao
      se ((placa = 3) ou (placa = 4)) entao
         escreva("Seu veículo não pode rodar na terça")

      senao
         se ((placa = 5) ou (placa = 6)) entao
            escreva("Seu veículo não pode rodar na quarta")

         senao
            se ((placa = 7) ou (placa = 8)) entao
               escreva("Seu veículo não pode rodar na quinta")

            senao
               se ((placa = 9) ou (placa = 0)) entao
                  escreva("Seu veículo não pode rodar na sexta")
               fimse
            fimse
         fimse
      fimse
   fimse



Fimalgoritmo