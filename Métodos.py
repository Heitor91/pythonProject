"""
Métodos representam os comportamentos dos objetos, ações que o objeto pode realizar no sistema

Divide-se em métodos de instancia e métodos de classe
"""

from passlib.hash import pbkdf2_sha256 as cryp

# Métodos de Instância


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 1234

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


p1 = Produto("Playstatiom", "VideoGame", 2300)

print(p1.desconto(20))

user1 = Usuario('Angelina', 'Jolie', 'jolie@gmail.com', '123456')

print(f'SENHA USER 1: {user1._Usuario__senha}')
