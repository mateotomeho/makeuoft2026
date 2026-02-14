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

# Scale to monitor resolution
screen_width, screen_height = screen.get_size()

# Load images
title_screen = pygame.image.load('title_screen.png')
begin_screen = pygame.image.load('begin_screen.png')
track1_wait_00 = pygame.image.load('track1_wait_00.png')
track1_b1press_00 = pygame.image.load('track1_b1press_00.png')
track1_b2press_00 = pygame.image.load('track1_b2press_00.png')
track1_correct_01 = pygame.image.load('track1_correct_01.png')
track1_correct_10 = pygame.image.load('track1_correct_10.png')
track1_incorrect_00 = pygame.image.load('track1_incorrect_00.png')

'''
track1_b1press_00 = pygame.image.load('track1_b1press_00.png')
track1_b1press_01 = pygame.image.load('track1_b1press_01.png')
track1_b1press_10 = pygame.image.load('track1_b1press_10.png')
track1_b2press_00 = pygame.image.load('track1_b2press_00.png')
track1_b2press_01 = pygame.image.load('track1_b2press_01.png')
track1_b2press_10 = pygame.image.load('track1_b2press_10.png')
'''

title_screen = pygame.transform.scale(title_screen, (screen_width, screen_height))
begin_screen = pygame.transform.scale(begin_screen, (screen_width, screen_height))
track1_wait_00 = pygame.transform.scale(track1_wait_00, (screen_width, screen_height))
track1_b1press_00 = pygame.transform.scale(track1_b1press_00, (screen_width, screen_height))
track1_b2press_00 = pygame.transform.scale(track1_b2press_00, (screen_width, screen_height))
track1_correct_01 = pygame.transform.scale(track1_correct_01, (screen_width, screen_height))
track1_correct_10 = pygame.transform.scale(track1_correct_10, (screen_width, screen_height))
track1_incorrect_00 = pygame.transform.scale(track1_incorrect_00, (screen_width, screen_height))

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
            current_image = track1_wait_00
        
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS

pygame.quit()

'''
# second image transition: begin screen
    if current_image == begin_screen and (b1 == 0 or b2 == 0):
        current_image = firstsong
'''
