#testando#
qtd=int(input())
valorleds_um=list(input())
valorleds_dois=list(input())
valorleds_tres=list(input())

listatotal_um=[]
listatotal_dois=[]
listatotal_tres=[]

um=2
dois=5
tres=5
quatro=4
cinco=5
seis=6
sete=3
oito=7
nove=6
zero=6

for i in range(qtd):
    #-----------------------------------------------#   
    for i in valorleds_um:
        if i == str(1):
            listatotal_um.append(um)
        elif i == str(2):
            listatotal_um.append(dois)
        elif i == str(3):
            listatotal_um.append(tres)
        elif i == str(4):
            listatotal_um.append(quatro)
        elif i == str(5):
            listatotal_um.append(cinco)
        elif i == str(6):
            listatotal_um.append(seis)
        elif i == str(7):
            listatotal_um.append(sete)
        elif i == str(8):
            listatotal_um.append(oito)
        elif i == str(9):
            listatotal_um.append(nove)
        elif i == str(0):
            listatotal_um.append(zero)
    #-----------------------------------------------#    
    for i in valorleds_dois:
        if i == str(1):
            listatotal_dois.append(um)
        elif i == str(2):
            listatotal_dois.append(dois)
        elif i == str(3):
            listatotal_dois.append(tres)
        elif i == str(4):
            listatotal_dois.append(quatro)
        elif i == str(5):
            listatotal_dois.append(cinco)
        elif i == str(6):
            listatotal_dois.append(seis)
        elif i == str(7):
            listatotal_dois.append(sete)
        elif i == str(8):
            listatotal_dois.append(oito)
        elif i == str(9):
         listatotal_dois.append(nove)
        elif i == str(0):
          listatotal_dois.append(zero)
    #-----------------------------------------------# 
    for i in valorleds_tres:
        if i == str(1):
            listatotal_tres.append(um)
        elif i == str(2):
            listatotal_tres.append(dois)
        elif i == str(3):
            listatotal_tres.append(tres)
        elif i == str(4):
            listatotal_tres.append(quatro)
        elif i == str(5):
            listatotal_tres.append(cinco)
        elif i == str(6):
            listatotal_tres.append(seis)
        elif i == str(7):
            listatotal_tres.append(sete)
        elif i == str(8):
            listatotal_tres.append(oito)
        elif i == str(9):
            listatotal_tres.append(nove)
        elif i == str(0):
            listatotal_tres.append(zero)
    print(sum(listatotal_um))
    print(sum(listatotal_dois))
    print(sum(listatotal_tres))
    qtd == False