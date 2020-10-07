a, b, c = input().split()
a=float(a)
b=float(b)
c=float(c)

# 10.0 20.1 5.1
# 0.0 20.0 5.0
# 10.0 3.0 5.0

delta=b**2-(4*a*c)

if a == 0:
    print('Impossivel calcular')
elif delta < 0:
    print('Impossivel calcular')
# elif x_um == 0 or x_dois == 0:
#     print('Impossivel calcular')
else:
    x_um=(-b+(delta**(1/2)))/(2*a)

    x_dois=(-b-(delta**(1/2)))/(2*a)
    
    print('R1 = {:.5f}'.format(x_um))
    print('R2 = {:.5f}'.format(x_dois))