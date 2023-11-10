import pygame as pg
from menu import menu
from db import get_usua_list
from main import rodar_jogo

pg.init()
pg.font.init()

tela = pg.display.set_mode((800, 600))
fonte = pg.font.SysFont('Consolas', 30)
texto_menu = fonte.render(menu(), 1, (255, 100, 100))
clock = pg.time.Clock()
sessao = True

while sessao:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sessao = False

        if e.type == pg.KEYDOWN:
            if e.key == 49:
                rodar_jogo()
            elif e.key == 50:
                get_usua_list()
            else:
                print('Pressione uma tecla válida.')

    tela.fill('green')

    tela.blit(texto_menu, (0, 0))

    pg.display.flip()

    clock.tick(60)

pg.quit()