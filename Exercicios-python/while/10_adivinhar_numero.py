#Jogo de adivinhação: o programa “pensa” no número 42. A pessoa tenta adivinhar com input(). Enquanto errar, mostre “maior” se o palpite for menor que 42, ou “menor” se for maior. Quando acertar, mostre “Acertou!”.
numero = 0
while numero != 42:
    numero = int(input("Digite um número: "))
    if numero == 42:
        print(f'Você acertou o número da sorte é {numero}')
    elif numero > 42:
        print("Número maior que o exato! ")
    else:
        print("Número menor que o exato! ")