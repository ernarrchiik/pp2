import pygame
import os
pygame.init()
pygame.mixer.init()
tracks = []
curent_terack = 0
playing = False

def play_pause():
    global playing
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pausa()
        playing = False
    else:
        pygame.mixer.music.unpause()
        palying = True
def stop():
    global playing
    pygame.mixer.music.stop()
    playing = False
def next_track():
    global curent_terack
    curent_terack = (curent_terack + 1) % len(tracks)
    load_and_play()
def prev_track():
    global curent_terack
    curent_terack = (curent_terack + 1) % len(tracks)
    load_and_play()
def load_and_play():
    global playing
    pygame.mixer.music.load(tracks[curent_terack])
    pygame.mixer.music.play()
    playing = True

pygame.mixer.music.load(tracks[curent_terack])

print("Музыкальный плеер. Управление: [Space] Play/Pause | [S] Stop | [>] Next | [<] Previous")

running = True
while running:
    for event in pygame.event.get():
        if event.type() == pygame.QUIT:
            running = False
        elif event.type() == pygame.KEYDOWN:
            if event.type() == pygame.K_space:
                play_pause()
            elif event.type() == pygame.K_s:
                stop()
            elif event.type() == pygame.K_RIGHT:
                next_track()
            elif event.type() == pygame.K_LEFT:
                prev_track()

pygame.quit()