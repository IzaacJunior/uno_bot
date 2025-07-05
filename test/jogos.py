from abc import ABC, abstractmethod

from beta import Baralho, Carta, Jogador


class Base(ABC):
    def __init__(self) -> None:
        self.baralho: Baralho = self._baralho()
        self.jogadores: list[Jogador] = []
        self.regras: list[object] = []
        self.atual: int = 0
        self.sentido: int = 1

    def add_jogador(self, nome: str) -> None:
        """
        Adiciona um jogador ao jogo.
        """
        self.jogadores.append(Jogador(nome))

    def proximo_jogador(self) -> None:
        """
        Avança para o próximo jogador
        """
        self.atual = (self.atual + self.sentido) % len(self.jogadores)

    def comprar(self, quantidade: int = 1) -> None:
        """
        Compra cartas do baralho para o jogador atual.
        """
        cartas_compradas = self.baralho.comprar(quantidade)
        self.jogadores[self.atual].cartas.extend(cartas_compradas)
        self.proximo_jogador()

    def descartar(self, cartas: list[Carta]) -> bool:
        """
        Descarta cartas do jogador atual para a pilha.
        """
        jogador = self.jogadores[self.atual]
        ultima_carta = self.baralho.pilha[-1]

        if not self.validar(cartas):
            return False

        for carta in cartas:
            jogador.cartas.remove(carta)
        self.baralho.pilha.extend(cartas)
        self.proximo_jogador()
        return True

    @abstractmethod
    def start(self, hand: int = 7) -> None:
        """
        Inicia o jogo, distribuindo cartas para os jogadores e colocando a primeira carta na pilha.
        """
        pass

    @abstractmethod
    def _baralho(self) -> Baralho:
        """
        Cria e embaralha o baralho de cartas.
        """
        pass

    @abstractmethod
    def validar(self, carta: Carta) -> None:
        """
        Valida se as cartas descartadas são válidas de acordo com as regras do jogo.
        """
        pass


class Uno(Base):
    def __init__(self) -> None:
        super().__init__()
        self.efeitos: list[object] = []

    def start(self, hand: int = 7) -> None:
        """
        Inicia o jogo
        """
        if not self.jogadores:
            raise ValueError("Nenhum jogador foi adicionado ao jogo")

        for jogador in self.jogadores:
            jogador.cartas.extend(self.baralho.comprar(hand))

        self.baralho.pilha.extend(self.baralho.comprar(1))
        return self.baralho.pilha[-1]

    def _baralho(self) -> Baralho:
        lista = []
        for j in range(1, 5):
            for i in range(1, 9):
                lista.append(Carta(valor=i, estilo=j))
            for i in range(10, 13):
                lista.append(Carta(valor=i, estilo=j, efeito=True))

        baralho = Baralho(lista)
        baralho.embaralhar()

        return baralho

    def validar(self, cartas: list[Carta]) -> bool:
        ultima_carta = self.baralho.pilha[-1]
        info = []
        for carta in cartas:
            info.append(any(regra(carta, ultima_carta) for regra in self.regras))
        return all(info)
