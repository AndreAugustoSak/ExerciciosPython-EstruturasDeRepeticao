# Faça um programa que leia e valide as seguintes informações:
    # Nome: maior que 3 caracteres;
    # Idade: entre 0 e 150;
    # Salário: maior que zero;
    # Sexo: 'f' ou 'm';
    # Estado Civil: 's', 'c', 'v', 'd';
def estrutura_de_repeticao_03():
    nome = str(input('Qual o seu nome? '))
    if len(nome) < 3:
        print('ERRO: o seu nome deve possuir mais que 3 caracteres!')
        estrutura_de_repeticao_03()
    def idade_1():
        idade = int(input('Qual a sua idade? '))
        if idade > 150 or idade < 0:
            print('ERRO: a sua idade deve ser entre 0 e 150 anos!')
            idade_1()
    idade_1()
    def salario_1():
        salario = float(input('Qual o seu salário? '))
        if salario <= 0:
            print('ERRO: o seu salário deve ser maior que zero!')
            salario_1()
    salario_1()
    def sexo_1():
        sexo = str(input('Qual o seu sexo (f ou m)? ')).strip().upper()
        if sexo != 'F' and sexo != 'M':
            print('''ERRO: o seu sexo deve ser 'f' ou 'm'!''')
            sexo_1()
    sexo_1()
    def estado_civil_1():
        estado_civil = str(input('''Qual o seu estado civil ('s', 'c', 'v', 'd')? ''')).strip().upper()
        if estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
            print('''ERRO: o seu estado civil deve ser 's', 'c', 'v', 'd'!''')
            estado_civil_1()
    estado_civil_1()
    print('Agora todas as suas informações estão corretas!')


estrutura_de_repeticao_03()