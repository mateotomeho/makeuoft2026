import serial
import time
import pygame

#ser = serial.Serial('COM3', 9600)
ser = serial.Serial('/dev/cu.usbmodem1301', 9600) # for mac
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

title_screen = pygame.transform.scale(title_screen, (screen_width, screen_height))
begin_screen = pygame.transform.scale(begin_screen, (screen_width, screen_height))
track1_wait_00 = pygame.transform.scale(track1_wait_00, (screen_width, screen_height))
track1_b1press_00 = pygame.transform.scale(track1_b1press_00, (screen_width, screen_height))
track1_b2press_00 = pygame.transform.scale(track1_b2press_00, (screen_width, screen_height))
track1_correct_01 = pygame.transform.scale(track1_correct_01, (screen_width, screen_height))
track1_correct_10 = pygame.transform.scale(track1_correct_10, (screen_width, screen_height))
track1_incorrect_00 = pygame.transform.scale(track1_incorrect_00, (screen_width, screen_height))


track2_wait_00 = pygame.image.load('track2_wait_00.png')
track2_wait_10 = pygame.image.load('track2_wait_10.png')
track2_wait_01 = pygame.image.load('track2_wait_01.png')


track2_b1press_00 = pygame.image.load('track2_b1press_00.png')
track2_b1press_01 = pygame.image.load('track2_b1press_01.png')
track2_b1press_10 = pygame.image.load('track2_b1press_10.png')
track2_b2press_00 = pygame.image.load('track2_b2press_00.png')
track2_b2press_01 = pygame.image.load('track2_b2press_01.png')
track2_b2press_10 = pygame.image.load('track2_b2press_10.png')


track2_correct_01 = pygame.image.load('track2_correct_01.png')
track2_correct_10 = pygame.image.load('track2_correct_10.png')
track2_correct_11 = pygame.image.load('track2_correct_11.png')
track2_correct_20 = pygame.image.load('track2_correct_20.png')
track2_correct_02 = pygame.image.load('track2_correct_02.png')

track2_incorrect_00 = pygame.image.load('track2_incorrect_00.png')
track2_incorrect_01 = pygame.image.load('track2_incorrect_01.png')
track2_incorrect_10 = pygame.image.load('track2_incorrect_10.png')


track3_wait_00 = pygame.image.load('track3_wait_00.png')
track3_wait_01 = pygame.image.load('track3_wait_01.png')
track3_wait_02 = pygame.image.load('track3_wait_02.png')
track3_wait_10 = pygame.image.load('track3_wait_10.png')
track3_wait_11 = pygame.image.load('track3_wait_11.png')
track3_wait_20 = pygame.image.load('track3_wait_20.png')



current_image = None 
current_image = title_screen

end_game = False


# GAME VARIABLES

# Players
player1 = "Player 1"
player2 = "Player 2"

# Tracks (mp3 files)
track1 = "Track 1"
track2 = "Track 2" 
track3 = "Track 3"

# Track booleans 
track1_is_done = False
track2_is_done = False
track3_is_done = False

# Game booleans
start_game = False
end_game = False

# Points
pointPlayer1 = 0
pointPlayer2 = 0
score = "00"

#Buzzed Logic
def buzzed():
    return player1

#Response for Voice Recorder Logic
def response_audio():
    return False

#Show Image Logic
def show_image(image):
    return  

#Update the score
def check_score():
    global score
    if pointPlayer1 == 0 and pointPlayer2 == 0:
        score = "00"
    elif pointPlayer1 == 1 and pointPlayer2 == 0:
        score = "10"
    elif pointPlayer1 == 0 and pointPlayer2 == 1:
        score = "01"
    elif pointPlayer1 == 1 and pointPlayer2 == 1:
        score = "11"
    elif pointPlayer1 == 2 and pointPlayer2 == 0:
        score = "20"
    elif pointPlayer1 == 0 and pointPlayer2 == 2:        
        score = "02"
    elif pointPlayer1 == 2 and pointPlayer2 == 1:
        score = "21"
    elif pointPlayer1 == 1 and pointPlayer2 == 2:
        score = "12"
    elif pointPlayer1 == 3 and pointPlayer2 == 0:
        score = "30"
    elif pointPlayer1 == 0 and pointPlayer2 == 3:
        score = "03"


