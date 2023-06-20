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

#Change ={
#    pg.a:(0, -5),
#    pg.b:(+5, -5),
#    pg.c:(+5, 0),
#    pg.d:(+5, +5),
#    pg.e:(0, +5),
#    pg.f:(-5, +5),
#    pg.g:(-5, 0),
#    pg.h:(-5, -5),

#} #追加機能1 




def check_bound(rect: pg.Rect) -> tuple[bool, bool]:
    #こうかとんRect，爆弾Rectが画面外 or 画面内かを判定する関数
    #引数：こうかとんRect or 爆弾Rect
    #戻り値：横方向，縦方向の判定結果タプル（True：画面内／False：画面外）
    
    yoko, tate = True, True
    if rect.left < 0 or WIDTH < rect.right:  # 横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  # 縦方向判定
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    kk_rct = kk_img.get_rect()
    #こうかとんsurface(bg_img)をこうかとんRect(bd_rct)から抽出
    kk_rct.center = 900, 400
    bd_img = pg.Surface((20, 20)) #直径20の円
    bd_img.set_colorkey((0, 0, 0))
    bd_imgs = []
    
    pg.draw.circle(bd_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH) 
    y = random.randint(0, HEIGHT)
    bd_rct = bd_img.get_rect()
    #爆弾surface(bg_img)を爆弾Rect(bd_rct)から抽出
    bd_rct.center = x,y  #爆弾の中心座標を連数で指定
    vx, vy = +5, +5 #爆弾の移動速度

    accs = [a for a in range(1,11)]  #追加機能2、加速のリスト
    
    for r in range(1, 11):
        bd_img = pg.Surface((20*r, 20*r))
        pg.draw.circle(bd_img, (255, 0, 0), (10*r, 10*r), 10*r)
        bd_imgs.append(bd_img) 
        #追加機能2、拡大爆弾のリスト

    clock = pg.time.Clock()
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if kk_rct.colliderect(bd_rct):  
            print("ゲームオーバー")
            return   # ゲームオーバー 
         
        key_list = pg.key.get_pressed()
        sum_mv = [0, 0] #合計移動量
        for k, mv in Moving.items():
            if key_list[k]:
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img,  kk_rct)
        bd_rct.move_ip(vx, vy) #爆弾の位置指定
        yoko, tate = check_bound(bd_rct)
        if not yoko:  # 横方向に画面外だったら
            vx *= -1
        if not tate:  # 縦方向に範囲外だったら
            vy *= -1
        avx, avy = vx*accs[min(tmr // 500, 9)], vy*accs[min(tmr//500, 9)] #追加機能2
        bd_rct.move_ip(avx, avy)
        bd_img = bd_imgs[min(tmr//500,9)] #追加機能2
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        
        clock.tick(50)
    



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()