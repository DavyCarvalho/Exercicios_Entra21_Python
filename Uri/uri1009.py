nome=input()
salario_fixo=float(input())
total_vendas=float(input())
comissao=((total_vendas*15)/100)
salario_final=salario_fixo+comissao
print('TOTAL = R$ {:.2f}'.format(salario_final))