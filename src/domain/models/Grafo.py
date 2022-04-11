class Grafo:

    def __init__(self, num_vet=0, num_arestas=0, lista_adj=None, mat_adj=None):
        self.num_vet = num_vet
        self.num_arestas = num_arestas

        if lista_adj == None:
            self.lista_adj = [[] for i in range(num_vet)]
        else:
            self.lista_adj = lista_adj

        if mat_adj == None:
            self.mat_adj = [[0 for i in range(num_vet)] for j in range(num_vet)]
        else:
            self.mat_adj = mat_adj


    def addAresta(self, source, destiny, value=1):
        if source < self.num_vet and destiny < self.num_vet:
            self.lista_adj[source].append((destiny, value))
            self.mat_adj[destiny][source] = value
            self.num_arestas += 1
        else:
            print("Aresta Inválida")


    def ler_arquivo(self, nome_arq):
        try:
            arq = open(nome_arq)
            str = arq.readline()
            str = str.split(" ")
            self.num_vet = int(str[0])
            self.num_arestas = int(str[1])
            print(f"Leitura numero de arestas: f{self.num_arestas}")
            self.lista_adj = [[] for i in range(self.num_vet)]
            self.mat_adj = [[0 for i in range(self.num_vet)] for j in range(self.num_vet)]

            for i in range(self.num_arestas):
                str = arq.readline()
                str = str.split(" ")
                source = int(str[0])
                destiny = int(str[1])
                value = int(str[2])
                self.addAresta(source, destiny, value)
        except IOError:
            print("Erro")


    def densidade(self):
        # Calcula a densidade de um grafo num_arestas / num_vet * num_vet-1.
        numeroDeAresta = self.num_arestas
        print(numeroDeAresta)
        numeroVertice = self.num_vet
        print(numeroVertice)
        densidade = self.num_arestas / (self.num_vet * (self.num_vet - 1))

        return float(densidade)


    def subgrafo(self, g2: Grafo):
        # verificar se g2 tem mais vertices que self
        # percorrer a matriz de adjacencia de g2
        # se alguma posição da matriz adj de g2 é != 0 e == 0 em self return False
        if g2.num_vert > self.num_vert:
            return False
        for i in range(len(g2.mat_adj)):
            for j in range(len(g2.mat_adj[i])):
                if g2.mat_adj[i][j] != 0 and self.mat_adj[i][j] == 0:
                    return False
        return True