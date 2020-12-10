# from itertools import permutations
# #importei a função permutations para fazer o cálculo de todas as possibilidades possiveis 
# #dentro de uma lista de números pré-definidos.

# listas_possiveis = list(permutations([1,2,3,4,5,6,7,8,9]))
# quadrados_magicos = 0
# #se for um quadrado mágico será acrescentado pelo contador
# print(len(listas_possiveis))
# for quadrado in listas_possiveis:
#     soma = quadrado[0] + quadrado[1] + quadrado[2]
#     contador = 0
    
#     for i in range(0,7,3):
# #o range irá da posição 0 a 7, pulando de 3 em 3, passando pela posição 0, 3, 6
#         if (quadrado[i] + quadrado[i+1] + quadrado[i+2]) == soma:
#             contador = contador + 1
#         else:
#             break
    
#     if contador < 3:
#         continue
    
#     for i in range(3):
# #o range irá passar 3x, passando pela posição 3, 6, 9
#         if (quadrado[i] + quadrado[i+3] + quadrado[i+6]) == soma:
#             contador = contador + 1
#         else:
#             break 
            
#     if contador < 6:
#         continue
    
#     for i in range(0,3,2):
# #o range irá da posição 0 a 3, pulando de 2 em 2, passando pela posição 0 e 3
#         if (quadrado[0+i] + quadrado[4] + quadrado[8-i]) == soma:
#             contador = contador + 1

#     if contador < 8:
#         continue

# #ao final de cada for será impresso caso o contador seja menor que 8
# #o contador vai até 8 porque pelas pesquisas são 8 possibilidades de quadrado mágico possíveis.
#     else:
#         quadrados_magicos +=1
#         print(f'''Quadrado Mágico Número {quadrados_magicos}
#         {quadrado[0]} {quadrado[1]} {quadrado[2]}
#         {quadrado[3]} {quadrado[4]} {quadrado[5]}
#         {quadrado[6]} {quadrado[7]} {quadrado[8]}''')

# """
# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
#      8  3  4 
#      1  5  9
#      6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3. 
# """

# import random 
# from itertools import permutations


# quadrado = list(permutations([1,2,3,4,5,6,7,8,9]))

# def gera_valores():
#      final_horizontal = False
#      final_vertical = False
#      final_diagonal = False
#      cont = 0

#      for valores in quadrado:
#           soma_horizontal1 = valores[0] + valores[1] + valores[2]
#           soma_horizontal2 = valores[3] + valores[4] + valores[5]
#           soma_horizontal3 = valores[6] + valores[7] + valores[8]

#           if (soma_horizontal1 == 15) and (soma_horizontal2 == 15) and (soma_horizontal3 == 15):
#                final_horizontal = True

#           soma_vertical1 = valores[0] + valores[3] + valores[6]
#           soma_vertical2 = valores[1] + valores[4] + valores[7]
#           soma_vertical3 = valores[2] + valores[5] + valores[8]

#           if (soma_vertical1 == 15) and (soma_vertical2 == 15) and (soma_vertical3 == 15):
#                final_vertical = True

#           soma_diagonal1 = valores[0] + valores[4] + valores[8]
#           soma_diagonal2 = valores[2] + valores[4] + valores[6]
     
#           if (soma_diagonal1 == 15) and (soma_diagonal2 == 15):
#                final_diagonal = True

#           if final_horizontal == True and final_vertical == True and final_diagonal == True: 
#                cont += 1 
#                print(f""" Quadrado Nº {cont}
#      {valores[0]} {valores[1]} {valores[2]}
#      {valores[3]} {valores[4]} {valores[5]}
#      {valores[6]} {valores[7]} {valores[8]}
#                """)
               
#           final_horizontal = False
#           final_vertical = False
#           final_diagonal = False
                  

# def  main():
#      tamanho = 1
#      while tamanho > 0:
#           gera_valores()
#           tamanho-=1


# if __name__ == "__main__":
#     main()


"""
Exercícios de Revisão
Blusoft/Senac - Formação em Python Entra21 2020
Autor: Marcus Moresco Boeno
Último update: 2020-11-26
----- Exercício 06 -----
# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e 
# colunas, com um número em cada posição e no qual a soma das linhas, 
# colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico 
# de lado 3, com números de 1 a 9:
#     8  3  4
#     1  5  9
#     6  7  2
#     Elabore uma função que identifica e mostra na tela todos os 
# quadrados mágicos com as características acima. Dica: produza todas 
# as combinações possíveis e verifique a soma quando completar cada 
# quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar 
# uma matriz 3x3.
"""

# Standard library imports
import sys
import os


def read_impar(txt:str) -> int:
    """Realiza leitura de valor inteiro ímpar positivo
    > Argumentos:
        - txt (str): Texto para input.
    
    > Output:
        - (int): Valor inteiro indicado pelo usuário
    """

    # Capta salário por hora
    while True:

        # Realiza leitura do salário
        try:
            f = int(input(txt))
        
        # Sai do sistema com a interrupção
        except KeyboardInterrupt:
            sys.exit("\n\nSaindo, até logo! ...\n")
        
        # Indica erro de tipo
        except ValueError:
            print("[ERRO] Valor inválido, digite novamente!")
        else:
            # Testa domínio
            if f > 0 and f % 2 == 1:
                return f
            print("[ERRO] Valor inválido, digite novamente!")


