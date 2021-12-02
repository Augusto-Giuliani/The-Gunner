# Importando...
import pygame as py
import random as r
from assets import shell,sergeant,howitzer,tank1,tank2,tank3,ground,shooting,shout,explosion_animation,explosion_animation2,plane,rocket_sound,rocket,smoke_animation,mine,submarine,missile_down,missile_up,big_enemy
from values import GROUND_HEIGHT,HEIGHT,HOWITZER_HEIGHT,HOWITZER_WIDTH,MINE_HEIGHT,PLANE_WIDTH,SERGEANT_HEIGHT,SERGEANT_WIDTH,SUBMARINE_WIDTH,TANK_HEIGHT,WIDTH

# Criando o objeto Ground ("chão" do jogo).
class Ground(py.sprite.Sprite):
    def __init__(self, assets):
        py.sprite.Sprite.__init__(self)
        self.image = assets[ground]
        self.mask = py.mask.from_surface(self.image) # --> criando uma máscara para o chão.
        # Posicionando o chão no background.
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - GROUND_HEIGHT

# Criando o objeto Mine (oferece uma segunda chance para o obuseiro).
class Mine(py.sprite.Sprite):
    def __init__(self,assets):
        py.sprite.Sprite.__init__(self)
        self.image = assets[mine]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando a mina logo do lado do obuseiro.
        self.rect = self.image.get_rect()
        self.rect.x = 20 + SERGEANT_WIDTH + HOWITZER_WIDTH 
        self.rect.y = HEIGHT - GROUND_HEIGHT - MINE_HEIGHT
        

# Criando o objeto Sergeant (representando visualmente o jogador).
class Sergeant(py.sprite.Sprite):
    def __init__(self, assets):
        py.sprite.Sprite.__init__(self)
        self.image = assets[sergeant]
        # Posicionando o sargento em cima do chão.
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = (HEIGHT - GROUND_HEIGHT) - SERGEANT_HEIGHT

# Criando o objeto Howitzer/obuseiro (realiza as ações do jogador).
class Howitzer(py.sprite.Sprite):
    def __init__(self, groups, assets):
        py.sprite.Sprite.__init__(self)
        self.image = assets[howitzer]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando o obuseiro em cima do chão, do lado do Sergeant.
        self.rect = self.image.get_rect()
        self.rect.x = 10 + SERGEANT_WIDTH
        self.rect.y = (HEIGHT - GROUND_HEIGHT) - HOWITZER_HEIGHT
        self.groups = groups 
        self.assets = assets
        # Shooting rate: só será possível atirar uma vez a cada 1000 ms.
        self.last_shot = py.time.get_ticks()
        self.shoot_ticks = 1000
    def shoot(self, CHARGE, game_data):
        # Verifica se pode atirar.
        now = py.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot
        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova granada vai ser criada logo ao final do tubo do obuseiro, junto com a fumaça do tiro.
            new_shell = Shell(self.assets,self.rect.top,self.rect.right,CHARGE)
            self.groups['all_sprites'].add(new_shell)
            self.groups['all_shells'].add(new_shell)
            self.assets[shout].play()
            self.assets[shooting].play() # --> toca o barulho de tiro.
            game_data['Shots taken'] += 1
            smoke = Smoke(self.rect.right,self.rect.top,self.assets)
            self.groups['all_sprites'].add(smoke)
    
