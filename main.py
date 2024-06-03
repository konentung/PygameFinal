from configuration import *
from weapons import *
from sprites import *
import sys
import os
import pygame

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()
    
    def get_image(self, x,y, width, height):
        sprite = pygame.Surface([width, height]) 
        sprite.blit(self.spritesheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        
        return sprite
    
class mixer:
    def __init__(self, path):
        self.music = pygame.mixer.music.load(path)
        self.sound = pygame.mixer.Sound(path)
        
    def play(self):
        pygame.mixer.music.play(-1)
        self.sound.play()
    
class Game:
    def __init__(self):
        pygame.font.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.caption = pygame.display.set_caption('Adventure Game')
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('assets/images/terrain.png')
        self.player_spritesheet = Spritesheet('assets/images/character.png')
        self.enemy_spritesheet = Spritesheet('assets/images/evil.png')
        self.weapon_spritesheet = Spritesheet('assets/images/sword.png')
        self.bullet_spritesheet = Spritesheet('assets/images/powerBall.png')
        self.fireballs_spritesheet = Spritesheet('assets/images/fireball.png')
        self.medicine_spritesheet = Spritesheet('assets/images/HP_medicine.png')
        self.campfire_spritesheet = Spritesheet('assets/images/campfire.png')
        self.music = mixer('assets/sounds/music.mp3')
        self.font_name = os.path.join('assets','font','font.ttf')
        self.running = True
        self.enemy_collided =False
        self.block_collided = False
        
    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j , column in enumerate(row):
                Ground(self,j,i)
                if column=='B':
                    Block(self,j,i)
                if column=='P':
                    self.player=Player(self,j,i)
                if column=="E":
                    Enemy(self,j,i)
                if column=="R":
                    Water(self,j,i)
                if column=="W":
                    Weapon(self,j,i)
                if column=="M":
                    Medicine(self,j,i)
                if column=="F":
                    Flower(self,j,i)
                if column=="L":
                    Lava(self,j,i)
                if column=="S":
                    Stone(self,j,i)
                if column=="C":
                    Campfire(self,j,i)
    
    def create(self):
        self.all_sprites =pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.water =  pygame.sprite.LayeredUpdates()
        self.flowers = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()
        self.stone = pygame.sprite.LayeredUpdates()
        self.enemies= pygame.sprite.LayeredUpdates()
        self.mainPlayer = pygame.sprite.LayeredUpdates()
        self.weapons = pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.LayeredUpdates()
        self.fireballs = pygame.sprite.LayeredUpdates()
        self.healthbar = pygame.sprite.LayeredUpdates()
        self.medicine = pygame.sprite.LayeredUpdates()
        self.campfire = pygame.sprite.LayeredUpdates()
        self.createTileMap()
    
    def update(self):
        self.all_sprites.update()
        self.music.play()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
    
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    # def draw_text(self, text, size, x, y):
    #     font = pygame.font.Font(self.font_name, size)
    #     text_surface = font.render(text, True, WHITE)
    #     text_rect = text_surface.get_rect()
    #     text_rect.midtop = (x,y)
    #     self.screen.blit(text_surface, text_rect)
    
    def camera(self):
        if self.enemy_collided==False and self.block_collided==False:
            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_LEFT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x += PLAYER_STEPS
    
            elif pressed[pygame.K_RIGHT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x -= PLAYER_STEPS
                    
            elif pressed[pygame.K_UP]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y += PLAYER_STEPS     
                    
            elif pressed[pygame.K_DOWN]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y -= PLAYER_STEPS   
                
    def main(self):
        while self.running:
            self.events()
            self.camera()
            self.update()
            self.draw()
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                game.running=False
            if self.player.health <=0:
                self.running=False

    # def draw_init(self):
    #     self.screen.fill(BLACK)
    #     self.draw_text('擊倒怪物們!', 64, WIN_WIDTH/2, WIN_HEIGHT/4)
    #     self.draw_text('↑ ↓ ← → 控制主角移動，按下空白鍵發動攻擊', 20, WIN_WIDTH/2, WIN_HEIGHT/2)
    #     self.draw_text('按Enter開始遊戲', 32, WIN_WIDTH/2, WIN_HEIGHT*3/4)
    
    # def draw_end(self):
    #     self.screen.fill(BLACK)
    #     self.draw_text('Game Over', 64, WIN_WIDTH/2, WIN_HEIGHT/4)
    #     self.draw_text('按Enter重新開始', 32, WIN_WIDTH/2, WIN_HEIGHT*3/4)

game = Game()
game.create()

while game.running:
    # if DRAW_INITIAL:
    #     game.draw_init()
    #     # keypress = pygame.key.get_pressed()
    #     # if keypress[pygame.K_KP_ENTER]:
    #     #     DRAW_INITIAL = False
    # else:
        game.main()
    
pygame.quit()
sys.exit()
