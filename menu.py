import pygame
import sys

pygame.init()

largura_tela = 600
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Meu Jogo")



def mostrar_menu(pontuacao = '0'):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Lógica para manipular eventos de teclado (por exemplo, pressionar ESPAÇO para iniciar o jogo)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return# Retorna da função para começar o jogo

        # Desenhe elementos do menu na tela
        tela.fill((0, 0, 0))  # Preenche a tela com fundo preto
        fonte = pygame.font.Font(None, 36)
        texto1 = fonte.render(f"Ultima pontuação {pontuacao}", True, (255, 255, 255))
        texto = fonte.render("Pressione ESPAÇO para iniciar", True, (255, 255, 255))  # Texto branco
        tela.blit(texto, (largura_tela // 2 - texto.get_width() // 2, altura_tela // 2 - texto.get_height() // 2))
        tela.blit(texto1, (largura_tela // 2 - texto1.get_width() // 2, altura_tela // 2 + texto.get_height()))  # Posição abaixo do texto principal
        pygame.display.flip()  # Atualiza a tela

# Chame a função do menu antes de começar o jogo principal
mostrar_menu()

