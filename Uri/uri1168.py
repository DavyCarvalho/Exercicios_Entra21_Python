qtd=int(input())
for i in range(qtd):
    
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
    
    valorleds=list(input())
    listatotal=[]

    for i in valorleds:
        if i == str(1):
            listatotal.append(um)
        elif i == str(2):
            listatotal.append(dois)
        elif i == str(3):
            listatotal.append(tres)
        elif i == str(4):
            listatotal.append(quatro)
        elif i == str(5):
            listatotal.append(cinco)
        elif i == str(6):
            listatotal.append(seis)
        elif i == str(7):
            listatotal.append(sete)
        elif i == str(8):
            listatotal.append(oito)
        elif i == str(9):
            listatotal.append(nove)
        elif i == str(0):
            listatotal.append(zero)
    resultado=(sum(listatotal))
    print(f'{resultado} leds')

#FUNCIONOOOOOOOOOOOOOU AMÉMMM!!!!!!