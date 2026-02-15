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

audio_files = {
    "track1": "song1_clip.mp3",
    "track2": "song2_clip.mp3",
    "track3": "song3_clip.mp3"
}

good_answers = { # will be lowercase by default
    "track1": ["will always", "i'll always", "love you", "whitney", "houston", "wit", "whit", "hue"],
    "track2": ["perfect", "ed", "sheer", "sheeran", "shear"],
    "track3": ["love story", "story", "tailor", "taylor", "swift"]
}

# Load images
title_screen = pygame.image.load('title_screen.png')
begin_screen = pygame.image.load('begin_screen.png')

track1_wait_00 = pygame.image.load('track1_wait_00.png')
track1_b1press_00 = pygame.image.load('track1_b1press_00.png')
track1_b2press_00 = pygame.image.load('track1_b2press_00.png')
track1_correct_01 = pygame.image.load('track1_correct_01.png')
track1_correct_10 = pygame.image.load('track1_correct_10.png')
track1_incorrect_00 = pygame.image.load('track1_incorrect_00.png')

track2_wait_00 = pygame.image.load('track2_wait_00.png')
track2_wait_01 = pygame.image.load('track2_wait_01.png')
track2_wait_10 = pygame.image.load('track2_wait_10.png')
track2_b1press_00 = pygame.image.load('track2_b1press_00.png')
track2_b1press_01 = pygame.image.load('track2_b1press_01.png')
track2_b1press_10 = pygame.image.load('track2_b1press_10.png')
track2_b2press_00 = pygame.image.load('track2_b2press_00.png')
track2_b2press_01 = pygame.image.load('track2_b2press_01.png')
track2_b2press_10 = pygame.image.load('track2_b2press_10.png')
track2_correct_01 = pygame.image.load('track2_correct_01.png')
track2_correct_10 = pygame.image.load('track2_correct_10.png')
track2_correct_11 = pygame.image.load('track2_correct_11.png')
track2_correct_02 = pygame.image.load('track2_correct_02.png')
track2_correct_20 = pygame.image.load('track2_correct_20.png')
track2_incorrect_00 = pygame.image.load('track2_incorrect_00.png')
track2_incorrect_01 = pygame.image.load('track2_incorrect_01.png')
track2_incorrect_10 = pygame.image.load('track2_incorrect_10.png')

track3_wait_00 = pygame.image.load('track3_wait_00.png')
track3_wait_01 = pygame.image.load('track3_wait_01.png')
track3_wait_10 = pygame.image.load('track3_wait_10.png')
track3_wait_11 = pygame.image.load('track3_wait_11.png')
track3_wait_02 = pygame.image.load('track3_wait_02.png')
track3_wait_20 = pygame.image.load('track3_wait_20.png')
track3_b1press_00 = pygame.image.load('track3_b1press_00.png')
track3_b1press_01 = pygame.image.load('track3_b1press_01.png')
track3_b1press_10 = pygame.image.load('track3_b1press_10.png')
track3_b1press_11 = pygame.image.load('track3_b1press_11.png')
track3_b1press_02 = pygame.image.load('track3_b1press_02.png')
track3_b1press_20 = pygame.image.load('track3_b1press_20.png')
track3_b2press_00 = pygame.image.load('track3_b2press_00.png')
track3_b2press_01 = pygame.image.load('track3_b2press_01.png')
track3_b2press_10 = pygame.image.load('track3_b2press_10.png')
track3_b2press_11 = pygame.image.load('track3_b2press_11.png')
track3_b2press_02 = pygame.image.load('track3_b2press_02.png')
track3_b2press_20 = pygame.image.load('track3_b2press_20.png')
track3_correct_01 = pygame.image.load('track3_correct_01.png')
track3_correct_10 = pygame.image.load('track3_correct_10.png')
track3_correct_11 = pygame.image.load('track3_correct_11.png')
track3_correct_02 = pygame.image.load('track3_correct_02.png')
track3_correct_20 = pygame.image.load('track3_correct_20.png')
track3_correct_03 = pygame.image.load('track3_correct_03.png')
track3_correct_30 = pygame.image.load('track3_correct_30.png')
track3_correct_21 = pygame.image.load('track3_correct_21.png')
track3_correct_12 = pygame.image.load('track3_correct_12.png')
track3_incorrect_00 = pygame.image.load('track3_incorrect_00.png')
track3_incorrect_01 = pygame.image.load('track3_incorrect_01.png')
track3_incorrect_10 = pygame.image.load('track3_incorrect_10.png')
track3_incorrect_11 = pygame.image.load('track3_incorrect_11.png')
track3_incorrect_02 = pygame.image.load('track3_incorrect_02.png')
track3_incorrect_20 = pygame.image.load('track3_incorrect_20.png')

