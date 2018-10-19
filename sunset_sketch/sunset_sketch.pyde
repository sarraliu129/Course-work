# while loop
# increase variable
#use draw() for animation
import time
def setup():
    size (640, 480)

x = 0
y = 0

def setup():
    size(640, 480)


def draw():
    global x
    global y
    noStroke()
    if x >= 640:
        x = 0
    background(230, 153, 0)
    x += 1
    fill(250, 250, 250)
    ellipse(x, height / 5, 50 , 50 )
    ellipse (x + 35, height / 5 , 70 , 50)
    ellipse (x - 35, height / 5 + 15, 65, 50 )
    ellipse (x - 10, height / 5 - 15, 65, 50 )
    ellipse (x, height / 5, 50, 50)
    
    fill(0, 30, 179)
    rect(0, 350, 700 , 250)
    
    if y < 480:
         y += 1
         fill(255, 255, 25)
         ellipse(width/2, 350 - y, 70, 70)
         time.sleep(0.5)

    
    
