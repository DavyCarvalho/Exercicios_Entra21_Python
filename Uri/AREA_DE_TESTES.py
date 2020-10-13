# lista_nomes =['Manuel', 'Laura', 'Antonio', 'Jasmim', 'Maria', 'Silvia', 'Lu', 

# 'Pancracio', 'Diogo', 'Ricardo', 'Miguel', 'Andre']

# lista_ordenada = sorted(lista_nomes)

# print(lista_ordenada)



# lista_dieta=list(input())
# cafe_da_manha=list(input())
# almoco=list(input())

# lista_rango=[]

# for i in cafe_da_manha:
#     lista_rango.append(i)
# for i in almoco:
#     lista_rango.append(i)

# print(lista_dieta)
# print(lista_rango)


# print(12%8)
# print(27/9)
# print(259%111)

# print(200.01**(1/2))

# num='oi'
# print(id(num))
# print(type(id(num)))

# dic = {1:{'davy':'carvalho'}}

"print(dic['davy']) isso non ekisziste"
# print(dic[1])

# dic = {1:'a'}

# print(dic.items())  "SAIDA = dict_items([(1, 'a')])"
# print(dic.values())  "SAIDA = dict_values(['a'])"
# print(dic.keys())  "SAIDA = dict_keys([1])"

# lista_pessoas = [
#     {1:['davy','carvalho',21,{'Rua':'Itajai','Numero':4880,'Complemento':'Galpão','Bairro':'Vorstadt','Cidade':'Blumenau','Estado':'SC'}]},
#     {2:['danyel','jorge',17,{'Rua':'Itajai','Numero':9999,'Complemento':'Galpão','Bairro':'Vorstadt','Cidade':'Pindamonhangaba','Estado':'SC'}]}
#     ]

lista_pessoas = [{3 : 'id_usuario', 'nome': 'eduarda', 'sobrenome': 'taschetto', 'idade': 19, 'endereco': {'rua': 'manoel', 'numero': '242', 'complemento': 'casa', 'bairro': 'figueira', 'cidade': 'gaspar', 'estado': 'sc'}}]

def pessoa_especifica_dados(pessoa_id):
    for dicionario in lista_pessoas:
        for chave, valor in dicionario.items():
            if chave == pessoa_id:
                return(f'''
                Nome: {valor[0]}
                Sobrenome: {valor[1]}
                Idade: {valor[2]}
                ''')
                
def endereco_por_id(pessoa_id):
    for dicionario in lista_pessoas:
        for chave, valor in dicionario.items():
            if chave == pessoa_id:
                for valor in dicionario.values():
                    for chave, valor in valor[3].items():
                        print(f'{chave}: {valor}')
    return('')

print(pessoa_especifica_dados(3))
print(endereco_por_id(3))

