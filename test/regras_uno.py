from beta import Carta


class UnoRegras:
    def mesma_cor(self, carta1: Carta, carta2: Carta) -> bool:
        return carta1.estilo == carta2.estilo

    def mesmo_valor(self, carta1: Carta, carta2: Carta) -> bool:
        return carta1.valor == carta2.valor


class UnoEfeitos:
    def pular(self) -> bool:
        pass

    def inverter(self) -> bool:
        pass

    def mais_dois(self) -> bool:
        pass

    def mais_quatro(self, cor: int) -> bool:
        pass

    def trocar_baralho(self) -> bool:
        pass

    def mutar(self) -> bool:  # Silenciar os jogadores
        pass

    def bater(
        self,
    ) -> bool:  # Usar o emoji do discord para representar o efeito de bater
        pass


def coringa(carta: Carta) -> bool:
    return carta.valor in [10, 11, 12]  # Exemplo: 10 = +2, 11 = Inverter, 12 = Pular
