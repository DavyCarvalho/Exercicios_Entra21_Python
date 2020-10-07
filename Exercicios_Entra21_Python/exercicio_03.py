#--- Exercício 3 - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

dados_livro = {'Título':'Jogos Vorazes', 
                'Edição':'Scholastic', 
                'Autor':'Suzanne Collins', 
                'Data de publicação':'14 de setembro 2008'}

titulo, edicao, autor, data_pub = dados_livro.values()

paragrafo1 = '''    Uma vez, quando eu estava de tocaia em uma árvore,
imóvel, esperando a caça aparecer, adormeci e caí de costas no
chão de uma altura de três metros. Foi como se o impacto
tivesse expulsado cada centímetro cúbico de ar de meus pulmões. 
E fiquei lá deitada, lutando para respirar, para me
mover, enfim, para fazer qualquer coisa.'''

paragrafo2 = '''    É assim que me sinto agora, tentando lembrar como se
respira, incapaz de falar, totalmente atordoada, ouvindo o
nome repicar no interior de meu crânio. Alguém está segurando meu braço, 
um garoto da Costura, e talvez eu tenha começado a cair e ele me pegou.'''

print('''
Título: {}
Edição: {}
Autor: {}
Data de publicação: {}

{}
{}

'''.format(titulo, edicao, autor, data_pub, paragrafo1, paragrafo2))