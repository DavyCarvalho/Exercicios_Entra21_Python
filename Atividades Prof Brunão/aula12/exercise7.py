# frase = input('Digite uma frase com espaços:\n\n').lower()
                                                            
# print(f"""
#       A frase tem:
#       {frase.count(" ")} espaços
#       {frase.count("a")} letras A
#       {frase.count("e")} letras E
#       {frase.count("i")} letras I
#       {frase.count("o")} letras O
#       {frase.count("u")} letras U
#       """)

# import re
# palavra = input("Digite uma palavra:").upper()
# palavra_vogais = re.findall(r'A|E|I|O|U', palavra)
# palavra_espacos = re.findall(r' ', palavra)

# print(f'As vogais aparecem: {len(palavra_vogais)}x')
# print(f'Osespaços aparencem: {len(palavra_espacos)}x')

# from unicodedata import normalize


# frase = input('\nDigite Uma Frase: ').lower()
# target = normalize('NFKD', frase).encode('ASCII','ignore').decode('ASCII')
# print(target)
# espacos = frase.count(' ')

# a = target.count('a')
# e = target.count('e')
# i = target.count('i')
# o = target.count('o')
# u = target.count('u')

# print(f'''\n
# A frase Contém:

#     - {espacos} espaços.
#     - {a} vezes a vogal a.
#     - {e} vezes a vogal e.
#     - {i} vezes a vogal i.
#     - {o} vezes a vogal o.
#     - {u} vezes a vogal u.''')

