
lista_global_passageiros=[]
lotacao = 4

def clear():
    from os import system, name
    system('cls')

def cabecalho():
    uber = 'UBÊR TOP'
    return f"""
    {uber:=^50}
    """

def cadastrar_pessoa():
    global lista_global_passageiros
    global lotacao
    
    
    nome=input('Nome do passageiro: ')
    idade=input('Idade do passageiro: ')
    cpf=str(input('CPF do passageiro: '))

    passageiro = Pessoa(nome,idade,cpf)

    return passageiro

class Pessoa:
    global lista_global_passageiros
    global lotacao
    
    def __init__(self,nome:str,idade:int,cpf:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Veiculo:
    global lista_global_passageiros
    global lotacao

    def __init__(self,modelo:str,cor:str,placa:str):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
    
    def apresentar_veiculo(self):
        return f"""
        Dados do veículo:

        Modelo: {self.modelo}
        Cor: {self.cor}
        Placa: {self.placa}
        """
    
    def apresentar_passageiro(self):
        #passageiro = cadastrar_pessoa()
        return f"""
        Passageiro atual:
        
        Nome: {lista_global_passageiros[0].nome.upper()}
        Idade: {lista_global_passageiros[0].idade}
        CPF: {lista_global_passageiros[0].cpf}
        """

    def lotacao_maxima(self):
               
        while True:
            
            passageiros = int(input('Quantos passageiros embarcaram? '))

            if passageiros <= lotacao:
                return'Número de passageiros permitido!'
            else:
                print(f'LOTAÇÃO EXCEDIDA, DISPENSE {passageiros-lotacao} PASSAGEIROS PARA SEGUIR VIAGEM!')
    
    def salvar_passageiro(self):
        passageiro = cadastrar_pessoa()
        lista_global_passageiros.append(passageiro)
        return "Passageiro Cadastrado com sucesso!"
    
    #def nova_viagem(self):
        return True

    def verificador(self):
               
        while True:
            pergunta = input("""
        Deseja fazer uma nova viagem? 
        Digite S ou N
        """)

            if pergunta == 'S' or pergunta == 's':
                lista_global_passageiros.clear()
                return True 
            elif pergunta == 'N' or pergunta == 'n':
                lista_global_passageiros.clear()
                return False
            else:
                print("Resposta invalida, favor responder novamente!")

class Uno(Veiculo):
    global lista_global_passageiros
    global lotacao

    def __init__(self,modelo:str,cor:str,placa:str):
        super().__init__(modelo,cor,placa)

uno = Uno('Uno','Prata','MMM1234')

while True:

    print(cabecalho())

    print(uno.salvar_passageiro())

    print(uno.apresentar_veiculo())

    print(uno.lotacao_maxima())

    print(uno.apresentar_passageiro())

    if not uno.verificador(): # o If só roda se a condição for True! por isso o NOT
        break

#IMPLEMENTAR LIMPEZA DE TELA !!!!!!

