import pygame
import sys

WHITE = (255, 255, 255)
DARKGRAY = (50, 50, 50)

def main():
    pygame.init()
    pygame.display.set_caption("Slime")
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    icon = pygame.image.load("slime.png") # 載入圖片
    pygame.display.set_icon(icon)   # 設置視窗icon    

    while True:
        screen.fill(WHITE)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()          
        

        # 畫史萊姆
        pygame.draw.ellipse(screen, (150, 200, 255), [250, 250, 300, 250])
        pygame.draw.ellipse(screen, DARKGRAY, [250, 250, 300, 250], 1)
        pygame.draw.line(screen, DARKGRAY, (300, 350), (350, 350), 5)
        pygame.draw.line(screen, DARKGRAY, (450, 350), (500, 350), 5)
        pygame.draw.polygon(screen, (255, 100, 100), [[400, 400], [350, 425], [450, 425]])

        pygame.display.update()
        

if __name__ == '__main__':
    main()
