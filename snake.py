from os import system, name
from time import sleep 
from random import randint

class Field():
    def __init__(self,w,l):
        self.map = []
        self.width = w
        self.length = l
    def get(self):
        self.map = ["#"+['x']*self.length+"#"]*self.width
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
        self.field = Field(5,5)
    def play_game(self):
        print("Game started!")

def clear():
    if name == "nt":
        system('cls')
    else:
        system('clear')

test = Game()
test.play_game()

# sleep(2)
# clear()
