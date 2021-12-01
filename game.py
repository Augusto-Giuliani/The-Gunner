# Importando as bibliotecas necessárias.
import pygame as py
import random as r
from assets import load_assets, explosion_hit, explosion_miss, background,mission, call, plane_info, plane_sound, shell_info,tank_info,support,ruler
from sprites import Enemy_tank, Explosion, Explosion2, Ground, Howitzer,  Mine, Sergeant, Plane
from values import BLACK,EXPLODING, FPS, HEIGHT,PLAYING,QUIT,TRYAGAIN,VICTORY,RED,WIDTH,RULER_WIDTH,HOWITZER_WIDTH,PLANE_INFO_WIDTH
from screens import pause_screen

# Criando a função com a estrutura fundamental do jogo.
def game_screen(screen,game_data):
    # Variável para o ajuste de velocidade do jogo (quantos fps).
    clock = py.time.Clock()
    # Carregando os assets.
    assets  = load_assets()
    # Criando os grupos.
    all_sprites = py.sprite.Group()
    all_enemies = py.sprite.Group()
    all_shells = py.sprite.Group()
    all_rockets = py.sprite.Group()

    groups = dict()
    groups['all_sprites'] = all_sprites
    groups['all_shells'] = all_shells
    groups['all_enemies'] = all_enemies
    groups['all_rockets'] = all_rockets
    # Criando o jogador (obuseiro e sargento).
    player = Howitzer(groups,assets)
    sergeant = Sergeant(assets)
    all_sprites.add(player)
    all_sprites.add(sergeant)
    # Criando o "chão" e a mina.
    floor = Ground(assets)
    all_sprites.add(floor)
    mine = Mine(assets)
    all_sprites.add(mine)
    # Criando variável que contém o número de blindados/inimigos destruídos. 
    enemy_down = 0
    # Criando variável que contém o número de blindados/inimigos criados. 
    enemy_created = 0
    # Criando variável que contém o número de tiros realizados, dentro do dicionário com dados do jogo. 
    game_data['Shots taken'] = 0
    # Criando variável que contém o número de blindados/inimigos que precisam ser destruídos para cumprir a missão, dentro do dicionário com dados do jogo. 
    game_data['Mission'] = 20
    # Criando variáveis que serão usadas em caso de suporte aéreo.
    air_support = False # --> True quando o suporte aéreo for ativado.
    activate_air_support = False # --> True quando o suporte aéreo pode ser ativado/está na "espera" (ícone do avião aparece no canto direito).
    to_get_air_support = 2 # --> Quantos inimigos precisa destruír consecutivamente (sem erros) para conseguir suporte aéreo.
    consecutive_hits_for_air_support = 0
    # Criando variável que vai ser usada para o suporte topográfico (dar o alcance médio no terreno, de cada carga, para o jogador).
    topografic_support = False
    activate_topographic_support = False
    to_get_topographic_support = game_data['Mission']/2 # --> Quando chegar na metade do objetivo, o suporte topográfico poderá ser acionado.
    # Variável para tocar o som de suporte uma vez.
    support_sound_air = True
    support_sound_topo = True
    # Criando o inimigo.
    for i in range(3):
        enemy = Enemy_tank(assets,i+1)
        all_sprites.add(enemy)
        all_enemies.add(enemy)
        enemy_created += 1

    # LOOP PRINCIPAL

    # Tocando música principal.
    py.mixer.music.load('sounds/playing.mp3')
    py.mixer.music.play(loops=-1)

    STATE = PLAYING # --> Criando variável que contém o estado do jogo na tela game.
    while STATE != QUIT and STATE != TRYAGAIN and STATE != VICTORY:

        clock.tick(FPS) #--> ajustagem da velocidade do jogo.

        # Tratando eventos.
        for event in py.event.get():
            if event.type == py.QUIT:
                STATE = QUIT
            # Só verifica eventos do teclado se estiver no estado de "jogando".
            if STATE == PLAYING:
                # Verificando se apertou alguma tecla.
                if event.type == py.KEYDOWN:
                    # A velocidade inicial do projétil varia de acordo com a carga de projeção escolhida (teclas 1-7). O jogador deve apertar a tecla de acordo com a carga que deseja.
                    if event.key == py.K_1:
                        player.shoot(1,game_data) 
                    elif event.key == py.K_2:
                        player.shoot(2,game_data)
                    elif event.key == py.K_3:
                        player.shoot(3,game_data)
                    elif event.key == py.K_4:
                        player.shoot(4,game_data)
                    elif event.key == py.K_5:
                        player.shoot(5,game_data)
                    elif event.key == py.K_6:
                        player.shoot(6,game_data)
                    elif event.key == py.K_7:
                        player.shoot(7,game_data)
                    # Caso o suporte aéreo esteja "na espera" (ícone do avião apareceu na tela), a tecla "8" vai ativá-lo.
                    elif activate_air_support and event.key == py.K_8:
                        assets[call].play()
                        assets[plane_sound].play()
                        player_plane = Plane(groups,assets)
                        all_sprites.add(player_plane)
                        air_support = True # --> Ativando suporte aéreo.
                        activate_air_support = False # --> Ícone some da tela.
                    # Caso o suporte aéreo seja ativado, a tecla "8" é o gatilho para atirar o foguete.
                    elif air_support and event.key == py.K_8:
                        player_plane.shoot()
                    # Caso o suporte topográfico esteja "na espera" (ícone da régua apareceu na tela), a tecla "9" vai ativá-lo.
                    elif activate_topographic_support and event.key == py.K_9:
                        topografic_support = True # --> Ativando suporte topográfico.
                        activate_topographic_support = False # --> Ícone some da tela.
                    # Caso o jogador queira uma pausa...
                    elif event.key == py.K_p:
                        STATE = pause_screen(screen)

        # Atualizando estado do jogo.
        all_sprites.update()

        if STATE == PLAYING:
            # Verificando se houve colisão entre o projétil e o inimigo, entre o projétil e o "chão", entre o inimigo e o obuseiro, entre o foguete e o "chão", entre o foguete e o inimigo e entre a mina e o inimigo.
            hits = py.sprite.groupcollide(all_enemies, all_shells, True, True, py.sprite.collide_mask)
            hits2 = py.sprite.groupcollide(all_enemies, all_rockets, True, True, py.sprite.collide_mask)
            misses = py.sprite.spritecollide(floor, all_shells, True, py.sprite.collide_mask)
            misses2 = py.sprite.spritecollide(floor, all_rockets, True, py.sprite.collide_mask)
            collision = py.sprite.spritecollide(player, all_enemies, True, py.sprite.collide_mask)
            mine_hit = py.sprite.spritecollide(mine, all_enemies, True, py.sprite.collide_mask)

            # O inimigo destruído precisa ser recriado.
            for enemy in hits:
                consecutive_hits_for_air_support += 1
                consecutive_hits_for_submarine_support += 1
                assets[explosion_hit].play()
                if enemy_created < game_data['Mission']: # --> Não aparecer inimigos a mais do que a missão já estebelece.
                    e = Enemy_tank(assets,r.choice([1,2,3]))
                    all_sprites.add(e)
                    all_enemies.add(e)
                    enemy_created += 1
                # No lugar do inimigo destruído, adicionando uma explosão.
                explosion = Explosion2(enemy.rect.centerx,enemy.rect.centery - 55,assets)
                all_sprites.add(explosion)
                enemy_down +=1 
            for enemy in mine_hit:
                assets[explosion_hit].play()
                mine.kill() # --> A mina some da tela, mas continua no mesmo lugar.
                mine.rect.y = HEIGHT # --> Altera a posição da mina para que os outros inimigos possam colidir com o obuseiro.
                if enemy_created < game_data['Mission']: # --> Não aparecer inimigos a mais do que a missão já estebelece.
                    e = Enemy_tank(assets,r.choice([1,2,3]))
                    all_sprites.add(e)
                    all_enemies.add(e)
                    enemy_created += 1
                # No lugar do inimigo destruído, adicionando uma explosão.
                explosion = Explosion2(enemy.rect.centerx,enemy.rect.centery - 55,assets)
                all_sprites.add(explosion)
                enemy_down +=1
            for enemy in hits2:
                assets[explosion_hit].play()
                if enemy_created < game_data['Mission']: # --> Não aparecer inimigos a mais do que a missão já estebelece.
                    e = Enemy_tank(assets,r.choice([1,2,3]))
                    all_sprites.add(e)
                    all_enemies.add(e)
                    enemy_created += 1
                # No lugar do inimigo destruído, adicionando uma explosão.
                explosion = Explosion2(enemy.rect.centerx,enemy.rect.centery - 55,assets)
                all_sprites.add(explosion)
                enemy_down +=1
            # Caso o projétil atinja o "chão".
            for shell in misses:
                consecutive_hits_for_air_support = 0 
                consecutive_hits_for_submarine_support = 0
                assets[explosion_miss].play()
                explosion = Explosion(shell.rect.centerx,shell.rect.centery - 30,assets)
                all_sprites.add(explosion)  
            for rocket in misses2:
                assets[explosion_miss].play()
                explosion = Explosion(rocket.rect.centerx,rocket.rect.centery - 30,assets)
                all_sprites.add(explosion)
            # Caso o inimigo atinja o obuseiro (player), GAME OVER.
            for enemy in collision:
                assets[explosion_hit].play()
                player.kill()
                explosion_player = Explosion2(player.rect.centerx,player.rect.centery - 60,assets)
                explosion_enemy = Explosion2(enemy.rect.centerx,enemy.rect.centery - 55,assets)
                all_sprites.add(explosion_player)
                all_sprites.add(explosion_enemy)
                STATE = EXPLODING
                explosion_tick = py.time.get_ticks()
                explosion_duration = explosion_player.frame_ticks*len(explosion_player.explosion_anim2) + 1000
        elif STATE == EXPLODING:
            now = py.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                STATE = TRYAGAIN
        # Caso um número (mission) de blindados/inimigos seja destruído, vitória do usuário.
        if enemy_down >= game_data['Mission']:
            STATE = VICTORY
        # Caso o número de inimigos destruídos consecutivamente seja atinjido, o suporte aéreo poderá ser ativado (modo de "espera"; ícone aparece).
        if consecutive_hits_for_air_support == to_get_air_support and not air_support and not activate_air_support:
            activate_air_support = True
            support_sound_air = True
            consecutive_hits_for_air_support = 0
        # Caso o avião já tenha saído da tela...
        if air_support and player_plane.rect.x > WIDTH:
            air_support = False
        # Caso o número de inimigos destruídos atinja o previsto para suporte topográfico.
        if enemy_down >= to_get_topographic_support and not topografic_support:
            activate_topographic_support = True 
        # Gerando as saídas...
        # Fundo.
        screen.blit(assets[background],(0,0))
        # Todo os sprites.
        all_sprites.draw(screen)
        # Informações úteis na tela...
        font = py.font.SysFont(None,80)
        font2 = py.font.SysFont(None,40)
        # Desenhando o número de blindados/inimigos destruídos.
        text_enemies_down = font.render('{:03d}'.format(enemy_down),True,RED)
        text_rect = text_enemies_down.get_rect()
        text_rect.bottomleft = (120,180)
        screen.blit(text_enemies_down,text_rect) # --> Dado numérico.
        screen.blit(assets[tank_info],(10,100)) # --> Ícone.
        # Desenhando o número de blindados/inimigos que precisam ser destruídos.
        text_mission = font.render('{:03d}'.format(game_data['Mission']),True,RED)
        text_rect = text_mission.get_rect()
        text_rect.bottomleft = (120,100)
        screen.blit(text_mission,text_rect) # --> Dado numérico.
        screen.blit(assets[mission],(-10,10)) # --> Ícone.
        # Desenhando o número de disparos realizados.
        text_shots = font.render('{:03d}'.format(game_data['Shots taken']),True,RED)
        text_rect = text_mission.get_rect()
        text_rect.bottomleft = (WIDTH - 110,130)
        screen.blit(text_shots,text_rect) # --> Dado numérico.
        screen.blit(assets[shell_info],(WIDTH - 240,20)) # --> Ícone.
        # Desenhando o ícone do avião caso o suporte aéreo possa ser ativado.
        if activate_air_support:
            consecutive_hits_for_air_support = 0
            if support_sound_air:
                assets[support].play()
                support_sound_air = False
            screen.blit(assets[plane_info],(WIDTH - PLANE_INFO_WIDTH - 10,300)) # --> Ícone.
        # Desenhando o ícone da régua caso o suporte topográfico possa ser ativado.
        if activate_topographic_support:
            if support_sound_topo:
                assets[support].play()
                support_sound_topo = False
            screen.blit(assets[ruler],(WIDTH - RULER_WIDTH - 10,200 - 10)) # --> Ícone.
        # Caso o suporte topográfico seja ativado.
        if topografic_support:
            # Desenhando os números no chão para indicar os alcances de cada carga.
            range_number_scale = font2.render('     1         2             3                  4                         5                            6                                 7',True,BLACK)
            range_number_scale_rect = range_number_scale.get_rect()
            range_number_scale_rect.bottomleft = (HOWITZER_WIDTH+50,HEIGHT-2)
            screen.blit(range_number_scale,range_number_scale_rect) # --> Dado numérico.
            # Desenhando as marcas de cada número do alcance.
            range_number_scale_mark = font2.render('    |          |              |                   |                         |                             |                                  |',True,BLACK)
            range_number_scale_mark_rect = range_number_scale_mark.get_rect()
            range_number_scale_mark_rect.bottomleft = (HOWITZER_WIDTH+50,HEIGHT-4)
            screen.blit(range_number_scale_mark,range_number_scale_mark_rect) # --> Marcas.
        # Atualizando os novos frames do jogo para o jogador/usuário.
        py.display.update()
    state = STATE # --> Convertendo de volta para o estado de jogo do arquivo THE GUNNER.
    return state






 
            
                    



