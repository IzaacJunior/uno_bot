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
        self.jogadores.append(Jogador(nome))

    def proximo_jogador(self) -> None:
        """Avança para o próximo jogador"""
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
        for carta in cartas:
            print("-----")
            print(self.regras)
            print("-----")
            if any(regra(carta, ultima_carta) for regra in self.regras):
                continue
            return False

        for carta in cartas:
            jogador.cartas.remove(carta)
        self.baralho.pilha.extend(cartas)
        self.proximo_jogador()
        return True

    @abstractmethod
    def _baralho(self) -> Baralho:
        pass

    @abstractmethod
    def validar(self, carta: Carta) -> None:
        pass


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

        self.baralho.pilha.extend(self.baralho.comprar(1))
        return self.baralho.pilha[-1]

    def _baralho(self) -> Baralho:
        lista = []
        for j in range(1, 5):
            for i in range(1, 12):
                lista.append(Carta(valor=i, estilo=j))

        baralho = Baralho(lista)
        baralho.embaralhar()

        return baralho

    def validar(self, carta: Carta) -> bool:
        ultima_carta = self.pilha[-1]
        if not any(regra(carta, ultima_carta) for regra in self.regras):
            return False
        ...
        return True

    def add_efeito(self, efeito: any) -> None:
        pass
