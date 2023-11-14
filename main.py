import pygame;
import random;
import sys;
import sqlite3;

pygame.init();
pygame.font.init();
pygame.display.set_caption("Snake Game");

largura, altura = 800, 600;

tela = pygame.display.set_mode((largura, altura));

relogio = pygame.time.Clock();
fonte = pygame.font.SysFont("Calibri", 25);

pontuacao = 0

#cores RGB
fundo = (0, 153, 51);
branco = (255, 255, 255);
preto = (0, 0 , 0);
azul = (20, 20, 255);
vermelho = (255, 20, 20);


#variaveis da cobrinha
tamanho_quadrado = 10;
velocidade_jogo = 15;

def conexao_db():
    db = sqlite3.connect('snake_game.db')

    return db


def get_list_usuarios():
    sql = " select nome_usua, pont_usua, data_jogd from usuario order by pont_usua desc "

    con = conexao_db()

    cursor = con.cursor()

    cursor.execute(sql)

    resultado = cursor.fetchall()

    con.close()

    return resultado


def cadastra_usua(nome_usua, pont_usua):
    con = conexao_db()

    sql = '''
        insert into usuario (
            nome_usua, 
            pont_usua, 
            data_jogd
        ) values (
            ?, 
            ?, 
            date('now')
        )'''

    cursor = con.cursor()

    cursor.execute(sql, (nome_usua, pont_usua))

    con.commit()

    con.close()


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
        
        relogio.tick(velocidade_jogo) # Limita a taxa de atualização da tela para 60 frames por segundo

    pontuacao = tamanho_cobra - 1

    return [nome, pontuacao]

# menu

def mostrar_menu(pontuacao='0'):
    nome_jogador = ""

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
                    dados = rodar_jogo(nome_jogador)
                    cadastra_usua(dados[0], dados[1])
                    mostra_lista()

                elif event.key == pygame.K_BACKSPACE:
                    # Remove o último caractere quando o jogador pressiona Backspace
                    nome_jogador = nome_jogador[:-1]

                else:
                    # Adiciona caracteres à entrada do jogador
                    nome_jogador += event.unicode


        tela.fill(preto)  # Preenche a tela com fundo preto
        texto = fonte.render("Digite seu nome: " + nome_jogador, True, branco)
        tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 0.5))


        texto1 = fonte.render(f"Ultima pontuação {pontuacao}", True, branco)
        texto = fonte.render("Pressione ENTER para iniciar o jogo.", True, branco)
        tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 2))
        tela.blit(texto1, (largura // 2 - texto1.get_width() // 2, altura // 2 + texto.get_height()))

        pygame.display.flip()  # Atualiza a tela


def mostra_lista():
    em_pagina = True;

    lista_usuarios = get_list_usuarios();

    tela.fill(preto)

    while em_pagina:
        # Renderiza a lista
        for i, item in enumerate(lista_usuarios):
            texto = fonte.render(f"{i + 1}. Nome: {item[0]} | Pontuação: {item[1]} | Data da tentativa: {item[2]}", 1, branco)

            tela.blit(texto, (30, 50 + i * 40))

        texto_fim = fonte.render("Pressione 1 para jogar novamente | Pressione 2 para sair", 1, branco)

        tela.blit(texto_fim, (1, 1))

        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                em_pagina = False

            if e.type == pygame.KEYDOWN:
                if e.key == 49:
                    em_pagina = False;
                    mostrar_menu();
                    sys.exit()

                if e.key == 50:
                    em_pagina = False;
                    sys.exit()


def inicia_game():
    em_game = True;

    while em_game:

        tela.fill(preto);
        texto = fonte.render("Tecle 1 para Jogar | Tecle 2 para ver as pontuações.", True, branco);
        tela.blit(texto, (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 0.5));
        pygame.display.flip();

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                em_game = False
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == 49:
                    mostrar_menu()
                    em_game = False
                    sys.exit()


                elif e.key == 50:
                    mostra_lista()
                    em_game = False
                    sys.exit()

                else:
                    texto_validacao = fonte.render('Pressione uma tecla válida.', True, branco)
                    tela.blit(texto_validacao, (1, 1))
                    pygame.display.flip()
    pygame.quit()
    sys.exit()


inicia_game()
