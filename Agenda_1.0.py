"""
Autor Heitor de Carvalho
Projeto: Agenda 1.0
Objetivo: Capacidade de 10 nomes. Devo conter nome, telefone e email.
Funções obrigatórias: Adicionar, Remover, Localizar*, Mostrar agenda toda, Mostrar Contato
*Não interativo diretamente com usuário
"""


class Agenda:
    """-------------------------------------------Atributos de Classe-------------------------------------------"""
    lista = []
    limite = 10

    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    """---------------------------------------Getters e Setters dos atributos---------------------------------------"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    """------------------------------------------------Métodos-------------------------------------------------"""
    def armazena(self):
        """Método responsável por armazenar os dados na lista"""
        if len(Agenda.lista) < Agenda.limite:
            Agenda.lista.append((self.__nome, self.__telefone, self.__email))
            return print('Contato armazenado')
        else:
            return print("AGENDA CHEIA!!!!!")

    @staticmethod
    def busca_pessoa(pessoa):
        """Método responsável pela busca na lista, retorna posição no index"""
        for i in range(0, len(Agenda.lista)):
            if pessoa == Agenda.lista[i][0]:
                return i
        return f'{pessoa} não está na lista!!!!'

    @staticmethod
    def imprime_pessoa(nome):
        index = Agenda.busca_pessoa(nome)
        if type(index) == int:
            print(f'Nome: {Agenda.lista[index][0]}|'
                  f'Idade: {Agenda.lista[index][1]}|'
                  f'Altura: {Agenda.lista[index][2]}')
        else:
            print(index)

    @staticmethod
    def imprime_agenda():
        for i in range(0, len(Agenda.lista)):
            print(Agenda.lista[i])

    @staticmethod
    def remove_pessoa(nome):
        index = Agenda.busca_pessoa(nome)
        if type(index) == int:
            Agenda.lista.__delitem__(index)
            print("Contato removido com sucesso!")
        else:
            return index


"""________________________________________________________________________________________________________________
----------------------------------------Programa principal------------------------------------------------------"""
contatos = Agenda("New", "(00)0000-0000", "new@new.com")
contatos.armazena()
print(contatos.busca_pessoa("New"))
contatos.imprime_pessoa("New")
contatos.imprime_agenda()
contatos.remove_pessoa("New")
# Menu da agenda
while True:
    op = input("(A)diciona|(L)ocaliza|(R)emove|(C)ontatos|(P)essoa|(S)air:")
    if op.upper() == 'A':
        contatos.nome, contatos.telefone, contatos.email = input("Insira o nome:"), \
                                                           input("Insira o idade:"), \
                                                           input("Insira o altura:")
        contatos.armazena()
    elif op.upper() == 'L':
        busca = input("Digite o nome a ser encontrado:")
        print(f'{busca} está no index:{contatos.busca_pessoa(busca)}')
    elif op.upper() == 'R':
        busca = input("Digite o nome a ser removido:")
        contatos.remove_pessoa(busca)
    elif op.upper() == 'C':
        contatos.imprime_agenda()
    elif op.upper() == 'P':
        busca = input("Digite o nome a ser localizado:")
        contatos.imprime_pessoa(busca)
    elif op.upper() == 'S':
        exit(0)
    else:
        print("Comando inválido!!")
