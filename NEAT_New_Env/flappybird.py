
import math
import os
from random import randint
from collections import deque
from copy import copy

import pygame
from pygame.locals import *


FPS = 80
WIN_WIDTH = 284 * 2 
WIN_HEIGHT = 512


class Bird(pygame.sprite.Sprite):
    
    WIDTH = HEIGHT = 32
    SINK_SPEED = 0.07
    CLIMB_SPEED = 0.2
    CLIMB_DURATION = 333.3

    def __init__(self, x, y, msec_to_climb, images):
        
        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

    def update(self, delta_frames=1):
       
        if self.msec_to_climb > 0:
            frac_climb_done = 1 - self.msec_to_climb/Bird.CLIMB_DURATION
            self.y -= (Bird.CLIMB_SPEED * frames_to_msec(delta_frames) *
                       (1 - math.cos(frac_climb_done * math.pi)))
            self.msec_to_climb -= frames_to_msec(delta_frames)
        else:
            self.y += Bird.SINK_SPEED * frames_to_msec(delta_frames)

    @property
    def image(self):
       
        if pygame.time.get_ticks() % 500 >= 250:
            return self._img_wingup
        else:
            return self._img_wingdown

    @property
    def mask(self):
        
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown

    @property
    def rect(self):
   
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)


class PipePair(pygame.sprite.Sprite):

    WIDTH = 80
    PIECE_HEIGHT = 32

    def __init__(self, pipe_end_img, pipe_body_img,velocidade):
       
        self.x = float(WIN_WIDTH - 1)
        self.score_counted = 0
        self.velocidade = velocidade
        self.image = pygame.Surface((PipePair.WIDTH, WIN_HEIGHT), SRCALPHA)
        self.image.convert() 
        self.image.fill((0, 0, 0, 0))
        total_pipe_body_pieces = int(
            (WIN_HEIGHT -                  
             3 * Bird.HEIGHT -             
             3 * PipePair.PIECE_HEIGHT) /  
            PipePair.PIECE_HEIGHT         
        )
        self.bottom_pieces = randint(1, total_pipe_body_pieces)#Seleção aleatória dos tubos
        self.top_pieces = total_pipe_body_pieces - self.bottom_pieces

       
        for i in range(1, self.bottom_pieces + 1):
            piece_pos = (0, WIN_HEIGHT - i*PipePair.PIECE_HEIGHT)
            self.image.blit(pipe_body_img, piece_pos)
        bottom_pipe_end_y = WIN_HEIGHT - self.bottom_height_px
        bottom_end_piece_pos = (0, bottom_pipe_end_y - PipePair.PIECE_HEIGHT)
        self.image.blit(pipe_end_img, bottom_end_piece_pos)

        
        for i in range(self.top_pieces):
            self.image.blit(pipe_body_img, (0, i * PipePair.PIECE_HEIGHT))
        top_pipe_end_y = self.top_height_px
        self.image.blit(pipe_end_img, (0, top_pipe_end_y))

        self.yb_final = bottom_pipe_end_y
        self.yt_final = top_pipe_end_y
       
        self.top_pieces += 1
        self.bottom_pieces += 1

        
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def top_height_px(self):
       
        return self.top_pieces * PipePair.PIECE_HEIGHT

    @property
    def bottom_height_px(self):
        
        return self.bottom_pieces * PipePair.PIECE_HEIGHT

    @property
    def visible(self):
        
        return -PipePair.WIDTH < self.x < WIN_WIDTH

    @property
    def rect(self):
        
        return Rect(self.x, 0, PipePair.WIDTH, PipePair.PIECE_HEIGHT)

    def update(self, delta_frames=1):
        
        self.x -= self.velocidade* frames_to_msec(delta_frames)

    def collides_with(self, bird):
    
        return pygame.sprite.collide_mask(self, bird)


