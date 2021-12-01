# Importando as bibliotecas necessárias.
import pygame as py
import os
from values import GROUND_HEIGHT, HEIGHT, HOWITZER_HEIGHT, HOWITZER_WIDTH, IMG, MISSION_HEIGHT,MISSION_WIDTH, SERGEANT_HEIGHT, SERGEANT_WIDTH, SHELL_HEIGHT, SHELL_WIDTH,SOUND, TANK_HEIGHT, TANK_INFO_HEIGHT, TANK_INFO_WIDTH, TANK_WIDTH, WIDTH,PLANE_HEIGHT,PLANE_WIDTH,PLANE_INFO_HEIGHT,PLANE_INFO_WIDTH,ROCKET_HEIGHT,ROCKET_WIDTH,SHELL_INFO_HEIGHT,SHELL_INFO_WIDTH,RULER_HEIGHT,RULER_WIDTH,MINE_HEIGHT,MINE_WIDTH,SUBMARINE_HEIGHT,SUBMARINE_WIDTH,MISSILE_HEIGHT,MISSILE_WIDTH,SUBMARINE_INFO_HEIGHT,SUBMARINE_INFO_WIDTH
# Criando variáveis para cada asset.
intro = 'intro_screen'
inception = 'inception_screen'
background = 'background'
gameover = 'gameover_screen'
tryagain = 'tryagain_screen'
victory = 'victory_screen'
tank1 = 'tank1'
tank2 = 'tank2'
tank3 = 'tank3'
ground = 'ground'
howitzer = 'howitzer'
sergeant = 'sergeant'
shell = 'shell'
shell_info = 'shell_info'
shooting = 'shooting'
shout = 'shout'
explosion_miss = 'explosion_miss'
explosion_hit = 'explosion_hit'
explosion_animation = 'explosion_animation'
explosion_animation2 = 'explosion_animation2'
smoke_animation = 'smoke_animation'
mission = 'mission'
tank_info = 'tank_info'
plane_info = 'plane_info'
plane = 'plane'
rocket = 'rocket'
rocket_sound = 'rocket_sound'
plane_sound = 'plane_sound'
call = 'call'
call2 = 'call2'
pause = 'pause_screen'
ruler = 'ruler'
support = 'support'
mine = 'mine'
submarine = 'submarine'
submarine_sound = 'submarine_sound'
submarine_info = 'submarine_info'
missile_up = 'missile_up'
missile_down = 'missile_down'
missile_sound = 'missile_sound'
ocean_background = 'ocean_background'

