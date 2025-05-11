
                                                                            #SISTEMA DE GESTÃO DE DOCAS Inicio 4/5/25

class Encomenda:
    estados_validos = ("pendente", "em preparação", "expedida", "entregue", "cancelada")

    def __init__(self, id_encomenda, descricao, cliente, estado, doca, data):
      

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

class Gestor_de_encomendas():
    
    def __init__(self): #metodo de inicialização da class
       
      self.encomenda = [] #abertura para receber informação
    
    def adicionar_encomenda(self, encomenda):
        
        if any(encomenda.id == novo.id for encomenda in self.encomenda):
            print("\t!Id já existente!\n")
            return
        self.encomenda.append(novo)    #associar encomenda
        

    def remover_encomenda(self, id_encomenda):
        
      encontrado = False #inicializar em false

      for artigo in self.encomenda: #iterar na lista turma
         if artigo.id == id_encomenda: #verifica condição
            self.encomenda.remove(artigo) # se a condição for verdade remover
            encontrado = True  # entrada em verdade
            print("Encomenda removida com sucesso\n")
            break #paragem

      if not encontrado: #se não entrar em verdade
          print("\tNão foi possivel remover a encomenda.\n")
          


    def procurar_encomenda(self, id_encomenda): #metodo de procura
        encontrado = False
        for encomenda in self.encomenda:

            if encomenda.id == id_encomenda:

                encontrado = True

                encomenda.exibir_detalhes()
                break # Para logo que encontrar

        if not encontrado:
            print("\tEncomenda não encontrada.\n")



    def listar_encomendas(self): #metodo para listar
        if not self.encomenda:
            print("Não existem encomendas registadas.")
            return #caso não seja encontrado nada para logo

        for encomendas in self.encomenda:
            encomendas.exibir_detalhes() #caso encontre exibe detalhes


    def filtrar_por_estado(self, estado): #metodo de filtragem

        encontrado = False #inicilizar a false

        for encomenda in self.encomenda:
            if encomenda.estado.lower() == estado.lower():
                encontrado = True
                encomenda.exibir_detalhes()

        if not encontrado:
            print("\tEstado não encontrado!\n")    

    def atualizar_o_estado_da_encomenda(self,id_encomenda): #metodo para atualizar o estado
        
         encontrado = False

         for encomenda in self.encomenda:

             if encomenda.id == id_encomenda:
                encomenda.atualizar_estado()
                encontrado = True
                return
         if not encontrado:
            print("\tImpossivel alterar o estado da encomenda!\n")
                            
                                                                        #paragem  8/5/2025 21:00 #retorno 11/5/25 17:00
                                                     

#Fim de classes e metodos 11/5/25 17:46
# Inicio do Menu                                                     e funções
def erro (mensagem): #Função de erro
    print(f"!!!!!!ERRO!!!!!!!! {mensagem}") #Mensagem generica com mensagem personalizada quando a função for invocada

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

def guardar_dados(): #função para guardar os dados
     dados = [] #abertura da variavel dados para receber informação dos dados a guardar

     for encomenda in lista_de_encomendas.encomenda: #aceder a lista de encomendas do gestor
          dados.append({
               "id": encomenda.id,
               "descricao": encomenda.descricao,
               "cliente": encomenda.cliente,
               "estado": encomenda.estado,
               "doca": encomenda.doca,
               "data": encomenda.data
          }) #informação que quremos acomular
     with  open("Encomendas.json", "w", encoding="utf-8") as ficheiro: #criação do ficheiro para escrita com o nome ficheiro
                json.dump(dados, ficheiro, ensure_ascii=False, indent= 4) #guardar dados no ficheiro


lista_de_encomendas = Gestor_de_encomendas() #atribuimos igualdade para a função dados  

def carregar_dados(): #Função para carregar os dados guardados no json

    if os.path.exists("Encomendas.json"): #verifica se o ficheiro existe
         with open("Encomendas.json", "r", encoding="utf-8") as ficheiro: #se existrir abre para leitura
            try:
                dados = json.load(ficheiro) #carrega os dados
            except json.JSONDecodeError:
                print("Erro: O ficheiro está corrompido ou mal formatado.")
                return    

            for encomendas_dict in dados: #iterar sobre os dicionarios do json
                id_encomenda = int(encomendas_dict["id"])
                descricao = str(encomendas_dict["descricao"])
                cliente= str(encomendas_dict["cliente"])
                estado = str(encomendas_dict["estado"])
                doca = int(encomendas_dict["doca"])
                data = str(encomendas_dict["data"])
                encomenda = Encomenda(id_encomenda, descricao, cliente, estado, doca, data) #precisamos de definir uma variavel
                lista_de_encomendas.adicionar_encomenda(encomenda) #lista de encomendas criada na função menu e acedemos ao meotodo adicionar encomenda da class Gestor de encomendas e guardamos a variavel da linha acima.

                        #Check-point 19:01

                        
