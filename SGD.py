                                                                           #SISTEMA DE GESTÃO DE DOCAS Inicio 4/5/25
import json

import os

class Encomenda:
    estados_validos = ("pendente", "em preparação", "expedida", "entregue", "cancelada")

    def __init__(self, id_encomenda, descricao, cliente: 'Cliente', estado, doca: 'Doca', data):#'Cliente' e 'Doca'<- Relacionar com a class,
       #Valida o estado inicial
       if not self.estado_valido(estado):
           raise ValueError(f"Estado '{estado}' inválido. Estados válidos: {self.estados_validos}") #Bloqueia a criação de estados invalidos mais a ferente 
      

       self.id = id_encomenda #id da encomenda

       self.descricao = descricao #descricao da encomenda

       self.cliente = cliente #nome cliente

       self.estado = estado #estado da encomenda

       self.doca = doca #doca atribuida 

       self.data = data #hora da criação da encomenda

    def estado_valido(self, estado):
        return estado in self.estados_validos

    def atualizar_estado(self, novo_estado=None):
        if novo_estado is None:
         novo_estado = input("Introduz o novo estado da encomenda:\n").lower()
         if not self.estado_valido(novo_estado):
            raise ValueError(f"Estado '{novo_estado}' inválido. Estados válidos: {self.estados_validos}")
        self.estado = novo_estado
        print("Estado atualizado com sucesso.\n")

    def exibir_detalhes(self):
        
       print(f""" ID da encomenda: {self.id}             
Estado: {self.estado}
Descrição: {self.descricao}
Cliente: {self.cliente}
Doca atribuída: {self.doca}
Data da encomenda: {self.data}
""")

class User:
    utilizadores_validos = {
        "utilizador": "sgd",
        "admin": "adminsgd"
    }

    def __init__(self, nome, role):
        self.nome = nome
        self.role = role  # "admin" ou "gestor"

    @classmethod
    def autenticar(cls):
        conta = input("Introduz uma conta de utilizador:\n")
        if conta in cls.utilizadores_validos:
            senha = input("Introduz a password de utilizador:\n")
            if senha == cls.utilizadores_validos[conta]:
                print("Acesso autorizado\n")
                return cls(nome=conta, role=conta)
            else:
                print("Password incorreta.\n")
                return None
        else:
            print("Utilizador inválido!\n")
            return None

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

  def atualizar_o_estado_da_encomenda(self, id_encomenda):
    encontrado = False
    for encomenda in self.encomendas:
        if encomenda.id == id_encomenda:
            novo_estado = input("Introduz o novo estado da encomenda:\n").lower()
            try:
                encomenda.atualizar_estado(novo_estado)
                print("Estado atualizado com sucesso.\n")
            except ValueError as e:
                print(f"Erro: {e}\n")
            encontrado = True
            return
    if not encontrado:
        print("\tImpossível alterar o estado da encomenda!\n")
                            
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
            if doca.id_doca == remover:
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

    def ocupar_doca(self, id_doca):
        encontrado = False
        for doca in self.lista_de_docas:
            if doca.id_doca == id_doca:
                doca.ocupar()
                encontrado = True
                return
        if not encontrado:
            print("Doca não encontrada.\n")
      
#Fim de classes e metodos 11/5/25 17:46
# Inicio do Menu e funções

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
    if os.path.exists("encomendas.json"):  # verifica se o ficheiro existe
        with open("encomendas.json", "r", encoding="utf-8") as ficheiro:
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


if __name__ == "__main__":
    utilizador = User.autenticar()
    if utilizador:
        if utilizador.role == "admin":
            print("Bem-vindo ADMIN!")
            menu_admin(gestor_encomendas, gestor_docas)
        else:
            print("Bem-vindo GESTOR!")
            menu_user(utilizador)
    else:
        print("Falha na autenticação. O programa vai terminar.")

                
def menu_admin(gestor_encomendas, gestor_docas):
        print("\n--- MENU ADMIN ---")
        print("1. Adicionar encomenda")
        print("2. Remover encomenda")
        print("3. Listar encomendas")
        print("4. Atualizar estado da encomenda")
        print("5. Filtrar encomendas por estado")
        print("6. Procurar encomenda")
        print("7. Adicionar doca")
        print("8. Remover doca")
        print("9. Listar docas")
        print("10. Ocupar doca")
        print("0. Sair")
        escolha = input("Opção: ")

        match escolha:
            case "1":
                print("Funcionalidade: Adicionar encomenda")
            case "2":
                id_encomenda = input("ID da encomenda a remover: ")
                gestor_encomendas.remover_encomenda(id_encomenda)
            case "3":
                gestor_encomendas.listar_encomendas()
            case "4":
                id_encomenda = input("ID da encomenda para atualizar estado: ")
                gestor_encomendas.atualizar_o_estado_da_encomenda(id_encomenda)
            case "5":
                estado = input("Estado para filtrar: ")
                gestor_encomendas.filtrar_por_estado(estado)
            case "6":
                id_encomenda = input("ID da encomenda a procurar: ")
                gestor_encomendas.procurar_encomenda(id_encomenda)
            case "7":
                print("Funcionalidade: Adicionar doca (a implementar com input do utilizador)")
            case "8":
                id_doca = input("ID da doca a remover: ")
                gestor_docas.remover_doca(id_doca)
            case "9":
                gestor_docas.listar_docas()
            case "10":
                id_doca = input("ID da doca a ocupar: ")
                gestor_docas.ocupar_doca(id_doca)
            case "0":
                print("A sair do menu Admin...")
            case _:
                print("Opção inválida!")

lista_de_encomendas = Gestor_de_encomendas() # criamos a lista de ecomendas e atribuimos igualdade à class Gestor de Encomendas

def menu_user(gestor_encomendas): 
    while True:
        print("\n--- MENU UTILIZADOR ---")
        print("1. Listar encomendas")
        print("2. Atualizar estado da encomenda")
        print("3. Filtrar encomendas por estado")
        print("4. Procurar encomenda")
        print("0. Sair")
        escolha = input("Opção: ")

        match escolha:
            case "1":
                gestor_encomendas.listar_encomendas()
            case "2":
                id_encomenda = input("ID da encomenda para atualizar estado: ")
                gestor_encomendas.atualizar_o_estado_da_encomenda(id_encomenda)
            case "3":
                estado = input("Estado para filtrar: ")
                gestor_encomendas.filtrar_por_estado(estado)
            case "4":
                id_encomenda = input("ID da encomenda a procurar: ")
                gestor_encomendas.procurar_encomenda(id_encomenda)
            case "0":
                print("A sair do menu Gestor...")
                break
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    gestor_encomendas = Gestor_de_encomendas()
    gestor_docas = Gestor_de_doca()

    # Carregar dados APÓS criar os gestores
    carregar_dados(gestor_encomendas)

    utilizador = User.autenticar()
    if utilizador:
        if utilizador.role == "admin":
            menu_admin(gestor_encomendas, gestor_docas)  # Corrigido o nome
        else:
            menu_user(gestor_encomendas)  # Usar menu_user, não menu_gestor
    else:
        print("Falha na autenticação. O programa vai terminar.")

        #Fim 24/5 17:30
