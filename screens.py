# Importando...
import pygame as py
from assets import intro,inception,tryagain,gameover,victory,pause,submarine_sound,ocean_background,the_mission,details,details2,load_assets
from sprites import Submarine
from values import GAMEOVER,HEIGHT,INCEPTION,INTRO,PLAYING,QUIT,GAME,TRYAGAIN,VICTORY,RED,FPS

# Criando a função que plota a tela INTRO e retorna o estado do jogo.
def intro_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets
    # Criando loop que trata eventos e redesenha o fundo.
    running = True
    state = INTRO
    while running:
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou a tecla "Espaço".
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    state = INCEPTION
                    running = False
        # Redesenhando o fundo a cada loop.
        screen.blit(assets[intro],(0,0))
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de INCEPTION e retorna o estado do jogo.
def inception_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets
    # Carregando e tocando a trilha sonora de começo.
    py.mixer.music.load('sounds/intro.mp3')
    py.mixer.music.play(loops=-1)
    # Criando loop que trata eventos e redesenha o fundo.
    running = True
    state = INCEPTION
    while running:
        # Redesenhando o fundo a cada loop.
        screen.blit(assets[inception],(0,0))
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou a tecla "Espaço".
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    state = GAME
                    running = False
                    state = the_mission_screen(screen)
                    state = details_screen(screen)
                    state = details2_screen(screen)
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de THE_MISSION e retorna o estado do jogo.
def the_mission_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets
    # Criando loop que trata eventos e redesenha o fundo.
    running = True
    state = GAME
    while running:
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou a tecla "Espaço".
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    running = False
        # Redesenhando o fundo a cada loop.
        screen.blit(assets[the_mission],(0,0))
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de DETAILS e retorna o estado do jogo.
def details_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets
    # Criando loop que trata eventos e redesenha o fundo.
    running = True
    state = GAME
    while running:
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou a tecla "Espaço".
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    running = False
        # Redesenhando o fundo a cada loop.
        screen.blit(assets[details],(0,0))
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de DETAILS2 e retorna o estado do jogo.
def details2_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets
    # Criando loop que trata eventos e redesenha o fundo.
    running = True
    state = GAME
    while running:
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou a tecla "Espaço".
            elif event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    running = False
        # Redesenhando o fundo a cada loop.
        screen.blit(assets[details2],(0,0))
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de TRYAGAIN, caso o obuseiro seja destruído.
def tryagain_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets
    # Carregando e tocando a trilha sonora de derrota.
    py.mixer.music.load('sounds/sad.mp3')
    py.mixer.music.play(loops=-1)
    # Criando loop que trata eventos e redesenha o fundo.
    running = True
    state = TRYAGAIN
    while running:
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou alguma tecla.
            elif event.type == py.KEYDOWN:
                if event.key == py.K_s: # --> Usuário apertou "s", volta para o jogo novamente.
                    state = GAME
                    running = False
                if event.key == py.K_n: # --> Usuário apertou "n", GAMEOVER.
                    state = GAMEOVER
                    running = False
        # Redesenhando o fundo a cada loop.
        screen.blit(assets[tryagain],(0,0))
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de GAMEOVER, caso o obuseiro seja destruído e o usuário tenha desistido.
def gameover_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets     
    # Redesenhando o fundo a cada loop.
    screen.blit(assets[gameover],(0,0))
    # Mostrando novo frame para o jogador.
    py.display.update()
    # Pausa por 3 segundos.
    py.time.delay(6000)
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return QUIT

