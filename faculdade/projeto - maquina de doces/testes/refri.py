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

def ValorDoces(Valor_Doces, Valor_total = 0.0): 
    """ 
    :para Valor_Doces: Valor dos Doces
    :para Valor_total: Valor total que foi inserido pelo cliente
    return: Valor total que foi pago
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
        elif nota_moeda == 10:
            Valor_depositado += nota_moeda
        elif nota_moeda == 5:
            Valor_depositado += nota_moeda
        elif nota_moeda == 2:
            Valor_depositado += nota_moeda
        elif nota_moeda == 1:
            Valor_depositado += nota_moeda
        elif nota_moeda == 0.5:
            Valor_depositado += nota_moeda
        else:
            print("Nota/moeda INVÁLIDA. Tente Novamente.")

    return Valor_depositado

def troco(Valor_Doces,Valor_dep):
    """ 
    :para Valor_Doces: Valor dos Doces
    :para Valor_dep: Valor total que foi inserido pelo cliente
    return: o valor do troco
    """
    troco = (Valor_dep - Valor_Doces)
    troco_disp = 0
    notas_20 = 1
    notas_10 = 1
    notas_5 = 1
    notas_2 = 1
    notas_1 = 1
    notas_0_5 = 1
    while troco > 0:
        troco = (Valor_dep - Valor_Doces)

        print(f'Valor pago: R${Valor_dep}')
        print(f'Troco: R${troco:.2f}')

        return troco
        if troco >= 20 and notas_20 > 0:
            qtd = min(troco // 20, notas_20)
            troco -= qtd * 20
            notas_20 -= qtd
            troco_disp += qtd * 20

        elif troco >= 10 and notas_10 > 0:
            qtd = min(troco // 10, notas_10)
            troco -= qtd * 10
            notas_10 -= qtd
            troco_disp += qtd * 10

        elif troco >= 5 and notas_5 > 0:
            qtd = min(troco // 5, notas_5)
            troco -= qtd * 5
            notas_5 -= qtd
            troco_disp += qtd * 5

        elif troco >= 2 and notas_2 > 0:
            qtd = min(troco // 2, notas_2)
            troco -= qtd * 2
            notas_2 -= qtd
            troco_disp += qtd * 2

        elif troco >= 1 and notas_1 > 0:
            qtd = min(troco // 1, notas_1)
            troco -= qtd * 1
            notas_1 -= qtd
            troco_disp += qtd * 1
            
        elif troco >= 0.5 and notas_0_5 > 0:
            qtd = min(troco // 0.5, notas_1)
            troco -= qtd * 0.5
            notas_0_5 -= qtd
            troco_disp += qtd * 0.5
        else:
            break
    return troco_disp


def troco_sep(xtroco):
    """ 
    :para xtroco: Troco
    return: A separação do troco
    """
   # if xtroco >= 20:
   #     print('R$20.00')
   #     troco(xtroco - 20)

   # elif xtroco >= 10:
    #    print('R$10.00')
    #    troco(xtroco - 10)

   # elif xtroco >= 5:
   #     print('R$5.00')
   #     troco(xtroco - 5)

   # elif xtroco >= 2:
   #     print('R$2.00')
   #     troco(xtroco - 2)

   # elif xtroco >= 1:
   #     print('R$1.00')
   #     troco(xtroco - 1)

   # elif xtroco >= 0.50:
   #     print('R$0.50')
   #     troco(xtroco - 0.50)
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
        

def infos(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5, faturamento):
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
    print(f"| NOTAS DE R$20,00:  x{notas_20}                  |")
    print(f"| NOTAS DE R$10,00:  x{notas_10}                  |")
    print(f"| NOTAS DE R$5,00:   x{notas_5}                  |")
    print(f"| NOTAS DE R$2,00:   x{notas_2}                  |")
    print(f"| MOEDAS DE R$1,00:  x{notas_1}                 |")
    print(f"| MOEDAS DE R$0,50:  x{notas_0_5}                  |")
    print("|                                        |")
    print("*--------------FATURAMENTO---------------*")
    print("|                                        |")
    print(f"| FATURAMENTO: {faturamento}                      |")
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
        
    
def perguntadoce(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5):
    continuar = input("Deseja comprar outro Doce? (S/N):")
    if continuar == "s" or continuar == "S":
        maquina(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5, faturamento = 0.00)
    elif continuar == "n" or continuar == "N":
        print('Obrigado pela preferencia. Volte Sempre!!!')
        exit()

def maquina(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5, faturamento = 0.00,):
    """
    Função responsável por exibir as mensagens e realizar as vendas.

    Parâmetros:
    a: Estoque do produto 'a'
    b: Estoque do produto 'b'
    c: Estoque do produto 'c'

    Retorno:
    Função não retona nada.
    """
    menu_inicial()
    continua = input(" ---> Enter para continuar...")
    limpaTela()
    while True:
        menu(qtd_kit, qtd_suflair, qtd_fini, qtd_bis)
        op = opc()

        if op >= 1 and op <= 6:
            if op == 1:
                if qtd_kit < 1:
                    print("ESTOQUE INSUFICIENTE")
                    perguntadoce()
                else:
                    print("Você Escolheu KITKAT!")
                    print("Preço: R$3,00")
                    precoDoce = escolha1(op)

                    valorIns =ValorDoces(precoDoce)

                    if valorIns < precoDoce:
                        print("Money Insuficiente. Insira mais dinheiro:")
                        continue
                    else:
                        if valorIns > precoDoce:
                            print("Pegue seu Troco: ")
                            troco_valor = troco(precoDoce, valorIns)
                            troco_sep(troco_valor)
                        elif valorIns == precoDoce:
                            print("Obrigado!")
                        
                    

                        qtd_kit = qtd_kit - 1
                        faturamento = faturamento + precoDoce

                    
                        perguntadoce(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5)

            elif op == 2:
                if qtd_suflair < 1:
                    print("ESTOQUE INSUFICIENTE")
                    perguntadoce()
                else:
                    print("Você Escolheu SUFLAIR!")
                    print("Preço: R$6,50")
                    precoDoce = escolha1(op)

                    valorIns =ValorDoces(precoDoce)

                    if valorIns < precoDoce:
                        print("Money Insuficiente. Insira mais dinheiro:")
                        continue
                    else:
                        print("Pegue seu Troco: ")
                        troco_valor = troco(precoDoce, valorIns)
                
                    qtd_suflair = qtd_suflair - 1
                    faturamento = faturamento + precoDoce
                perguntadoce(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5)

            elif op == 3:
                if qtd_fini < 1:
                    print("ESTOQUE INSUFICIENTE")
                    perguntadoce()
                else:
                    print("Você Escolheu FINI TUBES!")
                    print("Preço: R$4,50")
                    precoDoce = escolha1(op)

                    valorIns =ValorDoces(precoDoce)

                    if valorIns < precoDoce:
                        print("Money Insuficiente. Insira mais dinheiro:")
                        continue
                    else:
                        print("Pegue seu Troco: ")
                        troco_valor = troco(precoDoce, valorIns)
                    qtd_fini = qtd_fini - 1
                    faturamento = faturamento + precoDoce
                    perguntadoce(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5)

            elif op == 4:
                if qtd_bis < 1:
                    print("ESTOQUE INSUFICIENTE")
                    perguntadoce()
                else:
                    print("Você Escolheu BIS XTRA!")
                    print("Preço: R$2,00")
                    precoDoce = escolha1(op)

                    valorIns =ValorDoces(precoDoce)

                    if valorIns < precoDoce:
                        print("Money Insuficiente. Insira mais dinheiro:")
                        continue
                    else:
                        print("Pegue seu Troco: ")
                        troco_valor = troco(precoDoce, valorIns)

                    qtd_bis = qtd_bis - 1
                    faturamento = faturamento + precoDoce
                    
                    perguntadoce(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5)
            
            elif op == 5:
                infos(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5, faturamento)
                continua = input(" ---> Enter para continuar...")
                limpaTela()
                maquina(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5, faturamento = 0.00)

            elif op == 6:
                perg = input("Realmente deseja sair? (S/N)")
                if perg == "S" or perg == "s":
                    print('Obrigado pela preferencia.')
                    break
                elif perg == "N" or perg == "n":
                    limpaTela()
                    maquina(qtd_kit, qtd_suflair, qtd_fini, qtd_bis, notas_20, notas_10, notas_5, notas_2, notas_1, notas_0_5, faturamento = 0.00)




        
def main():
    maquina(5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5.00)
main()