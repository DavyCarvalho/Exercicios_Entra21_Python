#fase de testes
qntd_testes=int(input())
for i in range(qntd_testes):
    
    lista_dieta=list(input())
    cafe_da_manha=list(input())
    almoco=list(input())
    
    lista_rango=[]
    
    for i in cafe_da_manha:
        lista_rango.append(i)
    for i in almoco:
        lista_rango.append(i)

    lista_dieta=sorted(lista_dieta)
    lista_rango=sorted(lista_rango)
    
    for i in lista_dieta:
        if not i in lista_rango: #errado (está apenas invertendo o sinal!!!!!)
            print('CHEATER')
            break
        elif i in lista_rango:
            for i in lista_rango:
                    if i in lista_dieta:
                        lista_dieta.remove(i)
            print(lista_dieta)
    
    
    



# IWANTSODER
# SOW
# RAT
        