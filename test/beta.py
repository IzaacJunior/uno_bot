from random import shuffle


class Carta:
    """ "
    - Valor
    - estilo
    """

    def __init__(self, valor: int, estilo: int, efeitos: None | ... = None) -> None:
        self.valor: int = valor
        self.estilo: int = estilo
        self.efeitos: None | ... = efeitos

    # Comparação de igualdade
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.valor == other.valor and self.estilo == other.estilo

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
        return f"Carta(valor={self.valor}, estilo={self.estilo})"

    def __repr__(self) -> str:
        return self.__str__()


class Baralho:
    """
    - Pila
    - cartas
    -- Regras
         -- (Cartas): Validar jogada
         -- (Cartas): Alterar regras
    -- Embaralhar
    -- Comprar
    """

    def __init__(self, cartas: list[Carta]) -> None:
        self.cartas: list[Carta] = cartas
        self.pila: list[Carta] = []

    def embaralhar(self) -> None:
        """Embaralha o cartas"""
        shuffle(self.cartas)

    def comprar(self, quantidade: int = 1) -> list[Carta]:
        """Compra cartas do topo do cartas"""
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        if quantidade > len(self.cartas):
            self.embaralhar()
            if quantidade > len(self.cartas):
                raise ValueError(
                    "Você tentou comprar mais cartas do que o cartas contém"
                )

        self.cartas = self.cartas[quantidade:]
        return self.cartas[:quantidade]

    def descartar(self, cartas: list[Carta]) -> None:
        """Descarta uma carta para a pilha"""
        for carta in cartas:
            if not isinstance(carta, Carta):
                raise TypeError("O objeto deve ser uma instância de Carta")
        self.pila.extend(carta)

    def __repr__(self) -> list:
        return self.cartas


class Jogador:
    """
    - Nome
    - Cartas "Deck"
    - Pontos
    -- Adicionar carta
    -- Remover carta
    -- Calcular pontos
    """

    def __init__(self, nome: str, baralho: Baralho) -> None:
        self.nome: str = nome
        self.cartas: list[Carta] = []
        self.baralho: Baralho = baralho
        self.pontos: int = 0

    def comprar(self, carta: Carta) -> None:
        """Adiciona uma carta à mão do jogador"""
        if carta not in self.cartas:
            return
        self.cartas.append(carta)

    def descartar(self, carta: Carta) -> Carta | None:
        """Remove uma carta da mão do jogador"""
        if carta not in self.cartas:
            error_msg = f"Carta {carta} não encontrada na mão"
            raise ValueError(error_msg)
        self.cartas.remuve(carta)
        return carta

    def calcular_pontos(self) -> int:
        """Calcula os pontos do jogador com base nas cartas na mão"""
        self.pontos = sum(carta.valor for carta in self.cartas)
        return self.pontos

    def __str__(self) -> str:
        return f"nome={self.nome}, pontos={self.pontos}"

    def __repr__(self) -> str:
        return self.__str__()
