#!/usr/bin/python
# Speed of Stars Version 1.1
# Made by: Zac Pez
# Last Modified: Nov 26, 2012
# Inspired from Dave Wessels Demo Lab2 on python 


# Display an initial message in the command window
print "Speed of Stars - Version 1.1"

# Include (import) any required modules
import os
import getpass
import math
import time
import pygame
from pygame.locals import *

# The change directory will only work while on a machine at VIU
os.chdir("/home/student/pezzd/DiscoveryDays/speedofstars/")


name = getpass.getuser() #raw_input('Enter your name: ')

# Initialize pygame
pygame.init()
pygame.display.set_caption("Speed of Stars")

# Set an initial size for the game display,
#     and open the display
textColour = (32, 128, 192)
screenSize = width,height = 800,600
display = pygame.display.set_mode(screenSize)

# Initial speed of the Star
speed = [1,1]
sspeed = str(math.sqrt(speed[0]*speed[0]+ speed[1]*speed[1]))
myfont = pygame.font.SysFont("Comic Sans MS", 30)
label = myfont.render(sspeed, 1, textColour)

# Show Intro for a few Seconds
IntroPNG = pygame.image.load("images/Intro.png")
IntroBox = IntroPNG.get_rect()
display.blit(IntroPNG, IntroBox)
pygame.display.flip()


# Start in the Menu Select Play or High Scores
MenuPNG = pygame.image.load("images/Menu.png")
MenuBox = MenuPNG.get_rect()
HSPNG = pygame.image.load("images/HS.png")
HSBox = MenuPNG.get_rect()
DiffPNG = pygame.image.load("images/Diff.png")
DiffBox = DiffPNG.get_rect()
DescPNG = pygame.image.load("images/Desc.png")
DescBox = DescPNG.get_rect()
SubPNG = pygame.image.load("images/sub.png")
SubBox = SubPNG.get_rect()

# Give back the difficulty and relevent high scores list based on user selection
def diffSetting():
   display.blit(DiffPNG, DiffBox)
   pygame.display.flip()
   difficulty = False
   while difficulty == False:
      for event in pygame.event.get():
         if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < 140:
               difficulty = True
               highscore = open("highscores", "a+", 0)
               return 0, highscore
            elif y < 260:
               difficulty = True
               highscore = open("highscores_high", 'a+', 0)
               return 10, highscore
            elif y < 390:
               difficulty = True
               highscore = open("highscores_medium", 'a+', 0)
               return 50, highscore
            elif y < 600:
               difficulty = True
               highscore = open("highscores_low", 'a+', 0)
               return 100, highscore
            else:
               print("Must use a Valid difficulty")


# View the current High Scores
def highScoreMenu():
   inHighScores = True
   # Built text from Data
   textHS = ['','','','','','','','','','']
   display.blit(HSPNG, HSBox)
   pygame.display.flip()
   while inHighScores:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            inHighScores = False
         if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < 510:
               inHighScores = False
            else:
               if x < 175:
                  # Open and Print the top ten high scores from highscores_high
                  display.blit(HSPNG, HSBox)
                  pygame.display.flip()
                  os.system("sort -n -r highscores_high -o highscores_high")
                  viewer = open("highscores_high", 'r+')
                  count = 0
                  for line in viewer:
                     if count < 10:
                        textHS[count] = myfont.render(line.rstrip(), 1, textColour)
                        display.blit(textHS[count],(150+count*30, 140+count*30))
                        pygame.display.flip()
                     else:
                        break
                     count = count + 1
                     
               elif x < 430:
                  # Open and Print the top ten high scores from highscores_medium
                  display.blit(HSPNG, HSBox)
                  pygame.display.flip()
                  os.system("sort -n -r highscores_medium -o highscores_medium")
                  viewer = open("highscores_medium", 'r+')
                  count = 0
                  for line in viewer:
                     if count < 10:
                        textHS[count] = myfont.render(line.rstrip(), 1, textColour)
                        display.blit(textHS[count],(150+count*30, 140+count*30))
                        pygame.display.flip()
                     else:
                        break
                     count = count + 1
                     
               elif x < 615:
                  # Open and Print the top ten high scores from highscores_low
                  display.blit(HSPNG, HSBox)
                  pygame.display.flip()
                  os.system("sort -n -r highscores_low -o highscores_low")
                  viewer = open("highscores_low", 'r+')
                  count = 0
                  for line in viewer:
                     if count < 10:
                        textHS[count] = myfont.render(line.rstrip(), 1, textColour)
                        display.blit(textHS[count],(150+count*30, 140+count*30))
                        pygame.display.flip()
                     else:
                        break
                     count = count + 1
                     
               elif x < 800:     
                  # Go back to Main Menu
                  return
              
