import pygame
import math

# Alunos: Luca Zoio, Lucas de Jesus
# ======================================================
#   SIMULAÇÃO DA LEI DE MALUS EM PYTHON COM PYGAME
# ======================================================

def validar_angulo(valor_str):
    try:
        valor = float(valor_str)
        if 0 <= valor <= 360:
             return valor, None
        else:
            return 0, "Ângulo fora do intervalo válido (0-360)."
    except ValueError:
            return 0, "Entrada inválida."

def tela_de_jogo(tela):
    
    intensidade_inicial = 0.0
    angulo = 0.0
    angulo2 = 0.0
    luz_ja_polarizada = None # None pois não escolheu ainda
    
    # ===================================================
    #                    ELEMENTOS
    # ===================================================

    # BotAo sim/não
    btn_sim = pygame.Rect(50, 420, 80, 40)
    btn_nao = pygame.Rect(150, 420, 80, 40)
    
    cor_botao_inativo = (200, 200, 200)
    cor_botao_ativo = (100, 255, 100) # Verde
    
    # Caixas de Input
    caixa_input_angulo = pygame.Rect(490, 580, 140, 40)
    caixa_input_angulo_2 = pygame.Rect(955, 580, 140, 40)
    caixa_input_intensidade = pygame.Rect(60, 190, 140, 40)
    
    # Cores 
    cor_inativa = pygame.Color('lightskyblue3')
    cor_ativa = pygame.Color('dodgerblue2')
    cor_angulo = cor_inativa
    cor_angulo_2 = cor_inativa
    cor_intensidade = cor_inativa

    # Strings
    ativo = False
    angulo_escolhido = ''
    
    ativo_2 = False
    angulo_escolhido_2 = ''
    
    ativo_intensidade = False
    intensidade_escolhida = ''
    
    # Fontes
    fonte_input = pygame.font.Font(None, 32)
    fonte_input_intensidade = pygame.font.Font(None, 32)
    
    fonte = pygame.font.get_default_font()             
    fonte_texto = pygame.font.SysFont(fonte, 25)   

    # ===================================================
    #               LOOP DA TELA DO JOGO
    # ===================================================
    rodando = True
    while rodando:
        # Eventos do Jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            # Eventos de mouse
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Se clicar na caixa, ela ativa
                if caixa_input_angulo.collidepoint(evento.pos):
                    ativo = not ativo
                elif caixa_input_intensidade.collidepoint(evento.pos):
                    ativo_intensidade = not ativo_intensidade
                elif caixa_input_angulo_2.collidepoint(evento.pos):
                    ativo_2 = not ativo_2
                else:
                    ativo = False
                    ativo_intensidade = False
                    ativo_2 = False
                
                # Botões Sim/Não
                if btn_sim.collidepoint(evento.pos):
                    luz_ja_polarizada = True
                elif btn_nao.collidepoint(evento.pos):
                    luz_ja_polarizada = False
                    
                    
                cor_angulo = cor_ativa if ativo else cor_inativa
                cor_intensidade = cor_ativa if ativo_intensidade else cor_inativa
                cor_angulo_2 = cor_ativa if ativo_2 else cor_inativa
                
            # Evento de teclado
            elif evento.type == pygame.KEYDOWN:
                
                if evento.key == pygame.K_ESCAPE:
                    return "menu"
                
                # Reset
                if evento.key == pygame.K_r:
                    print("Reiniciando a simulação...")
                    intensidade_inicial = 0.0
                    angulo = 0.0
                    angulo2 = 0.0
                    luz_ja_polarizada = None
                    angulo_escolhido = ''
                    angulo_escolhido_2 = ''
                    intensidade_escolhida = ''
                    cor_angulo = cor_inativa
                    cor_intensidade = cor_inativa
                    cor_angulo_2 = cor_inativa
                    ativo = False
                    ativo_2 = False
                    ativo_intensidade = False
                    
                
                # Logica de input
                elif ativo_intensidade:
                    if evento.key == pygame.K_RETURN:
                        try:
                            val = float(intensidade_escolhida)
                            intensidade_inicial = val if val >= 0 else 0
                        except: intensidade_inicial = 0
                        intensidade_escolhida = ''
                    elif evento.key == pygame.K_BACKSPACE:
                        intensidade_escolhida = intensidade_escolhida[:-1]
                    else:
                        intensidade_escolhida += evento.unicode
                
                elif ativo:
                    if evento.key == pygame.K_RETURN:
                        val, _ = validar_angulo(angulo_escolhido)
                        angulo = val
                        angulo_escolhido = ''
                    elif evento.key == pygame.K_BACKSPACE:
                        angulo_escolhido = angulo_escolhido[:-1]
                    else:
                        angulo_escolhido += evento.unicode
                
                elif ativo_2:
                    if evento.key == pygame.K_RETURN:
                        val, _ = validar_angulo(angulo_escolhido_2)
                        angulo2 = val
                        angulo_escolhido_2 = ''
                    elif evento.key == pygame.K_BACKSPACE:
                        angulo_escolhido_2 = angulo_escolhido_2[:-1]
                    else:
                        angulo_escolhido_2 += evento.unicode

        # ===================================================
        #                 DESENHO NA TELA
        # ===================================================
        tela.fill((255, 255, 255))
        
        # CAIXAS DE INPUT
        # Angulo 1
        pygame.draw.rect(tela, (240, 240, 240), caixa_input_angulo)
        pygame.draw.rect(tela, cor_angulo, caixa_input_angulo, 2)
        tela.blit(fonte_input.render(angulo_escolhido, True, (0,0,0)), (caixa_input_angulo.x+5, caixa_input_angulo.y+5))
        
        # Angulo 2
        pygame.draw.rect(tela, (240, 240, 240), caixa_input_angulo_2)
        pygame.draw.rect(tela, cor_angulo_2, caixa_input_angulo_2, 2)
        tela.blit(fonte_input.render(angulo_escolhido_2, True, (0,0,0)), (caixa_input_angulo_2.x+5, caixa_input_angulo_2.y+5))
        
        # Intensidade
        pygame.draw.rect(tela, (240, 240, 240), caixa_input_intensidade)
        pygame.draw.rect(tela, cor_intensidade, caixa_input_intensidade, 2)
        tela.blit(fonte_input_intensidade.render(intensidade_escolhida, True, (0,0,0)), (caixa_input_intensidade.x+5, caixa_input_intensidade.y+5))

        # Feixe de luz
        pygame.draw.rect(tela, (255, 255, 0), pygame.Rect(100, 100, 1240, 30)) 
        
        # Polarizadores de lado
        pygame.draw.rect(tela, (128, 128, 128), pygame.Rect(550, 50, 40, 150))
        pygame.draw.rect(tela, (128, 128, 128), pygame.Rect(1008, 50, 40, 150))
        
        # Imagens
        try:
            fonte_luz_img = pygame.image.load('images/Fonte_de_Luz.png')
            tela.blit(pygame.transform.scale(fonte_luz_img, (120, 120)), (60, 50))
            
            pol_img = pygame.image.load('images/Polarizador.png')
            tela.blit(pygame.transform.scale(pol_img, (310, 310)), (412, 250)) 
            tela.blit(pygame.transform.scale(pol_img, (310, 310)), (872, 250)) 
            
            sensor_img = pygame.image.load('images/Sensor_de_Luz.png')
            tela.blit(pygame.transform.scale(sensor_img, (170, 170)), (1300, 50))
        except: pass 

        # TEXTOS
        tela.blit(fonte_texto.render('Insira a Intensidade Inicial (W/m²):', 1, (0,0,0)), (50, 270))
        tela.blit(fonte_texto.render('Insira o ângulo do polarizador (°):', 1, (0,0,0)), (430, 640))
        tela.blit(fonte_texto.render('Insira o ângulo do analisador (°):', 1, (0,0,0)), (898, 640))
        
        msg_reset = 'Pressione "R" para reiniciar valores  |  ESC para Voltar'
        tela.blit(fonte_texto.render(msg_reset, 1, (0, 0, 0)), (50, 780))

        # BOTÕES
        txt_pergunta = fonte_texto.render("A luz inicial já foi polarizada?", True, (0,0,0))
        tela.blit(txt_pergunta, (50, 380)) 
        
        cor_sim = cor_botao_ativo if luz_ja_polarizada == True else cor_botao_inativo
        pygame.draw.rect(tela, cor_sim, btn_sim)
        txt_sim = fonte_texto.render("Sim", True, (0,0,0))
        tela.blit(txt_sim, txt_sim.get_rect(center=btn_sim.center))
        
        cor_nao = cor_botao_ativo if luz_ja_polarizada == False else cor_botao_inativo
        pygame.draw.rect(tela, cor_nao, btn_nao)
        txt_nao = fonte_texto.render("Não", True, (0,0,0))
        tela.blit(txt_nao, txt_nao.get_rect(center=btn_nao.center))

        # CÁLCULO DA LEI DE MALUS
        if luz_ja_polarizada is not None:
            
            # Logica
            if luz_ja_polarizada:
                i_p1 = intensidade_inicial * (math.cos(math.radians(angulo)) ** 2)
            else:
                i_p1 = intensidade_inicial / 2
            
            txt_res1 = f'Intensidade após 1º: {i_p1:.2f} W/m²'
            tela.blit(fonte_texto.render(txt_res1, 1, (0,0,0)), (430, 670))

            # Calculo final
            delta_angulo = math.radians(angulo2 - angulo)
            i_final = i_p1 * (math.cos(delta_angulo) ** 2)
            
            txt_res2 = f'Intensidade Final: {i_final:.2f} W/m²'
            tela.blit(fonte_texto.render(txt_res2, 1, (0,0,0)), (1270, 240))

        pygame.display.flip()