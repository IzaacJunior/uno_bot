import jogos as jg
from colored import fore, style
from regras import UnoRegras


def azul(text: str) -> str:
    print(f"{fore('blue')}{text.center(30, '-')}{style('reset')}")


def red(text: str) -> str:
    print(f"{fore('red')}{text.center(30, '-')}{style('reset')}")


def verde(text: str) -> str:
    print(f"{fore('green')}{text.center(30, '-')}{style('reset')}")


def pprint(*args: object) -> None:
    print(*args, sep="\n", end="\n\n")


def main() -> None:
    print("Iniciando o jogo UNO...")


if __name__ == "__main__":
    uno = jg.Uno()

    uno.add_jogador("Jogador 1")
    uno.add_jogador("Jogador 2")
    uno.add_jogador("Jogador 3")

    regras = UnoRegras()
    lista_de_regras = [
        regras.mesma_cor,
        regras.mesmo_valor,
    ]
    uno.regras.extend(lista_de_regras)

    uno.start()

    azul("Caratas")
    uno.baralho.cartas.sort()
    pprint(*uno.baralho.cartas)
    azul("Pila")
    pprint(*uno.baralho.pilha)
    while True:
        red(f"Vez do Jogador: {uno.jogadores[uno.atual].nome}")
        verde(f"{uno.baralho.pilha[-1]}")
        pprint(*uno.jogadores[uno.atual].cartas)
        op = input("Digite um numero para decartar ou '' para comprar: ")
        if not op:
            uno.comprar(1)
        else:
            test = uno.descartar([uno.jogadores[uno.atual].cartas[int(op) - 1]])
            print(test)
