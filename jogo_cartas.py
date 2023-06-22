from typing import List, Dict, Tuple
import random

# ♠ ♥ ♣ ♦ ♤ ♡ ♧ ♢ -> todos os naipes
CARTAS: List[str] = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
NAIPES: List[str] = '♠ ♡ ♢ ♣'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]

def criar_baralho(aleatório: bool = False) -> BARALHO:
    """Cria um baralho com 52 cartas"""
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES] #aqui temos uma lista de tuplas
    if aleatório:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])

def jogar() -> None:
    """Inicia um novo jogo de baralho para 4 jogadores"""
    baralho: BARALHO = criar_baralho(aleatório=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(baralho))}

    for jogador, baralho in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in baralho)
        print(f'{jogador}: {carta}')

if __name__ == '__main__':
    jogar()