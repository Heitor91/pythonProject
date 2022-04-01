"""
Atributos REpresentam as caracteristicas do objeto

Em python dividimos os os atributos em 3 grupos:
- Atributos de classe
- Atributos de instância
- Atributos dinâmicos


# Atributos de instancia: São atributos  declarados dentro de um metodo construtor

#OBS: Método construtor é um metodo especial para construção de um objeto.

"""
# Classe de instância publica

class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

# Atributos de instância podem ser publicos ou privados
# Em python por convenção ficou estabelecido que todo atributo de uma classe é publico
# ou seja pode ser acessado em todo o projeto
# para ser tratado como privado deve se utilizar o underscore no inicio de seu nome


#Atributos privados

class Produto:

    imposto = 1.05  # Imposto de 5%

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha


# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email)
#print(user.__senha)  #Error Atrubute

print(user._Acesso__senha)  #Temos acesso, mas não deveríamos dele

#Atributos de Classe
p1 = Produto('PlayStation4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.imposto)
print(p2.imposto)
print(p1.valor)
print(p2.valor)