def limpar_tela():
    """Limpeza da tela
    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Limpa terminal antes de cada execução
    # "cls" para windows e "clear" para linux/mac (posix)
    os.system('cls') if os.name == 'nt' else os.system('clear')


def quadrado_magico_base(N:int) -> list:
    """Retorno o quadrado mágico base
    > Argumentos:
        - N (int): Dimensão da matriz quadrada.
    
    > Output:
        - (list): Lista de lista representando o quadrado mágico
            NxN.
    """
    # Cria matriz base para operações
    A = [[0]*N for i in range(N)]
    
    # Inicializa termos para a contrução do quadrado mágico
    n, i, j = 1, 0, N//2

    # Itera sobre termos do quadrado mágico
    while n <= N**2:

        # Insere termo na matriz
        A[i][j] = n
        
        # Avança para próximo termo
        n += 1

        # Movimenta o cursor uma linha acima e uma coluna para direita
        # Se o cursor sair do grid ajuste a posição para a primeira 
        # coluna ou última linha
        newi, newj = (i-1) % N, (j+1) % N
        
        # Se a nova posição do cursor já estiver preenchida, movimente 
        # o cursor para a linha logo abaixo abaixo
        if A[newi][newj]: # Se preenchida True, se não False (0)
            i += 1
        else:
            # Mantem a nova posição do cursor caso o campo ainda
            # não tenha sido preenchido
            i, j = newi, newj
    
    # Retorna quadrado mágico base
    return A


def rotaciona_90_counterclock(A:list) -> list:
    """Rotaciona a matriz em 90 graus (anti_horario)
    > Argumentos:
        - A (list): Matriz a ser rotacionada.
    
    > Output:
        - (list): Matriz rotacionada.
    """
    # Recupera dimensão da matriz
    N = len(A)

    # Cria deep copy
    B = [[i for i in row] for row in A]
    
    # Rotaciona matriz
    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][N-1-i]
        
    # Retorna matriz rotacionada
    return B


def reflete_matriz(A:list) -> list:
    """Reflete a matriz com base na coluna central
    > Argumentos:
        - A (list): Matriz a ser rotacionada.
    
    > Output:
        - (list): Matriz rotacionada.
    """
    # Recupera dimensão da matriz
    N = len(A)
    
    # Cria deep copy
    B = [[i for i in row] for row in A]
    
    # Reflete primeira e terceira colunas
    for i in range(N):
        B[i][0], B[i][N-1] = B[i][N-1], B[i][0]
    
    # Retorna a matriz refletida
    return B


def reflexoes_e_rotacoes(A:list) -> list:
    """Encontra reflexoes e rotacoes do quadrado mágico
    > Argumentos:
        - A (list): Matriz base do quadrado mágico.
    
    > Output:
        - (list): Lista com todas as possibilidades do quadrado mágico.
    """

    # Recupera dimensão da matriz
    N = len(A)
    
    # Reflete Matriz base
    X = reflete_matriz(A)

    # Rotaciona matriz A e reflete na matriz Y
    B = rotaciona_90_counterclock(A)
    Y = reflete_matriz(B)

    # Rotaciono matriz B e reflito na matriz Z 
    C = rotaciona_90_counterclock(B)
    Z = reflete_matriz(C)

    # Rotaciono matiz C e reflito na W
    D = rotaciona_90_counterclock(C)
    W = reflete_matriz(D)

    # Retorna lista de matriz componentes do quadrado mágico
    return [A, B, C, D, X, Y, Z, W]


def main():
    """Menu principal
    > Argumentos:
        - Sem argumentos.
    
    > Output:
        - Sem output.
    """
    # Apresentação
    print("\n\n > QUADRADOS MÁGICOS!")
    print("\nMatrizes nxn com linhas, colunas e diagonal de mesma soma\n")

    # Capta dimensões do quadrado mágico a ser criado
    n = read_impar("Digite dimensão n do quadrado (ímpar): ")

    # Apresenta cabeçalho
    print("\n" + "*"*60)
    print(f"{f' POSSÍVEIS QUADRADOS MÁGICOS ({n}x{n}) ':^60}")
    print("*"*60 + "\n")

    # Computa quadrado mágico base
    base = quadrado_magico_base(n)

    # Computa possibilidades do quadrado mágico
    M = reflexoes_e_rotacoes(base)

    # Apresenta possíveis quadrados mágicos
    for pos, matriz in enumerate(M):
        print(f"  > Quadrado {pos+1}: {matriz}")

    # Apresenta rodapé
    print("\n" + "*"*60 + "\n")


if __name__ == "__main__":

    # Executa aplicação
    while True:
        
        # Executa rotina
        main()

        # Verifica se usuário deseja executar nova rodada
        while True:

            # Capta resposta do usuário
            try:
                res = input("Realizar nova consulta?! [(s)/n] ").strip().lower()
            
            # Sai do sistema
            except KeyboardInterrupt:
                sys.exit("\n\nSaindo, até logo! ...\n")
            
            # Teste se input é válido
            else:
                if res in "sn":
                    break
                print("[ERRO] Digite 's' para continuar ou 'n' para sair!")
            
        # Verifica se usuario deseja terminar execução
        if res == "n":
            break

        # Limpar terminal para nova execução
        limpar_tela()
    
    # Indica saída do sistema
    print("\nSaindo, até logo! ...\n")