end_00 = pygame.image.load('end_00.png')
end_01 = pygame.image.load('end_01.png')
end_02 = pygame.image.load('end_02.png')
end_03 = pygame.image.load('end_03.png')
end_10 = pygame.image.load('end_10.png')
end_11 = pygame.image.load('end_11.png')
end_12 = pygame.image.load('end_12.png')
end_20 = pygame.image.load('end_20.png')
end_21 = pygame.image.load('end_21.png')
end_30 = pygame.image.load('end_30.png')

title_screen = pygame.transform.scale(title_screen, (screen_width, screen_height))
begin_screen = pygame.transform.scale(begin_screen, (screen_width, screen_height))

track1_wait_00 = pygame.transform.scale(track1_wait_00, (screen_width, screen_height))
track1_b1press_00 = pygame.transform.scale(track1_b1press_00, (screen_width, screen_height))
track1_b2press_00 = pygame.transform.scale(track1_b2press_00, (screen_width, screen_height))
track1_correct_01 = pygame.transform.scale(track1_correct_01, (screen_width, screen_height))
track1_correct_10 = pygame.transform.scale(track1_correct_10, (screen_width, screen_height))
track1_incorrect_00 = pygame.transform.scale(track1_incorrect_00, (screen_width, screen_height))

track2_wait_00 = pygame.transform.scale(track2_wait_00, (screen_width, screen_height))
track2_wait_01 = pygame.transform.scale(track2_wait_01, (screen_width, screen_height))
track2_wait_10 = pygame.transform.scale(track2_wait_10, (screen_width, screen_height))
track2_b1press_00 = pygame.transform.scale(track2_b1press_00, (screen_width, screen_height))
track2_b1press_01 = pygame.transform.scale(track2_b1press_01, (screen_width, screen_height))
track2_b1press_10 = pygame.transform.scale(track2_b1press_10, (screen_width, screen_height))
track2_b2press_00 = pygame.transform.scale(track2_b2press_00, (screen_width, screen_height))
track2_b2press_01 = pygame.transform.scale(track2_b2press_01, (screen_width, screen_height))
track2_b2press_10 = pygame.transform.scale(track2_b2press_10, (screen_width, screen_height))
track2_correct_01 = pygame.transform.scale(track2_correct_01, (screen_width, screen_height))
track2_correct_10 = pygame.transform.scale(track2_correct_10, (screen_width, screen_height))
track2_correct_11 = pygame.transform.scale(track2_correct_11, (screen_width, screen_height))
track2_correct_02 = pygame.transform.scale(track2_correct_02, (screen_width, screen_height))
track2_correct_20 = pygame.transform.scale(track2_correct_20, (screen_width, screen_height))
track2_incorrect_00 = pygame.transform.scale(track2_incorrect_00, (screen_width, screen_height))
track2_incorrect_01 = pygame.transform.scale(track2_incorrect_01, (screen_width, screen_height))
track2_incorrect_10 = pygame.transform.scale(track2_incorrect_10, (screen_width, screen_height))

