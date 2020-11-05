
# Calcule o valor total dos itens e aplique descontos:

# se o valor for superior a 100, 2% de desconto
# se o valor for superior a 200, 5% de desconto
# se o valor for superior a 500, 10% de desconto

# descubra qual o item mais caro da lista

# ordene os itens da lista por ordem alfabética

listaitenscompra={'bebida' : 100, 'salada' : 30, 'pao' : 50, 'carne' : 150, 'picles': 30, 'maionese' : 15}

totalcompra=sum(listaitenscompra.values())
maiorvalor=max(listaitenscompra.values())

print('''
======ITEMS COMPRADOS=======
''')

listaitenscompra_ordenada={}

for item in sorted(listaitenscompra):
    for chave, valor in listaitenscompra.items():
        if item == chave:
            listaitenscompra_ordenada[chave]=valor

for chave, valor in listaitenscompra_ordenada.items():
    print(f'''
{chave} ---------- R${valor}''')

    
for chave, valor in listaitenscompra.items():
    if valor == maiorvalor:
        print(f'''
        Seu item mais caro foi '{chave}' no valor de R${valor}

        ''')

desconto_um=2/100
desconto_dois=5/100
desconto_tres=10/100

if totalcompra >= 100 and totalcompra < 200:
    print(f'''
    Valor total da compra: R${totalcompra}
    Desconto: R${totalcompra*desconto_um}

    Valor com desconto: R${totalcompra-(totalcompra*desconto_um)}
    ''')
elif totalcompra >= 200 and totalcompra < 500:
    print(f'''
    Valor total da compra: R${totalcompra}
    Desconto: R${totalcompra*desconto_um}

    Valor com desconto: R${totalcompra-(totalcompra*desconto_um)}
    ''')
elif totalcompra > 500:
    print(f'''
    Valor total da compra: R${totalcompra}
    Desconto: R${totalcompra*desconto_um}

    Valor com desconto: R${totalcompra-(totalcompra*desconto_um)}
    ''')