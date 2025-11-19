# main.py

import pygame
import menu      
import lei_de_malus
import tutorial



pygame.init()
largura_tela =  1540
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela), pygame.RESIZABLE) 
pygame.display.set_caption("Simulação - Simulação Lei de Malus") 
cor_tela = (255, 255, 255)
tela.fill(cor_tela)


estado_do_jogo = "menu"


while True:
    
    if estado_do_jogo == "menu":
        estado_do_jogo = menu.tela_menu(tela)
        
    elif estado_do_jogo == "jogar":
        estado_do_jogo = lei_de_malus.tela_de_jogo(tela)
    
    elif estado_do_jogo == "tutorial":
        estado_do_jogo = tutorial.tela_tutorial(tela)
        
    else:
        break

pygame.quit()
print("Simulação encerrada.")