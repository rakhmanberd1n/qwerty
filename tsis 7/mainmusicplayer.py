import pygame
pygame.mixer.init()


pygame.init()
screen = pygame.display.set_mode((444, 200))
pygame.display.set_caption("AIU MusicPlayer")


music_files = [r"C:\Users\lenovo\Desktop\pp\tsis 7\sounds\Arctic_Monkeys_-_I_Wanna_Be_Yours_47842917.mp3", r"C:\Users\lenovo\Desktop\pp\tsis 7\sounds\Ed_Sheeran_-_Perfect_47828368.mp3",
               r"C:\Users\lenovo\Desktop\pp\tsis 7\sounds\Glass_Animals_-_Heat_Waves_74022754.mp3",r"C:\Users\lenovo\Desktop\pp\tsis 7\sounds\Lord_Huron_-_take_me_back_to_the_night_we_met_75457535.mp3"]
current_music = 0
pygame.mixer.music.load(music_files[current_music])

font = pygame.font.SysFont(None, 48)


play_text = font.render("PLAY", True, (99, 45, 156))
stop_text = font.render("STOP", True, (128, 0, 110))
next_text = font.render("NEXT", True, (0, 120, 128))
prev_text = font.render("PREV", True, (128, 128, 128))


play_rect = play_text.get_rect()
play_rect.center = (60, 95)
stop_rect = stop_text.get_rect()
stop_rect.center = (170, 95)
next_rect = next_text.get_rect()
next_rect.center = (270, 95)
prev_rect = prev_text.get_rect()
prev_rect.center = (370, 95)


pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_music])
                pygame.mixer.music.play()

    
    screen.fill((0, 0, 0))
    screen.blit(play_text, play_rect)
    screen.blit(stop_text, stop_rect)
    screen.blit(next_text, next_rect)
    screen.blit(prev_text, prev_rect)
    pygame.display.flip()


pygame.quit()