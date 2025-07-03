from random import shuffle


class Estilos:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def uno(self) -> ...:
        return (self.x, self.y)


class Efeito: ...


class Carta:
    """ "
    - Valor
    - estilo
    - Primeira mão
    -- Efeito (Baralho)
    """

    def __init__(
        self, valor: int, estilo: tuple[int, int], efeito: Efeito | None = None
    ) -> None:
        self.valor: int = valor
        self.estilo: tuple[int, int] = estilo
        self.efeito: Efeito = efeito

    # Comparação de igualdade
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor == other.valor

    # Menor que
    def __lt__(self, other: "Carta") -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor < other.valor

    # Menor ou igual
    def __le__(self, other: "Carta") -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor <= other.valor

    # Maior que
    def __gt__(self, other: "Carta") -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor > other.valor

    # Maior ou igual
    def __ge__(self, other: "Carta") -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor >= other.valor

    # Diferente (não igual)
    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f"Carta(valor={self.valor}, estilo={self.estilo}, efeito={self.efeito})"

    def __repr__(self) -> str:
        return self.__str__()


class Baralho:
    """
    - Pila
    - Baralho
    -- Regras
         -- (Cartas): Validar jogada
         -- (Cartas): Alterar regras
    -- Embaralhar
    -- Comprar
    """

    def __init__(self, baralho: list[Carta]) -> None:
        self.baralho: list[Carta] = baralho
        self.pila: list[Carta] = []

    def embaralhar(self) -> None:
        """Embaralha o baralho"""
        shuffle(self.baralho)

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

        self.baralho = self.baralho[quantidade:]
        return self.baralho[:quantidade]


class Jogador:
    """
    - Nome
    - Cartas "Deck"
    - Pontos
    -- Adicionar carta
    -- Remover carta
    -- Calcular pontos
    """

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.cartas: list[Carta] = []
        self.pontos: int = 0

    def pegar_carta(self, carta: Carta) -> None:
        """Adiciona uma carta à mão do jogador"""
        if carta in self.cartas:
            ...
            self.cartas.append(carta)

    def jogar_carta(self, carta: Carta) -> None:
        """Remove uma carta da mão do jogador"""
        if carta in self.cartas:
            self.cartas.remove(carta)

    def calcular_pontos(self) -> int:
        """Calcula os pontos do jogador com base nas cartas na mão"""
        self.pontos = sum(carta.valor for carta in self.cartas)
        return self.pontos

    def __str__(self) -> str:
        return f"nome={self.nome}, pontos={self.pontos}"

    def __repr__(self) -> str:
        return self.__str__()
