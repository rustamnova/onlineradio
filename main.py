import os
import pygame
import subprocess
import time

def play_radio(url):
    # удаляем временные файлы, если они есть
    if os.path.isfile('temp.mp3'):
        os.remove('temp.mp3')
    if os.path.isfile('temp.wav'):
        os.remove('temp.wav')

    # загружаем поток и сохраняем его в mp3 файл
    subprocess.call(['ffmpeg', '-i', url, '-f', 'mp3', '-ab', '128k', '-vn', '-y', 'temp.mp3'])

    # конвертируем mp3 файл в wav формат
    subprocess.call(['ffmpeg', '-i', os.path.abspath('temp.mp3'), '-ar', '44100', '-ac', '2', '-f', 'wav', '-y', 'temp.wav'])

    # инициализируем Pygame
    pygame.init()

    # загружаем и проигрываем файл в wav формате
    try:
        pygame.mixer.music.load(os.path.abspath('temp.wav'))
        pygame.mixer.music.play()
        # ждем, пока поток не закончится
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except pygame.error:
        print('Ошибка проигрывания музыки')

    # очищаем Pygame и удаляем временные файлы
    pygame.mixer.quit()
    pygame.quit()
    if os.path.isfile('temp.mp3'):
        os.remove('temp.mp3')
    if os.path.isfile('temp.wav'):
        os.remove('temp.wav')

# тестируем функцию на радио-потоке
play_radio("http://stream.radioreklama.bg:80/radio1rock128.mp3")
