class Teste:

    lista = []

    def __init__(self, var, var2):
        self.__var = var
        self.__var2 = var2

    @property
    def var(self):
        return self.__var

    @property
    def var2(self):
        return self.__var2

    @var.setter
    def var(self, var):
        self.__var = var

    @var2.setter
    def var2(self, var2):
        self.__var2 = var2

    def insere(self):
        Teste.lista.append([self.__var, self.__var2])

    @staticmethod
    def remove(index):
        Teste.lista.__delitem__(index)


def inicia():
    aux = Teste('a', 'b')
    aux.insere()
    aux.remove(0)
    return aux
