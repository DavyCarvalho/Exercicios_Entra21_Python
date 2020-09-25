valor=float(input())
valor=valor+0.001 #corrigindo erro do python com casas decimais 

notas_100=valor//100
resto=valor%100

notas_50=resto//50
resto=resto%50

notas_20=resto//20
resto=resto%20

notas_10=resto//10
resto=resto%10

notas_5=resto//5
resto=resto%5

notas_2=resto//2
resto=resto%2

moedas_1=resto//1
resto=resto%1

moedas_50=resto//0.50
resto=resto%0.50

moedas_25=resto//0.25
resto=resto%0.25

moedas_10=resto//0.10
resto=resto%0.10

moedas_5=resto//0.05
resto=resto%0.05

moedas_01=resto//0.01

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(notas_100))
print('{:.0f} nota(s) de R$ 50.00'.format(notas_50))
print('{:.0f} nota(s) de R$ 20.00'.format(notas_20))
print('{:.0f} nota(s) de R$ 10.00'.format(notas_10))
print('{:.0f} nota(s) de R$ 5.00'.format(notas_5))
print('{:.0f} nota(s) de R$ 2.00'.format(notas_2))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(moedas_1))
print('{:.0f} moeda(s) de R$ 0.50'.format(moedas_50))
print('{:.0f} moeda(s) de R$ 0.25'.format(moedas_25))
print('{:.0f} moeda(s) de R$ 0.10'.format(moedas_10))
print('{:.0f} moeda(s) de R$ 0.05'.format(moedas_5))
print('{:.0f} moeda(s) de R$ 0.01'.format(moedas_01))
