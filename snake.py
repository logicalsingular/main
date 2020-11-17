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
        self.field = []
        self.width = w
        self.length = l

    def background(self):
        self.field = [["x"] * self.width for i in range(self.length)]
        
    def add_entity(self,x,y,s):
        self.field[x][y] = s
        
    # def draw(self):
    #     for x in range(self.width):
    #         for y in range(self.length):
    #             print(self.field[x][y],end = '')
    #         print('')
    def draw(self):
        for x in range(self.length):
            for y in range(self.width):
                print(self.field[x][y],end = '')
            print('')
class Entity():
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.symbol = s

class Game():
    def __init__(self):
        self.field = Field(25,4)
        self.live = True

    def play_game(self):
        print("Game started!")
        while True:
            # response = input("Press any key to start or \"x\" for exit: ")
            # if response == "x":
            #     break
            clear()
            head = Entity(1,0,"O")
            # apple = Entity(2,1, "@")
            apple = Entity(randint(0,3),randint(0,24), "@")
            self.field.background()
            self.field.add_entity(head.x,head.y,head.symbol)
            self.field.add_entity(apple.x,apple.y,apple.symbol)
            print("#"*25)           
            self.field.draw()
            sleep(0.1)
            

test = Game()
test.play_game()

# sleep(2)
# clear()
