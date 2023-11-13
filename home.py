import pygame as pg
from menu import menu
from main import mostrar_menu, altura, largura
from pontuacoes import mostra_lista

pg.init()
pg.font.init()

tela = pg.display.set_mode((largura, altura))
fonte = pg.font.SysFont('Helvetica', 20)
texto_menu = fonte.render(menu(), 1, 'white')
clock = pg.time.Clock()
rodando = True

while rodando:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            rodando = False

        if e.type == pg.KEYDOWN:
            if e.key == 49:
                mostrar_menu()

            elif e.key == 50:
                mostra_lista()

            else:
                print('Pressione uma tecla válida.')

    tela.fill('black')

    tela.blit(texto_menu, (170, 160))

    pg.display.flip()

else:
    pg.font.quit()
    pg.quit()