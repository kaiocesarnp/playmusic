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
                #  O init() inicializa vários módulos do Pygame, como o som, gráficos, fontes, etc., e configura o ambiente de execução do Pygame para que ele possa ser executado corretamente.
                # O método init() é uma etapa crucial para garantir que a biblioteca Pygame esteja pronta para ser usada em seu programa. 
                    # Se você não chamar o init(), as funções Pygame não serão carregadas corretamente e o seu programa provavelmente apresentará erros.


# pygame.mixer.music.load("tovaritch_mode_avion.mp3"): Esta linha carrega o arquivo de música "tovaritch_mode_avion.mp3" na memória. A função "load()" da classe "pygame.mixer.music" é usada para carregar o arquivo de música.
                            # pygame.mixer.music é um módulo da biblioteca Pygame que fornece funcionalidades para reproduzir música e sons em seu jogo ou aplicativo.
                            # pygame.mixer.music é uma subclasse do módulo pygame.mixer, que é usado para trabalhar com sons em geral, incluindo efeitos sonoros.

# pygame.mixer.music.play(): Esta linha inicia a reprodução da música carregada anteriormente. A função "play()" da classe "pygame.mixer.music" é usada para começar a tocar a música.

# while pygame.mixer.music.get_busy(): Esta linha cria um loop que espera a música terminar de tocar. A função "get_busy()" da classe "pygame.mixer.music" retorna True enquanto a música está tocando, então o loop continua até que essa função retorne False.
                                        # Essa linha cria um loop que espera a música terminar de tocar. O while é um comando em Python que permite 
                                            # que um bloco de código seja repetido enquanto uma condição for verdadeira. Nesse caso, a condição é 
                                            # pygame.mixer.music.get_busy(), que verifica se a música ainda está tocando.
                                        # Enquanto a música estiver sendo reproduzida, a função get_busy() retornará True, o que manterá o loop ativo.
                                            #  Quando a música terminar de tocar, a função get_busy() retornará False, 
                                            # encerrando o loop e continuando a execução do programa.

# pygame.time.Clock().tick(10): Essa linha de código define a velocidade de atualização da tela e controla a taxa de quadros do jogo. 
                                # Esta linha pausa o loop por 10 milissegundos a cada iteração, evitando que o loop use muita CPU. A função "pygame.time.Clock().tick()" é usada para definir a taxa de quadros do jogo.
                                # O pygame.time.Clock() cria um objeto que pode ser usado para controlar o tempo em seu jogo, enquanto o método 
                                    # .tick(10) especifica a taxa de atualização da tela em quadros por segundo (FPS). Nesse caso, a taxa de 
                                    # quadros é definida como 10, o que significa que a tela será atualizada 10 vezes por segundo.
                                # Essa linha de código é importante para evitar que o jogo execute muito rapidamente ou muito devagar. Se o 
                                    # jogo for executado muito rapidamente, ele pode ser difícil de jogar ou até mesmo causar problemas de 
                                    # desempenho no computador. Se o jogo for executado muito devagar, a jogabilidade pode ser afetada negativamente.


# pygame.quit(): Esta linha encerra a biblioteca Pygame, liberando recursos do sistema. É importante chamar essa função no final do seu programa.







