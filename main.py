# ------------------------------------------------------------------------------------
# Import statements
# ------------------------------------------------------------------------------------
import pygame, sys
from pygame.locals import QUIT
import random
import math

# ------------------------------------------------------------------------------------
# Initialize Variables
# ------------------------------------------------------------------------------------
score = 0
width = 400                                          # Screen width
height = 300                                         # Screen height
my_yellow = (255,190,50)                             # Yellow screen
my_red = (255,0,0)                                   # Red ball
my_green = (0,255,0)                                 # Gren ball
ball_size = 15                                       # Ball size
ballX = width/2                                      # Ball x position mid-screen
ballY = height/2                                     # Ball y position mid-screen
appleX = random.randrange(10,width-10)               # Choose ramdom apple x position
appleY = random.randrange(10,height-10)              # Choose random apple y position

# ------------------------------------------------------------------------------------
# Initialize pygame
# ------------------------------------------------------------------------------------
pygame.init()              
SCREEN = pygame.display.set_mode((width, height))    # Create screen with givenn size
pygame.display.set_caption('Hello Callum!')           # Screen caption

# ------------------------------------------------------------------------------------
# Forever loop
# ------------------------------------------------------------------------------------

while True:
    # Check for key input.
    keys = pygame.key.get_pressed()                  # get key press. Assign to 'keys'

    # Check events for quit
    for event in pygame.event.get():                 # Step through events
        if event.type == QUIT:                       # If event is quit, then quit.
            pygame.quit()
            sys.exit()

    # Paint screen background yellow 
    SCREEN.fill(my_yellow)                      

    # Determine how to move the ball based on key pressed
    if keys[pygame.K_RIGHT]:
      ballX += 0.1
    if keys[pygame.K_LEFT]:
      ballX -= 0.1
    if keys[pygame.K_UP]:
      ballY -= 0.1
    if keys[pygame.K_DOWN]:
      ballY += 0.1

    # Check for collision between ball and apple and increase score.
    if math.dist((appleX, appleY),(ballX, ballY)) <=(2*ball_size):
      appleX = random.randrange(ball_size, width - ball_size)
      appleY = random.randrange(ball_size, height - ball_size)
      score+=1
      print(score)
      pygame.display.set_caption('Score is: ' + str(score))     # Screen caption

    # Draw the red apple and green ball
    pygame.draw.circle(SCREEN,(my_red),(appleX, appleY),ball_size)
    pygame.draw.circle(SCREEN,(my_green),(ballX, ballY ), ball_size )
  
    # Update the display
    pygame.display.update()