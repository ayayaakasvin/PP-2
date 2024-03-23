import pygame
import GetTheListOfFiles

def main():
    clock = pygame.time.Clock()
    
    screenObject = GetTheListOfFiles.ScreenProperties(1280, 720)
    screen = screenObject.returnScreen()
    object_of_music = GetTheListOfFiles.Music()
    music_library = object_of_music.mp3_list_of_folder()
    current_index = 0
    current_song = music_library[current_index]
    pygame.mixer.music.load(music_library[current_index])
    pygame.mixer.music.play(0)
    playing = False
    backgroundObject = GetTheListOfFiles.ScreenProperties.Background(screenObject)
    backgroundImage = backgroundObject.backgroundProperties(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                playing = not playing
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                current_index = (current_index + 1) % len(music_library)
                current_song = music_library[current_index]
                object_of_music.play_music(current_song)
                playing = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                current_index = (current_index - 1) % len(music_library)
                object_of_music.play_music(music_library[current_index])
                current_song = music_library[current_index]
                playing = True
                        
        if playing:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

        backgroundObject.backgroundSet(screen)        
        screenObject.SongText(current_song)
        screenObject.IsPlayingText(playing, current_song)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()