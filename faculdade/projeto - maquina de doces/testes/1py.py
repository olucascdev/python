def titulo(txt):
    print("=" * 32)
    print("|                              |")
    print(txt)
    print("|                              |")
    print("=" * 32)

def traco():
    print("|                              |")

def traco2():
    print("*------------------------------*")

def produtinhos(qtd_kit, qtd_suflair, qtd_fini, qtd_bis):
    if qtd_kit < 1:
        print("| (1) - KITKAT.......INDISPONIVEL |")
    else:
        print("| (1) - KITKAT..........R$3,00 |")
    if qtd_suflair < 1:    
        print("| (2) - SUFLAIR......INDISPONIVEL |") 
    else:
       print("| (2) - SUFLAIR.........R$6,50 |")
    if qtd_fini < 1:
         print("| (3) - FINI TUBES......R$4,50 |")
    else:
        print("| (3) - FINI TUBES.....INDISPONIVEL |")
    if qtd_bis < 1:
        print("| (4) - BIS XTRA........INDISPONIVEL |")
    else:
        print("| (4) - BIS XTRA........R$2,00 |")
    
def infomacoes():
    print("| (5) - INFORMAÇÕES INTERNAS   |")
    print("| (6) - FINALIZAR              |")

def exibir_menu():

    """
    -> Mostra Menu principal da Máquina
    """
    
    titulo("|     DOCERIA DO LUQUINHAS     |")
    traco()
    print("*---------PRODUTINHOS----------*")
    traco()
    produtinhos()
    traco()
    traco2()
    traco()
    print("*------------OUTROS------------*")
    traco()
    infomacoes()
    traco()
    traco2()

def maquina(quantidadeCoca):
    while True:
        exibir_menu() 
        escolha = input("Escolha sua felicidade: ")
    
        if escolha == "1":

            print()
        elif escolha == "2":
            print()
        elif escolha == "3":
            print()
        elif escolha == "4":
            print()
        elif escolha == "5":
            exit
        elif escolha == "6":
            exit
        else:
            print("Opção inválida. Escolha uma opção válida (1-5).")
def main():
    
main()

def exibir_estoque(estq_kit):
    titulo("|    INFORMAÇÕES INTERNAS      |")
    traco()
    print("*-----------ESTOQUE------------*")
    traco()
    print(f"| KITKAT:            x{qtd_kit}        |")
    print(f"| SUFLAIR:           x{qtd_suflair}        |")
    print(f"| FINI TUBES:        x{qtd_fini}        |")
    print(f"| BIS XTRA:          x{qtd_bis}        |")
    traco()
    traco2()
    traco()
    print("*------------CAIXA-------------*")
    traco()
    print(f"| NOTAS DE R$20,00:  x{notas_20}        |")
    print(f"| NOTAS DE R$10,00:  x{notas_10}        |")
    print(f"| NOTAS DE R$5,00:   x{notas_5}        |")
    print(f"| NOTAS DE R$2,00:   x{notas_2}        |")
    print(f"| MOEDAS DE R$1,00:  x{moedas_1}        |")
    print(f"| MOEDAS DE R$0,50:  x{moedas_0_5}        |")
    traco()
    traco2()
    traco()
    print(f"| FATURAMENTO: {faturamento}             |")
    traco()
    traco2()

    estq_kit: 5
estq_suflair = 5
estq_fini = 5
estq_bis = 5
qtd_nota_20 = 5
qtd_nota_10 = 5 
qtd_nota_5 = 5 
qtd_nota_2 = 5 
qtd_moeda_1 = 5 
qtd_moeda_0_5 = 5
faturamento = 0.00



def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def teste(i = 1):
    while True:
        limpaTela()
        print(f"Iteracao: {i}")
        if i >= 5: # Finaliza o programa após 5 iterações
            exit()
        input("--> Enter para continuar...")