import pygame
import sys
import math

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GOLD  = (255, 216,   0)
SILVER= (192, 192, 192)
COPPER= (192, 112,  48)

def main():
    pygame.init()
    pygame.display.set_caption("首次繪製的Pygame圖形")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # 繪製線條
        #               Surface color  起點     終點    寬度
        pygame.draw.line(screen, RED, [0,0], [100,200], 10)

        # 繪製矩形
        #               Surface color [左上角x,y,寬,高]   寬度
        pygame.draw.rect(screen, RED, [200,50,120,80])
        pygame.draw.rect(screen, GREEN, [200,200,60,180], 5)

        # 繪製多邊形
        #                  Surface  color  [ 座標1  ,   座標2   ,   座標3  ]  寬度
        pygame.draw.polygon(screen, BLUE, [[250,400], [200,500], [300,500]], 10)
        
        # 繪製圓形
        #                  Surface color  圓心座標  半徑  寬度
        pygame.draw.circle(screen, GOLD, [400,100], 60)

        # 繪製橢圓形
        #                   Surface color   [左上角x, y     ,寬,高]  寬度
        pygame.draw.ellipse(screen, SILVER, [400-80,300-40,160,80])
        pygame.draw.ellipse(screen, COPPER, [400-40,500-80,80,160], 20)

        ang = math.pi*tmr/36 # 變動弧度
        #               Surface color [左上角x, y     , 寬 ,高]   起始角度    結束角度 寬度
        pygame.draw.arc(screen, BLUE, [600-100,300-200,200,400],    0,     math.pi*2)
        pygame.draw.arc(screen, WHITE, [600-100,300-200,200,400], ang, ang+math.pi/2, 8)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
