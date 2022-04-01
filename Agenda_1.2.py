"""
Autor Heitor de Carvalho
Projeto: Agenda 1.1
1.0: Capacidade de 10 nomes. Devo conter nome, telefone e email.
Funções obrigatórias: Adicionar, Remover, Localizar*, Mostrar agenda toda, Mostrar Contato
*Não interativo diretamente com usuário

1.1: Validação estrutural do email no formato exemple@exemple.com ou exemple@exemple.com

1.2: Formatação do telefone para celular (00)12345-6789 ou fixo (00)1234-5678 caso não possua a quantidade certa de
     números deve realizar a recusa
"""
from Custom_Libraries.Auxiliar_functions import imprime_validade, formata_telefone

"""-------------------------------------Declaração da classe agenda---------------------------------------------"""


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
print(contatos.armazena())
print(contatos.busca_pessoa("New"))
contatos.imprime_pessoa("New")
contatos.imprime_agenda()
contatos.remove_pessoa("New")
# Menu da agenda
while True:
    op = input("(A)diciona|(L)ocaliza|(R)emove|(C)ontatos|(P)essoa|(S)air:")
    # =====Menu Operacional de adicionar contato======================================================================
    if op.upper() == 'A':
        contatos.nome = input("Insira o nome:")
        while True:
            aux_tel = input("Insira o telefone:")
            aux_txt, aux_valida = formata_telefone(aux_tel)
            if aux_valida:
                contatos.telefone = aux_txt
                break
            print(f'Formato de número {aux_txt}')
        # =====Chama validador de e-mail==============================================================================
        while True:
            conta = input("Insira o email:")
            aux_txt, aux_valida = imprime_validade(conta)
            if aux_valida:
                contatos.email = conta
                break
            print(f'E-mail {aux_txt} Insira um valor correto')
        contatos.armazena()
    # =====Menu Operacional de localizar contato======================================================================
    elif op.upper() == 'L':
        busca = input("Digite o nome a ser encontrado:")
        print(f'{busca} está no index:{contatos.busca_pessoa(busca)}')
    # =====Menu Operacional de remover contato========================================================================
    elif op.upper() == 'R':
        busca = input("Digite o nome a ser removido:")
        contatos.remove_pessoa(busca)
    # =====Menu Operacional de imprimir agenda completa===============================================================
    elif op.upper() == 'C':
        contatos.imprime_agenda()
    # =====Menu Operacional de imprimir contato expecífico============================================================
    elif op.upper() == 'P':
        busca = input("Digite o nome a ser localizado:")
        contatos.imprime_pessoa(busca)
    # =====Menu Operacional para sair do programa=====================================================================
    elif op.upper() == 'S':
        exit(0)
    # =====Menu Operacional de invalidação de comando=================================================================
    else:
        print("Comando inválido!!")