track3_wait_00 = pygame.transform.scale(track3_wait_00, (screen_width, screen_height))
track3_wait_01 = pygame.transform.scale(track3_wait_01, (screen_width, screen_height))
track3_wait_10 = pygame.transform.scale(track3_wait_10, (screen_width, screen_height))
track3_wait_11 = pygame.transform.scale(track3_wait_11, (screen_width, screen_height))
track3_wait_02 = pygame.transform.scale(track3_wait_02, (screen_width, screen_height))
track3_wait_20 = pygame.transform.scale(track3_wait_20, (screen_width, screen_height))
track3_b1press_00 = pygame.transform.scale(track3_b1press_00, (screen_width, screen_height))
track3_b1press_01 = pygame.transform.scale(track3_b1press_01, (screen_width, screen_height))
track3_b1press_10 = pygame.transform.scale(track3_b1press_10, (screen_width, screen_height))
track3_b1press_11 = pygame.transform.scale(track3_b1press_11, (screen_width, screen_height))
track3_b1press_02 = pygame.transform.scale(track3_b1press_02, (screen_width, screen_height))
track3_b1press_20 = pygame.transform.scale(track3_b1press_20, (screen_width, screen_height))
track3_b2press_00 = pygame.transform.scale(track3_b2press_00, (screen_width, screen_height))
track3_b2press_01 = pygame.transform.scale(track3_b2press_01, (screen_width, screen_height))
track3_b2press_10 = pygame.transform.scale(track3_b2press_10, (screen_width, screen_height))
track3_b2press_11 = pygame.transform.scale(track3_b2press_11, (screen_width, screen_height))
track3_b2press_02 = pygame.transform.scale(track3_b2press_02, (screen_width, screen_height))
track3_b2press_20 = pygame.transform.scale(track3_b2press_20, (screen_width, screen_height))
track3_correct_01 = pygame.transform.scale(track3_correct_01, (screen_width, screen_height))
track3_correct_10 = pygame.transform.scale(track3_correct_10, (screen_width, screen_height))
track3_correct_11 = pygame.transform.scale(track3_correct_11, (screen_width, screen_height))
track3_correct_02 = pygame.transform.scale(track3_correct_02, (screen_width, screen_height))
track3_correct_20 = pygame.transform.scale(track3_correct_20, (screen_width, screen_height))
track3_correct_03 = pygame.transform.scale(track3_correct_03, (screen_width, screen_height))
track3_correct_30 = pygame.transform.scale(track3_correct_30, (screen_width, screen_height))
track3_correct_21 = pygame.transform.scale(track3_correct_21, (screen_width, screen_height))
track3_correct_12 = pygame.transform.scale(track3_correct_12, (screen_width, screen_height))
track3_incorrect_00 = pygame.transform.scale(track3_incorrect_00, (screen_width, screen_height))
track3_incorrect_01 = pygame.transform.scale(track3_incorrect_01, (screen_width, screen_height))
track3_incorrect_02 = pygame.transform.scale(track3_incorrect_02, (screen_width, screen_height))
track3_incorrect_10 = pygame.transform.scale(track3_incorrect_10, (screen_width, screen_height))
track3_incorrect_11 = pygame.transform.scale(track3_incorrect_11, (screen_width, screen_height))
track3_incorrect_20 = pygame.transform.scale(track3_incorrect_20, (screen_width, screen_height))

end_00 = pygame.transform.scale(end_00, (screen_width, screen_height))
end_01 = pygame.transform.scale(end_01, (screen_width, screen_height))
end_02 = pygame.transform.scale(end_02, (screen_width, screen_height))
end_03 = pygame.transform.scale(end_03, (screen_width, screen_height))
end_10 = pygame.transform.scale(end_10, (screen_width, screen_height))
end_11 = pygame.transform.scale(end_11, (screen_width, screen_height))
end_12 = pygame.transform.scale(end_12, (screen_width, screen_height))
end_20 = pygame.transform.scale(end_20, (screen_width, screen_height))
end_21 = pygame.transform.scale(end_21, (screen_width, screen_height))
end_30 = pygame.transform.scale(end_30, (screen_width, screen_height))

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

