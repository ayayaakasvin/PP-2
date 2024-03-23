import pygame
import Properties

def main():
    clock = pygame.time.Clock()

    screenObject = Properties.ScreenProperties(1280, 720) # hd resolution
    screen = screenObject.returnScreen()

    circleProperties = Properties.CircleProperties()

    userInput = Properties.Input(circleProperties, screenObject)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 128, 0))
        

        userInput.ArrowPressed()

        circleProperties.drawTheCircle(screen)
        
        pygame.display.flip()
        clock.tick(45)

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()