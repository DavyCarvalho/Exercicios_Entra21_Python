lista_produtos = {'arroz':40.0, 'feijao':30.0, 'batata':20.0 }

produto_escolhido = input("Qual o produto escolhido?\n")

for produto,valor in lista_produtos.items():
    if produto == produto_escolhido:
        print("Seu {} de R${} tem 5% de desconto e fica no valor de R${}"
        .format(produto, valor, valor-(valor*5)/100))