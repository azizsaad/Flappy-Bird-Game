import pygame
import math
import random

pygame.init()

FPS = 32
screen_wid = 289
screen_heig = 511
screen = pygame.display.set_mode((screen_wid, screen_heig))

bird_load = pygame.image.load('bird.png')
bird = pygame.transform.scale(bird_load, (50, 50))

pipe_load = pygame.image.load('pipe.png')
pipe = pygame.transform.scale(pipe_load, (70, 250))



def welcomeScreen():


    screen.fill((255,255,255))
    birdx = int(screen_wid/5)
    birdy = int((screen_heig - bird.get_height())/2)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
            else:
                screen.blit(bird,(birdx,birdy))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def getRandomPipe():

    pipeHeight = 250
    offset = screen_heig/3
    y2 = offset + random.randrange(0, int(screen_heig - 1.2 * offset))
    pipeX = screen_wid + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe



def mainGame():

    birdx = int(screen_wid/5)
    birdy = int(screen_wid/2)

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [
        {'x': screen_wid+200, 'y':newPipe1[0]['y']},
        {'x': screen_wid+200+(screen_wid/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': screen_wid+200, 'y':newPipe1[1]['y']},
        {'x': screen_wid+200+(screen_wid/2), 'y':newPipe2[1]['y']},
    ]
    pipeVelX = -4

    bird_vely = -9
    bird_maxvely = 10
    bird_minvely = -8
    bird_accy = 1

    bird_flapaccv = -8
    bird_flapped = False

    while True:

        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if birdy > 0:
                        bird_vely = bird_flapaccv
                        bird_flapped = True

        crashTest = isCollide(birdx,birdy,upperPipes,lowerPipes)

        if crashTest:
            return

        if bird_vely < bird_maxvely and not bird_flapped:
            bird_vely += bird_accy

        if bird_flapped:
            bird_flapped = False
        birdheight = bird.get_height()

        for upperPipes,lowerPipes in zip(upperPipes,lowerPipes):
            upperPipes['x'] += pipeVelX
            lowerPipes['x'] += pipeVelX

        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        if upperPipes[0]['x'] < -pipe[0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)


        for upperPipes,lowerPipes in zip(upperPipes, lowerPipes):
            screen.blit(pipe[0], (upperPipe['x'], upperPipe['y']))
            screen.blit(pipe[1], (lowerPipe['x'], lowerPipe['y']))

        screen.blit(bird, (birdx, birdy))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(birdx,birdy,upperPipes,lowerPipes):

    if birdy > - 25  or birdy < 0:
        return True

    return False


if __name__ == "__main__":
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    while True:
        mainGame() # This is the main game function
