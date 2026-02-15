# #Speech to Text Recognition with Gemini
# import os
# from google import genai

# client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# AUDIO_PATH = "test_audio1.mp3"  

# #Upload the audio file
# uploaded = client.files.upload(file=AUDIO_PATH)

# #Ask Gemini to transcribe it
# response = client.models.generate_content(
#     #model="gemini-2.0-flash",
#     model="models/gemini-3-flash-preview",
#     contents=[
#         "Transcribe this audio exactly. Output only the transcript.",
#         uploaded,
#     ],
# )

# print(response.text)

##############################################################################
#Record audio from microphone, save as .mp3, and transcribe with Gemini API
import os
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
from google import genai

SECONDS = 5
SAMPLE_RATE = 44100
WAV_PATH = "recorded_5s.wav"
MP3_PATH = "recorded_5s.mp3"

#MODEL = "models/gemini-3-flash-preview" 
#MODEL = "models/gemini-2.5-flash"
#MODEL = "models/gemini-2.5-flash-lite"


#CAN'T USE:
#MODEL = "models/gemini-2.0-flash"
#MODEL = "models/gemini-2.5-flash-native-audio-preview-12-2025"
#MODEL = "models/gemini-2.0-flash-lite"
#MODEL = "models/gemini-2.5-pro"
#MODEL = "models/gemini-2.0-flash-001"
#MODEL = "models/gemini-3-pro-preview"

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

#Speech to text recognition with Gemini API
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Error run: export GEMINI_API_KEY='YOUR_KEY'")

client = genai.Client(api_key=api_key)

uploaded = client.files.upload(file=MP3_PATH)

response = client.models.generate_content(
    model=MODEL,
    contents=[
        "Transcribe this audio exactly. Output only the transcript.",
        uploaded,
    ],
)

print("Transcript:")
print(response.text)
