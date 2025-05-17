
                                                                            #SISTEMA DE GESTÃO DE DOCAS Inicio 4/5/25
import json

import os

class Encomenda:
    estados_validos = ("pendente", "em preparação", "expedida", "entregue", "cancelada")

    def __init__(self, id_encomenda, descricao, cliente: 'Cliente', estado, doca: 'Doca', data):#'Cliente' e 'Doca'<- Relacionar com a class,
       if estado not in self.estados_validos:
        raise ValueError(f"Estado '{estado}' inválido. Estados válidos: {self.estados_validos}") #Bloqueia a criação de estados invalidos mais a ferente 
      

       self.id = id_encomenda #id da encomenda

       self.descricao = descricao #descricao da encomenda

       self.cliente = cliente #nome cliente

       self.estado = estado #estado da encomenda

       self.doca = doca #doca atribuida 

       self.data = data #hora da criação da encomenda



    def atualizar_estado(self):                                                     #Pausa 4/5/25 20:30  #retorno 8/5/25 19:20
           
           print(f"O estado atual da encomenda é: {self.estado}")

           print(f"Os estados possiveis da ecomenda são: {self.estados_validos}")

           novo_estado = input("Introduz um novo estado para a encomenda:\n")

           if novo_estado in self.estados_validos:
               
               self.estado = novo_estado

           else:
               print("Estado invalido!") 

   
    def exibir_detalhes(self):
        
       print(f"""
               ID da encomenda: {self.id}
               Estado: {self.estado}
               Descrição: {self.descricao}
               Cliente: {self.cliente}
               Doca atribuída: {self.doca}
               Data da encomenda: {self.data}
               """)

class User:
    utilizadores_validos = {
        "gestor" : "sgd",
        "admin" : "adminsgd" 
    }

    def autenticar(self):
        conta = input("Introduz uma conta de utlizador:\n")
        if conta in self.utilizadores_validos:
                senha = input("Introduz a password de utlizador\n")
                if senha == self.utilizadores_validos[conta]:
                    print("Acesso Autoririzado\n")
                    return True
                else:
                    print("Password incorreta.\n")
                    return False

        else : 
                print("Utilizador invalido!\n")
                return False

class Cliente():
    def __init__(self, id_cliente, nome, morada, email, telefone):

        self.id_cliente = id_cliente

        self.nome = nome

        self.morada = morada

        self.email = email

        self.telefone = telefone

    def para_dict(self):
        return{
            "id_cliente": self.id_cliente,
            "nome": self.nome,
            "morada": self.morada,
            "email": self.email,
            "telefone": self.telefone

        }    
    
    def __str__(self):
        return f"{self.nome} ({self.email})"    

    def exibir_cliente(self):

        print("\n".join([ 
              (f"Id: {self.id_cliente}"),
              (f"Nome: {self.nome}"),
              (f"Morada: {self.morada}"),
              (f"Email:{self.email}"),
              (f"Telefone:{self.telefone}")
              ]))


class Doca():
    def __init__(self, id_doca, nome, capacidade, estado = "livre"):

        self.id_doca = id_doca

        self.nome = nome

        self.capacidade = capacidade

        self.estado = estado
    
    def para_dict(self):
        return {
            "id_doca": self.id_doca,
            "nome": self.nome,
            "capacidade": self.capacidade,
            "estado": self.estado
        }    

    def exibir_doca(self):

        print("\n".join([
            f"Id da doca: {self.id_doca}",
            f"Nome da doca: {self.nome}",
            f"Capacidade: {self.capacidade}",
            f"Estado: {self.estado}"
        ]))

    def ocupar(self):
        if self.estado == "ocupada":
            print(f"A doca '{self.id_doca}' já está ocupada.\n")
        else:
            self.estado = "ocupada"
            print(f"A doca '{self.id_doca}' foi ocupada com sucesso.\n")

    def libertar(self):
        if self.estado == "livre":
            print(f"A doca '{self.id_doca}' já está livre.\n")
        else:
            self.estado = "livre"
            print(f"A doca '{self.id_doca}' foi libertada com sucesso.\n")

    def __str__(self):
        return f"{self.nome} - {self.estado}"        


            
