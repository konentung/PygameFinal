import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("init")
    width, height = 400,300
    screen = pygame.display.set_mode((width, height))
    running = True
    
    # 遊戲迴圈
    while running:
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
                    
        # 更新遊戲背景
        screen.fill((0,0,0))
        
        # 更新遊戲畫面
        pygame.display.update()

if __name__ == '__main__':
    main()