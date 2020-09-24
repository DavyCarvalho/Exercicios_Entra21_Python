"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""

#teste
# nomes = [davy, emily,bianca,heitor,danyel]
# idades = [21,19,15,6,17]

nomes = []
idades = []

print('''
Preencha os dados dos clientes 
(Pressione ENTER em Idade para finalizar o programa)
''')

idade = 0

while not(idade == ''):
    name = input('Nome do cliente: ')
    if name == '':
        print('Nome em branco, favor digitar um nome!')
        continue
    idade = input('Idade do cliente:')
    if idade == '':
        print('Obrigado pela preferência')
        if int(idade) >= 18:
            print('Entrada Permitida')
        elif int(idade) < 18:
            print('Entrada Proibida')    
        lista_aprovados = input('''Deseja imprimir a lista de clientes com entrada permitida? 
        Digite 'S' para exibir ou 'ENTER' para seguir em frente''')
        if lista_aprovados == 's':
            for i in range(len(nomes)):
                if int(idades[i]) >= 18:
                    print(f"Nome: {nomes[i]} - Status: Entrada Permitida!")
        elif lista_aprovados == '':
            continue
    else:
        continue
    nomes.append(name)
    idades.append(idade)