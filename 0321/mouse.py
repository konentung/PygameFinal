import pygame
import sys

BLACK = (0, 0, 0)
LBLUE = (0, 102, 255)
PINK = (255, 102, 178)

def main():
    pygame.init()
    pygame.display.set_caption("Mouse")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        mBtn1, mBtn2, mBtn3 = pygame.mouse.get_pressed()
        txt = font.render(f"{mBtn1} {mBtn2} {mBtn3}", True, PINK)
        
        mouseX, mouseY = pygame.mouse.get_pos()
        txt2 = font.render(f"(x, y) = ({mouseX} {mouseY})",True, LBLUE)
        
        screen.fill(BLACK)
        screen.blit(txt, (100, 100))
        screen.blit(txt2, (100, 200))
        pygame.display.update()
        clock.tick(10)
    
if __name__ == '__main__':
    main()