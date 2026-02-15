import serial
import time
import pygame
import requests

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

audio_files = {
    "track1": "song1_clip.mp3",
    "track2": "song2_clip.mp3",
    "track3": "song3_clip.mp3"
}

good_answers = { # will be lowercase by default
    "track1": ["will always", "love you", "whitney", "houston", "wit", "whit", "hue"],
    "track2": ["perfect", "ed", "sheer", "sheeran", "shear"],
    "track3": ["thousand", "1000", "years", "perri", "christina", "cristina", "perry", "parry", "perrier"]
}
# Load images

smile_screen = pygame.image.load('camera_intro.png')
smile_screen = pygame.transform.scale(smile_screen, (screen_width, screen_height))
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

def take_picture():
    url = "http://100.66.146.90/capture"

    # Download image
    response = requests.get(url, timeout=10)
    with open("esp32_image.jpg", "wb") as f:
        f.write(response.content)

    print("Image saved as esp32_image.jpg")

    # Show fullscreen
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    img = pygame.image.load("esp32_image.jpg")
    img = pygame.transform.scale(img, screen.get_size())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        screen.blit(img, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



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

    #CHECK TRACK 3 IMAGE
    if image == "p1song3":
        current_image = globals()[f"track3_b1press_{score}"]
        while current_image == globals()[f"track3_b1press_{score}"]: 
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
            current_image = None
            time.sleep(3)
    if image == "p2song3":
        current_image = globals()[f"track3_b2press_{score}"]
        while current_image == globals()[f"track3_b2press_{score}"]: 
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS
            current_image = None
            time.sleep(3)
    
    if image == f"track3_correct_{score}":
        current_image = globals()[f"track3_correct_{score}"]
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS
        while current_image == globals()[f"track3_correct_{score}"]: 
            line = ser.readline().decode().strip()
            b1, b2 = map(int, line.split(",")) # convert both inputs to int

            if b1 == 0 or b2 == 0: # a buzzer was pressed
                current_image = globals()[f"end_{score}"]
            
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS

    if image == f"track3_incorrect_{score}":
        current_image = globals()[f"track3_incorrect_{score}"]
        screen.blit(current_image, (0, 0))  # draw image
        pygame.display.flip()  # update screen
        clock.tick(60)  # limit FPS
        while current_image == globals()[f"track3_incorrect_{score}"]: 
            line = ser.readline().decode().strip()
            b1, b2 = map(int, line.split(",")) # convert both inputs to int

            if b1 == 0 or b2 == 0: # a buzzer was pressed
                current_image = globals()[f"end_{score}"]
            
            screen.blit(current_image, (0, 0))  # draw image
            pygame.display.flip()  # update screen
            clock.tick(60)  # limit FPS


#IMPORTANT
#User have 3 sec the see who buzzed first & record answer
#Then 10 sec to play the voice recording of their answer

import os
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
from google import genai

#Response for Voice Recorder Logic
def response_audio():
    #Record audio from microphone, save as .mp3, and transcribe with Gemini API
    SECONDS = 5
    SAMPLE_RATE = 44100
    WAV_PATH = "recorded_5s.wav"
    MP3_PATH = "recorded_5s.mp3"

    MODEL = "models/gemini-3-flash-preview" 

    #Record Audio from Microphone
    print(f"Recording for {SECONDS} seconds")
    audio = sd.rec(int(SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sd.wait()
    print("Recording done")

    # Save WAV first 
    sf.write(WAV_PATH, audio, SAMPLE_RATE)

    #Convert .wav to .mp3 using pydub (requires ffmpeg)
    print("Converting to MP3")
    try:
        AudioSegment.from_wav(WAV_PATH).export(MP3_PATH, format="mp3", bitrate="192k")
    except Exception as e:
        raise RuntimeError(
            "MP3 conversion failed. Make sure ffmpeg is installed (brew install ffmpeg on Mac).\n"
            f"Original error: {e}"
        )

    print(f"Saved MP3: {MP3_PATH}")

    # #Speech to text recognition with Gemini API
    # api_key = os.environ.get("GEMINI_API_KEY")
    # if not api_key:
    #     raise RuntimeError("Error run: export GEMINI_API_KEY='YOUR_KEY'")

    # client = genai.Client(api_key=api_key)

    # uploaded = client.files.upload(file=MP3_PATH)

    # response = client.models.generate_content(
    #     model=MODEL,
    #     contents=[
    #         "Transcribe this audio exactly. Output only the transcript.",
    #         uploaded,
    #     ],
    # )

    # print("Transcript:")
    # print(response.text)

    #response = response.text.lower().strip() # normalize transcript for comparison

    #To test without Gemini API
    response = good_answers["track1"] + good_answers["track2"] + good_answers["track3"] # combine all good answers for easier checking

    #Check if the response is correct using answer
    if track1_is_done == False:
        for ans in good_answers["track1"]:
            #Check if the response matches any of the correct answers
            if ans in response:
                return True
        return False
    
    elif track2_is_done == False:
        for ans in good_answers["track2"]:
            #Check if the response matches any of the correct answers
            if ans in response:
                return True
        return False
    
    elif track3_is_done == False:
        for ans in good_answers["track3"]:
            #Check if the response matches any of the correct answers
            if ans in response:
                return True
        return False
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
        pygame.mixer.init()
        pygame.mixer.music.load(audio_files["track1"])
        pygame.mixer.music.play()
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
        pygame.mixer.init()
        pygame.mixer.music.load(audio_files["track2"])
        pygame.mixer.music.play()
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

    #WAIT FOR TRACK 3 TRANSITION
    #CHECK TRACK 3
    while track3_is_done == False:
        pygame.mixer.init()
        pygame.mixer.music.load(audio_files["track3"])
        pygame.mixer.music.play()
        if buzzed() == player1:
            image_buzzed("p1song3")
            if response_audio() == True:
                pointPlayer1 += 1
                track3_is_done = True
                check_score()
                image_buzzed(f"track3_correct_{score}")
            else:
                track3_is_done = True
                check_score()
                image_buzzed(f"track3_incorrect_{score}")
        elif buzzed() == player2:
            image_buzzed("p2song3")
            if response_audio() == True:
                pointPlayer2 += 1
                track3_is_done = True
                check_score()
                image_buzzed(f"track3_correct_{score}")
            else:
                track3_is_done = True   
                check_score()
                image_buzzed(f"track3_incorrect_{score}")

    time.sleep(10) # wait for 5 seconds on end screen before quitting
    end_game = True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False

    current_image = smile_screen
    screen.blit(current_image, (0, 0))  # draw image
    pygame.display.flip()  # update screen
    clock.tick(60)  # limit FPS

pygame.quit()

#Take the picture at the end of the game for fun & memories
take_picture()

