import serial
import time
import pygame

ser = serial.Serial('COM3', 9600)
time.sleep(2)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # fullscreen
pygame.display.set_caption('Arduino Button Visual')
clock = pygame.time.Clock()

# Load images
title_screen = pygame.image.load('title_screen.png')
begin_screen = pygame.image.load('begin_screen.png')
firstsong = pygame.image.load('pressedagain.png')

current_image = title_screen

end_game = False

while end_game == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game = True

    while current_image == title_screen: # first image transition: title screen 
        line = ser.readline().decode().strip()
        b1, b2 = map(int, line.split(",")) # convert both inputs to int

        if b1 == 0 or b2 == 0: # a buzzer was pressed
            current_image = begin_screen
        
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS

    while current_image == begin_screen: # second image transition: begin screen
        line = ser.readline().decode().strip()
        b1, b2 = map(int, line.split(",")) # convert both inputs to int

        if b1 == 0 or b2 == 0: # a buzzer was pressed
            current_image = firstsong
        
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS

# pygame.quit()


'''
# second image transition: begin screen
    if current_image == begin_screen and (b1 == 0 or b2 == 0):
        current_image = firstsong
'''
