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

# pygame.init(): Esta linha inicializa a biblioteca Pygame. É importante chamar esta função antes de usar qualquer outra função em Pygame.

# pygame.mixer.music.load("tovaritch_mode_avion.mp3"): Esta linha carrega o arquivo de música "tovaritch_mode_avion.mp3" na memória. A função "load()" da classe "pygame.mixer.music" é usada para carregar o arquivo de música.

# pygame.mixer.music.play(): Esta linha inicia a reprodução da música carregada anteriormente. A função "play()" da classe "pygame.mixer.music" é usada para começar a tocar a música.








