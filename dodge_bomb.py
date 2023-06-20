import random
import sys
import pygame as pg



WIDTH, HEIGHT = 1600, 900
Moving ={
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = bg_img.koukaton_rect()
    #こうかとんsurface(bg_img)をこうかとんRect(bd_rct)から抽出
    kk_rct.center = 900, 400
    bd_img= pg.surface((20, 20)) #直径20の円
    bd_img.set_colorkey((0, 0, 0))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH) 
    y = random.randint(0, HEIGHT)
    bd_rct = bg_img.get_rect()
    #爆弾surface(bg_img)を爆弾Rect(bd_rct)から抽出
    bd_rct.center = x,y  #爆弾の中心座標を連数で指定
    vx, vy = +5, +5 #爆弾の移動速度

    clock = pg.time.Clock()
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        key_list = pg.key.get_pressed()
        sum_mv = [0, 0] #合計移動量
        for k, mv in Moving.items():
            if key_list[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bd_rct(vx, vy) #爆弾の位置指定
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(10)
    



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()