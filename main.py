import pygame;
import random;
import sys;


pygame.init();
pygame.display.set_caption("Snake Game");

largura, altura = 600, 400;

tela = pygame.display.set_mode((largura, altura));

relogio = pygame.time.Clock();

#cores RGB
fundo = (0, 153, 51);
branco = (255, 255, 255);
azul = (20, 20, 255);
vermelho = (255, 20, 20);


#variaveis da cobrinha
tamanho_quadrado = 10;
velocidade_jogo = 15;

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, azul, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(pontuacao, nome):
    fonte = pygame.font.SysFont("Helvetica", 25);
    texto = fonte.render(f"{nome}, pontos: {pontuacao}", True, branco);
    tela.blit(texto, [1, 1]);
    
def selecionar_velocidade(tecla):
    velocidade_x = 0;
    velocidade_y = 0;
   
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado 
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    
        
    return velocidade_x, velocidade_y

def rodar_jogo(nome):
    fim_jogo = False
    
    x = largura/2;
    y = altura/2;
    
    velocidade_x = 0;
    velocidade_y = 0;
    
    tamanho_cobra = 1;
    pixels = [];
    
    comida_x, comida_y = gerar_comida();
    
    
    while not fim_jogo:
        tela.fill(fundo);
            
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True;
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key);
        
        #desenha comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y);
        
        #atualizar a cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            mostrar_menu(tamanho_cobra - 1);
            fim_jogo = True;
        
        x += velocidade_x;
        y += velocidade_y;
        
        #desenhar cobra
        pixels.append([x, y]);
        if len(pixels) > tamanho_cobra:
            del pixels[0]
            
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True;
                
        desenhar_cobra(tamanho_quadrado, pixels);
        #desenha pontos
        desenhar_pontuacao(tamanho_cobra - 1, nome);
        
        
        #atualização da tela
        pygame.display.update();
        
        #Criar uma nova Comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1;
            comida_x, comida_y = gerar_comida();
        
        relogio.tick(velocidade_jogo);
        
        
#menu

def mostrar_menu(pontuacao='0'):
    nome_jogador = ""
    fonte = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    enquanto_no_menu = True
    while enquanto_no_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Inicia o jogo quando o jogador pressiona Enter (retorno)
                    enquanto_no_menu = False
                    rodar_jogo(nome_jogador)
                elif event.key == pygame.K_BACKSPACE:
                    # Remove o último caractere quando o jogador pressiona Backspace
                    nome_jogador = nome_jogador[:-1]
                else:
                    # Adiciona caracteres à entrada do jogador
                    nome_jogador += event.unicode

        tela.fill((0, 0, 0))  # Preenche a tela com fundo preto
        texto = fonte.render("Digite seu nome: " + nome_jogador, True, (255, 255, 255))
        tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 0.5))

        texto1 = fonte.render(f"Ultima pontuação {pontuacao}", True, (255, 255, 255))
        texto = fonte.render("Pressione ESPAÇO para iniciar", True, (255, 255, 255))  # Texto branco
        tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 2))
        tela.blit(texto1, (largura // 2 - texto1.get_width() // 2, altura // 2 + texto.get_height()))
        
        pygame.display.flip()  # Atualiza a tela
        clock.tick(30)  # Limita a taxa de atualização da tela para 30 frames por segundo

    return nome_jogador



