# n = int(input('Digite um número: '))
# tot = 0
# for c in range(1, n + 1, +1):
#     if n % c == 0:
#         print('\033[34m', end= ' ')
#         tot += 1
#     else:
#         print('\033[m', end= ' ')
#     print('{}'.format(c), end= ' ')
# print('\nO número {} foi divisivel {} vezes'.format(n, tot))
# if tot == 2:
#     print('E por isso ele é primo')
# else:
#     print('Esse número não é primo')

    
while True:
    try:
        number = int(input('Digite Um Número: '))
    except:
        print('\n- Digite Novamente -')
    else:
        break
print(f'\nOs Número Primos Entre 1 e {​​​​​number}​​​​​ São: ')
primos = []
vezes =0
for a in range(1, number +1):
    count =0
    for elemento in range(1, number +1):
        vezes = vezes +1
        #print(vezes)
        if a % elemento ==0:
            count +=1
        else:
            pass
    if count ==2:
        primos.append(a)
    else:
        pass
print(primos)

