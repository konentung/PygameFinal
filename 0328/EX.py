import pygame
import sys

def main():
    pygame.init()
    pygame.display.set_caption("Drag Image Example")
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))    

    clock = pygame.time.Clock()

    # 載入圖片
    garbagecan = pygame.image.load("garbagecan.png")
    garbagecan_rect = garbagecan.get_rect()
    garbagecan_rect.center = (525, 225)
    garbage = pygame.image.load("garbage.png")
    garbage_rect = garbage.get_rect()
    garbage_rect.center = (width // 2, 500)

    img_bg = pygame.image.load("bg.png")

    dragging = False  # 判斷是否正在拖動圖片

    while True:
        screen.fill((255, 255, 255))
        screen.blit(img_bg, [0,0])
        screen.blit(garbagecan, garbagecan_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # 解除初始化pygame模組
                sys.exit() # 結束程式
            # 滑鼠事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                if garbage_rect.collidepoint(event.pos):
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    garbage_rect.move_ip(event.rel)
                else:
                    if garbage_rect.colliderect(garbagecan_rect):
                        garbage_rect.center = (-30, -30)
            
        # 繪製圖片
        screen.blit(garbage, garbage_rect)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
