from pprint import pprint

from beta import Baralho, Carta, Jogador


class Uno:
    def __init__(self) -> None:
        self.baralho: Baralho = self.__baralho()
        self.jogadores: list[Jogador] = []
        self.regras: list[any] = []

    def start(self) -> None:
        """
        Inicia o jogo
        """
        if not self.jogadores:
            raise ValueError("Nenhum jogador foi adicionado ao jogo")

        for jogador in self.jogadores:
            jogador.cartas.extend(self.baralho.comprar(7))

        self.baralho.pila.extend(self.baralho.comprar(1))
        return self.baralho.pila[-1]

    def __baralho(self) -> Baralho:
        lista = []
        for j in range(1, 5):
            for i in range(1, 9):
                lista.append(Carta(valor=i, estilo=(j, i), efeito=None))

        baralho = Baralho(lista)
        baralho.embaralhar()

        return baralho

    def validar(self, carta: Carta) -> None:
        ultima_carta = self.__repr__()
        for regra in self.regras:
            if not regra.validar(carta, ultima_carta):
                msg = f"A carta {carta} não é válida para jogar sobre {ultima_carta}"
                raise ValueError(msg)

    def __repr__(self) -> Carta:
        return self.baralho.pila[-1]


if __name__ == "__main__":
    uno = Uno()
    uno.jogadores.append(Jogador("Jogador 1"))
    uno.jogadores.append(Jogador("Jogador 2"))
    print(f"Jogadores: {[*uno.jogadores]}")

    test = uno.start()
    print(f"Baralho inicial: {test}")

    pprint(list(uno.baralho.baralho))
