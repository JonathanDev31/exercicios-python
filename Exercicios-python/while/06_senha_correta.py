#Peça uma senha ao usuário com input() e repita a pergunta enquanto ele não digitar "python123". Quando acertar, mostre "Acesso liberado".

senha = 'python123'
contador = True
usuario = input("Digite a sua senha: ")

while usuario != senha:
    print('Senha incorreta! Digite novamente.')
    usuario = input("Digite a sua senha: ")
print("Acesso liberado!")