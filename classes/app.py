import pygame as pg
import random
import time


class App:

    def __init__(self): 
        print("App loaded...")
        self.screen = pg.display.set_mode((720, 720))
        self.bars = [180+(x*8) for x in range(60)]
        random.shuffle(self.bars)
        self.idx = 0

    def update(self):
        pg.display.flip()

    def draw(self):
        self.screen.fill((25,25,25))
        for i in range(60):
            pg.draw.rect(self.screen, (200, 200, 250), pg.Rect(i*12,0,12,self.bars[i]), 1)

    def bubble_sort(self):
        for i in range(len(self.bars)):
            for j in range(0, len(self.bars)-i-1):
                if self.bars[j] > self.bars[j+1]:
                    self.bars[j], self.bars[j+1] = self.bars[j+1], self.bars[j]
                self.draw()
                self.update()
                time.sleep(0.005)

    def run(self):
        self.bubble_sort()
        self.draw()
        self.update()