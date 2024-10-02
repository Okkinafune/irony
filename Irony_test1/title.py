# -*- coding:utf-8 -*-
from pygame.locals import *
import pygame
import sys
import os
from scene import scene1

def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode((480, 360))    # 画面を作成
    pygame.display.set_caption("片隅アイロニー")    # タイトルを作成

    print(__file__)
    path = __file__
    s = str(path)
    a = s + "/.."
    os.chdir(a)
    print(os.getcwd())
    icon = pygame.image.load("img/img_icon.png")
    pygame.display.set_icon(icon)
    button = pygame.Rect(180, 120, 120, 60)  # creates a rect object

    #STEP1.フォントの用意  
    font = pygame.font.SysFont(None, 50)
    
    #STEP2.テキストの設定
    text1 = font.render("start", True, (0,0,0))
    
    
    running = True
    #メインループ
    while running:
        screen.fill((0,0,0))  #画面を黒で塗りつぶす
        
        pygame.draw.rect(screen, (255, 255, 255), button)

        screen.blit(text1, (200, 135))

        pygame.display.update() #描画処理を実行
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                running = False
                pygame.quit()  #pygameのウィンドウを閉じる
                sys.exit() #システム終了
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                   scene1.defscene1()
                    
                    
                    
if __name__=="__main__":
    main()
