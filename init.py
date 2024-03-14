import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("init")
    width, height = 400,300
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    # 彙整圖片
    img_bg = pygame.image.load("bg.png")
    img_chara = [
        pygame.image.load("chara1.png"),
        pygame.image.load("chara2.png"),
    ]
    tmr = 0
    
    running = True
    while running:
        tmr = tmr + 1
        
        for event in pygame.event.get(): # 迴圈處理pygame事件
            if event.type == pygame.QUIT: # 當視窗的x被按下
                pygame.quit() # 解除初始化pygame模組
                sys.exit() # 結束程式
            # 鍵盤的事件
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((640, 360))
                if event.key == pygame.K_F11:
                    screen = pygame.display.set_mode((640, 360), pygame.FULLSCREEN)
                    
        x = tmr%160
        for i in range(5):
            screen.blit(img_bg, [i*160-x, 0])
            
        # 更新遊戲畫面       
        screen.fill((0,0,0))
        screen.blit(img_chara[tmr%2], (224,160))
        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    main()