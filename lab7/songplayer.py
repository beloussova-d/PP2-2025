import pygame
import time

pygame.init()
screen=pygame.display.set_mode((400,300))
done = False
clock=pygame.time.Clock()
color=(255,0,0)

_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3']
# _currently_playing_song = None

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play()

# def play_next_song():
#     global _songs
#     _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
#     pygame.mixer.music.load(_songs[0])
#     pygame.mixer.music.play()
index1=0
def play_next_song():
    global _songs, index1
    index1=(index1+1)%3
    pygame.mixer.music.load(_songs[index1])
    pygame.mixer.music.play()

def play_prev_song():
    global _songs, index1
    index1=(index1-1)%3
    pygame.mixer.music.load(_songs[index1])
    pygame.mixer.music.play()

is_paused=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type == SONG_END:
            play_next_song()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            play_next_song()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            is_paused=not is_paused
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            play_prev_song()

    if is_paused: pygame.mixer.music.pause()
    else: pygame.mixer.music.unpause()


    pygame.display.flip()
    clock.tick(60)
