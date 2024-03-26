import pygame


pygame.init()


def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def next_song(music_list, current_index):
    current_index = (current_index + 1) % len(music_list)
    play_music(music_list[current_index])
    return current_index


def prev_song(music_list, current_index):
    current_index = (current_index - 1) % len(music_list)
    play_music(music_list[current_index])
    return current_index


music_files = ['song.mp3', 'miagi.mp3']


current_index = 0


play_music(music_files[current_index])


pygame.display.set_caption("Music Player")
window = pygame.display.set_mode((300, 200))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music(music_files[current_index])
            elif event.key == pygame.K_RIGHT:  
                current_index = next_song(music_files, current_index)
            elif event.key == pygame.K_LEFT:  
                current_index = prev_song(music_files, current_index)
            elif event.key == pygame.K_s:  
                stop_music()


pygame.quit()                        