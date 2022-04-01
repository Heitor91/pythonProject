"""
Autor Heitor de Carvalho                                                                          Projeto: Agenda 3.1.0
1.0: Capacidade de 10 nomes. Devo conter nome, telefone e email.
Funções obrigatórias: Adicionar, Remover, Localizar*, Mostrar agenda toda, Mostrar Contato
1.1: Validação estrutural do email no formato exemple@exemple.com ou exemple@exemple.com
1.2: Formatação do telefone para celular (00)12345-6789 ou fixo (00)1234-5678 caso não possua a quantidade certa de
     números deve realizar a recusa
2.0: Permitir adicionar o contato com apenas o nome (Obrigatório) e uma forma de contato, não precisa constar email e
     telefone juntos
2.0.1: Importar classes e funnções de arquivos externos, otimizar código principal
2.1.0: Ampliar para 3 telefones e 2 emails por contato
3.0.0: Acrescentar os campos sobrenome, empresa, cargo, data de nascimento e criar um gerenciador de credenciais que
       deve conter, nome e sobrenome (Abreviar sobrenomes do meio para não ultrapassar 20 caracteres), empresa, cargo,
       idade
"""
from Custom_Libraries.AuxClass import Agenda
from Custom_Libraries.Auxiliar_functions import entra_nome, lista_contato, data_nascimento, empresa

# =====================================================================================================================
# =================================================Programa principal==================================================
# =====================================================================================================================
contatos = Agenda.start_class()
# ================================Menu da agenda=====================================================================
while True:
    op = input("(A)diciona|(L)ocaliza|(R)emove|(C)ontatos|(P)essoa|(S)air:")
    # =====Menu Operacional de adicionar contato======================================================================
    if op.upper() == 'A':
        contatos.nome = entra_nome(True)  # Função de entrada do nome
        contatos.sobrenome = entra_nome(False)
        while True:
            contatos.telefone, val_tel = lista_contato(True)
            contatos.email, val_mail = lista_contato(False)
            if val_tel or val_mail:
                break
            print('É necessário pelo menos 1 telefone ou 1 e-mail')
        contatos.data_de_nascimento = data_nascimento()
        contatos.empresa, contatos.cargo = empresa()
        contatos.armazena()
    # =====Menu Operacional de localizar contato======================================================================
    elif op.upper() == 'L':
        busca = input("Digite o nome a ser encontrado:")
        print(f'{busca.capitalize()} está no index:{contatos.busca_pessoa(busca.capitalize())}')
    # =====Menu Operacional de remover contato========================================================================
    elif op.upper() == 'R':
        busca = input("Digite o nome a ser removido:")
        contatos.remove_pessoa(busca.capitalize())
    # =====Menu Operacional de imprimir agenda completa===============================================================
    elif op.upper() == 'C':
        contatos.imprime_agenda()
    # =====Menu Operacional de imprimir contato expecífico============================================================
    elif op.upper() == 'P':
        busca = input("Digite o nome a ser localizado:")
        contatos.imprime_pessoa(busca.capitalize())
    # =====Menu Operacional para sair do programa=====================================================================
    elif op.upper() == 'S':
        exit(0)
    # =====Menu Operacional de invalidação de comando=================================================================
    else:
        print("Comando inválido!!")
