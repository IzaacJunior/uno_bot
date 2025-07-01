# Cartas
#   - Valor
#   - estilo
#   - Primeira mão
#   -- Efeito (Baralho)
# Baralho
#   - Pila
#   - Baralho
#   -- Regras
#        -- (Cartas): Validar jogada
#        -- (Cartas): Alterar regras
#   -- Embaralhar
#   -- Comprar

from random import shuffle


class Estilos:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def uno(self) -> ...:
        return (self.x, self.y)


class Carta:
    def __init__(self, valor: int, estilo: tuple[int, int], efeito: any) -> None:
        self.valor: int = valor
        self.estilo: Estilos = Estilos(*estilo)
        self.efeito: any = efeito


class Baralho:
    def __init__(self) -> None:
        self.baralho: list[Carta] = []
        self.pila: list[Carta] = []
        self.regras: dict[str, any] = {}

    def embaralhar(self) -> None:
        """Embaralha o baralho"""
        shuffle(self.baralho)

    def regras(self, regras: dict[str, any]) -> None: ...

    def comprar(self, quantidade: int = 1) -> list[Carta]:
        """Compra cartas do topo do baralho"""
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        if quantidade > len(self.baralho):
            self.embaralhar()
            if quantidade > len(self.baralho):
                raise ValueError(
                    "Você tentou comprar mais cartas do que o baralho contém"
                )

        cartas_compradas = self.baralho[:quantidade]
        self.baralho = self.baralho[quantidade:]
        return cartas_compradas


class Jogador:
    # Jogador
    #   - Nome
    #   - Cartas "Deck"
    #   - Pontos
    #   -- Adicionar carta
    #   -- Remover carta
    #   -- Calcular pontos
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.cartas: list[Carta] = []
        self.pontos: int = 0

    def adicionar_carta(self, carta: Carta) -> None:
        """Adiciona uma carta à mão do jogador"""
        self.cartas.append(carta)

    def remover_carta(self, carta: Carta) -> None:
        """Remove uma carta da mão do jogador"""
        if carta in self.cartas:
            self.cartas.remove(carta)

    def calcular_pontos(self) -> int:
        """Calcula os pontos do jogador com base nas cartas na mão"""
        self.pontos = sum(carta.valor for carta in self.cartas)
        return self.pontos
