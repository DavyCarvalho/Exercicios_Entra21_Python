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
        if i in lista_rango:
            lista_dieta.remove(i)
    for i in lista_rango:
        if not i in lista_dieta:
            print('CHEATER')
            break
    print(lista_dieta)



# IWANTSODER
# SOW
# RAT
        