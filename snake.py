from os import system, name
from time import sleep 
from random import randint
import curses

def clear():
    # Clear command line
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
        # Generates field
        self.field = [["x"] * self.width for i in range(self.length)]
        
    def add_entity(self,x,y,s):
        # Add entity to field
        self.field[x][y] = s
        
    def draw(self):
        # Draw generated field with entity
        print(u'\u2554'+u'\u2550'*self.width+u'\u2557')
        for x in range(self.length):
            print(u'\u2551',end= '')
            for y in range(self.width):
                print(self.field[x][y],end = '')
            print(u'\u2551')
        print(u'\u255a'+u'\u2550'*self.width+u'\u255d')

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
        response = input("Press any key to start or \"x\" for exit: ")
        if response == "x":
            exit()
        while True:
            # Todolist: 
            # snake moving and control
            # board detecting 

            head = Entity(1,0,"O")
            apple = Entity(randint(0,3),randint(0,24), "@")
            while True:
                clear()

                self.field.background()
                self.field.add_entity(head.x,head.y,head.symbol)
                self.field.add_entity(apple.x,apple.y,apple.symbol)
                self.field.draw()
                
                sleep(0.1)
            

test = Game()
test.play_game()