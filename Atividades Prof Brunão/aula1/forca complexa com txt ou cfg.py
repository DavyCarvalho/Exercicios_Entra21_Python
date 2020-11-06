from os import system, name 

palavra = ''
chances = 0

def carregar_config():
    global palavra
    global chances
    linhas_arquivo = []
    with open('forca.txt') as arquivo:
        for linha in arquivo:
            linhas_arquivo.append(linha.strip())
    palavra = str(linhas_arquivo[0])
    chances = int(linhas_arquivo[1])

def jogar():
    global palavra
    global chances
    carregar_config()
    letras_usadas = []
    while True:
        tentativa_palavra = ""

        # for windows 
        if name == 'nt': 
            system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else: 
            system('clear')       
  
        print(f"Número de chances: {chances} - tentativas:")
        print(*letras_usadas) # imprime item por item do array==lista
        print("\n")
        for letra in palavra:
            if letra in letras_usadas:
                tentativa_palavra=tentativa_palavra + letra #tentativa_palavra += letra MESMA COISA
            else:
                tentativa_palavra=tentativa_palavra + '_' #tentativa_palavra += '_' MESMA COISA
        #for letra in palavra:
            #tentativa_palavra += letra if letra in letras_usadas else "_" JEITO MAIS RESUMIDO DO PROFESSOR

        print(tentativa_palavra + "\n\n")

        if tentativa_palavra == palavra:
            print(f"Você ganhou sobranu {chances} tentativas!")
            break

        chute = input("Digite uma letra:")
        letras_usadas.append(chute)
        
        if not chute in palavra:
            chances -= 1

        if chances == 0:
            print("Você perdeu!")
            break

# implementar a função carregar_config
    # implementar a função verifica_fim_jogo
    # implementar a função limpar_tela

    # previnir que o usuário digite números
    # previnir que o usuário repita letras

    # implementar menu de usuário com as seguintes opções:
    # 1 - Jogar
    # 2 - Modificar as configurações
    # 3 - sair
    
    # https://realpython.com/quizzes/python-dicts/viewer/

if __name__ == "__main__":
    jogar()
