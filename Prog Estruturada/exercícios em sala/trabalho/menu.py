# Agenda de Contatos
agenda = []


def adiciona(nome, tel):
  agenda.append([nome,tel])

print('-'*30)
print('     Agendar de Contatos')
print('-'*30)

def mostraContato(nome):
  for i in range(len(agenda)):
    if(nome == agenda[i][0]):
      print(*agenda[i])
      break

def mostraLista():
  if(len(agenda) == 0):
    print('Agenda vazia')
  else:
    for contato in agenda:
      print(*contato)

def apagaContato(nome):
  for i in range(len(agenda)):
    if(nome == agenda[i][0]):
      agenda[i].clear()
      break

def apagaTodosContatos():
  agenda.clear()


while True:
  print('1 - Cadastrar contato;')
  print('2 - Listar contato;')
  print('3 - Listar todos os contatos;')
  print('4 - Apagar contato;')
  print('5 - Apagar todos os contatos;')
  print('6 - Sair.')

  op = int(input('Entre com a opção desejada: '))

  if op == 1:
    nome = input('Digite o nome:')
    tel = int(input('Digite o telefone:'))
    adiciona(nome,tel)
    print("Contato adicionado!")
  elif op == 2:
    nome = input('Digite o nome para a pesquisa:')
    print('-'*30)
    mostraContato(nome)
    print('-'*30)
  elif op == 3:
    print('-'*30)
    print('Todos os contatos')
    mostraLista()
    print('-'*30)
  elif op == 4:
    nome = input('Digite o nome para a pesquisa:')
    apagaContato(nome)
  elif op == 5:
    apagaTodosContatos()
    print("Todos os contatos foram apagados")
  elif op == 6:
    break
  else:
    print('Digite a opção correta!')

print('-'*30)
print('Obrigado por usar a agenda!!!')
print('-'*30)