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

def ValorDoces(Valor_Doces, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5): 
    """ 
    Função responsável por permitir que o cliente insira notas ou moedas para comprar doces até que o valor total seja alcançado.

    :param Valor_Doces: O valor total dos doces que o cliente deseja comprar.
    :param qtd_notas_20: Quantidade de notas de R$20,00 disponíveis.
    :param qtd_notas_10: Quantidade de notas de R$10,00 disponíveis.
    :param qtd_notas_5: Quantidade de notas de R$5,00 disponíveis.
    :param qtd_notas_2: Quantidade de notas de R$2,00 disponíveis.
    :param qtd_notas_1: Quantidade de notas de R$1,00 disponíveis.
    :param qtd_notas_0_5: Quantidade de moedas de R$0,50 disponíveis.

    :return: O valor total que foi pago pelo cliente.
    """
    Valor_depositado = 0.0
    while Valor_depositado < Valor_Doces:
        try:
            nota_moeda = float(input("Coloque seu money: "))
        except ValueError:
            print("Nota/moeda INVÁLIDA. Tente Novamente.")
            continue
    
        if nota_moeda == 20:
            Valor_depositado += nota_moeda
            qtd_notas_20 += 1
        elif nota_moeda == 10:
            Valor_depositado += nota_moeda
            qtd_notas_10 += 1
        elif nota_moeda == 5:
            Valor_depositado += nota_moeda
            qtd_notas_5 += 1
        elif nota_moeda == 2:
            Valor_depositado += nota_moeda
            qtd_notas_2 += 1
        elif nota_moeda == 1:
            Valor_depositado += nota_moeda
            qtd_notas_1 += 1
        elif nota_moeda == 0.5:
            Valor_depositado += nota_moeda
            qtd_notas_0_5 += 1
        else:
            print("Nota/moeda INVÁLIDA. Tente Novamente.")

    return Valor_depositado, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5
    
