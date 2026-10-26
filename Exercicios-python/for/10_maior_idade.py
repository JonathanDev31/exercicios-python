#com a mesma lista idades, descubra a maior idade e imprima (30).

idades = [12, 18, 25, 16, 30]
maior = idades[0]
for idade in idades:
    if idade > maior:
        maior = idade
print(maior)