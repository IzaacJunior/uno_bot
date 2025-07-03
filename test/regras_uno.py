from beta import Carta


def mesma_cor(carta1: Carta, carta2: Carta) -> bool:
    return carta1.estilo == carta2.estilo


# Exemplo de uso das comparações
if __name__ == "__main__":
    carta1 = Carta(5, (1, 2))
    carta2 = Carta(3, (4, 2))
    carta3 = Carta(5, (2, 2))
    carta4 = Carta(7, (1, 2))

    print(f"1 {carta1 == carta3}")
    print(f"2 {carta1 > carta2}")
    print(f"3 {carta2 < carta4}")
    print(f"4 {carta1 >= carta3}")
    print(f"5 {carta2 <= carta1}")
    print(f"6 {carta1 != carta2}")
    print("--" * 10)
    print(f"Mesma cor: {mesma_cor(carta1, carta2)}")  # True (mesmo estilo)
    print(f"Mesma cor: {mesma_cor(carta1, carta3)}")  # True (mesmo estilo)
    print(f"Mesma cor: {mesma_cor(carta2, carta3)}")  # True (mesmo estilo)
    print(f"Mesma cor: {mesma_cor(carta1, carta4)}")  # True (mesmo estilo)

    # Também funciona com sorting
    cartas = [carta4, carta1, carta2, carta3]
    print("Antes de ordenar:")
    print(*cartas, sep="\n")
    cartas.sort()
    print("Depois de ordenar:")
    print(*cartas, sep="\n")
