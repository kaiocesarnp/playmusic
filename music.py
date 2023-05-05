import pygame

# Inicializa o pygame
pygame.init()

# Carrega a música
pygame.mixer.music.load("tovaritch_mode_avion.mp3")

#Toca a música
pygame.mixer.music.play()

# Espera até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Encerra o pygame
pygame.quit()

# Explicação linha por linha:

# import pygame: Esta linha importa a biblioteca Pygame, que é uma biblioteca de jogos em Python que também pode ser usada para trabalhar com áudio e vídeo.

# 






