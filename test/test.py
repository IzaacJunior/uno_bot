import beta as jg


def main(): ...


if __name__ == "__main__":
    main()
    # Testando a classe Jogador
    jogador = jg.Jogador("Jogador 1")
    print(f"Nome do Jogador: {jogador.nome}")

    # Testando a classe Carta
    carta = jg.Carta(5, (1, 2), "Efeito de exemplo")
    print(
        f"Valor da Carta: {carta.valor}, Estilo: {carta.estilo}, Efeito: {carta.efeito}"
    )

    # Testando a classe Baralho
    baralho = jg.Baralho()
    baralho.embaralhar()
    print(f"Baralho embaralhado: {[carta.valor for carta in baralho.baralho]}")
