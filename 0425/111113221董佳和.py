import pygame
import sys

width, height = 800,600 # 宣告視窗大小為800x600
SKYBLUE = (100, 200, 200)
WHITE = (255, 255, 255)
PINK = (255, 150, 200)
final_stage = 3

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
def draw_clear_txt(screen, index):
    font = pygame.font.Font(None, 100) # 建立字型物件
    txt = font.render('CLEAR!', True, WHITE) # 繪製字串
    txt_rect = txt.get_rect(center=(width // 2, (height-40) // 2))  # 計算文字矩形的位置
    screen.blit(txt, txt_rect)
    
    font2 = pygame.font.Font(None, 40) # 建立字型物件
    if index != final_stage:
        txt2 = font2.render('Press N to next stage.', True, WHITE)
    else:
        txt2 = font2.render('You passed all stages!', True, WHITE)
    txt2_rect = txt2.get_rect(center=(width // 2, (height-40) // 2 + 80))
    screen.blit(txt2, txt2_rect)
            
def init_maze(index):
    if index<=1:
        maze = [
            [1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1,0,0,1],
            [1,0,1,1,0,0,1,0,0,1],
            [1,0,0,1,0,0,0,0,0,1],
            [1,0,0,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1]
        ]
        init_maze_x, init_maze_y = 1, 1
    elif index==2:
        maze = [
                [1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,0,0,0,0,1],
                [1,0,0,1,0,0,0,0,1,1],
                [1,0,0,0,0,1,0,0,0,1],
                [1,0,0,0,0,1,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1]
            ]
        init_maze_x, init_maze_y = 2, 3
    elif index == 3:
        maze = [
                [1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,0,1,1,1,1,1,1,0,1],
                [1,0,1,0,0,0,0,1,0,1],
                [1,0,1,0,1,1,0,1,0,1],
                [1,0,0,0,1,1,0,0,0,1],
                [1,1,1,1,1,1,1,1,1,1]
            ]
        init_maze_x, init_maze_y = 1, 1
    return maze, init_maze_x, init_maze_y
    
def main():
    pygame.init() # 初始化pygame模組
    pygame.display.set_caption("咪咪的使命") # 設定視窗名稱
    screen = pygame.display.set_mode((width, height)) # 設定視窗大小
    font = pygame.font.Font(None, 40) # 建立字型物件
    img_cat = pygame.image.load('img/mimi.png') # 載入貓咪圖片
    img_home = pygame.image.load('img/home.png')
    index = 0
    is_init = True
    
    pygame.mixer.music.load('sound/bgm.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    enter = pygame.mixer.Sound('sound/enter.mp3')
    pop = pygame.mixer.Sound('sound/pop.mp3')
    punch = pygame.mixer.Sound('sound/punch.mp3')
    restart = pygame.mixer.Sound('sound/restart.mp3')
    meow = pygame.mixer.Sound('sound/meow.mp3')

    while True:
        if index == 0:
            screen.blit(img_home, [0, 0])
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        index = 1
                        enter.play()
        else:
            screen.fill((207,252,255))
            
            if is_init:
                maze, init_maze_x, init_maze_y = init_maze(index)
                maze_x, maze_y = init_maze_x, init_maze_y
                meow_played = False
                
            if maze[maze_y][maze_x] == 0: # 將貓咪現在位置改色
                maze[maze_y][maze_x] = 2
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if maze[maze_y-1][maze_x] == 0:
                            maze_y = maze_y-1
                            is_init = False
                            pop.play()
                        else:
                            punch.play()
                    if event.key == pygame.K_DOWN:
                        if maze[maze_y+1][maze_x] == 0:
                            maze_y = maze_y+1
                            is_init = False
                            pop.play()
                        else:
                            punch.play()
                    if event.key == pygame.K_LEFT:
                        if maze[maze_y][maze_x-1] == 0:
                            maze_x = maze_x-1
                            is_init = False
                            pop.play()
                        else:
                            punch.play()
                    if event.key == pygame.K_RIGHT:
                        if maze[maze_y][maze_x+1] == 0:
                            maze_x = maze_x+1
                            is_init = False
                            pop.play()
                        else:
                            punch.play()
                    if event.key == pygame.K_r and not stage_clear(maze):
                        is_init = True
                        restart.play()
                    if event.key == pygame.K_n and stage_clear and index != final_stage:
                        index += 1
                        is_init = True
                        enter.play()
                            
            draw_maze(screen, maze)
            screen.blit(img_cat, [maze_x*80, maze_y*80])
            
            # 顯示文字:第幾關
            stage_txt = font.render('STAGE'+str(index), True, (161, 31, 101))
            stage_txt_rect = [10, 565]
            screen.blit(stage_txt, stage_txt_rect)
            
            # 顯示文字:按R重來
            restart_txt = font.render('You can press R to restart.', True, (161, 31, 101))
            restart_txt_rect = restart_txt.get_rect(center=(width // 2, 580))
            screen.blit(restart_txt, restart_txt_rect)
            
            if stage_clear(maze):
                draw_clear_txt(screen, index)
                if not meow_played:
                    meow.play()
                    meow_played = True
            
        pygame.display.update()
                                            
if __name__ == '__main__':  # 呼叫main函數
    main()

