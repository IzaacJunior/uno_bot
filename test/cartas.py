from enum import Enum
from random import shuffle


class TypeCarta(Enum):
    COMUM = "Comum"
    RARA = "Rara"


class Naipe(Enum):
    PRIMEIRO = "Um"
    SEGUNDO = "Dois"
    TERCEIRO = "Três"
    QUARTO = "Quatro"
    QUINTO = "Especial"


class Carta:
    def __init__(self, nome: str, tipo: TypeCarta, naipe: Naipe) -> None:
        self.nome: str = nome
        self.tipo: TypeCarta = tipo
        self.naipe: Naipe = naipe

    def __repr__(self) -> str:
        return f"{self.nome} ({self.tipo.value}, {self.naipe.value})"


class Baralho:
    def __init__(self) -> None:
        self.baralho: list[object] = []
        self.descarte: list[object] = []

    def embaralhar(self) -> None:
        """Pega todas as cartas da pilla de descarte menos a ultim e embaralha o baralho"""
        self.baralho.extend(self.descarte[:-1])
        shuffle(self.baralho)

    def comprar(self, quantidade: int = 1) -> list[object]:
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

    def resetar(self) -> None:
        """Reinicia o baralho para seu estado original"""
        self.baralho.clear()
        self.descarte.clear()


class Jogador:
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.cartas: list[object] = []
        self.pontos: int = 0

    def adicionar_carta(self, carta: list[object]) -> None:
        """Adiciona uma carta à mão do jogador"""
        self.cartas.extend(carta)

    def remover_carta(self, carta: object) -> None:
        """Remove uma carta da mão do jogador"""
        if carta in self.cartas:
            self.cartas.remove(carta)


class Jogo:
    def __init__(self) -> None:
        self.jogadores: list[Jogador] = []
        self.jogador_atual: int = 0
        self.direcao: int = 1  # 1 para sentido horário, -1 para anti-horário

    def proximo_jogador(self) -> None:
        """Avança para o próximo jogador"""
        self.jogador_atual = (self.jogador_atual + self.direcao) % len(self.jogadores)

    def adicionar_jogador(self, jogador: Jogador) -> None:
        """Adiciona um jogador ao jogo"""
        self.jogadores.append(jogador)

    def distribuir_cartas(self, baralho: Baralho, quantidade: int) -> None:
        """Distribui cartas para todos os jogadores"""
        for jogador in self.jogadores:
            cartas = baralho.comprar(quantidade)
            jogador.adicionar_carta(cartas)

    def iniciar_jogo(self, baralho: Baralho, quantidade_cartas: int) -> str:
        """Inicia o jogo com os jogadores e distribui cartas"""
        if len(self.jogadores) < 2:
            return "É necessário pelo menos dois jogadores para iniciar o jogo."
        baralho.embaralhar()
        self.distribuir_cartas(baralho, quantidade_cartas)
        self.proximo_jogador()
        return "Jogo iniciado com sucesso! Cartas distribuídas para os jogadores."

    def jogar_carta(self, jogador: Jogador, carta: object) -> str:
        """Permite que o jogador jogue uma carta"""
        ...
