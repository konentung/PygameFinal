import pygame
import sys

WHITE = (255, 255, 255)
DARKGRAY = (50, 50, 50)
start_x=300; end_x=start_x+255
R_y=50; G_y=R_y+50; B_y=R_y+100 

# 畫拖曳條與球
def draw_slider(screen, color, x, y):
    y+=15
    line = pygame.draw.line(screen, DARKGRAY, (start_x, y), (end_x, y), 5)
    circle = pygame.draw.circle(screen, color, (x, y), 8)
    return line,circle

def main():
    pygame.init()
    pygame.display.set_caption("Slime")
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    icon = pygame.image.load("0321/slime.png") # 載入圖片
    pygame.display.set_icon(icon)   # 設置視窗icon

    R_state=0 # 初始化按下狀態    
    R = 150 # 初始化紅色數值    
    R_x = start_x+R # 初始化拖曳球位置

    G_state=0; B_state=0
    G = 200; B = 255
    G_x = start_x+G; B_x = start_x+B

    while True:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 若檢測到滑鼠抬起，則不可調整數值
            if event.type == pygame.MOUSEBUTTONUP and R_state:
                R_state=0
            if event.type == pygame.MOUSEBUTTONUP and G_state:
                G_state=0
            if event.type == pygame.MOUSEBUTTONUP and B_state:
                B_state=0
             

        # 若檢測到滑鼠在對應位置按下，可調整數值
        if pygame.mouse.get_pressed()[0]:
            # 拖曳球
            if R_circle.collidepoint(pos):
                R_state=1
            if G_circle.collidepoint(pos):
                G_state=1
            if B_circle.collidepoint(pos):
                B_state=1
            
        # 獲取滑鼠位置        
        pos = pygame.mouse.get_pos()

        # 設置拖曳球的活動範圍
        R_x = min(max(pos[0], start_x), end_x) if R_state else R_x
        G_x = min(max(pos[0], start_x), end_x) if G_state else G_x
        B_x = min(max(pos[0], start_x), end_x) if B_state else B_x
        '''
        if R_state:
            R_x = pos[0]
            if R_x > end_x:
                R_x = end_x
            elif R_x < start_x:
                R_x = start_x
        '''    

        # 畫拖曳條
        R_line,R_circle = draw_slider(screen, (255, 0, 0), R_x, R_y)
        G_line,G_circle = draw_slider(screen, (0, 255, 0), G_x, G_y)
        B_line,B_circle = draw_slider(screen, (0, 0, 255), B_x, B_y)

        # 實際顏色
        R = R_x - start_x
        G = G_x - start_x
        B = B_x - start_x

        # 畫史萊姆
        pygame.draw.ellipse(screen, (R, G, B), [250, 250, 300, 250])
        pygame.draw.ellipse(screen, DARKGRAY, [250, 250, 300, 250], 1)
        pygame.draw.line(screen, DARKGRAY, (300, 350), (350, 350), 5)
        pygame.draw.line(screen, DARKGRAY, (450, 350), (500, 350), 5)
        pygame.draw.polygon(screen, (255, 100, 100), [[400, 400], [350, 425], [450, 425]])

        pygame.display.update()
        

if __name__ == '__main__':
    main()
