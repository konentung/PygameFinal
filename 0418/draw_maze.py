import pygame
import sys

width, height = 800,600 # 宣告視窗大小為800x600
SKYBLUE = (100, 200, 200)
WHITE = (255, 255, 255)
PINK = (255, 150, 200)

# 畫迷宮
def draw_maze(screen,maze):
    # 畫格子顏色:0是白色沒走過、1是藍色障礙物、2是粉色已走過
    for y in range(7):
        for x in range(10):
            if maze[y][x] == 0:
                #                 畫布     顏色    x座標  y座標  寬  長
                pygame.draw.rect(screen, WHITE, [x*80, y*80, 80, 80])
            elif maze[y][x] == 1:
                pygame.draw.rect(screen, SKYBLUE, [x*80, y*80, 80, 80])
            elif maze[y][x] == 2:
                pygame.draw.rect(screen, PINK, [x*80, y*80, 80, 80])

        # 畫格子線
            if x != 0: # 橫的
                #                 畫布    顏色   起始座標       終點座標     寬
                pygame.draw.line(screen, WHITE, [x*80, 0], [x*80, height-41], 1)
        if y != 0:  # 直的
            pygame.draw.line(screen, WHITE, [0, y*80], [width, y*80], 1)

def main():
    pygame.init() # 初始化pygame模組
    pygame.display.set_caption("咪咪的使命") # 設定視窗名稱
    screen = pygame.display.set_mode((width, height)) # 設定視窗大小
    img_cat = pygame.image.load('img/mimi.png') # 載入貓咪圖片
    cat_x, cat_y = 0,0 # 初始化貓咪位置

    maze = [
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,0,1],
            [1,0,1,1,0,0,1,0,0,1],
            [1,0,0,1,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1]
        ]

    while True:   
        screen.fill((207,252,255))     
        for event in pygame.event.get(): # 迴圈處理pygame事件
            if event.type == pygame.QUIT: # 當視窗的x被按下
                pygame.quit() # 解除初始化pygame模組
                sys.exit() # 結束程式
            if event.type == pygame.KEYDOWN:  # 當按下按鍵時
                    if event.key == pygame.K_UP:   # 當按鍵為上方向鍵
                        if cat_y > 0:
                            cat_y -= 80
                        
                    if event.key == pygame.K_DOWN:   # 當按鍵為下方向鍵
                        if cat_y < 560-80:
                            cat_y += 80
                                            
                    if event.key == pygame.K_LEFT:   # 當按鍵為左方向鍵
                        if cat_x > 0:
                            cat_x -= 80
                                            
                    if event.key == pygame.K_RIGHT:   # 當按鍵為右方向鍵
                        if cat_x < 800-80:
                            cat_x += 80
        draw_maze(screen, maze) 
        screen.blit(img_cat, [cat_x,cat_y])
        pygame.display.update()
                                            
if __name__ == '__main__':  # 呼叫main函數
    main()

