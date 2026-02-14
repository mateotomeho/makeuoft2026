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

current_image = title_screen

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# first state: title screen 
    line = ser.readline().decode().strip()
    b1, b2 = map(int, line.split(",")) # convert both inputs to int
    if b1 == 0 or b2 == 0: # a buzzer was pressed
        current_image = begin_screen

    screen.blit(current_image, (0, 0))  # draw image
    pygame.display.flip()  # update screen
    clock.tick(60)  # limit FPS

pygame.quit()


'''
    if line == 'BUTTON1' or line == 'BUTTON2': # button 1 pressed
        current_image = img_pressed
    elif line == 'BUTTON2': # button 1 pressed
        current_image = img_normal
'''