import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("init")
    width, height = 400,300
    screen = pygame.display.set_mode((width, height))
    while True:        
        for event in pygame.event.get(): # 迴圈處理pygame事件
            if event.type == pygame.QUIT: # 當視窗的x被按下
                pygame.quit() # 解除初始化pygame模組
                sys.exit() # 結束程式


if __name__ == '__main__':
    main()