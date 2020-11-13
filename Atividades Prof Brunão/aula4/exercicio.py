# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)

passageiro_atual = []

def cadastrar_passageiro():
    nome=input('Nome do passageiro: ')
    idade=input('Idade do passageiro: ')
    cpf=str(input('CPF do passageiro: '))

    passageiro = Pessoa(nome,idade,cpf)

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
    def informacoes_completas(self):
        return f"""
        Modelo: {type(self).__name__}

        informações do veiculo: 
        Categoria: {self.categoria} 
        Tração: {self.tracao}
        Lugares: {self.lugares}
        Peso: {self.peso} Ton
        Cor: {self.cor}
        """
    def partida(self):
        return "tchararara ram... tchararara ram... vrum... vrum vruuum"
    def acelerar(self):
        return "VRUUUUUUUUUUUUUUUUUM"
    def freiando(self):
        return "tchuuuuuuuuuuuuuuuuu"
    def apresentar_pessoa(self):
        return f"""
        Seu passageiro atual chama-se {passageiro.nome} e tem {passageiro.idade} anos.
        CPF: {passageiro.cpf}
        """
    def inserir_passageiro(self):
        self.passageiro_atual.append(cadastrar_passageiro())

    def remover_passageiro(self):
        self.passageiro_atual.clear()
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

class Kombi(Veiculo):
    def __init__(self,cor:str):
        super().__init__("Micro-onibus",'Traseira',12,1.200,cor)

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
        return "tchararara ram... tchararara ram... brumbrumbrumbrum"
    def acelerar(self):
        return "braaaaaaaaaaaaaaaaaam brambraaaaaaam"
    def freiando(self):
        return "Chiado alto, uiiiiiiiiiii"

        # super().informacoes()
        # super().partida()
        # super().acelerando()
        # super().freiando()

class Up(Veiculo):
    def __init__(self,cor:str):
        super().__init__('Hatch','Dainteira',4,900,cor)

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
        return "tchararara ram... tchararara ram... buuuuuuuuuu"
    def acelerar(self):
        return "pote de sorvete stage 2 é só pipoco"
    def freiando(self):
        return "economizou nos freios agora a caixinha não bréka....."

        # super().informacoes()
        # super().partida()
        # super().acelerando()
        # super().freiando()

#class Chamadas_Marea_Kombi_UP:

    # marea = Marea('Prata')
    # kombi = Kombi('Branca')
    # up = Up('Cinza')

    # print(marea.informacoes(),'\n',marea.partida(),'\n',marea.acelerar(),'\n',marea.freiando())
    # print(kombi.informacoes(),'\n',kombi.partida(),'\n',kombi.acelerar(),'\n',kombi.freiando())
    # print(up.informacoes(),'\n',up.partida(),'\n',up.acelerar(),'\n',up.freiando())

m = Marea('Cinza').apresentar_veiculo()
p = Marea('Cinza').apresentar_pessoa()
r = Marea('Cinza').remover_passageiro()

print(m,'\n',p,'\n',r)



