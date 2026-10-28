#Peça números ao usuário e some todos eles. O laço termina quando a pessoa digitar 0. No final, mostre a soma.
soma = 0
numero = int(input("Digite um número para somar (0 para sair): "))
while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número para somar (0 para sair): "))
print(f'A soma dos números é {soma} ')