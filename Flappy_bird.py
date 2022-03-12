import pygame
import neat
import time
import os
import BirdClass
import PipeClass
import BaseClass
pygame.font.init()

WIN_WIDTH = 500
WIN_HEIGHT = 800
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans",50)

def draw_window(win, bird, pipes, base, score): 
    win.blit(BG_IMG,(0,0))
    
    for pipe in pipes:
        pipe.draw(win)
    text = STAT_FONT.render("Score:"+str(score),1,(255,255,255))
    win.blit(text, (WIN_WIDTH-10-text.get_width(), 10))
    base.draw(win)
    bird.draw(win)
    pygame.display.update()


def main():    
    bird = BirdClass.Bird(230,350)
    base = BaseClass.Base(730)
    pipes = [PipeClass.Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        add_pipe = False
        rem = []
        #bird.move()   
        for pipe in pipes:
            if pipe.collide(bird):
                pass
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            pipe.move()
        if add_pipe:
            score+=1
            pipes.append(PipeClass.Pipe(700))
        
        for r in rem:
            pipes.remove(r)

        if bird.y + bird.img.get_height() >= 730:
            pass

        base.move()                        
        draw_window(win, bird, pipes, base, score)   

    pygame.quit()
    quit()

main()