# Play Speed of Stars with selected Difficulty
def playGame(difficulty):
    # load an image and keep track of the rectangular
    # section of the display it gets placed in
    starImage = pygame.image.load("images/star.png")
    starBox = starImage.get_rect()

    # This keeps cycling through the "while loop"
    #   until the player has clicked the close box
    inGame = True
    start = time.time()
    while inGame:
       # Check for any events that need to be processed,
       #    e.g. the player clicking the close box
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             return sspeed
          if event.type == KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                return sspeed
             if event.key == pygame.K_UP and abs(speed[1]) < 255:
                speed[1] -= 1
             if event.key == pygame.K_DOWN and abs(speed[1]) < 255:
                speed[1] += 1
             if event.key == pygame.K_LEFT and abs(speed[0]) < 255:
                speed[0] -= 1
             if event.key == pygame.K_RIGHT and abs(speed[0]) < 255:
                speed[0] += 1
          if event.type == pygame.MOUSEBUTTONDOWN:
             x, y = event.pos
             if y > 510:
                if x > 550:
                   return sspeed

       # Move the star at its current speed
       starBox = starBox.move(speed)
    
       # flip the horizontal speed value if the star
       #   goes off the left or the right of the display
       if starBox.left < 0 or starBox.right > width:
          speed[0] = - speed[0]
    
       # flip the vertical speed value if the star
       #   goes off the top or the bottom of the display
       if starBox.top < 0 or starBox.bottom > height:
          speed[1] = - speed[1]
    
       # define the colour black (RGB values)
       
       black = abs(int(speed[0])),abs(int(speed[0])),abs(int(speed[1]))
    
       # fill the screen buffer with black
       display.fill(black)
    
       # update the buffer to include the image of the star
       display.blit(starImage, starBox)
       sspeed = str(int(math.sqrt(speed[0]*speed[0]+ speed[1]*speed[1])*300000/360.62))
       label = myfont.render("Speed: " + sspeed + "km/s", 1, textColour)
       display.blit(label, (5, 5))
       
       # redraw the screen from the buffer
       if (time.time() <= start + 4):
          display.blit(DescPNG, (500, 400))
       else:
          display.blit(SubPNG, (550, 510))
       pygame.display.flip()
    
       # pause for 100 milliseconds (one-tenth of a second)
       # before going on to repeat the cycle again
       pygame.time.delay(difficulty)
      
# Main Event loop to handle all of the modules of the game
inMenu = True
start = time.time()
while inMenu:
   inMenu = True
   if time.time() > start + 3:
      display.blit(MenuPNG, MenuBox)
      pygame.display.flip()
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         inMenu = False
      if event.type == MOUSEBUTTONDOWN:
         x, y = event.pos
         if y < 170:
            difficulty, highscore = diffSetting();
            if (difficulty > 0):
               sspeed = playGame(difficulty);
               highscore.write(sspeed + ' km/s: ' + name  + '\n')
            highscore.close()
            
            speed = [1,1]
         elif y < 340:
            highScoreMenu();
         elif y < 510:
            inMenu =False

# End of Script
            
