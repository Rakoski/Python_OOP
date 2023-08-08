from time import sleep


def exibit_menu():
    cont = False
    lista = []
    while True:
        print("-=-" * 30)
        print("MENU DE OPÇÕES")
        print("-=-" * 30)
        print("""
                 1. CRIAR VETOR
                 2. PREENCHER VETOR
                 3. EXIBIR VETOR
                 4. EXIBIR QUANTOS VALORES X TEM NO VETOR
                 5. SAIR""")
        print()
        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            cont = True
            print("criando vetor...")
            sleep(0.5)
            print("vetor criado!")

        elif escolha == 2:
            if not cont:
                raise IndexError("Vetor não criado")
            while True:
                numero = int(input("Que valores quer colocar? Número 100 para: "))
                if numero == 100:
                    break
                lista.append(numero)

        elif escolha == 3:
            if not cont:
                raise IndexError("Vetor não criado")
            print(lista)

        elif escolha == 4:
            if not cont:
                raise IndexError("Vetor não criado")
            print(exibir_valores(lista))

        elif escolha == 5:
            if not cont:
                raise IndexError("Vetor não criado")
            print("saindo...")
            sleep(0.5)
            break
        else:
            print("escolha não encontrada...")



def exibir_valores(vetor):
    cont = 0
    x = int(input("qual número você quer saber quantos tem? "))
    if x in vetor:
        cont += 1
    print(f"Existem {cont} de {x} em {vetor}")


exibit_menu()