# Criando a função que plota a tela de PAUSE, caso o jogador aperte a tecla "P".
def pause_screen(screen):
    assets = load_assets() # --> criando o dicionário com os assets
    # Carregando e tocando a trilha sonora de pausa.
    py.mixer.music.load('sounds/pause.mp3')
    py.mixer.music.play(loops=-1) 
    running = True
    state = PLAYING
    while running:
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou alguma tecla.
            elif event.type == py.KEYDOWN:
                if event.key == py.K_p: # --> Usuário apertou "P", termina o loop e volta para  o jogo.
                    running = False
        # Redesenhando o fundo a cada loop.
        screen.blit(assets[pause],(0,0))
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Voltando a música principal.
    py.mixer.music.load('sounds/playing.mp3')
    py.mixer.music.play(loops=-1)
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de VICTORY, caso o usuário tenha cumprido a missão do jogo.
def victory_screen(screen,game_data):
    assets = load_assets() # --> criando o dicionário com os assets
    # Carregando e tocando a trilha sonora de vitória.
    py.mixer.music.load('sounds/victory.mp3')
    py.mixer.music.play(loops=-1)
    # Criando loop que trata eventos e redesenha o fundo.
    running = True
    state = VICTORY
    while running:
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
            # Verifica se o usuário apertou alguma tecla.
            elif event.type == py.KEYDOWN:
                if event.key == py.K_s: # --> Usuário apertou "s", volta para o jogo novamente.
                    state = GAME
                    running = False
                if event.key == py.K_n: # --> Usuário apertou "n", GAMEOVER.
                    state = GAMEOVER
                    running = False
        # Redesenhando o fundo da introdução a cada loop.
        screen.blit(assets[victory],(0,0))
        # Desenhando dados do jogo.
        font = py.font.SysFont(None,45)
        # Número de tiros realizados, performance/eficiência (tiros por inimigo) e classificação.
        performance = game_data['Shots taken']/game_data['Mission']
        rating = ''
        if performance <= 0.85:
            rating = 'Gunner'
        elif performance <= 1.35:
            rating = 'Profissional'
        elif performance <= 2:
            rating = 'Iniciante'
        else:
            rating = 'Bisonho'
        title = font.render('FEEDBACK',True,RED)
        text_rect = title.get_rect()
        text_rect.bottomleft = (10,HEIGHT/2)
        screen.blit(title,text_rect)
        shots = font.render('- Quantidade de disparos: {}'.format(game_data['Shots taken']),True,RED) 
        text_rect = shots.get_rect()
        text_rect.bottomleft = (10,HEIGHT/2+80)
        screen.blit(shots,text_rect)
        efficiency = font.render('- Performance: {:.1f}'.format(performance),True,RED) 
        text_rect = efficiency.get_rect()
        text_rect.bottomleft = (10,HEIGHT/2+160)
        screen.blit(efficiency,text_rect)
        classification = font.render('- Classificação: {}'.format(rating),True,RED) 
        text_rect = classification.get_rect()
        text_rect.bottomleft = (10,HEIGHT/2+240)
        screen.blit(classification,text_rect)

        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state

# Criando a função que plota a tela de OCEAN, caso o jogador aperte a tecla "0" (se estiver "na espera" o suporte de submarino).
def ocean_screen(screen):
    # Variável para o ajuste de velocidade (quantos fps).
    clock = py.time.Clock()
    assets = load_assets() # --> criando o dicionário com os assets
    # Criando o grupo de sprites e o submarino.
    all_sprites_ocean = py.sprite.Group()
    groups_ocean = dict()
    groups_ocean['all_sprites_ocean'] = all_sprites_ocean
    submarine = Submarine(groups_ocean,assets)
    all_sprites_ocean.add(submarine)
    # Som do submarino.
    assets[submarine_sound].play()
    # Marcando o tempo inicial e determinando a duração.
    origin = py.time.get_ticks()
    duration_to_shoot = 3000
    duration_to_end = 10000
    # Para não atirar de novo.
    not_launched = True 

    running = True
    state = PLAYING
    while running:
        now = py.time.get_ticks()
        clock.tick(FPS) #--> ajustagem da velocidade do jogo.
        # Processa os eventos.
        for event in py.event.get():
            # Verifica se foi fechado (" botão X").
            if event.type == py.QUIT:
                state = QUIT
                running = False
        if now - origin > duration_to_shoot and not_launched:
            submarine.shoot()
            not_launched = False
        if now - origin > duration_to_end:
            running = False

        all_sprites_ocean.update() # Atualizando os sprites.
        # Desenhando a cada loop os sprites e o fundo.
        screen.blit(assets[ocean_background],(0,0))
        all_sprites_ocean.draw(screen)
        # Mostrando novo frame para o jogador.
        py.display.update()
    # Retorna o novo/mesmo estado do jogo, dando prosseguimento ao jogo ou continuando no mesmo lugar.
    return state



     