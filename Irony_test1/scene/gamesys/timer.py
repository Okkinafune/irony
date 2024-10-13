import sys
import pygame
from pygame.locals import *
import os
import time
import os

#カレントディレクトリの変更
path = __file__
s = str(path)
a = s + "/../.."
os.chdir(a)
over = False
timerS = 0


def timer(m,s):
    #タイマーフォント設定
    fontT = pygame.font.SysFont(None, 50)
    
    while True:
        for y in range(m):
           for x in range(s):
               time.sleep(1)
               s -= 1
               timerS = m + ":" + s
               timertext = fontT.render(timerS, True, (0,0,0))
               
        time.sleep(1)
        m -= 1
        s += 59
               
 