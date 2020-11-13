passageiro_atual = []

def cadastrar_passageiro():
    nome=input('Nome do passageiro: ')
    idade=input('Idade do passageiro: ')
    cpf=str(input('CPF do passageiro: '))

    passageiro = Pessoa(nome,idade,cpf)
    # passageiro_atual.append(passageiro)

    return passageiro

class Pessoa():
    global passageiro_atual
    
    def __init__(self,nome:str,idade:int,cpf:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Veiculo():
    global passageiro_atual

    def __init__(self,categoria:str,tracao:str,lugares:int,peso:float,cor:str):
        self.categoria = categoria
        self.tracao = tracao
        self.lugares = lugares
        self.peso = peso
        self.cor = cor

    def apresentar_veiculo(self):
        return f"""
        Modelo: {type(self).__name__}
        Categoria: {self.categoria} 
        Cor: {self.cor}
        """

    def apresentar_pessoa(self):
        passageiro = cadastrar_passageiro()
        return f"""
        Seu passageiro atual chama-se {passageiro.nome} e tem {passageiro.idade} anos.
        CPF: {passageiro.cpf}
        """
    def inserir_passageiro(self):
        passageiro_atual.append(cadastrar_passageiro())

    def remover_passageiro(self):
        passageiro_atual.clear()
        return "Lista limpa"

class Marea(Veiculo):
    def __init__(self,cor:str):
        super().__init__('Sedan','Dianteira',5,1.200,cor)
    
    #Está função caso não haja alterações não é necessaria ser reesccrita, pois  com o
    # super().__init__ acima, ele ja herdou todas as funções da classe Pai
    # def informacoes(self):
    #     return f"""
    #     informações do veiculo:
    #     Categoria: {self.categoria}
    #     Tração: {self.tracao}
    #     Lugares: {self.lugares}
    #     Peso: {self.peso}
    #     Cor: {self.cor}
    #     """    

    def partida(self):
        return "tchararara ram... tchararara ram... BUUUUUUMMMMM"
    def acelerar(self):
        return "boom super sonico e logo após uma explosão atomica"
    def freiando(self):
        return "Quem tem freio é bicicleta, aqui é pé na bomba"

        # super().informacoes()
        # super().partida()
        # super().acelerando()
        # super().freiando()


m = Marea('Cinza').apresentar_veiculo()
p = Marea('Cinza').apresentar_pessoa()
r = Marea('Cinza').remover_passageiro()

print(m,'\n',p,'\n',r)