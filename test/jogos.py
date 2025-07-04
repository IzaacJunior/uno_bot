from abc import ABC, abstractmethod

from beta import Baralho, Carta, Jogador


class Base(ABC):
    def __init__(self) -> None:
        self.baralho: Baralho = self._baralho()
        self.jogadores: list[Jogador] = []
        self.regras: list[any] = []
        self.atual: int = 0
        self.sentido: int = 1

    def add_jogador(self, nome: str) -> None:
        self.jogadores.append(Jogador(nome, self.baralho))
        return

    @abstractmethod
    def _baralho(self) -> Baralho:
        pass

    @abstractmethod
    def validar(self, carta: Carta) -> None:
        pass

    def __repr__(self) -> Carta:
        return self.baralho.pila[-1]


class Uno(Base):
    def __init__(self) -> None:
        super().__init__()

    def start(self, hand: int = 7) -> None:
        """
        Inicia o jogo
        """
        if not self.jogadores:
            raise ValueError("Nenhum jogador foi adicionado ao jogo")

        for jogador in self.jogadores:
            jogador.cartas.extend(self.baralho.comprar(hand))

        self.baralho.pila.extend(self.baralho.comprar(1))
        return self.baralho.pila[-1]

    def _baralho(self) -> Baralho:
        lista = []
        for j in range(1, 5):
            for i in range(1, 12):
                lista.append(Carta(valor=i, estilo=j))

        baralho = Baralho(lista)
        baralho.embaralhar()

        return baralho

    def comprar(self, quantidade: int = 1) -> None:
        """
        Compra cartas do baralho para o jogador atual.
        """
        if not self.jogadores:
            raise ValueError("Nenhum jogador foi adicionado ao jogo")

        cartas_compradas = self.baralho.comprar(quantidade)
        self.jogadores[self.atual].cartas.extend(cartas_compradas)
        self.atual += 1

    def descartar(self, cartas: list[Carta]) -> None:
        """
        Descarta cartas do jogador atual para a pilha.
        """
        if not self.jogadores:
            raise ValueError("Nenhum jogador foi adicionado ao jogo")

        if not cartas:
            raise ValueError("Nenhuma carta foi fornecida para descartar")
        jogador = self.jogadores[self.atual]
        for carta in cartas:
            if carta not in jogador.cartas:
                msg = f"A carta {carta} não está na mão do jogador {jogador.nome}"
                raise ValueError(msg)

        for carta in cartas:
            jogador.cartas.remove(carta)
        self.baralho.pila.extend(cartas)

    def validar(self, carta: Carta) -> bool:
        ultima_carta = self.__repr__()
        if not any(regra(carta, ultima_carta) for regra in self.regras):
            return False
        ...
        return True
