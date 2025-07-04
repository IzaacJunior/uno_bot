import jogos as jg
from colored import fore, style


def azul(text: str) -> str:
    print(f"{fore('blue')}{text.center(30, '-')}{style('reset')}")


def red(text: str) -> str:
    print(f"{fore('red')}{text.center(30, '-')}{style('reset')}")


def pprint(*args: object) -> None:
    print(*args, sep="\n", end="\n\n")


def main() -> None:
    print("Iniciando o jogo UNO...")


if __name__ == "__main__":
    uno = jg.Uno()

    uno.add_jogador("Jogador 1")
    uno.add_jogador("Jogador 2")
    uno.add_jogador("Jogador 3")

    uno.start()

    azul("Caratas")
    uno.baralho.cartas.sort()
    pprint(*uno.baralho.cartas)
    azul("Pila")
    pprint(*uno.baralho.pila)
