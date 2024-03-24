import os, pygame

class Music:
    path_to_files : str = "/media/ayayaakasvin/6A5A629E5A6266B3/Study/repos/python/TSIS_7/PlayerTask"

    def returnFilesAsAList(self, path) -> list :
        return os.listdir(path)
    
    def mp3_list_of_folder(self) -> list :
        musicFiles = []
        for file in self.returnFilesAsAList(self.path_to_files):
            if len(file) >= 4 and file[-4:].lower() == ".mp3":
                musicFiles.append(file)
        
        return musicFiles
    
    def play_music(self, musicName: str) -> None:
        try:
            pygame.mixer.music.load(musicName)
            pygame.mixer.music.play(0)
        except pygame.error as e:
            print(f"Error loading music: {e}")
    

class ScreenProperties:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.screen = pygame.display.set_mode((self.x, self.y))
    
    def returnScreen(self):
        return self.screen
    
    def SongText (self, SongName : str):
        font = pygame.font.SysFont("arialbold", 72)
        text = font.render(SongName, True, (0, 128, 0))
        self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, self.screen.get_height() // 2 - text.get_height() // 2))

    def IsPlayingText(self, status: bool, SongName : str):
        font = pygame.font.SysFont("arialbold", 69)

        if status:
            song_status = font.render("Now Playing:", True, (0, 128, 0))
        else:
            song_status = font.render("Going to Play:", True, (0, 128, 0))

        text_width = song_status.get_width()
        screen_width = pygame.display.get_surface().get_width()
        text_x = (screen_width - text_width) // 2
        text = font.render(SongName, True, (0, 128, 0))

        self.screen.blit(song_status, (text_x, (self.screen.get_height() // 2) - 50 - text.get_height() // 2))