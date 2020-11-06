
class Garrafa:
    def __init__(self, marca:str, litragem:float, material:str):
        self.marca = marca
        self.litragem = litragem
        self.material = material

    def __str__(self):
        return f"A garrafa da marca {self.marca} tem {self.litragem} litros e é feita de {self.material}"
    
    def cair(self):
        print("Crack, splashhhhh")

class Monitor:
    def __init__(self, marca:str, polegadas:int, peso:int):
        self.marca = marca
        self.polegadas = polegadas
        self.peso = peso

    def __str__(self):
        return f"O monitor da marca {self.marca} tem {self.polegadas} polegadas e pesa {self.peso} quilos"
    
    def ligando(self):
        print("bi bop")

class Relogio:
    def __init__(self, hora:int, minutos:int, segundos:int):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self):
        return f"Agora são {self.hora}:{self.minutos}:{self.segundos}"

    def tic(self):
        print("tictactictac")

class Livro:
    def __init__(self, nome:str, cor:str, pagina:int):
        self.nome = nome
        self.cor = cor
        self.pagina = pagina
    
    def __str__(self):
        return f"O livro {self.nome} de cor {self.cor} esta aberto na pagina {self.pagina}"
    
    def rasgar(self):
        print("raaaaash")
    
class Bicicleta:
    def __init__(self, cor:str, aro:int, peso:int):
        self.cor = cor
        self.aro = aro
        self.peso = peso

    def __str__(self):
        return f"A bike {self.cor} aro {self.aro} pesa {self.peso}"

    def quebrar(self):
        print("Ah mano acabei de tirar da revisão")

if __name__ == "__main__":

    g = Garrafa("First",0.5,"vidro")
    print(g)

    print(isinstance(g, Garrafa))

    g.cair()

    #######

    m = Monitor("Razer",21,3)
    print(m)

    print(isinstance(m, Monitor))

    m.ligando()

    #######

    r = Relogio(16,45,56)
    print(r)

    print(isinstance(r, Relogio))

    r.tic()

    ########

    l = Livro('aladin','verde',34)
    print(l)

    print(isinstance(l, Livro))

    l.rasgar()

    #######

    b = Bicicleta("branca",29,14)
    print(b)

    print(isinstance(b, Bicicleta))

    b.quebrar()
