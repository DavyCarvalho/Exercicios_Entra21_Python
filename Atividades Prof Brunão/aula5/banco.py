from veiculos import Pessoa

class DataSaver():
    """
    Essa é uma classe auxiliar com funçoes uteis para armazenamento e leitura do nosso banco de dados 
    que esta usando um arquivo .txt
    """
    __banco_de_dados = "Clientes_Banco.txt"
    
    # def __init__(self):
        # pass    
    
    
    def nome_arquivo(self):
        """
        Esta funcão nos retorna o nome do arquivo .txt (Nosso banco de dados)
        """
        
        return "Clientes_Banco.txt"    
    
    
    def procurar_pessoa(self, cpf_buscado):
        """
        Esta função abre nosso arquivo .txt no modo de leitura usando o parametro 'r' salvando 
        ele numa variavel (arquivo), logo após criamos uma nova variavel e atribuimos a 
        ela o nosso arquivo junto da função .readlines() que cria uma lista onde cada linha do nosso txt 
        vira um elemento da lista, dessa forma conseguimos manusear nosso arquivo de texto com o loop 'for'.
        """
        try:
            with open (self.__banco_de_dados, 'r') as arquivo:
                
                linhas_arquivo = arquivo.readlines()
                
                for linha in linhas_arquivo:
                    if cpf_buscado == linha.strip().split(",")[2]:
                        nome, idade, cpf, *outros = linha.strip().split(",")  
  
                        return nome, idade, cpf, outros
                    """
                    Explicação: 
                    
                    conteudo do arquivo txt =   Davy,21,106
                                                artur,27,123
                                                jessica,27,321

                    linhas_arquivo = arquivo.readlines()
                                ==
                    linhas_arquivo = ["Davy,21,106\n","artur,27,123\n","jessica,27,321\n"]
                    
                    for linha(ELEMENTO) in linhas_arquivo(LISTA):
                    
                        if cpf_buscado(ELEMENTO_BUSCADO) == linha.strip().split(",")[2]: 
                        
                        linha.strip() = "Davy,21,106"
                        linha.split(",") = ['Davy','21','106']
                        
                        indice-------------> 0 --> 1 --> 2
                        
                        linha.strip().split(",")[2] = '106'
                        
                            nome, idade, cpf, *outros = linha.strip().split(",")
                            nome, idade, cpf, *outros = 'Davy', '21', '106'
                            
                            nome = 'Davy'
                            idade = '21'
                            cpf = '106'
                            outros = []
                    
                    
                    """
                
        except FileNotFoundError:
            print(u"Não há pessoas cadastradas!")
            return None
        
        
    def salvar_pessoa(self, pessoa):
        """
        Esta função faz o trabalho de criar uma nova linha para o arquivo txt, e 
        atribui essa linha a uma variavel (conteudo), o return dela é a chamada da 
        função escrever_arquivo() usando a variavel 'conteudo' como um dos parametros
        """
        
        conteudo = f"{pessoa.nome},{pessoa.idade},{pessoa.cpf}\n"
        
        return self.escrever_arquivo(self.__banco_de_dados, conteudo)
    
      
    def escrever_arquivo(self, nome_arquivo, conteudo):
        """
        Esta função recebe uma variavel que contem um nova linha para o arquivo txt criada 
        pela função salvar_pessoa(), abre o arquivo txt e salva essa nova linha
        """
       
        try:
            
            with open(nome_arquivo, "a") as arquivo:
                arquivo.write(conteudo)
        
        except FileNotFoundError:
            
            with open(nome_arquivo, "a") as arquivo:
                print(u"Arquivo criado, pois ainda não existia.")
                
                arquivo.write(conteudo)
                
        return True
    
    
    def verificar_conta(self, cpf):
        """
        Esta função usa o return da função procurar_pessoa(), usando especificamente a variavel 
        outros - que no caso de a pessoa ter uma conta, vai conter uma lista de dados. 
        Usando o if com a função len, nós comparamos se o cumprimento dessa lista é maior que 0, caso seja,
        quer dizer que a pessoa já tem uma conta dando return 'False', caso contrario quer dizer que ela
        ainda não tem uma conta e o return é 'True', usamos esses returns booleanos para ativar ou não, 
        alguma condição
        """
        
        nome, idade, cpf, outros = self.procurar_pessoa(cpf)
        
        if len(outros) != 0:
            return True
        
        else:
            return False
         
