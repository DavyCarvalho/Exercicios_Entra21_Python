# (b - c) < a < b + c
# (a - c) < b < a + c
# (a - b) < c < a + b

def condicoes(a,b,c):
  """
    aisdaosidhoaish
  """
  condicao_um = (b-c) < a < (b+c)
  condicao_dois = (a-c) < b < (a+c)
  condicao_tres = (a-b) < c < (a+b)

  if condicao_um and condicao_dois and condicao_tres:
    print('É um triângulo')
    if a==b==c:
      print('Triângulo Equilátero')
    elif a==b!=c:
      print('Triângulo Isósceles')
    elif a!=b!=c:
      print('Triângulo Escaleno')
  else:
    print('Não é um triângulo')


a = float(input('Qual o lado1 do tiângulo? '))
b = float(input('Qual o lado2 do tiângulo? '))
c = float(input('Qual o lado3 do tiângulo? '))

condicoes(a,b,c)