#Peça números ao usuário até ele digitar 0, como no exercício 7. No final, mostre quantos números foram digitados (sem contar o 0) e a soma deles.
soma = 0
contador = 0
numero = int(input("Digite um numero (0 para sair): "))
while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um numero (0 para sair): "))
    contador += 1
print(f"Você digitou {contador} número de vezes e a soma dos números é {soma} ")