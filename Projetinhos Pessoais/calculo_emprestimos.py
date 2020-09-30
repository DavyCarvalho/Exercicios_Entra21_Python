contratos=int(input('Numero de contratos: '))
print('\n')
lista_prazo=[]
lista_vista=[]

for i in range(contratos):
    valor_prazo=float(input(f'Valor a prazo do contrato ({i+1}): '))
    lista_prazo.append(valor_prazo)
    valor_vista=float(input(f'Valor a vista do contrato ({i+1}): '))
    lista_vista.append(valor_vista)
    print('---------------------------')

resultado_prazo=sum(lista_prazo)
resultado_vista=sum(lista_vista)

print('Valor total a prazo = R${:.2f}'.format(resultado_prazo))
print('Valor total a vista = R${:.2f}'.format(resultado_vista))
print('\n')

# 5813.48
# 4740.50

# 882.98
# 849.16

# 14509.17
# 10232.42

# 7262.48
# 5922.09

# 6567.73
# 5627.86

# 3084.27
# 2798.46
