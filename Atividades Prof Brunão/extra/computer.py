# Crie as seguintes classes com suas determinadas carcteristicas
# ram, hd, processador

# Agora, crie a classe Placa_mae, que deve ser composta pelos 3 itens acima

# Por fim, utilizando herança, crie dispositivos que utilizam a placa mãe; 
# por exemplo: computador
from time import sleep 

class Ram():
    """
    Essa é a memoria rapida do computador, onde as informações são alocadas para se poder trabalhar com elas....
    """
    def iniciar_ram(self):
        return 'Mémoria RAM - READY'
    
    
    def desligar_ram(self):
        return 'Mémoria RAM - ShutDown'
    
    
    def salvar_dado_rapido_ram(self):
        return 'Informações alocadas na Memória RAM!'
    
    
    def liberar_memoria_ram(self):
        return 'Memória RAM liberada!'
 

class Hd():
    """
    Essa é a memória de lenta do computador, onde as informações são alocadas a longo prazo...
    """
    def iniciar_hd(self):
        return 'HD - READY'
    
    
    def desligar_hd(self):
        return 'HD - ShutDown'
    
    
    def salvar_arquivo_hd(self):
        return 'Arquivo Salvo no HD!'
    
    
    def apagar_arquivo_hd(self):
        return 'Arquivo apagado do HD com sucesso!'  
    
    
class Processador():
    """
    Essa é a ferramenta que o computador usa para trabalhar com os dados alocados nas memórias...
    """        
       
        
    def iniciar_processador(self):
        return 'PROCESSADOR - READY'
    
    
    def desligar_processador(self):
        return 'Processador - ShutDown'

    
    def processar_dados(self):
        return "Carregando...\n\nDados carregados!"
    
    
    
    # def salvar_no_hd(self):
    #     return Hd(self).salvar_arquivo_hd()
    
    
    # def salvar_arquivo_ram(self):
    #     return Ram(self).salvar_dado_rapido_ram()   
    
    
    def erro_processador(self):
        return 'Erro! Não foi possível computar os dados!'
    
    
class Placa_mae():
    """
    É responsavel por ligar e administrar as funçoes de todos os componentes...
    """
    def __init__(self,Ram:object, Hd:object, Processador:object):
        self.Ram = Ram
        self.Hd = Hd
        self.Processador = Processador
    
    
    def salvar_dado_hd(self):
        return self.Hd.salvar_arquivo_hd()
    
    
    def salvar_dado_ram(self):
        return self.Ram.salvar_dado_rapido_ram()
    
    
class Computador():
    """
    A maquina enfim....
    """
    
    def __init__(self, Placa_mae:object):
        self.Placa_mae = Placa_mae
        self.pc_ligado = False   #criando uma variavel de verificação para saber se o PC ta ligado

    def ligar_pc(self):
        if self.pc_ligado == False:
            print("Iniciando o windous.... ")
            sleep(1)
            print(f"{self.Placa_mae.Ram.iniciar_ram()}\n"
                    f"{self.Placa_mae.Hd.iniciar_hd()}\n"
                    f"{self.Placa_mae.Processador.iniciar_processador()}\n")
            self.pc_ligado = True
            return "Windous Iniciado!!!\n"
        else:
            return "O pc ja ta ligado oh MERDA!"
                
    
    
    def alocar_dados_ram(self):
        return f"{self.Placa_mae.Ram.salvar_dado_ram()}"
    
    
    def alocar_dados_hd(self):
        return f"{self.Placa_mae.Ram.salvar_dado_hd()}"
    
    
    def desligar_pc(self):
        if self.pc_ligado == True:
            print(f"{self.Placa_mae.Ram.desligar_ram()}")
            print(f"{self.Placa_mae.Hd.desligar_hd()}\n"
            f"{self.Placa_mae.Processador.desligar_processador()}\n")
            sleep(1)
            print(f"Computador desligado com sucesso! Xau!\n")
            self.pc_ligado = False
            return f"{' WINDOUS ':=^30}\n"
        else:
            return ("O sua anta o pc ja ta desligado, não sei nem como " 
                    "essa mensagem ta aparecendo pra ti!")
    
    
def main():
    
    print(f"{' WINDOUS ':=^30}\n")
    
    ram = Ram()
    hd = Hd()
    processador = Processador()
    
    placa_mae = Placa_mae(ram, hd, processador)
    
    computador = Computador(placa_mae)
    
    print(f'{computador.ligar_pc()}\n')
    
    print(f'{computador.ligar_pc()}\n')
    
    print(f'{computador.Placa_mae.Processador.processar_dados()}\n')
    
    print(f'{computador.Placa_mae.salvar_dado_hd()}\n')
    
    print(f'{computador.Placa_mae.salvar_dado_ram()}\n')
    
    print(f'{computador.desligar_pc()}\n')
    
    print(f'{computador.desligar_pc()}\n')
    
    
if __name__ == "__main__":
    main()