# -*- coding:utf-8 -*-
import sys
import pygame
from pygame.locals import *
import os
import time
from gamesys import timer

#カレントディレクトリの変更
path = __file__
s = str(path)
a = s + "/../.."
os.chdir(a)

# 画面サイズ 600×500
SCREEN_SIZE = (240, 180)

def defscene1():
    # Pygameの初期化
    pygame.init()  

    # タイトルバーの設定（大きさ600*500）
    screen = pygame.display.set_mode(SCREEN_SIZE)
    
    buttonM = pygame.Rect(80, 120, 80, 40)  # creates a rect object
    #必要画像の読み込み
    #背景
    background = pygame.image.load("img/background/room1.png")
    screen.blit(background, (0, 0))
    #キャラ画像
    character = pygame.image.load("img/character/Irony_chara.png")
    #フォント  
    font = pygame.font.Font("img/font/Irohamaru/Irohamaru-mikami-Medium.ttf", 27)
    
    rects = (0,0,64,64)
    screen.blit(character, (88, 58), area=rects)

    #テキストの設定
    text1 = font.render("見守る", True, (0,0,0))

    while True:

        # 画面を更新
        pygame.display.update()  
        pygame.draw.rect(screen, (255, 255, 255), buttonM)
        screen.blit(text1, (80, 120))

        # イベント処理
        for event in pygame.event.get():
            # 閉じるボタンが押されたら終了
            if event.type == QUIT:  
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttonM.collidepoint(event.pos):
                    timer.timer(1,00,False)




if __name__ == "__main__":
    defscene1()
