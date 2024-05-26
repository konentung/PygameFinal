WIN_WIDTH = 600
WIN_HEIGHT = 600
TILESIZE = 32
FPS = 60

HEALTH_LAYER =6
PLAYER_LAYER =5
WEAPON_LAYER = 7
ENEMY_LAYER=3
BLOCKS_LAYER= 2
GROUND_LAYER=1

PLAYER_STEPS = 4
ENEMY_STEPS =1
BULLET_STEPS= 6

ENEMY_HEALTH = 6
PLAYER_HEALTH= 10

BLACK=(0,0,0)
GREEN= (0,255,0)
RED =(255,0,0)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'B....FFF....BBB....SSSSSS..............FFFF...............B',
    'B....F.F.....B....SS....S............F....F..E............B',    
    'B....FSS....B....SS....SS...........F..E...F.....E........B',    
    'B....SSSSSSSSSSSSS.....S..................E..FF.FF....B...B',
    'B....CCC...............SSS...........F.E...F..............B',
    'B.....W..B.........E.....S..RRR......FF....F..BB.B........B',
    'B........B............SSSS.RRR..............RR............B',
    'B..BB.....P...S....E..S..RRR..............................B',
    'B....FFFFF....S..M....S......................FFFF.........B',
    'B...FRRRRRF...S.......SSSS..........BBBBB....F....FF...LLLL',
    'B..FRRRRRRRF..S..........S....................F.......LLLLL',
    'B...FRRRRRF...S..E......SS........RR..................LLLLL',
    'B....FFFFFE...SSSSSSSSSSS...................FFFF......LLLLB',
    'B..............S..RRS.................M..............LLLLLB',
    'B...SSSSSSSSSSSS.RR.S...............................LLL...B',
    'B...SFFFFFFRRRRRRR..S....E.........................LL.....B',
    'B...SFFFFFF....RR...S......................M.......L......B',
    'B...SFFBBBF..RRRR...S.....................................B',
    'B...SFFFFFF.RRRRRR..SSSSS....E......E...........E.E.......B',
    'B...SSSS...RRRRRRRRR.............................E........B',
    'B.........RRRRRRRRRRR.....................................B',    
    'BBBBBBBBBRRRRRRRRRRRRRBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',  
]