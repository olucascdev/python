def exib_menu():
    print("=" * 32)
    print("|                              |")
    print("{:^32}".format("|     DOCERIA DO LUQUINHAS     |"))
    print("|                              |")
    print("=" * 32)
    print()
    print("*---------PRODUTINHOS----------*")
    print("|                              |")
    print("| (1) - KITKAT..........R$3,00 |")
    print("| (2) - SUFLAIR.........R$6,50 |")
    print("| (3) - FINI TUBES......R$4,50 |")
    print("| (4) - BIS XTRA........R$2,00 |")
    print("|                              |")
    print("*------------------------------*")
    print("|                              |")                
    print("*------OUTRAS INFORMAÇÕES------*")
    print("|                              |")
    print("| (5) - INFORMAÇÕES INTERNAS   |")
    print("| (6) - FINALIZAR              |")
    print("|                              |")
    print("*------------------------------*")
    

 


def info(estq_kit,estq_sufl, estq_fini, estq_bis,qtd_20, qtd_10, qtd_5, qtd_2, qtd_1,qtd_05, faturamento):
    print("Estoque de produtos: ")
    print(f"KITKAT: {estq_kit}")
    print(f"SUFLAIR: {estq_sufl}")
    print(f"FINI TUBES: {estq_fini}")
    print(f"BIS XTRA: {estq_bis}")
    print("----------------------")
    print("Notas de R$20,00: ", qtd_20)
    print("Notas de R$10,00: ", qtd_10)
    print("Notas de R$5,00: ", qtd_5)
    print("Notas de R$2,00: ", qtd_2)
    print("Notas de R$1,00: ", qtd_1)
    print("Notas de R$0,50: ", qtd_05)
    print("----------------------")
    print(f"Faturamento: R${faturamento:.2f}")

    estq_kit = 5
    estq_sufl = 5 
    estq_fini = 5
    estq_bis = 5

    qtd_20 = 5
    qtd_10 = 5
    qtd_5 = 5
    qtd_2 = 5
    qtd_1 = 5
    qtd_05 = 5
    faturamento = 0 

def main(): 
    while True:
        exib_menu()
        opcao = input("Escolha uma Opção: ")

        if opcao == "1":
            venda("KITKAT",)
        elif opcao == "2":
            venda("SUFLAIR")
        elif opcao == "3":
            venda("FINI TUBES")
        elif opcao == "4":
            venda("BIS XTRA")
        elif opcao == "5":
            info()
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Escolha uma opção válida (1-6).")

main()
