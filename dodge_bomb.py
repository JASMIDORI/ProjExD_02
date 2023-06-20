import random
import sys
import pygame as pg



WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bd_img= pg.surface((20, 20)) #直径20の円
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH) 
    y = random.randint(0, HEIGHT)
    bd_rct = bg_img.get_rect()
    #爆弾surface(bg_img)爆弾Rect(bd_rct)から抽出

    bd_rct.center = x,y #爆弾Rectの中心座標

    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)
    



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()