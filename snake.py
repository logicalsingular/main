from os import system, name
from time import sleep 
from random import randint
import msvcrt

def clear():
    # Clear command line
    if name == "nt":
        system('cls')
    else:
        system('clear')

class Keyboard():
    def getchar(self):
        # Returns a keyboard character after kbhit() has been called.
        return msvcrt.getch().decode('utf-8')

    def kbhit(self):
        # Returns True if keyboard character was hit, False otherwise.
        return msvcrt.kbhit()

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
        # response = input("Press any key to start or \"x\" for exit: ")
        # if response == "x":
        #     exit()
        # Todolist: 
        # snake moving and control
        # board detecting 
        key = Keyboard()
        head = Entity(0,0,"O")
        apple = Entity(randint(0,3),randint(0,24), "@")

        while True:
            clear()

            self.field.background()
            self.field.add_entity(head.x,head.y,head.symbol)
            self.field.add_entity(apple.x,apple.y,apple.symbol)
            self.field.draw()
            # need switch case
            if key.kbhit():
                if key.getchar() == 'w':
                    head.x+=-1
                    head.y+=0     
                elif key.getchar() == 's':
                    head.x+=1
                    head.y+=0
                elif key.getchar() == 'd':
                    head.x+=0
                    head.y+=1
                elif key.getchar() == "a":
                    head.x+=0
                    head.y+=-1         
                else:
                    pass           

            

test = Game()
test.play_game()