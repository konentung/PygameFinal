import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("第一次以Pygame顯示圖片")
    width, height = 640, 360
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    img_bg = pygame.image.load("pg_bg.png") # 載入背景圖片
    img_chara = [ # 載入人物圖片
        pygame.image.load("pg_chara0.png"),
        pygame.image.load("pg_chara1.png")
    ]
    play = pygame.image.load("play.png") # 載入play按鈕圖片
    play = pygame.transform.scale(play, (50, 50)) # 縮放play按鈕
    play_circle = play.get_rect() # 取得play按鈕的矩形
    play_circle.center=(550, 50) # 設定play按鈕的位置
    pause = pygame.image.load("pause.png") # 載入pause按鈕圖片
    pause = pygame.transform.scale(pause, (50, 50)) # 縮放pause按鈕
    pause_circle = pause.get_rect() # 取得pause按鈕的矩形
    pause_circle.center=(600, 50) # 設定pause按鈕的位置
    tmr = 0
    paused = False

    while True:
        if paused:
            tmr = tmr
        else:
            tmr = tmr + 5
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if paused:
                        paused = False
                    else:
                        paused = True
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_circle.collidepoint(event.pos):
                    paused = False
                if pause_circle.collidepoint(event.pos):
                    paused = True
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        x = tmr % 160 # 根據tmr計算捲動背景的值
        for i in range(5):
            screen.blit(img_bg, [i * 160 - x, 0]) # 繪製背景

        screen.blit(play, play_circle)
        screen.blit(pause, pause_circle)

        screen.blit(img_chara[tmr % 2], [224, 160]) # 讓人物動起來
        
        pygame.display.update()
        clock.tick(5)
            

if __name__ == '__main__':
    main()
