# =====================================================================================================================
# Gera uma lista de caracteres inválidos===============================================================================
def caracteres_proibidos():
    lista = [chr(letra) for letra in range(32, 48)]
    lista.extend([chr(letra) for letra in range(58, 97)])
    lista.extend([chr(letra) for letra in range(123, 127)])
    # Remove da lista os caracteres auxiliares válidos
    lista.remove('.')
    lista.remove('_')
    lista.remove('@')
    return lista


# =====================================================================================================================
# O validador analisa o email para validar o formato se esta com os caracteres adequados===============================
def validador_email(conta):
    # Na etapa 1 ele separa a string pelo '@' e precise resultar em uma lista de 2 itens para passar
    if len(conta.split('@')) == 2:
        # Na etapa 2 ele compara o endereçamento se o split resulta em uma lista de 2 ou 3 itens e se o 2 item é '.com'
        if conta.split('@')[1].split('.')[1] == 'com' and 1 < len(conta.split('@')[1].split('.')) < 4:
            # Etapa 3 verifica a existencia de um 3 item do split anterior e se o item 2 possui 2 caracteres somente
            if len(conta.split('@')[1].split('.')) == 3 and len(conta.split('@')[1].split('.')[2]) != 2:
                return False
            # Etapa 4 analisa os caracteres proibidos
            c_proibidos = caracteres_proibidos()
            for letra in conta:
                if letra in c_proibidos:
                    return False
            return True  # Se passar pelos 4 testes recebe aprovação booleana
    else:
        return False


# =====================================================================================================================
# Entrada da variavel email e chama função de validação================================================================
def entra_email():
    # Retorna o resultado da validação=================================================================================
    def imprime_validade(aux):
        validade = validador_email(aux)
        if validade:
            return "válido", validade
        else:
            return 'INVÁLIDO!!!', validade

    while True:
        conta = input("Insira o email:")
        if conta == '':
            return ' ', False
        aux_txt, aux_valida = imprime_validade(conta)
        if aux_valida:
            return conta, True
        print(f'E-mail {aux_txt} Insira um valor correto')


# =====================================================================================================================
# Formata a entrada de valor do parametro de telefone para o padrão (ddd)numero-numero=================================
def formata_telefone(numero):
    if len(numero) == 11 and numero.isnumeric():  # Celular de 9 digitos + DDD
        numero = '(' + numero[:2] + ')' + numero[2:7] + '-' + numero[7:]
        return numero, True
    elif len(numero) == 10 and numero.isnumeric():  # Telefone de 8 digitos + DDD
        numero = '(' + numero[:2] + ')' + numero[2:6] + '-' + numero[6:]
        return numero, True
    # Caso não esteja no padrão aceito recusa o dado
    else:
        return 'inválido', False


# =====================================================================================================================
# Entrada da variavel nome e recusa caso possua algum caractere não alfabético=========================================
def entra_nome(first):
    def sel_condicional(cond):
        if cond:
            return aux_nome.isalpha()
        else:
            return aux_nome.replace(' ', '').isalpha()

    while True:
        aux_nome = (input(f'Insira o {"nome" if first else "sobrenome"}:')).capitalize()
        if aux_nome != "" and sel_condicional(first):
            return aux_nome
        print(f'O {"nome" if first else "sobrenome"} não é completamente alfabético, Insira um nome valido!!!!')


# =====================================================================================================================
# Entrada da variavel telefone e chama função de validação=============================================================
def entra_telefone():
    while True:
        aux_tel = input("Insira o telefone:")
        if aux_tel == '':
            return ' ', False
        aux_txt, aux_valida = formata_telefone(aux_tel)
        if aux_valida:
            return aux_txt, True
        print(f'Formato de número inválido !!!')


# =====================================================================================================================
# Distribuidor de chamada de função ===================================================================================
def lista_contato(tipo):
    """Entrada de dados para telefone e email. Entrada 'True' de for telefone e 'False' de for e-mail. É usado para
    definir as repetições do laço e a chamada de função apropriada"""
    lista = []
    mem_bool = False
    for i in range(3 if tipo else 2):
        numero, val_bool = entra_telefone() if tipo else entra_email()  # Função de entrada do telefone
        lista.append(numero)
        mem_bool = mem_bool or val_bool
    return lista, mem_bool


# =====================================================================================================================
# Formatador de data ==================================================================================================
def data_nascimento():
    while True:
        data = input('Data de nascimento somente numeros(ddmmaaaa):')
        if len(data) == 8:
            dtformatado = data[:2] + '/' + data[2:4] + '/' + data[4:]
            return dtformatado
        print(f'Faltaram {8 - len(data)} digitos!!!' if len(data) < 8 else f'{len(data) - 8} '
                                                                           f'digitos acima do permitido!!!')


# =====================================================================================================================
# Função receptora de empresa e cargo =================================================================================
def empresa():
    def entrada(bolean):
        return input(f'Insira o {"nome da empresa: " if bolean else "cargo exercido: "}').capitalize()

    while True:
        checa = True
        nome = entrada(checa)
        coorp = nome if nome.replace(' ', '').isalnum() else print("Entrada possui caracteres não autorizados!!")
        if coorp == nome:
            checa = False
            while True:
                nome = entrada(checa)
                if nome.replace(' ', '').isalnum():
                    return coorp, nome
                print("Entrada possui caracteres não autorizados!!")