def image_buzzed(image):
    global current_image
    global score

    #CHECK TRACK 1 IMAGE
    if image == "p1song1":
        current_image = track1_b1press_00
        while current_image == track1_b1press_00:             
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
            current_image = None
            time.sleep(3)


    if image == "p2song1":
        current_image = track1_b2press_00
        while current_image == track1_b2press_00:           
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
            current_image = None
            time.sleep(3)


    if image == "track1_correct_10":
        current_image = track1_correct_10
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS 
        while current_image == track1_correct_10: 
            line = ser.readline().decode().strip()
            b1, b2 = map(int, line.split(",")) # convert both inputs to int

            if b1 == 0 or b2 == 0: # a buzzer was pressed
                if score == "00":
                    current_image = track2_wait_00
                elif score == "10":
                    current_image = track2_wait_10
                elif score == "01":
                    current_image = track2_wait_01
            
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS

    if image == "track1_correct_01":
        current_image = track1_correct_01
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS 
        while current_image == track1_correct_01: 
            line = ser.readline().decode().strip()
            b1, b2 = map(int, line.split(",")) # convert both inputs to int

            if b1 == 0 or b2 == 0: # a buzzer was pressed
                if score == "00":
                    current_image = track2_wait_00
                elif score == "10":
                    current_image = track2_wait_10
                elif score == "01":
                    current_image = track2_wait_01
            
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
    
    if image == "track1_incorrect_00":
        current_image = track1_incorrect_00
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS 
        while current_image == track1_incorrect_00: 
            line = ser.readline().decode().strip()
            b1, b2 = map(int, line.split(",")) # convert both inputs to int

            if b1 == 0 or b2 == 0: # a buzzer was pressed
                if score == "00":
                    current_image = track2_wait_00
                elif score == "10":
                    current_image = track2_wait_10
                elif score == "01":
                    current_image = track2_wait_01
            
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS

     #CHECK TRACK 2 IMAGE
    if image == "p1song2":
        current_image = globals()[f"track2_b1press_{score}"]
        while current_image == globals()[f"track2_b1press_{score}"]: 
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
            current_image = None
            time.sleep(3)

    if image == "p2song2":
        current_image = globals()[f"track2_b2press_{score}"]
        while current_image == globals()[f"track2_b2press_{score}"]:             
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
            current_image = None
            time.sleep(3)

    if image == f"track2_correct_{score}":
        current_image = globals()[f"track2_correct_{score}"]
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS
        while current_image == globals()[f"track2_correct_{score}"]: 
            line = ser.readline().decode().strip()
            b1, b2 = map(int, line.split(",")) # convert both inputs to int

            if b1 == 0 or b2 == 0: # a buzzer was pressed
                current_image = globals()[f"track3_wait_{score}"]
            
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
    
    if image == f"track2_incorrect_{score}":
        current_image = globals()[f"track2_incorrect_{score}"]
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS
        while current_image == globals()[f"track2_incorrect_{score}"]: 
            line = ser.readline().decode().strip()
            b1, b2 = map(int, line.split(",")) # convert both inputs to int

            if b1 == 0 or b2 == 0: # a buzzer was pressed
                current_image = globals()[f"track3_wait_{score}"]
            
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS


# MAIN GAME LOOP
#Rules:
#Start the game, show song screen until a buzzer is pressed
#Check who buzzed first
#Check if response is correct (response_audio() == True)
#If correct, point for player, if wrong, no points
#Move to next track, repeat until all tracks are done


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

    #CHECK TRACK 1
    while track1_is_done == False:
        if buzzed() == player1:
            image_buzzed("p1song1")
            if response_audio() == True:
                pointPlayer1 += 1
                track1_is_done = True
                check_score()
                image_buzzed("track1_correct_10")
            else:
                track1_is_done = True
                check_score()
                image_buzzed("track1_incorrect_00")
        elif buzzed() == player2:
            image_buzzed("p2song1")
            if response_audio() == True:
                pointPlayer2 += 1
                track1_is_done = True
                check_score()
                image_buzzed("track1_correct_01")
            else:
                track1_is_done = True
                check_score()
                image_buzzed("track1_incorrect_00")

    #WAIT FOR TRACK 2 TRANSITION
    #CHECK TRACK 2
    while track2_is_done == False:
        if buzzed() == player1:
            image_buzzed("p1song2")
            if response_audio() == True:
                pointPlayer1 += 1
                track2_is_done = True
                check_score()
                image_buzzed(f"track2_correct_{score}")
            else:
                track2_is_done = True
                check_score()
                image_buzzed(f"track2_incorrect_{score}")
        elif buzzed() == player2:
            image_buzzed("p2song2")
            if response_audio() == True:
                pointPlayer2 += 1
                track2_is_done = True
                check_score()
                image_buzzed(f"track2_correct_{score}")
            else:
                track2_is_done = True
                check_score()
                image_buzzed(f"track2_incorrect_{score}")

    #CHECK TRACK 3
    while track3_is_done == False:
        if buzzed() == player1:
            image_buzzed("p1song3")
            if response_audio() == True:
                pointPlayer1 += 1
                track3_is_done = True
                check_score()
            else:
                track3_is_done = True
                check_score()
        elif buzzed() == player2:
            image_buzzed("p2song3")
            if response_audio() == True:
                pointPlayer2 += 1
                track3_is_done = True
                check_score()
            else:
                track3_is_done = True   
                check_score()

    end_game = True

# pygame.quit()


# while end_game == False:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             end_game = True

#     while current_image == title_screen: # first image transition: title screen 
#         line = ser.readline().decode().strip()
#         b1, b2 = map(int, line.split(",")) # convert both inputs to int

#         if b1 == 0 or b2 == 0: # a buzzer was pressed
#             current_image = begin_screen
        
#         screen.blit(current_image, (0, 0))  # draw image
#         pygame.display.flip()  # update screen
#         clock.tick(60)  # limit FPS

#     while current_image == begin_screen: # second image transition: begin screen
#         line = ser.readline().decode().strip()
#         b1, b2 = map(int, line.split(",")) # convert both inputs to int

#         if b1 == 0 or b2 == 0: # a buzzer was pressed
#             current_image = track_wait_00
        
#         screen.blit(current_image, (0, 0))  # draw image
#         pygame.display.flip()  # update screen
#         clock.tick(60)  # limit FPS

# pygame.quit()


'''
# second image transition: begin screen
    if current_image == begin_screen and (b1 == 0 or b2 == 0):
        current_image = firstsong
'''
