from os import system, name 

def jogar():
    palavra = "abelha"
    chances = 5
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
        


if __name__ == "__main__":
    jogar()
