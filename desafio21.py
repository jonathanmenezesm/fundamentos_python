# Faça um programa python que abra e reproduza o audio de um arquivo mp3

import pygame

# Inicializa o mixer
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load(r'C:\Users\Jonathan\PycharmProjects\PythonExercicios\amorefe.mp3')

# Reproduz o áudio
pygame.mixer.music.play()

# Aguarda até terminar
while pygame.mixer.music.get_busy():
    continue