# Criando o objeto projétil Shell.
class Shell(py.sprite.Sprite):
    def __init__(self, assets, bottom, centerx, CHARGE):
        py.sprite.Sprite.__init__(self)
        self.image = assets[shell]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando a parte inferior esquerda do projétil logo ao final do tubo do obuseiro.
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        # Determinando a velocidade do projétil (velocidade horizontal constante, velocidade vertical variável).
        # A velocidade inicial do projétil varia de acordo com a carga de projeção escolhida (1-7), e para cada carga escolhida haverá uma faixa de velocidade a ser considerada (como se houvesse uma incerteza no tiro).
        if CHARGE == 1:
            self.speedx = r.choice([1,1.25,1.5,1.75,2])
        elif CHARGE == 2:
            self.speedx = r.choice([2.25,2.5,2.75,3])
        elif CHARGE == 3:
            self.speedx = r.choice([3.25,3.5,3.75,4])
        elif CHARGE == 4:
            self.speedx = r.choice([4.25,4.5,4.75,5])
        elif CHARGE == 5:
            self.speedx = r.choice([5.25,5.5,5.75,6])
        elif CHARGE == 6:
            self.speedx = r.choice([6.25,6.5,6.75,7])
        elif CHARGE == 7:
            self.speedx = r.choice([7.25,7.5,7.75])
        self.speedy = -self.speedx
    # Atualiza a posição do projétil.
    def update(self):
        self.speedy += 0.1 # --> Atualizando a velocidade vertical, que varia com o tempo.
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        # Se o projétil passar do canto direito da tela, morre.
        if self.rect.bottom > WIDTH:
            self.kill()

# Criando o objeto inimigo Enemy_tank.
class Enemy_tank(py.sprite.Sprite):
    def __init__(self,assets,type):
        py.sprite.Sprite.__init__(self)
        # Escolhendo um tipo de blindado de acordo com o pedido.
        if type == 1:
            self.image = assets[tank1] 
        elif type == 2:
            self.image = assets[tank2]
        elif type == 3:
            self.image = assets[tank3]     
        self.mask = py.mask.from_surface(self.image)
        # Posicionando o inimigo em cima do chão, vindo do canto direito da tela.
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = (HEIGHT - GROUND_HEIGHT) - TANK_HEIGHT
        # Determinando a velocidade do inimigo (só mexe horizontalmente). Blindados diferentes possuem faixas de velocidades distintas.
        if self.image == assets[tank2]:
            self.speedx = r.choice([-3,-2.75,-2.5,-2.25])
        elif self.image == assets[tank1]:
            self.speedx = r.choice([-2,-1.75,-1.5,-1.25])
        elif self.image == assets[tank3]:
            self.speedx = r.choice([-1,-0.75,-0.5,-0.25])  
    # Atualiza a posição do inimigo.
    def update(self):
        self.rect.x += self.speedx

# Criando o objeto inimigo Big_enemy. Esse blindado tem mais de uma vida (mais resistente).
class Big_enemy(py.sprite.Sprite):
    def __init__(self,assets): 
        py.sprite.Sprite.__init__(self)
        self.image = assets[big_enemy]     
        self.mask = py.mask.from_surface(self.image)
        # Posicionando o inimigo em cima do chão, vindo do canto direito da tela.
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = (HEIGHT - GROUND_HEIGHT) - TANK_HEIGHT - 10
        # Definindo a quantidade de vidas.
        self.lives = 3
        # Determinando a velocidade do inimigo (só mexe horizontalmente). 
        self.speedx = r.choice([-0.5,-0.25,-0.1]) 
    def HITS(self):
        self.lives -= 1
    # Atualiza a posição do inimigo.
    def update(self):
        self.rect.x += self.speedx
        # Caso tenha perdido as vidas, morre.
        if self.lives == 0:
            self.kill()
        
        
# Criando uma classe para animação da Explosão 1.
class Explosion(py.sprite.Sprite):
    def __init__(self, centerx, centery, assets):
        py.sprite.Sprite.__init__(self)
        # Armazena a animação da explosão.
        self.explosion_anim = assets[explosion_animation]
        # Iniciando o processo de animação colocando a primeira imagem na tela.
        self.frame = 0 # Armazena o índice atual na animação.
        self.image = self.explosion_anim[self.frame] # Pega a primeira imagem.
        self.rect = self.image.get_rect()
        # Posiciona o centro da imagem.
        self.rect.centerx = centerx 
        self.rect.centery = centery 
        # Guardando o tick da primeira imagem (o momento em que a imagem foi mostrada).
        self.last_update = py.time.get_ticks()
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos. Quando py.time.get_ticks() - self.last_update() > self.frame_ticks a próxima imagem da animação será mostrada.
        self.frame_ticks = 50
    def update(self):
        # Verificando o tick atual.
        now = py.time.get_ticks()
        # Verificando quantos ticks se passaram desde a última mudança de frame.
        elapsed_ticks = now - self.last_update
        # Se estiver na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            # Avança um frame.
            self.frame += 1

            # Verificando se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Termina com o processo.
                self.kill()
            # Se ainda não chegou ao final da animação, troca de imagem.
            else:
                centerx = self.rect.centerx
                centery = self.rect.centery
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.centerx = centerx
                self.rect.centery = centery

