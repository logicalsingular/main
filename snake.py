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
        # self.map = [['x']*self.length]*self.width
        self.map = [["x","x","x","x","x"],["x","x","x","x","x"],["x","x","x","x","x"],["x","x","x","x","x"],["x","x","x","x","x"]]
        print(self.map)
        
    def add_entity(self,x,y,s):
        self.map[x][y] = s
        
    def draw(self):
        for x in range(self.width):
            for y in range(self.length):
                print(self.map[x][y],end = '')
            print('')

class Entity():
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.symbol = s

class Game():
    def __init__(self):
        self.field = Field(5,5)
        self.live = True

    def play_game(self):
        print("Game started!")
        while True:
            # response = input("Press any key to start or \"x\" for exit: ")
            # if response == "x":
            #     break
            head = Entity(1,0,"O")
            apple = Entity(2,1, "@")
            self.field.background()
            self.field.add_entity(head.x,head.y,head.symbol)
            self.field.add_entity(apple.x,apple.y,apple.symbol)
            self.field.draw()
            exit()

test = Game()
test.play_game()

# sleep(2)
# clear()
