import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("init")
    width, height = 400,300
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    # 彙整圖片
    img_bg = pygame.image.load("pg_bg.png")
    img_chara = [
        pygame.image.load("pg_chara1.png"),
        pygame.image.load("pg_chara2.png"),
    ]
    
    # 設定參數
    tmr = 0
    x = 0
    y = 160
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

        # 更新遊戲背景       
        # screen.fill((0,0,0))
        bg_x = 0
        while bg_x <= 640:
            screen.blit(img_bg, (bg_x, 0))
            bg_x += img_bg.get_width()
        
        # 循環動畫
        x = x + 16
        screen.blit(img_chara[tmr%2], (x, y))
        if x == width - 192:
            x_ = -img_chara[tmr%2].get_width()
        if x > width - 192:
            x_ = x_ + 16
            screen.blit(img_chara[tmr%2], (x_, y))
        if x == width:
            x = 0

        pygame.display.update()
        clock.tick(5)

if __name__ == '__main__':
    main()