# Criando uma classe para animação da Explosão 2.
class Explosion2(py.sprite.Sprite):
    def __init__(self, centerx, centery, assets):
        py.sprite.Sprite.__init__(self)
        # Armazena a animação da explosão.
        self.explosion_anim2 = assets[explosion_animation2]
        # Iniciando o processo de animação colocando a primeira imagem na tela.
        self.frame = 0 # Armazena o índice atual na animação.
        self.image = self.explosion_anim2[self.frame] # Pega a primeira imagem.
        self.rect = self.image.get_rect()
        # Posiciona o centro da imagem.
        self.rect.centerx = centerx
        self.rect.centery = centery
        # Guardando o tick da primeira imagem (o momento em que a imagem foi mostrada).
        self.last_update = py.time.get_ticks()
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos. Quando py.time.get_ticks() - self.last_update() > self.frame_ticks a próxima imagem da animação será mostrada.
        self.frame_ticks = 50
    def update(self):
        # Verificando o tick atual.
        now = py.time.get_ticks()
        # Verificando quantos ticks se passaram desde a última mudança de frame.
        elapsed_ticks = now - self.last_update
        # Se estiver na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            # Avança um frame.
            self.frame += 1

            # Verificando se já chegou no final da animação.
            if self.frame == len(self.explosion_anim2):
                # Termina com o processo.
                self.kill()
            # Se ainda não chegou ao final da animação, troca de imagem.
            else:
                centerx = self.rect.centerx
                centery = self.rect.centery
                self.image = self.explosion_anim2[self.frame]
                self.rect = self.image.get_rect()
                self.rect.centerx = centerx
                self.rect.centery = centery

# Criando uma classe para animação da fumaça do tiro.
class Smoke(py.sprite.Sprite):
    def __init__(self, centerx, centery, assets):
        py.sprite.Sprite.__init__(self)
        # Armazena a animação da explosão.
        self.smoke_anim = assets[smoke_animation]
        # Iniciando o processo de animação colocando a primeira imagem na tela.
        self.frame = 0 # Armazena o índice atual na animação.
        self.image = self.smoke_anim[self.frame] # Pega a primeira imagem.
        self.rect = self.image.get_rect()
        # Posiciona o centro da imagem.
        self.rect.centerx = centerx
        self.rect.centery = centery
        # Guardando o tick da primeira imagem (o momento em que a imagem foi mostrada).
        self.last_update = py.time.get_ticks()
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos. Quando py.time.get_ticks() - self.last_update() > self.frame_ticks a próxima imagem da animação será mostrada.
        self.frame_ticks = 50
    def update(self):
        # Verificando o tick atual.
        now = py.time.get_ticks()
        # Verificando quantos ticks se passaram desde a última mudança de frame.
        elapsed_ticks = now - self.last_update
        # Se estiver na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now
            # Avança um frame.
            self.frame += 1

            # Verificando se já chegou no final da animação.
            if self.frame == len(self.smoke_anim):
                # Termina com o processo.
                self.kill()
            # Se ainda não chegou ao final da animação, troca de imagem.
            else:
                centerx = self.rect.centerx
                centery = self.rect.centery
                self.image = self.smoke_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.centerx = centerx
                self.rect.centery = centery

