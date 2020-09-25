idade_em_dias=int(input())

anos=idade_em_dias//365
resto=idade_em_dias%365

meses=resto//30
resto=resto%30

dias=resto

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')
