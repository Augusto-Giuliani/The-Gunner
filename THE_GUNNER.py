# Importando as bibliotecas necessárias.
import pygame as py
from values import GAME,INTRO,QUIT,INCEPTION,WIDTH,HEIGHT,GAMEOVER,VICTORY,TRYAGAIN
from screens import intro_screen,inception_screen,gameover_screen,tryagain_screen,victory_screen
from game import game_screen

# Inicializações.
py.init()
py.mixer.init()

# Gerando a tela principal (com dimensões e título).
window = py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption('The Gunner')



# Gerando o loop que verifica qual o estado atual do jogo. Para cada estado será chamado uma função distinta.
state = INTRO # --> começa com a introdução
while state != QUIT:
    if state == INTRO: 
        state = intro_screen(window)
    elif state == INCEPTION:
        state = inception_screen(window)
    elif state == GAME:
        state = game_screen(window)
    elif state == TRYAGAIN:
        state = tryagain_screen(window)
    elif state == GAMEOVER:
        state = gameover_screen(window) 
    elif state == VICTORY:
        state = victory_screen(window)
    else:
        state = QUIT

# Finalização dos recursos utilizados.
py.quit()