# Criando o objeto Plane, que só aparece quando o jogador atinge uma certa "pontuação".
class Plane(py.sprite.Sprite):
    def __init__(self, groups, assets):
        py.sprite.Sprite.__init__(self)
        self.image = assets[plane]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando o avião no ar, partindo do lado do obuseiro.
        self.rect = self.image.get_rect()
        self.rect.x = 0 - PLANE_WIDTH
        self.rect.y = HEIGHT/2
        self.groups = groups 
        self.assets = assets
        # Shooting rate: só será possível atirar uma vez a cada 1000 ms.
        self.last_shot = py.time.get_ticks()
        self.shoot_ticks = 1000
        # Determinando a velocidade do avião (só mexe horizontalmente).
        self.speedx = 3
    def shoot(self):
        # Verifica se pode atirar.
        now = py.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot
        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova granada vai ser criada logo ao final do tubo do obuseiro.
            new_rocket = Rocket(self.assets,self.rect.midbottom)
            self.groups['all_sprites'].add(new_rocket)
            self.groups['all_rockets'].add(new_rocket)
            self.assets[rocket_sound].play()
    # Atualizando a posição do avião.
    def update(self):
        self.rect.x += self.speedx
        # Se o avião passar do canto direito da tela, morre.
        if self.rect.x > WIDTH:
            self.kill()

# Criando o objeto projétil Rocket.
class Rocket(py.sprite.Sprite):
    def __init__(self, assets, topleft):
        py.sprite.Sprite.__init__(self)
        self.image = assets[rocket]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando a parte superior esquerda do projétil logo no centro inferior do avião.
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        # Determinando a velocidade do projétil (velocidade horizontal e vertical constantes).
        self.speedx = 5
        self.speedy = self.speedx
    # Atualiza a posição do projétil.
    def update(self):
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        # Se o projétil passar do canto direito da tela, morre.
        if self.rect.left > WIDTH:
            self.kill()

# Criando o objeto Submarine, que só aparece quando o jogador atinge uma certa "pontuação".
class Submarine(py.sprite.Sprite):
    def __init__(self, groups_ocean, assets):
        py.sprite.Sprite.__init__(self)
        self.image = assets[submarine]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando o submarino na água, movimentando lentamente para a direita.
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH/2 - SUBMARINE_WIDTH
        self.rect.y = HEIGHT/2
        self.groups = groups_ocean
        self.assets = assets
        # Determinando a velocidade do submarino (só mexe horizontalmente).
        self.speedx = 1.5
    def shoot(self):
        # O míssel vai ser criado logo em cima do submarino.
        missile = Missile_Up(self.assets,(self.rect.centerx - 100,self.rect.top + 165))
        self.groups['all_sprites_ocean'].add(missile)
    # Atualizando a posição do submarino.
    def update(self):
        self.rect.x += self.speedx
        
# Criando o objeto projétil Missile_Up que parte do submarino.
class Missile_Up(py.sprite.Sprite):
    def __init__(self, assets,midbottom):
        py.sprite.Sprite.__init__(self)
        self.image = assets[missile_up]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando a parte inferior central do míssel logo no centro superior do submarino.
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom
        # Determinando a velocidade do míssel (velocidade vertical constante para cima).
        self.speedy = -3
    # Atualiza a posição do projétil.
    def update(self):
        self.rect.y += self.speedy
        # Se o míssel passar do canto de cima da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

# Criando o objeto projétil Missile_Down que cai do céu.
class Missile_Down(py.sprite.Sprite):
    def __init__(self,assets,midbottom):
        py.sprite.Sprite.__init__(self)
        self.image = assets[missile_down]
        self.mask = py.mask.from_surface(self.image)
        # Posicionando a parte superior central do míssel logo no céu.
        self.rect = self.image.get_rect()
        self.rect.midbottom = midbottom
        # Determinando a velocidade do míssel (velocidade vertical constante para baixo).
        self.speedy = 13
    # Atualiza a posição do projétil.
    def update(self):
        self.rect.y += self.speedy
        # Se o míssel passar da linha do chão, morre.
        if self.rect.bottom > HEIGHT - GROUND_HEIGHT:
            self.kill()

