# Programa que abre e reproduz o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('Exercicio021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
