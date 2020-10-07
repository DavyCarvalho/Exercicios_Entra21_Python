a, b, c, d = input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)

soma_cd = c + d
soma_ab = a + b
resto = a % 2

if b > c and d > a and soma_cd > soma_ab and c > 0 and d > 0 and resto == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')