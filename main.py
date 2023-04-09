import requests
import pygame
import os
from pydub import AudioSegment

def play_radio(radio_url):
    r = requests.get(radio_url, stream=True)
    with open('temp.mp3', 'wb') as f:
        for block in r.iter_content(1024):
            f.write(block)

    audio = AudioSegment.from_mp3('temp.mp3')
    audio.export('temp.wav', format='wav')

    pygame.mixer.init()
    temp_wav_path = os.path.abspath('temp.wav')
    if os.path.exists(temp_wav_path):
        pygame.mixer.music.load(temp_wav_path)
        pygame.mixer.music.play()
    else:
        print("File not found: ", temp_wav_path)

play_radio("http://stream.radioreklama.bg:80/radio1rock128.mp3")

