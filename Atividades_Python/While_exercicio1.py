"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um memu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""
opcao = ' '

while opcao != 'S' or opcao != 's':
    print(opcao)
    opcao = input('''
    Programa Soma/Subtração/Multiplicação

    1) Soma: 
    2) Subtração: 
    3) Multiplicação: 
    S) Sair: 

    Digite a opção desejada: 
    ''')

    print('\n')
    if opcao == '1':
        n1s = int(input("Digite o primeiro número para soma: "))
        n2s = int(input("Digite o segundo número para soma:: "))
        soma = n1s + n2s
        print(f"O resultado da soma é {soma}")
    elif opcao == '2':
        n1sb = int(input("Digite o primeiro número para subtração: "))
        n2sb = int(input("Digite o primeiro número para subtração: "))
        sub = n1sb - n2sb
        print(f"O resultado da subtração é {sub}")
    elif opcao == '3':
        n1m = int(input("Digite o primeiro número para multiplicação: "))
        n2m = int(input("Digite o primeiro número para multiplicação: "))
        mult = n1m * n2m
        print(f"O resultado da multiplicação é {mult}")
    elif opcao == 'S' or opcao == 's':
        print(f"Obrigado por usar nossos serviços!")
    else:
        print('Opção inválida!')
