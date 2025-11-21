import pygame
import math
pygame.init()

def tela_menu(tela):
    
    # Alunos: Luca Zoio, Lucas de Jesus
    # ======================================================
    #     SIMULAÇÃO DA LEI DE MALUS EM PYTHON COM PYGAME
    # ======================================================
    
    # ======================================================
    #               INICIALIZAR BOTOES DE MENU
    # ======================================================

    cor_botao_tutorial = (100, 100, 100) 
    cor_botao_jogar = (100, 100, 100) 
    cor_texto = (0, 0, 0) 

    rect_botao_tutorial = pygame.Rect(350, 340, 200, 100) 
    rect_botao_jogar = pygame.Rect(940, 340, 200, 100)
    texto_str_tutorial = "TUTORIAL"
    texto_str_jogar = "JOGAR"
    fonte_botao = pygame.font.Font(None, 36)
    superficie_texto_tutorial = fonte_botao.render(texto_str_tutorial, True, cor_texto)
    superficie_texto_jogar = fonte_botao.render(texto_str_jogar, True, cor_texto)
    
    
    rect_texto_tutorial = superficie_texto_tutorial.get_rect()
    rect_texto_jogar = superficie_texto_jogar.get_rect()

    rect_texto_tutorial.center = rect_botao_tutorial.center
    rect_texto_jogar.center = rect_botao_jogar.center
    
    
    pygame.display.flip() 

    # ======================================================
    #       LOOP INFINITO PARA SEMPRE ATUALIZAR A TELA 
    # ======================================================
    
    rodando = True
    while rodando:
        # Eventos de menu
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
        
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_botao_tutorial.collidepoint(evento.pos):
                    return "tutorial"
                elif rect_botao_jogar.collidepoint(evento.pos):
                    return "jogar"
                else:
                    pass

        # ======================================================
        #                  DESENHOS DA TELA
        # ======================================================
        tela.fill((255, 255, 255))
        retangulo_navegação = pygame.Rect(0, 0, 1540, 120)
        pygame.draw.rect(tela, (55, 150, 200), retangulo_navegação)
        
        # Botoes
        pygame.draw.rect(tela, cor_botao_tutorial, rect_botao_tutorial)
        pygame.draw.rect(tela, cor_botao_jogar, rect_botao_jogar)
        tela.blit(superficie_texto_tutorial, rect_texto_tutorial)
        tela.blit(superficie_texto_jogar, rect_texto_jogar)
        
        
        # ======================================================
        #                   TEXTOS NA TELA 
        # ======================================================
        
        # Textos
        texto_inicio='MENU INICIAL'
        texto_principal = 'SIMULAÇÃO DA LEI DE MALUS' 
        texto_str_alunos = "Alunos: Luca Zoio, Lucas de Jesus"                          
        fonte=pygame.font.get_default_font()              
        fonte_texto=pygame.font.SysFont(fonte, 60) 
        fonte_alunos=pygame.font.SysFont(fonte, 24)          
        texto_menu_tela = fonte_texto.render(texto_inicio, 3, (0,0,0)) 
        texto_menu_principal = fonte_texto.render(texto_principal, 3, (55,150,200))  
        tela.blit(texto_menu_tela,(620,200))
        tela.blit(texto_menu_principal,(450,250)) 
        tela.blit(fonte_alunos.render(texto_str_alunos, 1, (0,0,0)), (50, 760))                  
        
        
        pygame.display.flip()