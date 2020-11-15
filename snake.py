from os import system, name
from time import sleep 
from random import randint

def clear():
    if name == "nt":
        system('cls')
    else:
        system('clear')

class Field():
    def __init__(self,w,l):
        self.map = []
        self.width = w
        self.length = l

    def background(self):
        # self.map = [["#"]+['x']*self.length+["#"]]*self.width
        self.map = [['x']*self.length]*self.width
        print(self.map)
    def add_entity(self,x,y,s):
        self.map[14][24] = s

    def draw(self):
        for x in range(self.width):
            for y in range(self.length):
                print(self.map[x][y],end = "")
            print("")
        print(self.map)

class Entity():
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.symbol = s 

class Game():
    def __init__(self):
        self.field = Field(25,25)
        self.live = True

    def play_game(self):
        print("Game started!")
        while True:
            response = input("Press any key to start or \"x\" for exit: ")
            if response == "x":
                break
            head = Entity(12,12,"O")
            apple = Entity(3,3, "@")
            self.field.background()
            self.field.add_entity(head.x,head.y,head.symbol)
            # self.field.add_entity(apple.x,apple.y,apple.symbol)
            self.field.draw()
            exit()

test = Game()
test.play_game()

# sleep(2)
# clear()
