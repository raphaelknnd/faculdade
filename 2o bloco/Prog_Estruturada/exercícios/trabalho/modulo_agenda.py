# Agenda de Contatos
agenda = {}

arquivo = open('agenda_texto.txt', 'at')


def gravaAgenda():
    if len(agenda) == 0:
        print("Agenda vazia .")
    else:
        for contato in agenda.items():
            contatoStr = ' '.join(map(str, contato))
            arquivo.write(contatoStr)
        print("Agenda Gravada!")
        arquivo.close()


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