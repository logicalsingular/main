from os import system
from random import randint

class The_Map():
    def __init__(self,w,l):
        self.map = []
        self.width = w
        self.length = l
    def new(self):
        self.map = [['x']*self.l]*self.w
        print(self.map)
    def get_map(self):
        return self.map

class Snake():
    def __init__(self,x,y):
        self.head_x = x
        self.head_y = y
        self.symbol = 'O' 
        self.length = 1

class Apple():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.symbol = '@'

class Game():
    def __init__(self):
        self.the_map = The_Map(5,5)
    def play_game(self):

lol = Game()
lol.play_game()
