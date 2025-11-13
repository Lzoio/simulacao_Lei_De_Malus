import pygame
import math
import time
pygame.init()


def tela_de_jogo(tela):
    # ----------------------------------------------------
    # SIMULAÇÃO DA LEI DE MALUS EM PYTHON COM PYGAME
    # ----------------------------------------------------
    
    # ======================================================
    # CONFIGURAÇÃO DOS RETANGULOS DE OPACIDADE
    # TODO
    '''posicao_x_retan_opacidade = 470
    posicao_y_retan_opacidade = 150
    
    posicao_x_retan_opacidade_2 = 970
    posicao_y_retan_opacidade_2 = 150
    
    largura_retan_opacidade = 430
    altura_retan_opacidade = 30
    
    largura_retan_opacidade_2 = 500
    altura_retan_opacidade_2 = 30
    
    superficie_retan_opacidade = pygame.Surface((largura_retan_opacidade, altura_retan_opacidade), pygame.SRCALPHA)
    superficie_retan_opacidade_2 = pygame.Surface((largura_retan_opacidade_2, altura_retan_opacidade_2), pygame.SRCALPHA)
    opacidade_polarizador_1 = 128
    cor_retan_opacidade = (255, 255, 0, opacidade_polarizador_1)'''

    
    
    # ======================================================
    # CONFIGURAÇÕES INICIAIS DAS CAIXAS DE INPUT

    # detalhes da cor da caixa
    caixa_input = pygame.Rect(915, 650, 140, 40)
    cor_inativa = pygame.Color('lightskyblue3')
    cor_ativa = pygame.Color('dodgerblue2')
    cor = cor_inativa
    pygame.draw.rect(tela, cor, caixa_input, 2)
    
    caixa_input_intensidade = pygame.Rect(60, 190, 140, 40)
    cor_intensidade = cor_inativa
    pygame.draw.rect(tela, cor_intensidade, caixa_input_intensidade, 2)

    # inicializa variável de ativo e as de texto
    ativo = False
    angulo_escolhido = ''
    fonte_input = pygame.font.Font(None, 32)
    
    ativo_intensidade = False
    intensidade_escolhida = ''
    fonte_input_intensidade = pygame.font.Font(None, 32)
    


    # ======================================================
    # LOOP INFINITO PARA SEMPRE ATUALIZAR A TELA 
    # PERMITE O USUÁRIO FAZER O INPUT DO ANGULO

    # cria loop infinito
    rodando = True
    while rodando:
        # processameto de eventos
        for evento in pygame.event.get():
            # separa por tipos de eventos -> QUIT, KEYDOWN, MOUSEBUTTONDOWN, ETC.
            if evento.type == pygame.QUIT:
                rodando = False
                
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if caixa_input.collidepoint(evento.pos):
                    ativo = not ativo
                elif caixa_input_intensidade.collidepoint(evento.pos):
                    ativo_intensidade = not ativo_intensidade
                else:
                    ativo = False
                cor = cor_ativa if ativo else cor_inativa
                cor_intensidade = cor_ativa if ativo_intensidade else cor_inativa
                
            elif evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_ESCAPE:
                    return "menu"
                
                if ativo:
                    if ativo_intensidade == False:
                        if evento.key == pygame.K_RETURN:
                            
                            print(f"Ângulo inserido: {angulo_escolhido}")
                            if angulo_escolhido.isdigit():
                                angulo = int(angulo_escolhido) 
                                print(f"Valor do ângulo definido para: {angulo}")
                            elif angulo_escolhido.replace('.','',1).isdigit():
                                angulo = float(angulo_escolhido)
                                print(f"Valor do ângulo definido para: {angulo}")
                            elif float(angulo_escolhido) < 0 or float(angulo_escolhido) > 360:
                                angulo = 0
                                print("Ângulo fora do intervalo válido (0-360). Ângulo definido para 0.")
                            else:
                                angulo = 0 # valor padrão do angulo se não for int
                                print("Entrada inválida. Ângulo definido para 0.")
                            
                            angulo_escolhido = ''

                        elif evento.key == pygame.K_BACKSPACE:
                            angulo_escolhido = angulo_escolhido[:-1]
                        else:
                            angulo_escolhido += evento.unicode
                
                if ativo_intensidade:
                    if ativo == False:
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
                    
                if evento.key == pygame.K_BACKSPACE:
                    intensidade_escolhida = ''
                    angulo_escolhido = ''
                    if 'intensidade_inicial' in locals():
                        del intensidade_inicial
                    if 'angulo' in locals():
                        del angulo
                else:
                    pass
                
                        
        # ======================================================
        
        # refresh da tela para interacao com a caixa de texto
        tela.fill((255, 255, 255))
        
        # caixa de input de ângulo
        pygame.draw.rect(tela, (200, 200, 200), caixa_input)
        pygame.draw.rect(tela, cor, caixa_input, 2)

        # renderizar o texto e desenhar na tela
        superficie_txt = fonte_input.render(angulo_escolhido, True, (0, 0, 0))
        tela.blit(superficie_txt, (caixa_input.x+5, caixa_input.y+5))
        
        # caixa de input de intensidade inicial
        pygame.draw.rect(tela, (200, 200, 200), caixa_input_intensidade)
        pygame.draw.rect(tela, cor_intensidade, caixa_input_intensidade, 2)
        
        # renderizar o texto e desenhar na tela
        superficie_txt_intensidade = fonte_input_intensidade.render(intensidade_escolhida, True, (0, 0, 0))
        tela.blit(superficie_txt_intensidade, (caixa_input_intensidade.x+5, caixa_input_intensidade.y+5))
        
        # =======================================================
        # OPACIDADE DO FEIXE DE LUZ DE ACORDO COM O ANGULO
        # TODO
        '''
        if intensidade_escolhida != '':
            intensidade_inicial = float(intensidade_escolhida)
            opacidade_polarizador_1 = int(255 * (intensidade_inicial / 2) / intensidade_inicial)
            superficie_retan_opacidade.set_alpha(opacidade_polarizador_1)
            tela.blit(superficie_retan_opacidade, (posicao_x_retan_opacidade, posicao_y_retan_opacidade))
        else:
            opacidade_polarizador_1 = 0
        
        if angulo_escolhido != '':
            angulo = float(angulo_escolhido)
            intensidade_transmitida = (math.cos(math.radians(angulo)))**2
            opacidade_polarizador_2 = int(255 * intensidade_transmitida)
            superficie_retan_opacidade_2.set_alpha(opacidade_polarizador_2)
        else:
            opacidade_polarizador_2 = 0
        '''

        
        # ======================================================================
        #                   DESENHOS DA TELA DENTRO DO LOOP
        # ======================================================================
        # feixe de luz
        cor_feixe_antes = (255, 255, 0)
        feixe_de_luz = pygame.draw.rect(tela, cor_feixe_antes, pygame.Rect(100, 100, 1240, 30))
        
        # feixe de luz depois do primeiro polarizador
        

        # polarizadores (de lado)
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
        

        # polarizador #primeiro polarizador por onde a luz passa 
        # divide intensidade na metadeSet
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
                
        texto_voltar = 'Pressione ESC para voltar ao menu principal.'
        texto_voltar_tela = fonte_texto.render(texto_voltar, 1, (0,0,0))
        tela.blit(texto_voltar_tela,(50,270))
        
        
        texto_angulo = 'Insira o ângulo do analisador (°):'
        texto_angulo_tela = fonte_texto.render(texto_angulo, 1, (0,0,0))
        tela.blit(texto_angulo_tela,(850,710))
        
        texto_final = 'Aperte ESC para voltar ao menu principal.'
        texto_final_tela = fonte_texto.render(texto_final, 1, (0,0,0))
        tela.blit(texto_final_tela,(50, 750))
        
        
        # =======================================================
        # LÓGICA DA LEI DE MALUS
        
        if 'intensidade_inicial' in locals(): 
            intensidade_apos_primeiro_polarizador = intensidade_inicial / 2 
            texto_primeiro_polarizador = f'Intensidade no primeiro polarizador: W/m² {intensidade_apos_primeiro_polarizador:.2f}'
            texto_primeiro_polarizador_tela = fonte_texto.render(texto_primeiro_polarizador, 1, (0,0,0))
            tela.blit(texto_primeiro_polarizador_tela,(320, 610))
            pygame.display.flip()
        else: 0
        
        if 'angulo' in locals() and 'intensidade_inicial' in locals():
            intensidade_final = intensidade_apos_primeiro_polarizador * (math.cos(math.radians(angulo)))**2 
            texto_final = f'Intensidade final (W/m²): {intensidade_final:.2f}'
            texto_final_tela = fonte_texto.render(texto_final, 1, (0,0,0))
            tela.blit(texto_final_tela,(1270,240)) 
            pygame.display.flip()
        else: 0
        
        
        pygame.display.flip()
        

