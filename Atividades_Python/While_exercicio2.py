"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida"

"""

opcao1 = ' '

while opcao1 != 'S' and opcao1 != 's':
    opcao1 = input('''
    Programa Soma/Média/Taboada

    A) Soma: 
    B) Média: 
    C) Taboada: 
    S) Sair: 

    Digite a opção desejada: 
    ''')

    print('\n')
    if opcao1 == 'A' or opcao1 == 'a':
        n1soma = int(input("Digite o primeiro número para soma: "))
        n2soma = int(input("Digite o segundo número para soma: "))
        somaa = n1soma + n2soma
        print(f"O resultado da soma é {somaa}")
    elif opcao1 == 'B' or opcao1 == 'b':
        n1med = int(input("Digite o primeiro número para média: "))
        n2med = int(input("Digite o segundo número para média: "))
        n3med = int(input("Digite o terceiro número para média: "))
        n4med = int(input("Digite o quarto número para média: "))
        med = (n1med + n2med + n3med + n4med) / 4
        print(f"A média é {med}")
    elif opcao1 == 'C' or opcao1 == 'c':
        n1t = int(input("Digite o número para ver a taboada completa dele: "))
        print(f'A taboada de {n1t} é: ')
        for i in range(10):
            print(f"{n1t} x {i+1} = {(i+1)*n1t}")
    elif opcao1 == 'S' or opcao1 == 's':
        print(f"Obrigado por usar nossos serviços!")
    else:
        print('Opção inválida!')