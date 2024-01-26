import turtle, random
'''
Extra Credit Implemented:
-Optimize game speed using turtle.tracer(0,0) and turtle.update()
-No direction reversal by adding conditionals into movement methods
-Multiple Speeds by binding 1,2,3 to changes in the gameloop refresh speed
-"r" button resets game and allows for restart
'''

'''
Purpose:
This class represents the game itself and is ran to intialize all snake and food objects, as well as the design of the game board
Instance Variables:
self.player - represents the snake that the user controls
self.food - represents the food object that the player interacts with and moves towards in order to grow
self.num - a number that changes and allows for the changing of speeds within the game
Methods:
__init__:
    intializes the game board itself, as well as specializing the conditions at which the turtle will operate (tracer, speed, delay, coordinates, etc,)
    also creates objects of the snake and food class to start the game
    runs gameloop function and checks for keypress events to allow user to interact
one:
    sets speed to fast
two:
    sets speed to med.
three:
    sets speed to slow
gameloop:
    moves the snake, checks for collisions the snake makes, and updates conditionally to avoid redundancy
    does all these things on a timer set by the "one","two", and "three" methods
restart:
    clears the board and resets the length of the snake to one and its position to the middle
'''
class Game:
    def __init__(self):
        #Setup 700x700 pixel window
        turtle.clearscreen()
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.tracer(0, 0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)

        self.player = Snake(315,315,'green')
        self.food = Food("red")
        self.num = 100

        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.one, '1')
        turtle.onkeypress(self.two, '2')
        turtle.onkeypress(self.three, '3')
        turtle.onkeypress(self.restart, 'r')
        turtle.listen()
        turtle.mainloop()

    def one(self):
        self.num = 50
    def two(self):
        self.num = 100
    def three(self):
        self.num = 200

    def gameloop(self):
        self.player.move(self.food)
        self.player.collision()
        turtle.update()
        turtle.ontimer(self.gameloop,self.num)

    def restart(self):
        self.player.reset()
        Game()

'''
Purpose:
    The snake class represents the players snake within the game.  It is the snake that is controller and eats food to grow.
Instance Variables:
    self.x - represents the x position of the head of the snake
    self.y - represents the y position of the head of the snake
    self.color - represents the color of the snake
    self.segments - a list that contains each new segment of snake that is added during consumption of food
                  - the list is full of new snake objects
    self.vx&vy: - represnts the distance the snake object will move in the x or y direction each iteration of the move method
Methods:
    __init__: creates all the instance variables of the snake class and also calls grow to start the game with a length of 1
    grow: creates a new square turtle object of the specified color and postion and speed and adds it to the segments list
    reset: decreases size of the snake back to 1 and sets its speed to 0 and position to the middle of the map
           additionally removes the game over in the bottom left by writing game over in white with the font
    go_down,go_left,go_up,go_right:
        these move the snake in the specified direction while not allowing the snake to go backwards within itself
    move: takes in a food object as a parameter and checks to see if the current position of the snake is on a food object and then grows if it is
          moves all turtle objects within the segments list by setting their positon = to the next object within the list
          movement is done by changing the x and y pos. of the head snake by the current vy and vx values
          this moves all snakes towards the head at all times and grows the snake when it runs into a food
    collisions:
        checks at any point if the position of the head snake is the same as any of the rest of the snakes in segments, as well as if the head snake exits the field of play.
        if it is, then game over is written in the bottom left and the snake is stopped

'''
class Snake:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.vx = 30
        self.vy = 0

        self.grow()

    def grow(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.fillcolor(self.color)
        self.t.shape("square")
        self.t.shapesize(1.5,1.5)
        self.t.penup()
        self.t.setpos(self.x,self.y)
        self.segments.append(self.t)

    def reset(self):
        self.vx = 0
        self.vy = 0
        self.x = 315
        self.y = 315
        self.segments = self.segments[:-1]
        self.segments[-1].setpos(self.x,self.y)
        turtle.color('white')
        turtle.write("GAME OVER!!", font = ("Veranda",20,"normal"),align = "left")



    def go_down(self):
        if self.vy != 30:
            self.vx = 0
            self.vy = -30
    def go_up(self):
        if self.vy != -30:
            self.vx = 0
            self.vy = 30
    def go_left(self):
        if self.vx != 30:
            self.vx = -30
            self.vy = 0
    def go_right(self):
        if self.vx != -30:
            self.vx = 30
            self.vy = 0

    def move(self, food):
        if self.x+self.vx == food.x and self.y+self.vy == food.y:
            self.grow()
            food.move()
        for i in range(len(self.segments)-1):
            self.segments[i].setpos(int(self.segments[i+1].xcor()),int(self.segments[i+1].ycor()))
        self.x += self.vx
        self.y += self.vy
        self.segments[-1].setpos(self.x,self.y)

    def collision(self):
        if int(self.segments[-1].xcor()) > 600 or int(self.segments[-1].xcor()) < 0 or int(self.segments[-1].ycor()) < 0 or int(self.segments[-1].ycor()) > 600:
            self.vx = 0
            self.vy = 0
            turtle.write("GAME OVER!!", font = ("Veranda",20,"normal"),align = "left")

        for i in range(len(self.segments)-1):
            if int(self.segments[-1].xcor()) == int(self.segments[i].xcor()) and int(self.segments[-1].ycor()) == int(self.segments[i].ycor()) and len(self.segments) != 1:
                self.vx = 0
                self.vy = 0
                turtle.write("GAME OVER!! ", font = ("Veranda",20,"normal"),align = "left")


'''
Purpose:
Represents the food objects that are within the game
Instance Variables:
    self.x,self.y: represents the x and y positon of the food at any time
    self.color: represents the color of the food
    self.t: the turtle object that represents the food being displayed
Methods:
    __init__: sets the position of the food to any grid aligned position within the game board using 15 + 30*random.randint(0,19)
              also specifies the shape, size, and position of the food
    move: changes the x and y positions of the food object to a new random spot, then sets the positon to those values
'''
class Food:
    def __init__(self,color):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.color = color

        self.t = turtle.Turtle()
        self.t.fillcolor(self.color)
        self.t.shape("circle")
        self.t.shapesize(1.5,1.5)
        self.t.penup()
        self.t.setpos(self.x,self.y)

    def move(self):
            self.x = 15 + 30*random.randint(0,19)
            self.y = 15 + 30*random.randint(0,19)

            self.t.setpos(self.x,self.y)

if __name__ == "__main__":
    Game()
