from os import system , name
def menu_inicial():
    print("="* 42)
    print("|           DOCERIA DO LUQUINHAS         |")
    print("="* 42)

def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def menu(qtd_kit, qtd_suflair, qtd_fini, qtd_bis):

    print("="* 42)
    print("|           DOCERIA DO LUQUINHAS         |")
    print("="* 42)
    print("|                                        |")
    print("*-----------------PRODUTOS---------------*")
    print("|                                        |")
    if qtd_kit < 1:
        print("| (1) - KITKAT.......INDISPONIVEL        |")
    else:
        print("| (1) - KITKAT..........R$3,00           |")
    if qtd_suflair < 1:    
        print("| (2) - SUFLAIR......INDISPONIVEL       |") 
    else:
       print("| (2) - SUFLAIR.........R$6,50           |")
    if qtd_fini < 1:
         print("| (3) - FINI TUBES......INDISPONIVEL    |")
    else:
        print("| (3) - FINI TUBES......R$4,50           |")
    if qtd_bis < 1:
        print("| (4) - BIS XTRA........INDISPONIVEL     |")
    else:
        print("| (4) - BIS XTRA........R$2,00           |")
    print("|                                        |")
    print("*-----------OUTRAS INFORMAÇÕES-----------*")
    print("|                                        |")
    print("| (5) - INFORMAÇÕES INTERNAS             |")
    print("| (6) - FINALIZAR                        |")
    print("|                                        |")
    print("*----------------------------------------*")

def infos(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5, faturamento):
    print("="* 42)
    print("|          INFORMAÇÕES INTERNAS          |")
    print("="* 42)
    print("|                                        |")
    print("*----------------ESTOQUE-----------------*")
    print("|                                        |")
    print(f"| KITKAT:            x{qtd_kit}                  |")
    print(f"| SUFLAIR:           x{qtd_suflair}                  |")
    print(f"| FINI TUBES:        x{qtd_fini}                  |")
    print(f"| BIS XTRA:          x{qtd_bis}                  |")
    print("|                                        |")
    print("*-----------------CAIXA------------------*")
    print("|                                        |")
    print(f"| NOTAS DE R$20,00:  x{qtd_notas_20}                  |")
    print(f"| NOTAS DE R$10,00:  x{qtd_notas_10}                  |")
    print(f"| NOTAS DE R$5,00:   x{qtd_notas_5}                  |")
    print(f"| NOTAS DE R$2,00:   x{qtd_notas_2}                  |")
    print(f"| MOEDAS DE R$1,00:  x{qtd_notas_1}                  |")
    print(f"| MOEDAS DE R$0,50:  x{qtd_notas_0_5}                  |")
    print("|                                        |")
    print("*--------------FATURAMENTO---------------*")
    print("|                                        |")
    RED = '\033[35m'
    RST = '\033[00m'
    print(RED)
    print(f"| FATURAMENTO: R$ {faturamento:.2f}                   |")
    print(RST)
    print("|                                        |")
    print("*----------------------------------------*")

def escolha1(escolha):
    """ 
    :para escolha: Opção de escolha do Cliente
    return: Valor/preço da opção escolhida
    """
    if escolha == 1:
        return 3.00
    elif escolha == 2:
        return 6.50
    elif escolha == 3:
        return 4.50
    elif escolha == 4:
        return 2.00
    
def nomesdoces(nome):
    """ 
    :para nome: Opção de escolha 
    return: Nome da opção
    """
    if nome == 1:
        return "KITKAT"
    elif nome == 2:
        return "SUFLAIR"
    elif nome == 3:
        return "FINI TUBES"
    elif nome == 4:
        return "BIS XTRA"    

def opc():
    while True:
        try:
            opcao = int(input("Escolha uma Opção: "))
            if opcao >= 1 and opcao <= 6:
                return opcao
            else:
                print("Opção inválida. Você tem que digitar um número inteiro entre 1 e 6.")
        
        except:
            print("Opção inválida. Você tem que digitar um número inteiro entre 1 e 6.")

def perguntadoce(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5):
    continuar = input("Deseja comprar outro Doce? (S/N):")
    if continuar == "s" or continuar == "S":
        maquina(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5, faturamento = 0.00)
    elif continuar == "n" or continuar == "N":
        print('Obrigado pela preferencia. Volte Sempre!!!')
        exit()

def ValorInserido(valor_doces):
    valor_Inserido = 0
    qt_notas_20 = 0
    qt_notas_10 = 0
    qt_notas_5 = 0
    qt_notas_2 = 0
    qt_notas_1 = 0
    qt_notas_0_5 = 0

    while valor_Inserido < valor_doces:
        inserido = float(input("Insira seu Money:R$ "))
        if inserido < 0:
            return valor_Inserido, qt_notas_20, qt_notas_10, qt_notas_5, qt_notas_2, qt_notas_1, qt_notas_0_5
        if inserido != 20 or inserido != 10 or inserido != 5 or inserido != 2 or inserido != 1 or  inserido != 0.5:
            print("Nota/moeda INVÁLIDA. Tente Novamente.")
            continue
        if inserido == 20:
            qt_notas_20 += 1
        elif inserido == 10:
            qt_notas_10 += 1
        elif inserido == 5:   
            qt_notas_5 += 1 
        elif inserido == 2:
            qt_notas_2 += 1
        elif inserido == 1:
            qt_notas_1 += 1
        else: 
            qt_notas_0_5 += 1

        valor_Inserido += inserido

def troco(valor_inserido, valor_doces):
    troco = valor_inserido - valor_doces
     
def maquina():
