# Agenda de Contatos
agenda = {}


def adiciona(nome, tel):
    agenda[nome] = tel


def mostraContato(nome):
    if nome in agenda:
        print(nome.capitalize(), end=' ')
        print(agenda[nome])
    else:
      print('Contato não encontrado')


def mostraLista():
    if len(agenda) == 0:
        print('Agenda Vazia!')
    else:
        for contato in agenda.items():
            print(*contato)


def apagaContato(nome):
    if nome in (agenda):
        agenda.pop(nome)
    else:
      print('Contato não encontrado')

def apagaTodosContatos():
    agenda.clear()


print('-'*30)
print('     Agendar de Contatos')
print('-'*30)

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
    nome = nome.lower()
    adiciona(nome,tel)
    print("Contato Adicionado!")
  elif op == 2:
    nome = input('Digite o nome para a pesquisa:')
    nome = nome.lower()
    print('-'*30)
    mostraContato(nome)
    print('-'*30)
  elif op == 3:
    print('-'*30)
    print('     Todos os contatos')
    mostraLista()
    print('-'*30)
  elif op == 4:
    nome = input('Digite o nome para a pesquisa:')
    apagaContato(nome)
  elif op == 5:
    apagaTodosContatos()
    print("Todos contatos foram deletados!")
  elif op == 6:
    break
  else:
    print('Digite a opção correta!')

print('-'*30)
print('Obrigado por usar a agenda!!!')
print('-'*30)