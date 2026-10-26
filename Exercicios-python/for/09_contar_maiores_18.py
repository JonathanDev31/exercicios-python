#com a mesma lista idades, conte quantas são maiores ou iguais a 18 e imprima só a quantidade (3).
idades = [12, 18, 25, 16, 30]
contador = 0
for idade in idades:
    if idade >= 18:
        contador +=1
print(contador)