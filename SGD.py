
                                                                            #SISTEMA DE GESTÃO DE DOCAS Inicio 4/5/25
# SISTEMA DE GESTÃO DE DOCAS
import json
import os

class Encomenda:
    estados_validos = ("pendente", "em preparação", "expedida", "entregue", "cancelada")

    def __init__(self, id_encomenda, descricao, cliente: 'Cliente', estado, doca: 'Doca', data):
        if not self.estado_valido(estado):
            raise ValueError(f"Estado '{estado}' inválido. Estados válidos: {self.estados_validos}")
        
        self.id = id_encomenda
        self.descricao = descricao
        self.cliente = cliente
        self.estado = estado
        self.doca = doca
        self.data = data

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
        "admin": "adminsgd",
        "utilizador": "sgd"
    }

    def __init__(self, nome, role):
        self.nome = nome
        self.role = role

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

class Cliente:
    def __init__(self, id_cliente, nome, morada, email, telefone):
        self.id_cliente = id_cliente
        self.nome = nome
        self.morada = morada
        self.email = email
        self.telefone = telefone

    def para_dict(self):
        return {
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
            f"Id: {self.id_cliente}",
            f"Nome: {self.nome}",
            f"Morada: {self.morada}",
            f"Email:{self.email}",
            f"Telefone:{self.telefone}"
        ]))

class Doca:
    def __init__(self, id_doca, nome, capacidade, estado="livre"):
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

class Gestor_de_encomendas:
    def __init__(self):
        self.encomendas = []

    def adicionar_encomenda(self, encomenda):
        if any(e.id == encomenda.id for e in self.encomendas):
            print("\t!Id já existente!\n")
            return
        self.encomendas.append(encomenda)

    def remover_encomenda(self, id_encomenda):
        for encomenda in self.encomendas:
            if encomenda.id == id_encomenda:
                self.encomendas.remove(encomenda)
                print("Encomenda removida com sucesso\n")
                return
        print("\tNão foi possível remover a encomenda.\n")

    def procurar_encomenda(self, id_encomenda):
        for encomenda in self.encomendas:
            if encomenda.id == id_encomenda:
                encomenda.exibir_detalhes()
                return
        print("\tEncomenda não encontrada.\n")

    def listar_encomendas(self):
        if not self.encomendas:
            print("Não existem encomendas registadas.")
            return
        for encomenda in self.encomendas:
            encomenda.exibir_detalhes()

    def filtrar_por_estado(self, estado):
        encontrado = False
        for encomenda in self.encomendas:
            if encomenda.estado.lower() == estado.lower():
                encontrado = True
                encomenda.exibir_detalhes()
        if not encontrado:
            print("\tEstado não encontrado!\n")    

    def atualizar_o_estado_da_encomenda(self, id_encomenda):
        for encomenda in self.encomendas:
            if encomenda.id == id_encomenda:
                try:
                    novo_estado = input("Introduz o novo estado da encomenda:\n").lower()
                    encomenda.atualizar_estado(novo_estado)
                except ValueError as e:
                    print(f"Erro: {e}\n")
                return
        print("\tImpossível alterar o estado da encomenda!\n")

class Gestor_de_doca:
    def __init__(self):
        self.lista_de_docas = []

    def adicionar_doca(self, doca):
        if any(d.id_doca == doca.id_doca for d in self.lista_de_docas):
            print("A doca já existe")
            return
        self.lista_de_docas.append(doca)

    def remover_doca(self, id_doca):
        for doca in self.lista_de_docas:
            if doca.id_doca == id_doca:
                self.lista_de_docas.remove(doca)
                print("Doca removida com exito\n")
                return
        print("Doca não encontrada")

    def listar_docas(self):
        if not self.lista_de_docas:
            print("Não existem docas.")
            return
        for doca in self.lista_de_docas:
            doca.exibir_doca()

    def ocupar_doca(self, id_doca):
        for doca in self.lista_de_docas:
            if doca.id_doca == id_doca:
                doca.ocupar()
                return
        print("Doca não encontrada.\n")

# Funções auxiliares
def guardar_dados(gestor_encomendas, gestor_docas, nome_ficheiro="encomendas.json"):
    dados = []
    for encomenda in gestor_encomendas.encomendas:
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

