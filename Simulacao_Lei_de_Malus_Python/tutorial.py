import pygame
import math
import time
pygame.init()

def tela_tutorial(tela):

    # ----------------------------------------------------
    # SIMULAÇÃO DA LEI DE MALUS EM PYTHON COM PYGAME
    # ----------------------------------------------------

    # ======================================================
    # INICIALIZAR TELA DE TUTORIAL


    # ======================================================
    # LOOP INFINITO PARA SEMPRE ATUALIZAR A TELA 
    # PERMITE O USUÁRIO FAZER O INPUT DO ANGULO

    # cria loop infinito
    rodando = True
    while rodando:
        # processameto de eventos
        for evento in pygame.event.get():
            # separa por tipos de eventos -> QUIT, KEYDOWN, MOUSEBUTTONDOWN, ETC.
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "menu"
                else:
                    pass
            
            if evento.type == pygame.QUIT:
                rodando = False
        
        
        
        tela.fill((255,255,255))
        retangulo_navegação = pygame.Rect(0, 0, 1540, 120)
        pygame.draw.rect(tela, (55, 150, 200), retangulo_navegação)
        
        # ======================================================
        #                   TEXTOS NA TELA 
        # ======================================================
        
        
        # texto inicial 
        texto_inicio='TUTORIAL'                            
        fonte=pygame.font.get_default_font()              
        fonte_texto=pygame.font.SysFont(fonte, 60)           
        texto_inicio = fonte_texto.render(texto_inicio, 1, (55, 150, 200))  
        tela.blit(texto_inicio,(620, 200)) 
        
        texto_passo_1 = '1. No menu inicial, clique em "Jogar" para iniciar a simulação.'
        texto_passo_2 = '2. Insira a intensidade inicial do feixe de luz incidente na primeira caixa de texto.'
        texto_passo_3 = '3. Ao passar no primeiro polarizador, a intensidade será reduzida pela metade.'
        texto_passo_4 = '4. Insira o ângulo do analisador (segundo polarizador) na segunda caixa de texto.'
        texto_passo_5 = '5. A intensidade final será calculada usando a Lei de Malus e exibida na tela.'
        texto_passo_6 = '6. Pressione BACKSPACE para limpar os resultados e iniciar uma nova simulação.'
        
        texto_final = 'Pressione ESC para voltar ao menu principal.'
        
        fonte_texto_pequeno=pygame.font.SysFont(fonte, 30)
        texto_passo_1 = fonte_texto_pequeno .render(texto_passo_1, 1, (0,0,0))
        texto_passo_2 = fonte_texto_pequeno .render(texto_passo_2, 1, (0,0,0))
        texto_passo_3 = fonte_texto_pequeno .render(texto_passo_3, 1, (0,0,0))
        texto_passo_4 = fonte_texto_pequeno .render(texto_passo_4, 1, (0,0,0))
        texto_passo_5 = fonte_texto_pequeno .render(texto_passo_5, 1, (0,0,0))
        texto_passo_6 = fonte_texto_pequeno .render(texto_passo_6, 1, (0,0,0))
        texto_final = fonte_texto_pequeno.render(texto_final, 1, (0,0,0))
        
        tela.blit(texto_passo_1,(50, 300))
        tela.blit(texto_passo_2,(50, 350))
        tela.blit(texto_passo_3,(50, 400))
        tela.blit(texto_passo_4,(50, 450))
        tela.blit(texto_passo_5,(50, 500))
        tela.blit(texto_passo_6,(50, 550))
        tela.blit(texto_final,(50, 700))            

        
        pygame.display.flip()
            
        

    # atualizar tudo na tela após os desenhos e funções