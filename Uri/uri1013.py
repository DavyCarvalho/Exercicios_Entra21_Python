A, B, C=input().split()
A=int(A)
B=int(B)
C=int(C)
MAIORAB=(A+B+(abs(A-B)))/2
RESULTADO=(MAIORAB+C+(abs(MAIORAB-C)))/2
print(f'{int(RESULTADO)} eh o maior')
