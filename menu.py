import re


def menu():
    return "1. Jogar | 2. Ver pontuações"


def get_nome_jogador(nome_jogador):
    encontrado = re.search("^[A-z ]+$", nome_jogador)

    if not encontrado:
        return [
            False,
            'Digite um nome válido'
        ]

    else:
        return True