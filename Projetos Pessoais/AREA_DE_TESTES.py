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

# lista_pessoas = [{3 : 'id_usuario', 'nome': 'eduarda', 'sobrenome': 'taschetto', 'idade': 19, 'endereco': {'rua': 'manoel', 'numero': '242', 'complemento': 'casa', 'bairro': 'figueira', 'cidade': 'gaspar', 'estado': 'sc'}}]

# def pessoa_especifica_dados(pessoa_id):
#     for dicionario in lista_pessoas:
#         for chave, valor in dicionario.items():
#             if chave == pessoa_id:
#                 return(f'''
#                 Nome: {valor[0]}
#                 Sobrenome: {valor[1]}
#                 Idade: {valor[2]}
#                 ''')
                
# def endereco_por_id(pessoa_id):
#     for dicionario in lista_pessoas:
#         for chave, valor in dicionario.items():
#             if chave == pessoa_id:
#                 for valor in dicionario.values():
#                     for chave, valor in valor[3].items():
#                         print(f'{chave}: {valor}')
#     return('')

# print(pessoa_especifica_dados(3))
# print(endereco_por_id(3))

'trabalhando com arquivos e fatias de listas #eduardabraba'
# var = open('teste.txt','a')
# var.write('DAVY,EDUARDA,21,17')
# var.close()

# var = open('teste.txt','r')

# for linha in var:
#     elemento = linha.split(',')
#     for item in range(2):

        
# # lista = ['DAVY', 'EDUARDA', '21', '17','45','89']
# # print(lista[:1])
# # print(lista[2:3])
# # print(lista[1::3])


# # for linha in var:
# #     for letra in linha:
# #         print(letra)

# var.close()
# x=0
# while x<10:
#     print(x)
#     x+=1 #igual
#     x=x+1 #igual

'''
for letra in palavra:
            if letra in letras_usadas:
                tentativa_palavra=tentativa_palavra + letra #tentativa_palavra += letra MESMA COISA
            else:
                tentativa_palavra=tentativa_palavra + '_' #tentativa_palavra += '_' MESMA COISA
        #for letra in palavra:
            #tentativa_palavra += letra if letra in letras_usadas else "_" JEITO MAIS RESUMIDO DO PROFESSOR'
            # '''

# with open("Clientes_Banco.txt", "r") as arquivo:
#     linhas_arquivo = arquivo.readlines()

#     for lista_cliente in linhas_arquivo:
#         for dados in lista_cliente.split():
#             print(dados)

"""

class Veiculo():                                       #n_rodas:int 
    def __init__(self, cor:str, altura:str, peso:float, n_rodas=4, motor='eletrico'): 
        self.cor = cor
        self.altura = altura
        self.peso = peso
        self.n_rodas = n_rodas
        self.motor = motor
        
class Carro(Veiculo):
    def __init__(self,cor:str, altura:str, peso:float): # NÃO DECLARAR OS PARAMETROS QUE SÃO FIXOS DO ''CARRO''
        super().__init__(cor, altura, peso, 4, 'combustão') # DECLARAR AQUI OS PARAMETROS FIXOS 
        
car = Carro('BRANCA',33,1.2)

print(car.motor,'\n', car.n_rodas)

"""

# tupla = ('davy',21,10651143977)

# lista = list(tupla)

# for item in range(1):
#     print(f"""
#           Nome: {lista[0]}
#           Idade: {lista[1]}
#           CPF: {lista[2]}
#           """)

import sqlite3


# conn = sqlite3.connect('proprietarios_e_veiculos.db')
# cursor = conn.cursor()

# # vamos inserir valores na nossa tabela 
# cursor.execute("""
#     INSERT INTO proprietarios (nome_proprietario, id_veiculo, cpf, idade)
#     VALUES ('Davy', 1, '00000000000', 21)
# """)

# # grava no DB
# conn.commit()
# conn.close()


# conn = sqlite3.connect('proprietarios_e_veiculos.db')
# cursor = conn.cursor()

# cursor.execute("""
# SELECT * FROM proprietarios;
# """)
# print("""
# ===============================
#       Pessoas Cadastradas 
# -------------------------------""")
# for pessoa in cursor.fetchall():
#         dado = list(pessoa)
#         print(f"""
# ===============================
# ID PESSOA: {dado[0]}
# NOME: {dado[1]}
# ID VEÍCULO: {dado[2]}
# CPF: {dado[3]}
# IDADE: {dado[4]}
# CRIADO EM: {dado[5]}""")


# conn.close()



try:
    opcao = int(input('a: '))
    # if type(opcao) == int:
    print('num')
    
except ValueError:
        print('vazio')