class Cena_Flp(object):#Classe para Cenarios Diferentes
    
    def __init__(self,N_Pipes,velocidade):

        self.pipes = []
        self.NP = N_Pipes
        self.images = load_images()
        self.velocidade = velocidade
        self.intervalo = 3000 if(self.velocidade==0.18) else int(605/self.velocidade)
        
    def preenche(self):
        for _ in range(self.NP):
            pp = PipePair(self.images['pipe-end'], self.images['pipe-body'],self.velocidade)
            self.pipes.append(pp)

def load_images():

    def load_image(img_file_name):
        pygame.init()
        display_surface =  pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        file_name = os.path.join('.', 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background.png'),
            'pipe-end': load_image('pipe_end.png'),
            'pipe-body': load_image('pipe_body.png'),
            'bird-wingup': load_image('bird_wing_up.png'),
            'bird-wingdown': load_image('bird_wing_down.png')}


def frames_to_msec(frames, fps=FPS):
    
    return int(1000.0 * frames / fps)


def msec_to_frames(milliseconds, fps=FPS):
   
    return int(fps * milliseconds / 1000.0)
    

def flappyenv(nn,cenario):
  
    score = 0
        
    pygame.init()
    
    display_surface =  pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    
    pygame.display.set_caption('Pygame Flappy Bird')
    
    clock = pygame.time.Clock()
    
    bird = Bird(50, int(WIN_HEIGHT/2 - Bird.HEIGHT/2),2,(cenario.images['bird-wingup'], cenario.images['bird-wingdown']))
    
    frame_clock = 0

    score_font = pygame.font.SysFont(None, 32, bold=True)

    Pipes = deque()

    cont = 0
    
    done = paused = False

    FATOR_Y = 0
    
    while not done and cont <= cenario.NP-1:
        clock.tick(FPS)
        #Adiciona um par de tubos do cenário ao deque de tubos
        if not (paused or frame_clock % msec_to_frames(cenario.intervalo)):
            Pipes.append(copy(cenario.pipes[cont]))
            cont+=1

        #Processamento da Rede Neural e de seus Eventos
        I1 = bird.x - Pipes[0].x#/WIN_WIDTH
        I2 = bird.y - (Pipes[0].yt_final + (Pipes[0].yb_final - Pipes[0].yt_final)/2)#/WIN_WIDTH
        
        FATOR_Y = abs(I2)
        
        INPUT = (I1,I2)
        OUTPUT = nn.activate(INPUT)

        VAL = True if randint(0,100)/100 <= OUTPUT[0] else False
        
        
        if(VAL):
            event = pygame.event.Event(KEYUP,{'key':K_UP})
            pygame.event.post(event)


        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break
            elif e.type == KEYUP and e.key in (K_PAUSE, K_p):
                paused = not paused
            elif (e.type == KEYUP and e.key == K_UP):
                bird.msec_to_climb = Bird.CLIMB_DURATION
            

        if paused:
            continue
            

        #Tratamento das Colisões e outras coisas
        pipe_collision = any(p.collides_with(bird) for p in Pipes)
        if pipe_collision or 0 >= bird.y or bird.y >= WIN_HEIGHT - Bird.HEIGHT:
            done = True

        
        for x in (0, WIN_WIDTH / 2):
            display_surface.blit(cenario.images['background'], (x, 0))

        while not Pipes[0].visible:
            Pipes.popleft()

        for p in Pipes:
            p.update()
            display_surface.blit(p.image, p.rect)

        bird.update()
        display_surface.blit(bird.image, bird.rect)


        #Avaliar Pontuação do Fenótipo
        for p in Pipes:
            if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
                score += 1
                p.score_counted = True

        #Contagem de Scores no Display
        score_surface = score_font.render(str(score), True, (255, 255, 255))
        score_x = WIN_WIDTH/2 - score_surface.get_width()/2
        display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))
        
        
        pygame.display.flip()
        frame_clock += 1

    pygame.quit()
    return frame_clock-(FATOR_Y/10),score
