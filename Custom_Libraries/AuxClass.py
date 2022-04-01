# =====================================================================================================================
# =====================================================Classe Agenda===================================================
# =====================================================================================================================
class Agenda:
    """-------------------------------------------Atributos de Classe-------------------------------------------"""
    lista = []
    limite = 10

    def __init__(self, nome, telefone, email, sobrenome, empresa, cargo, data_de_nascimento):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data_de_nascimento = data_de_nascimento
        self.__telefone = telefone
        self.__email = email
        self.__empresa = empresa
        self.__cargo = cargo
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

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento
    """------------------------------------------------Métodos-------------------------------------------------"""
    def armazena(self):
        """Método responsável por armazenar os dados na lista"""
        if len(Agenda.lista) < Agenda.limite:
            Agenda.lista.append((self.__nome, self.__sobrenome, self.__data_de_nascimento,
                                 self.__telefone, self.__email, self.__empresa, self.__cargo))
            return 'Contato armazenado'
        else:
            return "AGENDA CHEIA!!!!!"

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
                  f'Telefone: {Agenda.lista[index][1]}|'
                  f'E-mail: {Agenda.lista[index][2]}')
        else:
            print(index)

    @staticmethod
    def imprime_agenda():
        def espacador():
            print("=" * 30)
        espacador()
        for i in range(0, len(Agenda.lista)):
            print(f'Contato: {Agenda.lista[i][0]} {Agenda.lista[i][1]}\t'
                  f'Data de Nascimento: {Agenda.lista[i][2]}\n'
                  f'Telefone(s): {Agenda.lista[i][3][0]} {Agenda.lista[i][3][1]} {Agenda.lista[i][3][2]}\n'
                  f'E-mail(s): {Agenda.lista[i][4][0]} {Agenda.lista[i][4][0]}\n'
                  f'Empresa: {Agenda.lista[i][5]}\t'
                  f'Cargo: {Agenda.lista[i][6]}')
            espacador()

    @staticmethod
    def remove_pessoa(nome):
        index = Agenda.busca_pessoa(nome)
        if type(index) == int:
            Agenda.lista.__delitem__(index)
            print("Contato removido com sucesso!")
        else:
            return index

    @staticmethod
    def start_class():
        aux = Agenda("", "", "", "", "", "", "")
        aux.remove_pessoa("")
        return aux
