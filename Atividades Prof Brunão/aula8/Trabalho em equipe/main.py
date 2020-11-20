from pessoa_veiculo import Pessoa, Carro

def main ():
    while True:
        op = int(input("""
        CONCESSIONÁRIA DO VELHO HERROR
        1 - Cadastrar pessoa
        2 - Cadastrar veículo
        3 - Deletar dados
        4 - Atualizar dados
        5 - Exibir dados
        6 - Sair
        """))

        if op == 1:
            cadastrar_pessoa()
        elif op == 2:
            cadastrar_veiculo()
        elif op == 3:
            deletar_dados()
        elif op == 4:
            atualizar_dados()
        elif op == 5:
            exibir_dados()
        elif op == 6:
            break
        else:
            print("Opção inválida! Tente novamente.")


#chamar a função salvar_pessoa_na_tabela no final
def cadastrar_pessoa():
    pass

#chamar a função salvar_veiculo_na_tabela no final
def cadastrar_veiculo():
    pass

def deletar_dados():
    pass

def atualizar_dados():
    pass

def exibir_dados():
    pass