class Gestor_de_encomendas():
    
  def __init__(self):
        self.utilizadores_validos = {
            "admin": "admin123",
            "user": "user123"
        }
        self.encomendas = []

  def autenticar(self):
        tentativas = 3
        while tentativas > 0:
            conta = input("Introduz uma conta de utilizador:\n")
            if conta in self.utilizadores_validos:
                senha = input("Introduz a password:\n")
                if senha == self.utilizadores_validos[conta]:
                    print("Acesso autorizado\n")
                    return True
                else:
                    print("Password incorreta.")
            else:
                print("Utilizador inválido.")

            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")
        print("Acesso negado.\n")
        return False

  def adicionar_encomenda(self, encomenda):
    
    if any(encomenda_existente.id == encomenda.id for encomenda_existente in self.encomendas):
        print("\t!Id já existente!\n")
        return
    self.encomendas.append(encomenda)    #associar encomenda
    

  def remover_encomenda(self, id_encomenda):
        
    encontrado = False #inicializar em false

    for artigo in self.encomendas: #iterar na lista turma
        if artigo.id == id_encomenda: #verifica condição
            self.encomendas.remove(artigo) # se a condição for verdade remover
            encontrado = True  # entrada em verdade
            print("Encomenda removida com sucesso\n")
            break #paragem

    if not encontrado: #se não entrar em verdade
        print("\tNão foi possivel remover a encomenda.\n")
        


  def procurar_encomenda(self, id_encomenda): #metodo de procura
    encontrado = False
    for encomenda in self.encomendas:

        if encomenda.id == id_encomenda:

            encontrado = True

            encomenda.exibir_detalhes()
            break # Para logo que encontrar

    if not encontrado:
        print("\tEncomenda não encontrada.\n")



  def listar_encomendas(self): #metodo para listar
    if not self.encomendas:
        print("Não existem encomendas registadas.")
        return #caso não seja encontrado nada para logo

    for encomendas in self.encomendas:
        encomendas.exibir_detalhes() #caso encontre exibe detalhes


  def filtrar_por_estado(self, estado): #metodo de filtragem

    encontrado = False #inicilizar a false

    for encomenda in self.encomendas:
        if encomenda.estado.lower() == estado.lower():
            encontrado = True
            encomenda.exibir_detalhes()

    if not encontrado:
        print("\tEstado não encontrado!\n")    

  def atualizar_o_estado_da_encomenda(self,id_encomenda): #metodo para atualizar o estado
        
    encontrado = False

    for encomenda in self.encomendas:

        if encomenda.id == id_encomenda:
            encomenda.atualizar_estado()
            encontrado = True
            return
    if not encontrado:
        print("\tImpossivel alterar o estado da encomenda!\n")
                            
                                                                        #paragem  8/5/2025 21:00 #retorno 11/5/25 17:00

class Gestor_de_doca():
    def __init__(self):
        self.lista_de_docas = []

    def adicionar_doca(self, doca):

            if any(d.nome == doca.nome for d in self.lista_de_docas):
                print("A doca já existe")
                return
            self.lista_de_docas.append(doca)

    def remover_doca(self, remover):
        
        encontrado = False

        for doca in self.lista_de_docas:
            if doca.id == remover:
                self.lista_de_docas.remove(doca)
                encontrado = True
                print("Doca removida com exito\n")
                guardar_dados()
                break
        if not encontrado:
            print("Doca não encontrada")
                                    

    def listar_docas(self) :
        if not self.lista_de_docas:
            print("Não existem docas.")
            return
        for doca in self.lista_de_docas:
            doca.exibir_doca()

    def ocupar_doca(id_doca):
        #continuar. Interrupção 00:10        




                                                     

