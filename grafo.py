class Grafo:
    def __init__(self, num_vertices):
        """
        Inicializa um grafo de dependência com um número fixo de vértices.

        Args:
            num_vertices (int): O número de vértices no grafo.
        """
        self.num_vertices = num_vertices
        self.grafo = [[False] * num_vertices for _ in range(num_vertices)]

    def adicionar_dependencia(self, dependencia, acao):
        """
        Adiciona uma dependência entre dois vértices no grafo.

        Args:
            dependencia (int): O vértice que é dependente.
            acao (int): O vértice que é uma ação dependente da dependência.
        """
        self.grafo[dependencia][acao] = True

    def ordenacao_topologica(self):
        """
        Realiza a ordenação topológica do grafo de dependência.

        Retorna:
            list: Uma lista contendo a ordem de execução das dependências.
        """
        resultado = []
        visitados = [False] * self.num_vertices

        def dfs(vertice):
            """
            Função de busca em profundidade (DFS) para explorar o grafo recursivamente.

            Args:
                vertice (int): O vértice atual sendo processado.
            """
            visitados[vertice] = True
            for i in range(self.num_vertices):
                if self.grafo[vertice][i] and not visitados[i]:
                    dfs(i)
            resultado.insert(0, vertice)

        for vertice in range(self.num_vertices):
            if not visitados[vertice]:
                dfs(vertice)

        return resultado


def main():
    # Número total de vértices no grafo
    num_vertices = 4

    # Exemplo de grafo de dependência inspirado no jogo FIFA
    grafo_fifa = Grafo(num_vertices)
    grafo_fifa.adicionar_dependencia(0, 1)
    grafo_fifa.adicionar_dependencia(0, 2)
    grafo_fifa.adicionar_dependencia(1, 2)
    grafo_fifa.adicionar_dependencia(1, 3)
    grafo_fifa.adicionar_dependencia(3, 2)

    # Realizar a ordenação topológica
    ordem_execucao = grafo_fifa.ordenacao_topologica()

    # Imprimir a ordem de execução das dependências
    print("Ordem de execução das dependências:")
    for i, acao in enumerate(ordem_execucao):
        print(acao+1, end=' -> ' if i+1 < len(ordem_execucao) else '\n')


if __name__ == '__main__':
    main()
