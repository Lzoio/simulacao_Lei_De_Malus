import pygame
import math
import time
pygame.init()
# Zoio, Novembro de 2025

def validar_angulo(valor_str):
    try:
        valor = float(valor_str)
        if 0 <= valor <= 360:
             return valor, None
        else:
            return 0, "Ângulo fora do intervalo válido (0-360). Ângulo definido para 0."
    except ValueError:
            return 0, "Entrada inválida. Ângulo definido para 0."

def tela_de_jogo(tela):
    # ----------------------------------------------------
    # SIMULAÇÃO DA LEI DE MALUS EM PYTHON COM PYGAME
    # ----------------------------------------------------
    
    # ======================================================
    # CONFIGURAÇÕES INICIAIS DAS CAIXAS DE INPUT
    # ======================================================

    # detalhes da cor da caixa
    caixa_input_angulo = pygame.Rect(450, 650, 140, 40)
    cor_inativa = pygame.Color('lightskyblue3')
    cor_ativa = pygame.Color('dodgerblue2')
    cor_angulo = cor_inativa
    pygame.draw.rect(tela, cor_angulo, caixa_input_angulo, 2)
    
    caixa_input_angulo_2 = pygame.Rect(915, 650, 140, 40)
    cor_angulo_2 = cor_inativa
    pygame.draw.rect(tela, cor_angulo_2, caixa_input_angulo_2, 2)
    
    caixa_input_intensidade = pygame.Rect(60, 190, 140, 40)
    cor_intensidade = cor_inativa
    pygame.draw.rect(tela, cor_intensidade, caixa_input_intensidade, 2)

    # inicializa variável de ativo e as de texto
    ativo = False
    angulo_escolhido = ''
    fonte_input = pygame.font.Font(None, 32)
    
    ativo_2 = False
    angulo_escolhido_2 = ''
    fonte_input = pygame.font.Font(None, 32)
    
    ativo_intensidade = False
    intensidade_escolhida = ''
    fonte_input_intensidade = pygame.font.Font(None, 32)
    
    
    


    # ======================================================
    # LOOP INFINITO PARA SEMPRE ATUALIZAR A TELA 
    # PERMITE O USUÁRIO FAZER O INPUT DO ANGULO
    # LÓGICA DE INTERAÇÃO COM A INTERFACE DO JOGO
    # ======================================================

    # cria loop infinito
    rodando = True
    while rodando:
        # processameto de eventos
        for evento in pygame.event.get():
            # separa por tipos de eventos -> QUIT, KEYDOWN, MOUSEBUTTONDOWN, ETC.
            if evento.type == pygame.QUIT:
                rodando = False
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if caixa_input_angulo.collidepoint(evento.pos):
                    ativo = not ativo
                elif caixa_input_intensidade.collidepoint(evento.pos):
                    ativo_intensidade = not ativo_intensidade
                elif caixa_input_angulo_2.collidepoint(evento.pos):
                    ativo_2 = not ativo_2
                    
                cor_angulo = cor_ativa if ativo else cor_inativa
                cor_intensidade = cor_ativa if ativo_intensidade else cor_inativa
                cor_angulo_2 = cor_ativa if ativo_2 else cor_inativa
                
                
            elif evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_ESCAPE:
                    return "menu"
                
                if ativo:
                    if ativo_intensidade == False and ativo_2 == False:
                        if evento.key == pygame.K_RETURN:
                            
                            print(f"Ângulo inserido: {angulo_escolhido}")
                            if angulo_escolhido.isdigit():
                                angulo = int(angulo_escolhido) 
                                print(f"Valor do ângulo definido para: {angulo}")
                            elif angulo_escolhido.replace('.','',1).isdigit():
                                angulo = float(angulo_escolhido)
                                print(f"Valor do ângulo definido para: {angulo}")
                            elif validar_angulo(angulo_escolhido) == False:
                                angulo = 0
                            
                            angulo_escolhido = ''

                        elif evento.key == pygame.K_BACKSPACE:
                            angulo_escolhido = angulo_escolhido_2[:-1]
                        else:
                            angulo_escolhido += evento.unicode
                
                if ativo_intensidade:
                    if ativo_2 == False and ativo == False:
                        if evento.key == pygame.K_RETURN:
                            
                            print(f"Intensidade inserida: {intensidade_escolhida}")
                            if intensidade_escolhida.isdigit():
                                intensidade_inicial = float(intensidade_escolhida) 
                                print(f"Valor da intensidade inicial definido para: {intensidade_inicial} W/m²")
                            elif intensidade_escolhida.replace('.','',1).isdigit():
                                intensidade_inicial = float(intensidade_escolhida)
                                print(f"Valor da intensidade inicial definido para: {intensidade_inicial} W/m²")
                            elif float(intensidade_escolhida) <  0:
                                intensidade_inicial = 0
                                print("Intensidade não pode ser negativa. Definida para 0 W/m².")
                            else:
                                intensidade_inicial = 0 # valor padrão se não for int
                                print("Entrada inválida. Intensidade inicial definida para 0 W/m².")
                            
                            intensidade_escolhida = ''

                        elif evento.key == pygame.K_BACKSPACE:
                            intensidade_escolhida = intensidade_escolhida[:-1]
                        else:
                            intensidade_escolhida += evento.unicode
                    else :
                        pass
                
                if ativo_2:
                    if ativo == False and ativo_intensidade == False:
                        if evento.key == pygame.K_RETURN:
                            
                            print(f"Ângulo inserido: {angulo_escolhido_2}")
                            if angulo_escolhido_2.isdigit():
                                angulo2 = int(angulo_escolhido_2) 
                                print(f"Valor do ângulo definido para: {angulo2}")
                            elif angulo_escolhido_2.replace('.','',1).isdigit():
                                angulo2 = float(angulo_escolhido_2)
                                print(f"Valor do ângulo definido para: {angulo2}")
                            elif validar_angulo(angulo_escolhido_2) == False:
                                angulo2 = 0
                            
                            angulo_escolhido_2 = ''

                        elif evento.key == pygame.K_BACKSPACE:
                            angulo_escolhido_2 = angulo_escolhido_2[:-1]
                        else:
                            angulo_escolhido_2 += evento.unicode
                else:
                    pass
                        
                    
                if evento.key == pygame.K_BACKSPACE:
                    intensidade_escolhida = ''
                    angulo_escolhido = ''
                    angulo_escolhido_2 = ''
                    if 'intensidade_inicial' in locals():
                        del intensidade_inicial
                    if 'angulo' in locals():
                        del angulo
                    if 'angulo2' in locals():
                        del angulo2
                else:
                    pass
                
                        
        # ======================================================
        # CAIXAS DE INPUT
        # ======================================================
        
        # refresh da tela para interacao com a caixa de texto
        tela.fill((255, 255, 255))
        
        # caixa de input de ângulo
        pygame.draw.rect(tela, (200, 200, 200), caixa_input_angulo)
        pygame.draw.rect(tela, cor_angulo, caixa_input_angulo, 2)

        # renderizar o texto e desenhar na tela
        superficie_txt_angulo = fonte_input.render(angulo_escolhido, True, (0, 0, 0))
        tela.blit(superficie_txt_angulo, (caixa_input_angulo.x+5, caixa_input_angulo.y+5))
        
        #caixa de input angulo 2
        pygame.draw.rect(tela, (200, 200, 200), caixa_input_angulo_2)
        pygame.draw.rect(tela, cor_angulo_2, caixa_input_angulo_2, 2)

        # renderizar o texto e desenhar na tela
        superficie_txt_angulo_2 = fonte_input.render(angulo_escolhido_2, True, (0, 0, 0))
        tela.blit(superficie_txt_angulo_2, (caixa_input_angulo_2.x+5, caixa_input_angulo_2.y+5))
        
        # caixa de input de intensidade inicial
        pygame.draw.rect(tela, (200, 200, 200), caixa_input_intensidade)
        pygame.draw.rect(tela, cor_intensidade, caixa_input_intensidade, 2)
        
        # renderizar o texto e desenhar na tela
        superficie_txt_intensidade = fonte_input_intensidade.render(intensidade_escolhida, True, (0, 0, 0))
        tela.blit(superficie_txt_intensidade, (caixa_input_intensidade.x+5, caixa_input_intensidade.y+5))

        
        # ======================================================================
        #                   DESENHOS DA TELA DENTRO DO LOOP
        # ======================================================================
        # feixe de luz
        cor_feixe_antes = (255, 255, 0)
        feixe_de_luz = pygame.draw.rect(tela, cor_feixe_antes, pygame.Rect(100, 100, 1240, 30))

        # polarizador de lado
        cor_polarizador = (128, 128, 128)
        polarizador_de_lado = pygame.draw.rect(tela, cor_polarizador, pygame.Rect(510, 50, 40, 150))
        

        # analisador de lado
        cor_analisador = (128, 128, 128)
        analisador_de_lado = pygame.draw.rect(tela, cor_analisador, pygame.Rect(968, 50, 40, 150))
        

        # fonte de luz 
        fonte_de_luz = pygame.image.load('images/Fonte_de_Luz.png')
        fonte_de_luz = pygame.transform.scale(fonte_de_luz, (120, 120))
        tela.blit(fonte_de_luz, (60, 50))
        

        # polarizador 
        #primeiro polarizador por onde a luz passa, divide intensidade na metade
        polarizador = pygame.image.load('images/Polarizador.png')
        polarizador = pygame.transform.scale(polarizador, (310, 310))
        tela.blit(polarizador, (372, 290))
        

        # analisador #segundo polarizador, muda intensidade com angulo
        analisador = pygame.image.load('images/Polarizador.png')
        analisador = pygame.transform.scale(analisador, (310, 310))
        tela.blit(analisador, (832, 290))
        

        # sensor_de_luz
        sensor_de_luz = pygame.image.load('images/Sensor_de_Luz.png')
        sensor_de_luz = pygame.transform.scale(sensor_de_luz, (170, 170))
        tela.blit(sensor_de_luz, (1300, 50))
        
        
        # ======================================================
        #                   TEXTOS NA TELA 
        # ======================================================
                                 
        fonte=pygame.font.get_default_font()              
        fonte_texto=pygame.font.SysFont(fonte, 25)                            
                
        texto_intensidade = 'Insira a Intensidade Inicial (W/m²):'
        texto_intensidade_tela = fonte_texto.render(texto_intensidade, 1, (0,0,0))
        tela.blit(texto_intensidade_tela,(50,270))
        
        texto_angulo = 'Insira o ângulo do polarizador (°):'
        texto_angulo_tela = fonte_texto.render(texto_angulo, 1, (0,0,0))
        tela.blit(texto_angulo_tela,(390,710))
        
        
        texto_angulo = 'Insira o ângulo do analisador (°):'
        texto_angulo_tela = fonte_texto.render(texto_angulo, 1, (0,0,0))
        tela.blit(texto_angulo_tela,(850,710))
        
        texto_final = 'Aperte ESC para voltar ao menu principal.'
        texto_final_tela = fonte_texto.render(texto_final, 1, (0,0,0))
        tela.blit(texto_final_tela,(50, 750))
        
        
        # =======================================================
        # LÓGICA DA LEI DE MALUS
        # =======================================================
        
        if 'intensidade_inicial' in locals() and 'angulo' in locals():
            if angulo != 0:
                intensidade_apos_primeiro_polarizador = intensidade_inicial * (math.cos(math.radians(angulo)))**2
                texto_primeiro_polarizador = f'Intensidade após primeiro polarizador: W/m² {intensidade_apos_primeiro_polarizador:.2f}'
                texto_primeiro_polarizador_tela = fonte_texto.render(texto_primeiro_polarizador, 1, (0,0,0))
                tela.blit(texto_primeiro_polarizador_tela,(320, 620))
                print(f"Intensidade após primeiro polarizador: {intensidade_apos_primeiro_polarizador:.2f} W/m²")
            else:
                intensidade_apos_primeiro_polarizador = intensidade_inicial / 2
                texto_primeiro_polarizador = f'Intensidade após primeiro polarizador: W/m² {intensidade_apos_primeiro_polarizador:.2f}'
                texto_primeiro_polarizador_tela = fonte_texto.render(texto_primeiro_polarizador, 1, (0,0,0))
                tela.blit(texto_primeiro_polarizador_tela,(320, 620))
                print(f"Intensidade após primeiro polarizador: {intensidade_apos_primeiro_polarizador:.2f} W/m²")
        else: 0

        
        if 'angulo2' in locals():
            intensidade_final = intensidade_apos_primeiro_polarizador * (math.cos(math.radians(angulo2)))**2 
            texto_final = f'Intensidade final (W/m²): {intensidade_final:.2f}'
            texto_final_tela = fonte_texto.render(texto_final, 1, (0,0,0))
            tela.blit(texto_final_tela,(1270,240)) 
            print(f"Intensidade final após o analisador: {intensidade_final:.2f} W/m²")
        else: 0
        
        pygame.display.flip()