#Fim de classes e metodos 11/5/25 17:46
# Inicio do Menu                                                     e funções
def erro (mensagem): #Função de erro
    print(f"!!!!!!ERRO!!!!!!!! {mensagem}") #Mensagem generica com mensagem personalizada quando a função for invocada

lista_de_encomendas = Gestor_de_encomendas() #atribuimos igualdade para a função dados      

def guardar_dados(nome_ficheiro="encomendas.json"):
    dados = []

    for encomenda in lista_de_encomendas.encomendas:
        dados.append({
            "id": encomenda.id,
            "descricao": encomenda.descricao,
            "cliente": encomenda.cliente.para_dict(),
            "estado": encomenda.estado,
            "doca": encomenda.doca.para_dict(),
            "data": encomenda.data
        })

    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Dados guardados com sucesso.")

def carregar_dados(lista_de_encomendas):  #  recebe a lista onde vai guardar
    if os.path.exists("Encomendas.json"):  # verifica se o ficheiro existe
        with open("Encomendas.json", "r", encoding="utf-8") as ficheiro:
            try:
                dados = json.load(ficheiro)  # carrega os dados do ficheiro JSON

                for item in dados:
                    cliente_dict = item["cliente"]
                    doca_dict = item["doca"]

                    # Criação correta do objeto Cliente
                    cliente = Cliente(
                        cliente_dict["id_cliente"],
                        cliente_dict["nome"],
                        cliente_dict["morada"],
                        cliente_dict["email"],
                        cliente_dict["telefone"]
                    )

                    # Criação do objeto Doca
                    doca = Doca(
                        doca_dict["id_doca"],
                        doca_dict["nome"],
                        doca_dict["capacidade"],
                        doca_dict["estado"]
                    )

                    # Criação da Encomenda com os dados lidos
                    encomenda = Encomenda(
                        id_encomenda=item["id"],
                        descricao=item["descricao"],
                        cliente=cliente,
                        estado=item["estado"],
                        doca=doca,
                        data=item["data"]
                    )

                    lista_de_encomendas.adicionar_encomenda(encomenda)

                print("\tDados Carregados Com SUCESSO!\n") 

            except json.JSONDecodeError:
                print("\tERRO: O ficheiro está corrompido ou mal formatado.\n")
    else:
        print("Ficheiro de dados não encontrado. Nenhum dado foi carregado.\n")

                
def menu(): #Contrutor de menu

    while True:  #enquanto existir interação devolve print
            
        try:

            print("\n".join([
                "\t\b[0] Terminar o programa",
                "\t\b[1] Adicionar encomenda",
                "\t\b[2] Remover encomenda",
                "\t\b[3] Procurar encomenda",
                "\t\b[4] Listar encomenda",
                "\t\b[5] Listar encomendas com o estado desejado",
                "\t\b[6] Atualizar o estado da encomenda\n"
            ]))

            op = int(input("Introduz um numero de [0] até [6]\n \t\bAtenção [0] PARA O PROGRAMA"))

            if op not in [0, 1, 2, 3, 4, 5, 6]: #verificação se o utilizador colocou uma opção correta.

                print("Introduz um valor válido!\n")

                continue #força a entrada no menu
            return op #retorna a escolha novamente
        
        except ValueError: #Usa o try para verificar exceção se o utilizador introduzir letras e não numeros!

                print("\t\bDeves introduzir um valor válido [um numero inteiro]!\n")

lista_de_encomendas = Gestor_de_encomendas() # criamos a lista de ecomendas e atribuimos igualdade à class Gestor de Encomendas



                        #Check-point 18:37
                        #Inicio 17/05 as 15:00 interrupção 19:00 retorno 22:00 feito class cliente user e doca desenvolver a class gestor de doca
                        #Interrupção 00:10
