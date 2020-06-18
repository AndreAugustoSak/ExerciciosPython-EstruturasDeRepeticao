# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

def estrutura_de_repeticao_01():
    nota = float(input('Digite uma nota de 0 a 10: '))
    if nota > 10 or nota < 0:
        print('Número inválido!')
        estrutura_de_repeticao_01()


estrutura_de_repeticao_01()