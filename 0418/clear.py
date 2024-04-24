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

# 過關判斷(若過關迷宮內只會有1跟2)
def stage_clear(maze):
    for row in maze:
        for cell in row:
            if cell == 0: # 找到一個0
                return False
    return True

# 繪製過關文字
def draw_clear_txt(screen):
    font = pygame.font.Font(None, 100) # 建立字型物件
    txt = font.render('CLEAR!', True, WHITE) # 繪製字串
    txt_rect = txt.get_rect(center=(width // 2, (height-40) // 2))  # 計算文字矩形的位置
    screen.blit(txt, txt_rect)
    
def draw_clear_img(screen):
    img = pygame.image.load('img/clear.png') # 載入過關圖片
    screen.blit(img, [width//2-255, height//2-60]) # 繪製過關圖片
    pygame.transform.scale(img, (100, 200)) # 縮放過關圖片
    
def main():
    pygame.init() # 初始化pygame模組
    pygame.display.set_caption("咪咪的使命") # 設定視窗名稱
    screen = pygame.display.set_mode((width, height)) # 設定視窗大小
    img_cat = pygame.image.load('img/mimi.png') # 載入貓咪圖片
    maze_x, maze_y = 2, 3 # 初始化貓咪位置

    maze = [
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,0,0,0,1],
            [1,0,0,1,0,0,0,0,1,1],
            [1,0,0,0,0,1,0,0,0,1],
            [1,0,0,0,0,1,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1]
        ]

    while True:   
        screen.fill((207,252,255))
        if maze[maze_y][maze_x] == 0: # 將貓咪現在位置改色
                maze[maze_y][maze_x] = 2 
        for event in pygame.event.get(): # 迴圈處理pygame事件
            if event.type == pygame.QUIT: # 當視窗的x被按下
                pygame.quit() # 解除初始化pygame模組
                sys.exit() # 結束程式
            if event.type == pygame.KEYDOWN:  # 當按下按鍵時
                    if event.key == pygame.K_UP:   # 當按鍵為上方向鍵
                        if maze[maze_y-1][maze_x] == 0: # 
                            maze_y = maze_y-1 # 更新角色位置
                        
                    if event.key == pygame.K_DOWN:   # 當按鍵為下方向鍵
                        if maze[maze_y+1][maze_x] == 0:
                            maze_y = maze_y+1
                                            
                    if event.key == pygame.K_LEFT:   # 當按鍵為左方向鍵
                        if maze[maze_y][maze_x-1] == 0:
                            maze_x = maze_x-1
                                            
                    if event.key == pygame.K_RIGHT:   # 當按鍵為右方向鍵
                        if maze[maze_y][maze_x+1] == 0:
                            maze_x = maze_x+1
        draw_maze(screen, maze) 
        screen.blit(img_cat, [maze_x*80, maze_y*80])

        if stage_clear(maze):
            draw_clear_img(screen)
            
        pygame.display.update()
                                            
if __name__ == '__main__':  # 呼叫main函數
    main()

