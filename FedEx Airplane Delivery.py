import pygame
from pygame import*
pygame.init()
import random
import math
import time

white = (255, 255,255)
WINWIDTH = 960
WINHEIGHT = 540
WINRES = (WINWIDTH, WINHEIGHT)
boxicon = pygame.image.load('Box.PNG')
#Boxes
boxesValue = 30
font = pygame.font.Font('freesansbold.ttf', 20)
textY = 510
textX = 850
def show_boxes(x, y):
    score  = font.render(': ' + str(boxesValue),True, (0, 0, 255))
    Window.blit(score, (x, y))


#Set up the Game Window
Window = pygame.display.set_mode((WINRES),pygame.RESIZABLE)
pygame.display.set_caption('FedEx Delivery Run!')
ICON = pygame.image.load('Logo.png')
pygame.display.set_icon(ICON)
bg = pygame.image.load('sky.png')
plane = pygame.image.load('plane.png')
birdpic = pygame.image.load('bird.png')
playerX = 60
playerY = 240
playerY_change = 0
def player(x,y):
    Window.blit(plane, (x, y))
def crash():
    if boxesValue <= 0:
        over = font.render('GAME OVER', True, (255, 0, 0))
        Window.blit(over, (420, 270))
        display.update()
        time.sleep(2)
        pygame.quit()
    
        
randint = random.randint


#Set up the Game Loop
Running = True
while Running:
    Window.fill((0, 0, 0)) 
    Window.blit(bg, (0, 0))
    Window.blit(boxicon, (790, 480))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_change = -0.5
            if event.key == pygame.K_s:
                playerY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                boxesValue -= 1
        
                
    playerY += playerY_change

    if playerY <= -9.5:
        playerY = -9.5
    elif playerY >=351:
        playerY = 351
    player(playerX,playerY)
    show_boxes(textX, textY)
    crash()
        
    pygame.display.update()
