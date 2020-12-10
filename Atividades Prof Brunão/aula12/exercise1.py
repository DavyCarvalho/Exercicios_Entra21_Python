sal_hora = float(input('Digite o salário que você ganha por hora: ').replace(',','.'))

num_horas = float(input('Digite quantas horas você trabalha por mês: '))

sal_bruto = (sal_hora*num_horas)

ir = (sal_bruto*(0.11))

inss = (sal_bruto*(0.08))

sindicato = (sal_bruto*(0.05))

contas = ir+inss+sindicato

sal_liq = sal_bruto - contas

print(f''' {'='*30}
+ Salário Bruto : R$ {sal_bruto}
- IR (11%) : R$ {ir}
- INSS (8%) : R$ {inss}
- Sindicato ( 5%) : R$ {sindicato}
= Salário Liquido : R$ {sal_liq}
{'='*30}''')