class Banco():
    """
    
    """
    def __init__(self, num_banco: str, agencia: str):
        self.num_banco = num_banco
        self.agencia = agencia
            
    def __str__(self):
        return (f"O banco {type(self).__name__} possui número {self.num_banco}"
                f"E pertence à agência {self.agencia}.")

    def criar_conta(self, nome_banco, cpf, conta):
        
        saldo = 0
        pessoas_nuconta = 0
        pessoas_viacredi = 0
        
        with open(data_saver.nome_arquivo(), "r") as arquivo:
            
            linhas_arquivo = arquivo.readlines()

            for pos, linha in enumerate(linhas_arquivo):
                
                if "NuConta" in linha:
                    pessoas_nuconta += 1
                                
                elif "Viacredi" in linha:
                    pessoas_viacredi += 1
                
                if cpf in linha.strip(','):
                    
                    posicao = pos
                    
            if nome_banco == "Viacredi":
                conta_corrente = 2374501 + pessoas_viacredi
             
            elif nome_banco == "NuConta":
                conta_corrente = 173 + pessoas_nuconta
            
            
            linhas_arquivo[posicao] = linhas_arquivo[posicao].strip()
            
            linhas_arquivo[posicao] += (f",{nome_banco},{conta.num_banco},"
                                    f"{conta.agencia},{conta_corrente},"
                                    f"{saldo}\n")
        
        with open(data_saver.nome_arquivo(), "w") as arquivo:
            arquivo.writelines(linhas_arquivo)    


    def depositar(self, cpf):
        
        deposito = float(input("Digite o valor a ser depositado:\nR$ "))
        
        with open(data_saver.nome_arquivo(), "r") as arquivo:
            linhas_arquivo = arquivo.readlines()
            
            for pos, linha in enumerate(linhas_arquivo):
                
                if cpf in linha.strip(','):
                    
                    linha_alterada = linhas_arquivo[pos].strip().split(",")
                    
                    saldo = float(linha_alterada[-1])
            
                    linha_alterada[-1] = str(saldo + deposito)
                    
                    linhas_arquivo[pos] = ",".join(linha_alterada)+"\n"
                
        with open(data_saver.nome_arquivo(), "w") as arquivo:
            arquivo.writelines(linhas_arquivo)

class NuConta(Banco):
    def __init__(self):
        super().__init__("260","0001")
            
class Viacredi(Banco):
    def __init__(self):
        super().__init__("085", "0101")
                
# class Conta():
    # def __init__(self, banco: Banco, pessoa: Pessoa):
        # self.banco = banco
        # self.pessoa = pessoa
                
if __name__ == "__main__":
    data_saver = DataSaver()
    while True:
        try: 
            valor = int(input(
                """Digite a operação desejada
                1 - Cadastrar Pessoa
                2 - Cadastrar Conta
                3 - Visualizar Saldo
                4 - Fazer um depósito
                5 - Procurar pessoa
                6 - Sair\n"""))

            if (valor not in range(1,7)):
                
                print("Valor inválido! Tente novamente.")
                continue
        
        except:
            print("Valor inválido! Tente novamente.")
            continue
        
        else:
        
            if valor == 1:
                
                nome = input("Insira o nome do cliente:\n")
                idade = int(input("Insira a idade do cliente:\n"))
                cpf = input("Insira o cpf do cliente:\n")                
                
                data_saver.salvar_pessoa(Pessoa(nome, idade, cpf))

            if valor == 2:
                
                cpf = input("Qual cpf você "
                                "gostaria de criar uma conta?")
                
                if data_saver.procurar_pessoa(cpf):
                    
                    nome, idade, cpf, outros = data_saver.procurar_pessoa(cpf)

                    if len(outros) != 0:
                        
                        print("Este cliente já possui uma conta!")
                        
                    else:   
                    
                        while True:
                            
                            opcao = int(input("""Em qual banco você deseja
    cadastrar a conta do cliente?
    
    1) NuConta
    2) Viacredi                               
    
    """))

                            if (opcao not in range(1,3)):
                                
                                print("Você digitou algo errado. Tente novamente")

                            elif opcao == 1:
                                banco = "NuConta"
                                conta = NuConta()
                                conta.criar_conta(banco, cpf, conta)
                                print(conta.agencia)
                                break
                            
                            else:
                                banco = "Viacredi"
                                conta = Viacredi()
                                conta.criar_conta(banco, cpf, conta)
                                print(conta.agencia)
                                break
                                                                
                else:
                    print("CPF não encontrado!\n")
                

            if valor == 3:
                
                cpf = input("Digite o CPF do cliente "
                            "para verificar seu saldo:\n")
                
                if data_saver.procurar_pessoa(cpf):
                    
                    if data_saver.verificar_conta(cpf):
                        
                        nome, idade, cpf, outros = data_saver.procurar_pessoa(cpf)
                    
                        saldo = outros[-1]

                        print(f"O saldo do cliente {nome} e cpf {cpf} é de:\n"
                            f"R${float(saldo):.2f}")
                    
                    else:
                        print("Cliente não possui conta em banco")
                        
                else:
                    print("Usuário não cadastrado!")
            
            if valor == 4:
                
                cpf = input("Digite o CPF do cliente "
                            "para verificar seu saldo:\n")
                
                if data_saver.verificar_conta(cpf):

                    deposito_banco = NuConta()
                
                    deposito_banco.depositar(cpf)
                
                else:
                    
                    print("Cliente não possui conta em banco")

            if valor == 5:
                cpf = input("Digite o CPF do cliente que você procura:\n")
                
                if data_saver.procurar_pessoa(cpf):
                    
                    nome, idade, cpf, outros = data_saver.procurar_pessoa(cpf)
                
                    print(f"""Resultado encontrado:
        Nome: {nome}
        Idade: {idade}
        CPF: {cpf}
        """)
   
            if valor == 6:
                print("Agradecemos a sua visita!")
                break