def carregar_dados(gestor_encomendas, gestor_docas):
    if os.path.exists("encomendas.json"):
        with open("encomendas.json", "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
                for item in dados:
                    # Carregar cliente
                    cliente = Cliente(
                        item["cliente"]["id_cliente"],
                        item["cliente"]["nome"],
                        item["cliente"]["morada"],
                        item["cliente"]["email"],
                        item["cliente"]["telefone"]
                    )
                    
                    # Carregar doca
                    doca = Doca(
                        item["doca"]["id_doca"],
                        item["doca"]["nome"],
                        item["doca"]["capacidade"],
                        item["doca"]["estado"]
                    )
                    gestor_docas.adicionar_doca(doca)
                    
                    # Criar encomenda
                    encomenda = Encomenda(
                        item["id"],
                        item["descricao"],
                        cliente,
                        item["estado"],
                        doca,
                        item["data"]
                    )
                    gestor_encomendas.adicionar_encomenda(encomenda)
                print("\tDados Carregados Com SUCESSO!\n")
            except json.JSONDecodeError:
                print("\tERRO: O ficheiro está corrompido ou mal formatado.\n")
    else:
        print("Ficheiro de dados não encontrado. Nenhum dado foi carregado.\n")

# Menus
def menu_admin(gestor_encomendas, gestor_docas):
    while True:
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
                try:
                    id_encomenda = input("ID da encomenda: ")
                    descricao = input("Descrição: ")
                    
                    print("\nDados do Cliente:")
                    cliente = Cliente(
                        input("ID do cliente: "),
                        input("Nome: "),
                        input("Morada: "),
                        input("Email: "),
                        input("Telefone: ")
                    )
                    
                    print("\nDados da Doca:")
                    doca = Doca(
                        input("ID da doca: "),
                        input("Nome: "),
                        int(input("Capacidade: "))
                    )
                    
                    encomenda = Encomenda(
                        id_encomenda,
                        descricao,
                        cliente,
                        "pendente",
                        doca,
                        input("Data (ex: 2024-05-20): ")
                    )
                    gestor_encomendas.adicionar_encomenda(encomenda)
                    guardar_dados(gestor_encomendas, gestor_docas)
                except Exception as e:
                    print(f"\nErro: {e}")

            case "2":
                gestor_encomendas.remover_encomenda(input("ID da encomenda a remover: "))
                guardar_dados(gestor_encomendas, gestor_docas)

            case "3":
                gestor_encomendas.listar_encomendas()

            case "4":
                gestor_encomendas.atualizar_o_estado_da_encomenda(input("ID da encomenda: "))
                guardar_dados(gestor_encomendas, gestor_docas)

            case "5":
                gestor_encomendas.filtrar_por_estado(input("Estado para filtrar: "))

            case "6":
                gestor_encomendas.procurar_encomenda(input("ID da encomenda: "))

            case "7":
                try:
                    gestor_docas.adicionar_doca(Doca(
                        input("ID da doca: "),
                        input("Nome da doca: "),
                        int(input("Capacidade: "))
                    ))
                    guardar_dados(gestor_encomendas, gestor_docas)
                except Exception as e:
                    print(f"\nErro: {e}")

            case "8":
                gestor_docas.remover_doca(input("ID da doca a remover: "))
                guardar_dados(gestor_encomendas, gestor_docas)

            case "9":
                gestor_docas.listar_docas()

            case "10":
                gestor_docas.ocupar_doca(input("ID da doca a ocupar: "))
                guardar_dados(gestor_encomendas, gestor_docas)

            case "0":
                print("A sair...")
                break

            case _:
                print("Opção inválida!")

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
                gestor_encomendas.atualizar_o_estado_da_encomenda(input("ID da encomenda: "))
            case "3":
                gestor_encomendas.filtrar_por_estado(input("Estado para filtrar: "))
            case "4":
                gestor_encomendas.procurar_encomenda(input("ID da encomenda: "))
            case "0":
                print("A sair do menu utilizador...")
                break
            case _:
                print("Opção inválida!")

# Bloco principal
if __name__ == "__main__":
    gestor_encomendas = Gestor_de_encomendas()
    gestor_docas = Gestor_de_doca()
    carregar_dados(gestor_encomendas, gestor_docas)

    user = User.autenticar()
    if user:
        if user.role == "admin":
            print("Bem-vindo ADMIN!")
            menu_admin(gestor_encomendas, gestor_docas)
        else:
            print("Bem-vindo Utilizador!")
            menu_user(gestor_encomendas)

#FIm 24/5 18:00
