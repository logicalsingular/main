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
    def up(self):
        self.x-=1
        return 'good'
        
    def down(self):
        self.x+=1
        return 'good'
    def right(self):
        self.y+=1
        return 'good'
    def left(self):
        self.y-=1
        return 'good'

class Game():
    def __init__(self):
        self.field = Field(25,4)
        self.live = True

    def play_game(self):
        # print("Game started!")
        # response = input("Press any key to start or \"x\" for exit: ")
        # if response == "x":
        #     exit()
        # Todolist: 
        # snake moving and control
        # board detecting 
        key = Keyboard()
        head = Entity(0,0,"O")
        apple = Entity(randint(0,3),randint(0,24), "@")

        def switch(argument):
            return {                
                'w': head.up(),     # x =-1 y =0,
                's': head.down(),   # x =+1 y =0,
                'd': head.right(),  # x = 0 y =1,
                'a': head.left(),   # x = 0 y =-1,
                'c': exit()         
            }.get(argument, head.up)

        while True:
            clear()

            self.field.background()
            self.field.add_entity(head.x,head.y,head.symbol)
            self.field.add_entity(apple.x,apple.y,apple.symbol)
            self.field.draw()


            if key.kbhit():
                the_key = key.getchar()
                switch(the_key)

            # clear keyboard buffer
            while key.kbhit():
                key.getchar()


if __name__ == '__main__':
    game = Game()
    game.play_game()