# Criando a função que carrega os arquivos de cada asset em um dicionário.
def load_assets():
    assets = dict()
    # IMAGENS.
    # Telas.
    assets[intro] = py.image.load(os.path.join(IMG,'intro.png')).convert()
    assets[intro] = py.transform.scale(assets['intro_screen'],(WIDTH,HEIGHT))
    assets[inception] = py.image.load(os.path.join(IMG,'inception.png')).convert()
    assets[inception] = py.transform.scale(assets['inception_screen'],(WIDTH,HEIGHT))
    assets[gameover] = py.image.load(os.path.join(IMG,'gameover.png')).convert()
    assets[gameover] = py.transform.scale(assets['gameover_screen'],(WIDTH,HEIGHT))
    assets[tryagain] = py.image.load(os.path.join(IMG,'tryagain.png')).convert()
    assets[tryagain] = py.transform.scale(assets['tryagain_screen'],(WIDTH,HEIGHT))
    assets[victory] = py.image.load(os.path.join(IMG,'victory.png')).convert()
    assets[victory] = py.transform.scale(assets['victory_screen'],(WIDTH,HEIGHT))
    assets[pause] = py.image.load(os.path.join(IMG,'pause.png')).convert()
    assets[pause] = py.transform.scale(assets['pause_screen'],(WIDTH,HEIGHT))
    # Background do jogo.
    assets[background] = py.image.load(os.path.join(IMG,'background.png')).convert()
    assets[background] = py.transform.scale(assets['background'],(WIDTH,HEIGHT))
    assets[ocean_background] = py.image.load(os.path.join(IMG,'ocean_background.png')).convert()
    assets[ocean_background] = py.transform.scale(assets['ocean_background'],(WIDTH,HEIGHT))
    # Sprites.
    assets[tank1] = py.image.load(os.path.join(IMG,'enemy_tank1.png')).convert_alpha()
    assets[tank1] = py.transform.scale(assets['tank1'],(TANK_WIDTH,TANK_HEIGHT))
    assets[tank2] = py.image.load(os.path.join(IMG,'enemy_tank2.png')).convert_alpha()
    assets[tank2] = py.transform.scale(assets['tank2'],(TANK_WIDTH,TANK_HEIGHT + 6))
    assets[tank3] = py.image.load(os.path.join(IMG,'enemy_tank3.png')).convert_alpha()
    assets[tank3] = py.transform.scale(assets['tank3'],(TANK_WIDTH + 10,TANK_HEIGHT + 6))
    assets[ground] = py.image.load(os.path.join(IMG,'ground.jpg')).convert()
    assets[ground] = py.transform.scale(assets['ground'],(WIDTH,GROUND_HEIGHT))
    assets[mine] = py.image.load(os.path.join(IMG,'mine.png')).convert_alpha()
    assets[mine] = py.transform.scale(assets['mine'],(MINE_WIDTH,MINE_HEIGHT))
    assets[howitzer] = py.image.load(os.path.join(IMG,'howitzer.png')).convert_alpha()
    assets[howitzer] = py.transform.scale(assets['howitzer'],(HOWITZER_WIDTH,HOWITZER_HEIGHT))
    assets[sergeant] = py.image.load(os.path.join(IMG,'sergeant.png')).convert_alpha()
    assets[sergeant] = py.transform.scale(assets['sergeant'],(SERGEANT_WIDTH,SERGEANT_HEIGHT))
    assets[shell] = py.image.load(os.path.join(IMG,'shell.png')).convert_alpha()
    assets[shell] = py.transform.scale(assets['shell'],(SHELL_WIDTH,SHELL_HEIGHT))
    assets[plane] = py.image.load(os.path.join(IMG,'plane.png')).convert_alpha()
    assets[plane] = py.transform.scale(assets['plane'],(PLANE_WIDTH,PLANE_HEIGHT))
    assets[rocket] = py.image.load(os.path.join(IMG,'rocket.png')).convert_alpha()
    assets[rocket] = py.transform.scale(assets['rocket'],(ROCKET_WIDTH,ROCKET_HEIGHT))
    assets[submarine] = py.image.load(os.path.join(IMG,'submarine.png')).convert_alpha()
    assets[submarine] = py.transform.scale(assets['submarine'],(SUBMARINE_WIDTH,SUBMARINE_HEIGHT))
    assets[missile_up] = py.image.load(os.path.join(IMG,'missile_up.png')).convert_alpha()
    assets[missile_up] = py.transform.scale(assets['missile_up'],(MISSILE_WIDTH,MISSILE_HEIGHT))
    assets[missile_down] = py.image.load(os.path.join(IMG,'missile_down.png')).convert_alpha()
    assets[missile_down] = py.transform.scale(assets['missile_down'],(MISSILE_WIDTH,MISSILE_HEIGHT))
    # Ícones para informação na tela.
    assets[mission] = py.image.load(os.path.join(IMG,'mission.png')).convert_alpha()
    assets[mission] = py.transform.scale(assets['mission'],(MISSION_WIDTH,MISSION_HEIGHT))
    assets[tank_info] = py.image.load(os.path.join(IMG,'tank_info.jpg')).convert_alpha()
    assets[tank_info] = py.transform.scale(assets['tank_info'],(TANK_INFO_WIDTH,TANK_INFO_HEIGHT))
    assets[plane_info] = py.image.load(os.path.join(IMG,'plane_info.png')).convert_alpha()
    assets[plane_info] = py.transform.scale(assets['plane_info'],(PLANE_INFO_WIDTH,PLANE_INFO_HEIGHT))
    assets[submarine_info] = py.image.load(os.path.join(IMG,'submarine_info.png')).convert_alpha()
    assets[submarine_info] = py.transform.scale(assets['submarine_info'],(SUBMARINE_INFO_WIDTH,SUBMARINE_INFO_HEIGHT))
    assets[shell_info] = py.image.load(os.path.join(IMG,'candieiro.png')).convert_alpha()
    assets[shell_info] = py.transform.scale(assets['shell_info'],(SHELL_INFO_WIDTH,SHELL_INFO_HEIGHT))
    assets[ruler] = py.image.load(os.path.join(IMG,'ruler.png')).convert_alpha()
    assets[ruler] = py.transform.scale(assets['ruler'],(RULER_WIDTH,RULER_HEIGHT))
    # Animações (frames).
    # Explosão 1.
    explosion_anim = list()
    for i in range(1,13):
        frame = os.path.join(IMG,'explosion_f{}.png'.format(i))
        image =  py.image.load(frame).convert_alpha()
        image = py.transform.scale(image,(100,100))
        explosion_anim.append(image)
    assets[explosion_animation] = explosion_anim
    # Explosão 2.
    explosion_anim2 = list()
    for i in range(1,21):
        frame = os.path.join(IMG,'explosion2_f{}.png'.format(i))
        image =  py.image.load(frame).convert_alpha()
        image = py.transform.scale(image,(200,200))
        explosion_anim2.append(image)
    assets[explosion_animation2] = explosion_anim2
    # Fumaça do tiro.
    smoke_anim = list()
    for i in range(1,6):
        frame = os.path.join(IMG,'smoke_f{}.png'.format(i))
        image =  py.image.load(frame).convert_alpha()
        image = py.transform.scale(image,(20,30))
        smoke_anim.append(image)
    assets[smoke_animation] = smoke_anim
    # SONS (como mais de uma trilha sonora vai ser usada, elas serão carregadas e tocadas no próprio código dos diferentes estágios - aqui só vamos carregar os "sons curtos").
    assets[shooting] = py.mixer.Sound(os.path.join(SOUND,'shooting.mp3'))
    assets[shout] = py.mixer.Sound(os.path.join(SOUND,'shout.mp3'))
    assets[explosion_hit] = py.mixer.Sound(os.path.join(SOUND,'explosion_hit.mp3'))
    assets[explosion_miss] = py.mixer.Sound(os.path.join(SOUND,'explosion_miss.mp3'))
    assets[plane_sound] = py.mixer.Sound(os.path.join(SOUND,'plane.mp3'))
    assets[rocket_sound] = py.mixer.Sound(os.path.join(SOUND,'rocket.mp3'))
    assets[call] = py.mixer.Sound(os.path.join(SOUND,'call.mp3'))
    assets[call2] = py.mixer.Sound(os.path.join(SOUND,'call2.mp3'))
    assets[support] = py.mixer.Sound(os.path.join(SOUND,'support.mp3'))
    assets[submarine_sound] = py.mixer.Sound(os.path.join(SOUND,'submarine.mp3'))
    assets[missile_sound] = py.mixer.Sound(os.path.join(SOUND,'missile.mp3'))
    return assets


