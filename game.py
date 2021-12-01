# Importando as bibliotecas necessárias.
import pygame as py
import random as r
from assets import load_assets, explosion_hit, explosion_miss, background
from sprites import Enemy_tank, Explosion, Explosion2, Ground, Howitzer, Sergeant
from values import EXPLODING, FPS, PLAYING, QUIT,TRYAGAIN,VICTORY


# Criando a função com a estrutura fundamental do jogo.
def game_screen(screen):
    # Variável para o ajuste de velocidade do jogo (quantos fps).
    clock = py.time.Clock()
    # Carregando os assets.
    assets  = load_assets()
    # Criando os grupos.
    all_sprites = py.sprite.Group()
    all_enemies = py.sprite.Group()
    all_shells = py.sprite.Group()
    groups = dict()
    groups['all_sprites'] = all_sprites
    groups['all_shells'] = all_shells
    groups['all_enemies'] = all_enemies
    # Criando o jogador (obuseiro e sargento).
    player = Howitzer(groups,assets)
    sergeant = Sergeant(assets)
    all_sprites.add(player)
    all_sprites.add(sergeant)
    # Criando o "chão" e a mina.
    floor = Ground(assets)
    all_sprites.add(floor)
    # Criando variável que contém o número de blindados/inimigos destruídos. 
    enemy_down = 0
    # Criando variável que contém o número de blindados/inimigos criados. 
    enemy_created = 0
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
                        player.shoot(1) 
                    elif event.key == py.K_2:
                        player.shoot(2)
                    elif event.key == py.K_3:
                        player.shoot(3)
                    elif event.key == py.K_4:
                        player.shoot(4)
                    elif event.key == py.K_5:
                        player.shoot(5)
                    elif event.key == py.K_6:
                        player.shoot(6)
                    elif event.key == py.K_7:
                        player.shoot(7)

        # Atualizando estado do jogo.
        all_sprites.update()

        if STATE == PLAYING:
            # Verificando se houve colisão entre o projétil e o inimigo, entre o projétil e o "chão", entre o inimigo e o obuseiro, entre o foguete e o "chão", entre o foguete e o inimigo e entre a mina e o inimigo.
            hits = py.sprite.groupcollide(all_enemies, all_shells, True, True, py.sprite.collide_mask)
            misses = py.sprite.spritecollide(floor, all_shells, True, py.sprite.collide_mask)
            collision = py.sprite.spritecollide(player, all_enemies, True, py.sprite.collide_mask)
            # O inimigo destruído precisa ser recriado.
            for enemy in hits:
                consecutive_hits_for_air_support += 1
                consecutive_hits_for_submarine_support += 1
                assets[explosion_hit].play()
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
        if enemy_down >= 10:
            STATE = VICTORY
        # Gerando as saídas...
        # Fundo.
        screen.blit(assets[background],(0,0))
        # Todo os sprites.
        all_sprites.draw(screen)
        
        # Atualizando os novos frames do jogo para o jogador/usuário.
        py.display.update()
    state = STATE # --> Convertendo de volta para o estado de jogo do arquivo THE GUNNER.
    return state






 
            
                    



