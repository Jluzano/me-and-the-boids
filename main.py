import tkinter as tk
import random
import math

# List of boids
boids = []

class Boid:
    def __init__(self, x, y, size, speedx, speedy, canvas):
        self.x = x
        self.y = y
        self.size = size
        self.speedx = speedx
        self.speedy = speedy
        self.canvas = canvas
        # Top left corner of the oval at (x - size, y - size), bottom right corner at (x + size, y + size)
        self.circle = canvas.create_oval(x - size, y - size, x + size, y + size, fill='white')

    # Movement function for the boid
    def move(self):
        self.x += self.speedx
        self.y += self.speedy
        # Checks if the boid has touched the sides of the canvas
        if self.x > self.canvas.winfo_width() - self.size or self.x < 0 + self.size:
            # Moves in the other direction
            self.speedx = -self.speedx
        # Checks if the boid has touched the top or bottom of the canvas
        if self.y > self.canvas.winfo_height() - self.size or self.y < 0 + self.size:
            self.speedy = -self.speedy
        # Updates the boid on the canvas
        self.canvas.move(self.circle, self.speedx, self.speedy)
    
    def alignment(self):
        avgx = 0
        avgy = 0
        count = 0
        for boid in boids:
            # Calculates the distance between itself and other boids around it
            distance = math.dist([self.x, self.y], [boid.x, boid.y])
            if boid != self and distance < 50:
                avgx += boid.speedx
                avgy += boid.speedy
                count += 1
        # Calculates the average speed and assigns it to the boid
        if count > 0:
            avgx /= count
            avgy /= count
            self.speedx = avgx
            self.speedy = avgy
                

        

def update():
    # Constantly calls the move function to move the boids
    for boid in boids:
        boid.alignment()
        boid.move()
    canvas.after(10, update)

# Creating the canvas
root = tk.Tk()
# Canvas is 800 x 600
canvas = tk.Canvas(root, width = 800, height = 600, bg='black')
canvas.pack()

# Creating a number of boids
for i in range(10):
    # Spawns boids in random places on the canvas
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    # Set a random velocity to each boid
    randx = random.randint(3, 5)
    randy = random.randint(3, 5)
    # Determining the size of the boid
    boid = Boid(x, y, 10, randx, randy, canvas)
    boids.append(boid)

update()
root.mainloop()
