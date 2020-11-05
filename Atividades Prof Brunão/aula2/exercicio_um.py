# Crie uma lista com todas as letras do alfabeto

consoantes=[]

for letra in range(97,123):
    consoantes.append(chr(letra))
# print(alfabeto)

# Remova as vogais dessa lista e crie uma tupla com elas

listavogais=[]

for vogal in consoantes:
    if vogal in 'aeiou' and vogal != '':
        consoantes.remove(vogal)
        listavogais.append(vogal)

tuplavogais=(tuple(listavogais))

# print(consoantes)
# print(tuplavogais)

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro favorito
colecao=[]
colecao = set(colecao)

for item in consoantes:
    if item in 'dvy':
        colecao.add(item)

for item in tuplavogais:
    if item in 'a':
        colecao.add(item)

colecao.add(21)
colecao.add('mogli')
print(colecao)

