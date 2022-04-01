"""
Heitor de Carvalho
Programa: agenda para 10 contatos contendo nome, idade e altura
"""


class Contatos:

    lista = []
    limite = 10

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def armazena(self):
        if len(Contatos.lista) < Contatos.limite:
            Contatos.lista.append((self.__nome, self.__idade, self.__altura))
            return print('Contato armazenado')
        else:
            return print("AGENDA CHEIA!!!!!")

    @staticmethod
    def remove_pessoa(nome):
        index = Contatos.busca_pessoa(nome)
        if type(index) == int:
            Contatos.lista.__delitem__(index)
            return print("Contato removido com sucesso!")
        else:
            return index

    @staticmethod
    def busca_pessoa(pessoa):
        for i in range(0, len(Contatos.lista)):
            if pessoa == Contatos.lista[i][0]:
                return i
        return f'{pessoa} não está na lista!!!!'

    @staticmethod
    def imprime_agenda():
        for i in range(0, len(Contatos.lista)):
            print(Contatos.lista[i])

    @staticmethod
    def imprime_pessoa(nome):
        index = Contatos.busca_pessoa(nome)
        if type(index) == int:
            print(f'Nome: {Contatos.lista[index][0]}|'
                  f'Idade: {Contatos.lista[index][1]}|'
                  f'Altura: {Contatos.lista[index][2]}')
        else:
            print(index)


"""--------------------------------------------------------------------------------------------------------------------
main:
--------------------------------------------------------------------------------------------------------------------"""
agenda = Contatos("New", 99, 9.99)
agenda.armazena()
agenda.remove_pessoa("New")
while True:
    op = input("(A)diciona|(L)ocaliza|(R)emove|(C)ontatos|(P)essoa|(S)air:")
    if op.upper() == 'A':
        agenda.nome, agenda.idade, agenda.altura = input("Insira o nome:"), \
                                                   input("Insira o idade:"), \
                                                   input("Insira o altura:")
        agenda.armazena()
    elif op.upper() == 'L':
        busca = input("Digite o nome a ser encontrado:")
        print(f'{busca} está no index:{agenda.busca_pessoa(busca)}')
    elif op.upper() == 'R':
        busca = input("Digite o nome a ser removido:")
        agenda.remove_pessoa(busca)
    elif op.upper() == 'C':
        agenda.imprime_agenda()
    elif op.upper() == 'P':
        busca = input("Digite o nome a ser localizado:")
        agenda.imprime_pessoa(busca)
    elif op.upper() == 'S':
        exit(0)
    else:
        print("Comando inválido!!")
