import pygame as pg
import db
from main import altura, largura

pg.init()
pg.font.init()

fonte = pg.font.SysFont('Helvetica', 15)
tela = pg.display.set_mode((largura, altura))
clock = pg.time.Clock()


def mostra_lista():
    lista_usuarios = db.get_list_usuarios()

    rodando = True

    while rodando:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False

        tela.fill('black')

        # Renderiza a lista
        for i, item in enumerate(lista_usuarios):
            texto = fonte.render(f"{i + 1}. Nome: {item[0]} - Pontuação: {item[1]} - Data da tentativa: {item[2]}", 1, 'white')

            tela.blit(texto, (60, 50 + i * 40))

        pg.display.flip()