def troco(Valor_Doces, Valor_dep, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5):
    """ 
    Função responsável por calcular o troco a ser dado ao cliente com base nos valores pagos e nas notas e moedas disponíveis.

    :param Valor_Doces: Valor dos doces a serem comprados.
    :param Valor_dep: Valor total que foi inserido pelo cliente.
    :param qtd_notas_20: Quantidade de notas de R$20,00 disponíveis.
    :param qtd_notas_10: Quantidade de notas de R$10,00 disponíveis.
    :param qtd_notas_5: Quantidade de notas de R$5,00 disponíveis.
    :param qtd_notas_2: Quantidade de notas de R$2,00 disponíveis.
    :param qtd_notas_1: Quantidade de notas de R$1,00 disponíveis.
    :param qtd_notas_0_5: Quantidade de moedas de R$0,50 disponíveis.

    :return: O valor do troco a ser dado ao cliente e as quantidades atualizadas de notas e moedas disponíveis.
    """
    troco = Valor_dep - Valor_Doces

    while troco > 0:
        if troco >= 20 and qtd_notas_20 > 0:
            qtd = min(troco // 20, qtd_notas_20)
            troco -= qtd * 20
            qtd_notas_20 -= qtd
            print("R$ 20,00")
        
        elif troco >= 10 and qtd_notas_10 > 0:
            qtd = min(troco // 10, qtd_notas_10)
            troco -= qtd * 10
            qtd_notas_10 -= qtd
            print("R$ 10,00")
        
        elif troco >= 5 and qtd_notas_5 > 0:
            qtd = min(troco // 5, qtd_notas_5)
            troco -= qtd * 5
            qtd_notas_5 -= qtd
            print("R$ 5,00")
        
        elif troco >= 2 and qtd_notas_2 > 0:
            qtd = min(troco // 2, qtd_notas_2)
            troco -= qtd * 2
            qtd_notas_2 -= qtd
            print("R$ 2,00")
        
        elif troco >= 1 and qtd_notas_1 > 0:
            qtd = min(troco // 1, qtd_notas_1)
            troco -= qtd * 1
            qtd_notas_1 -= qtd
            print("R$ 1,00 ")
        
        elif troco >= 0.5 and qtd_notas_0_5 > 0:
            qtd = min(troco // 0.5, qtd_notas_0_5)
            troco -= qtd * 0.5
            qtd_notas_0_5 -= qtd
            print("R$ 0,50")

    return troco, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5

def troco_sep(xtroco):
    """ 
    Função responsável por calcular a separação do troco em notas e moedas.

    :param xtroco: O valor do troco a ser separado.

    Esta função imprime as notas e moedas que compõem o troco, de maior valor para menor.

    Exemplo de uso:
     troco_sep(37.5)
    R$ 20,00
    R$ 10,00
    R$ 5,00
    R$ 2,00
    R$ 0,50

    :return: Nenhum valor é retornado.
    """

    while xtroco > 0:
        if xtroco >= 20:
            qtd = int(xtroco // 20)
            print("R$ 20,00")
            xtroco -= qtd * 20

        elif xtroco >= 10:
            qtd = int(xtroco // 10)
            print("R$ 10,00")
            xtroco -= qtd * 10

        elif xtroco >= 5:
            qtd = int(xtroco // 5)
            print("R$ 5,00")
            xtroco -= qtd * 5

        elif xtroco >= 2:
            qtd = int(xtroco // 2)
            print("R$ 2,00")
            xtroco -= qtd * 2

        elif xtroco >= 1:
            qtd = int(xtroco // 1)
            print("R$ 1,00")
            xtroco -= qtd * 1

        elif xtroco >= 0.5:
            qtd = float(xtroco // 0.5)
            print("R$ 0,50")
            xtroco -= qtd * 0.5
        
def infos(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5, faturamento):
    """"
     Função responsável por exibir informações internas sobre o estoque, caixa e faturamento.
        Parâmetros:
        qtd_kit (int): Quantidade de KitKat em estoque.
        qtd_suflair (int): Quantidade de Suflair em estoque.
        qtd_fini (int): Quantidade de Fini Tubes em estoque.
        qtd_bis (int): Quantidade de Bis Xtra em estoque.
        faturamento (float): Valor total faturado.
    """
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
    """"
     Função para obter uma opção válida do usuário.

    Retorna:
    int: A opção válida escolhida pelo usuário.

    Esta função solicita que o usuário escolha uma opção, que deve ser um número inteiro entre 1 e 6. 
    Caso o usuário insira uma opção inválida, a função continua pedindo uma opção válida até que seja inserida.
    """
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
    """"
    Pergunta ao cliente se deseja comprar outro doce e age de acordo com a resposta.
    Retorna:
    None
    Se o cliente responder "s" ou "S" (sim), a função chama a função `maquina()` com os parâmetros adequados para continuar a compra.
    Se o cliente responder "n" ou "N" (não), a função exibe uma mensagem de agradecimento e encerra o programa.
    """
    continuar = input("Deseja comprar outro Doce? (S/N):")
    if continuar == "s" or continuar == "S":
        maquina(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5, faturamento = 0.00)
    elif continuar == "n" or continuar == "N":
        print('Obrigado pela preferencia. Volte Sempre!!!')
        exit()
#def maquinapobre(valorIns, precoDoce, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5):
    #while True:
       # troco= valorIns - precoDoce
       # troco_possivel = (20 * qtd_notas_20) + (10 * qtd_notas_10) + (5 * qtd_notas_5) + (2 * qtd_notas_2) + qtd_notas_1 + (0.5 * qtd_notas_0_5)
       # if troco < troco_possivel:
        #    print("No momento Troco Indisponivel.")
         #   choice = input("Deseja, comprar esse produto?(S/N)")
         #   if choice == "s" or choice == "S":
         #       qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = troco(precoDoce, valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
          #  else:
          #      print("Pegue seu money")
           #     qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = troco(valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
           #     input("Enter para continuar.")
           #     continue
             #Não consegui incrementar

def maquina(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5, faturamento):
    """"
     Simula o funcionamento de uma máquina de venda de doces, gerenciando estoque, faturamento e troco.
     Parâmetros:
    qtd_kit (int): Quantidade de KitKats disponíveis.
    qtd_suflair (int): Quantidade de Suflairs disponíveis.
    qtd_fini (int): Quantidade de Fini Tubes disponíveis.
    qtd_bis (int): Quantidade de Bis Xtra disponíveis.
    qtd_notas_20 (int): Quantidade de notas de R$20,00 disponíveis.
    qtd_notas_10 (int): Quantidade de notas de R$10,00 disponíveis.
    qtd_notas_5 (int): Quantidade de notas de R$5,00 disponíveis.
    qtd_notas_2 (int): Quantidade de notas de R$2,00 disponíveis.
    qtd_notas_1 (int): Quantidade de notas de R$1,00 disponíveis.
    qtd_notas_0_5 (int): Quantidade de moedas de R$0,50 disponíveis.
    faturamento (float): Valor total faturado até o momento.
     Retorna:
    None
    """
    menu_inicial()
    continua = input(" ---> Enter para continuar...")
    limpaTela()
    while True:
        menu(qtd_kit, qtd_suflair, qtd_fini, qtd_bis)
        op = opc()
        if op >= 1 and op <= 6:
            if op == 1 and qtd_kit > 0:
                precoDoce = escolha1(op)
                valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = ValorDoces(precoDoce, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                if valorIns >= precoDoce:
                    qtd_kit -= 1
                    faturamento += precoDoce
                    print("Pegue seu Troco: ")
                    troco_valor, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = troco(precoDoce, valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                    troco_sep(troco_valor)
                    print(f"Faturamento atual: R${faturamento:.2f}")  
                else:
                    print("Money Insuficiente. Insira mais dinheiro.")
                    

            elif op == 2 and qtd_suflair > 0:      
                precoDoce = escolha1(op)
                valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = ValorDoces(precoDoce, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                if valorIns >= precoDoce:
                    qtd_suflair -= 1
                    faturamento += precoDoce
                    print("Pegue seu Troco: ")
                    troco_valor, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = troco(precoDoce, valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                    troco_sep(troco_valor)
                    print("Obrigado pela compra")
                    print(f"Faturamento atual: R${faturamento:.2f}")
                else:
                    print("Money Insuficiente. Insira mais dinheiro.")

            elif op == 3 and qtd_fini > 0:
                precoDoce = escolha1(op)
                valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = ValorDoces(precoDoce, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                if valorIns >= precoDoce:
                    qtd_fini -= 1
                    faturamento += precoDoce
                    print("Pegue seu Troco: ")
                    troco_valor, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = troco(precoDoce, valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                    troco_sep(troco_valor)
                    print("Obrigado pela compra")
                    print(f"Faturamento atual: R${faturamento:.2f}")
                else:
                    print("Money Insuficiente. Insira mais dinheiro.")
            elif op == 4 and qtd_bis > 0:
                precoDoce = escolha1(op)
                valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = ValorDoces(precoDoce, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                if valorIns >= precoDoce:
                    qtd_bis -= 1
                    faturamento += precoDoce
                    print("Pegue seu Troco: ")
                    troco_valor, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5 = troco(precoDoce, valorIns, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5)
                    troco_sep(troco_valor)
                    print(f"Faturamento atual: R${faturamento:.2f}")
                else:
                    print("Money Insuficiente. Insira mais dinheiro.")
            elif op == 5:
                infos(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, qtd_notas_20, qtd_notas_10, qtd_notas_5, qtd_notas_2, qtd_notas_1, qtd_notas_0_5, faturamento)
                continua = input(" ---> Enter para continuar...")
            elif op == 6:
                perg = input("Realmente deseja sair? (S/N)")
                if perg == "S" or perg == "s":
                    print(f'Obrigado pela preferência. Faturamento total: R${faturamento:.2f}')
                    break
                elif perg == "N" or perg == "n":
                    continue

def main():
    maquina(5,5,5,5,5,5,5,5,5,5, 0.00)
main()