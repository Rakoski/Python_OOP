# Tem que se chamar quantos_multiplos(). Pra executar ele, precisa de um número de 1 a 15 e contá-los (intervalo)
# agora eu quero saber quantos são múltiplos de determinado número

def quantos_multiplos(arr):
    numero = int(input("Digite seu número: "))
    cont = 0
    for c in range(len(arr)):
        if arr[c] % numero == 0:
            cont += 1
    print(f"Você possui {cont} números dividios por {numero} em", arr)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
quantos_multiplos(lista)
