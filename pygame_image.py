import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False) #演習8:左右反転した背景画像surface
    kt_img = pg.image.load("fig/3.png") #演習3:こうかとん画像surfaceの作成
    kt_img = pg.transform.flip(kt_img,True,False)
    kt_rct = kt_img.get_rect() #練習10-1:こうかとんRectの取得
    kt_rct.center = 300,200 #練習10-2:こうかとんの初期座標
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10-3:キーの押下状態取得
        ex2x = 0
        ex2y = 0

        if key_lst[pg.K_UP]:
            ex2y -= 1
        if key_lst[pg.K_DOWN]:
            ex2y += 1
        if key_lst[pg.K_LEFT]:
            ex2x -= 1
        if key_lst[pg.K_RIGHT]:
            ex2x += 2
            
        ex1x = -1
        ex1y = 0
        kt_rct.move_ip(ex2x + ex1x, ex2y + ex1y)


        x=tmr%3200 #練習9
        screen.blit(bg_img, [-x, 0]) #練習5:背景画像を右から左に
        screen.blit(bg_img2, [-x+1600, 0]) #練習7:2枚目の背景画像
        screen.blit(bg_img, [-x+3200, 0]) #練習9:3枚目の背景画像
        screen.blit(kt_img, kt_rct) #練習4:こうかとんsurfaceを貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6:FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()