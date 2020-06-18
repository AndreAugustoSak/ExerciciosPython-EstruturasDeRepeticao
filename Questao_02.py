# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
def estrutrura_de_repeticao_02():
    nome = str(input('Digite o seu nome: '))
    senha = str(input('Digite a sua senha: '))
    if nome == senha:
        print('ERRO: você não pode utilizar o seu nome como senha!')
        estrutrura_de_repeticao_02()


estrutrura_de_repeticao_02()