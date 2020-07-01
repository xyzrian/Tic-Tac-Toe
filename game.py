import pygame
import sys
import time
from pygame.locals import *

#Colour definitions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

#Screen size, icon, window name, image uploads/transformations
screen = pygame.display.set_mode((600, 700)) #Display screen size

fps = 25

pygame.display.set_caption("Otaku-Tac-Toe") #Screen name

game_icon = pygame.image.load('pixel_icon.png') #Uploading game icon
pygame.display.set_icon(game_icon) #Setting game icon

launch = pygame.image.load('launch.png')

background_img = pygame.image.load('background.png') #Uploading the background image

x_img = pygame.image.load('x_img.png') #Uploading the "X" image
x_img = pygame.transform.scale(x_img, (175, 175)) #Scaling the "X" image

o_img = pygame.image.load('o_img.png') #Uploading the "O" image
o_img = pygame.transform.scale(o_img, (175, 175)) #Scaling the "O" image

#For main program loop
X_or_O = 'x'
winner = None
draw = False
clock = pygame.time.Clock()

grid = [None]*9 #Tic tac toe grid as a list

#Functions
def launching_window():
    screen.blit(launch, (0, 0)) #Blits launch image to screen

    pygame.display.update()
    time.sleep(3) #3 second wait

    screen.fill(WHITE) #Clears screen
    screen.blit(background_img, (0, 0)) #Blits the background image onto the white screen
    for x in range(200, 600, 200): #Drawing the vertical lines
        pygame.draw.line(screen, WHITE, [x, 0], [x, 600], 5) #Parameters: window, colour, starting point, end point, thickness
    for x in range(200, 600, 200): #Drawing the horizontal lines
        pygame.draw.line(screen, WHITE, [0, x], [600, x], 5)
        
    pygame.display.flip() #Updates the user screen with the above drawing commands
    clock.tick(30) #30 frames per second
    whose_turn() #Runs the whose_turn() function

def whose_turn(w=None): #Switches turns until a winner is declared 
    global draw
    message = ""
    if w is None and all(grid):
        draw = True
        message = "Game has ended in a draw."
    elif w is None:
        message = "Yuno says it's " + X_or_O.upper() + "'s Turn!"
    else:
        if w is True:
            message = "X has won the game!"
        elif w is False:
            message = "O has won the game!"

    font = pygame.font.Font(None, 45)
    text = font.render(message, 1, BLACK)

    overlay_msg = pygame.Surface((600,100))  # Transparent rectangle will be layed over game to display win/draw message
    overlay_msg.fill((255,255,255))           # Fills this rectangle in white
    screen.blit(overlay_msg, (0, 600))    # Top left coords of rectangle 
    screen.blit(text, (50, 640))            # Blits the text
    pygame.display.flip()
    
def check_win(grid): #Win conditions
    winner = None
    if grid[0] == grid[1] == grid[2] and grid[0] != None:
        if grid[0] == "x":
            winner = True #winner = True if 'x' wins
        elif grid[0] == "o":
            winner = False #winner = False if 'o' wins
    elif grid[3] == grid[4] == grid[5] and grid[3] != None:
        if grid[3] == "x":
            winner = True
        elif grid[3] == "o":
            winner = False 
    elif grid[6] == grid[7] == grid[8] and grid[6] != None:
        if grid[6] == "x":
            winner = True
        elif grid[6] == "o":
            winner = False 
    elif grid[0] == grid[4] == grid[8] and grid[0] != None:
        if grid[0] == "x":
            winner = True
        elif grid[0] == "o":
            winner = False 
    elif grid[2] == grid[4] == grid[6] and grid[2] != None:
        if grid[2] == "x":
            winner = True
        elif grid[2] == "o":
            winner = False 
    elif grid[1] == grid[4] == grid[7] and grid[1] != None:
        if grid[1] == "x":
            winner = True
        elif grid[1] == "o":
            winner = False 
    elif grid[2] == grid[5] == grid[8] and grid[2] != None:
        if grid[2] == "x":
            winner = True
        elif grid[2] == "o":
            winner = False 
    elif grid[0] == grid[3] == grid[6] and grid[0] != None:
        if grid[0] == "x":
            winner = True
        elif grid[0] == "o":
            winner = False
    elif all(grid) and winner == None:
            draw = True 
    else:
        return None #If winner = None, no winner has been determined
    return winner 

def display_moves(space, win):
    global grid, X_or_O

    place_imgx = 12 #Places the X or O image 12 pixels from the left of the screen
    place_imgy = 12 #Places the X or O image 12 pixels from the top of the screen
    
    if space == 1:
        posx = (place_imgx, place_imgy)

    if space == 2:
        posx = (place_imgx + 200, place_imgy)

    elif space == 3:
        posx = (place_imgx + 400, place_imgy)

    elif space == 4:
        posx = (place_imgx, place_imgy + 200)

    elif space == 5:
        posx = (place_imgx + 200, place_imgy + 200)

    elif space == 6:
        posx = (place_imgx + 400, place_imgy + 200)

    elif space == 7:
        posx = (place_imgx, place_imgy + 400)

    elif space == 8:
        posx = (place_imgx + 200, place_imgy + 400)

    elif space == 9:
        posx = (place_imgx + 400, place_imgy + 400)

    if draw == False:
        grid[space -1] = X_or_O
        if X_or_O == 'x':
            win.blit(x_img, posx)
            X_or_O = 'o' #Changes to O's turn

        elif X_or_O == 'o':
            win.blit(o_img, posx)
            X_or_O = 'x' #Changes to X's turn

##    if draw == True:
##        X_or_O = None
##        whose_turn(w=0)
    
    pygame.display.flip()
    

def user_click(screen, grid): #Registers user-clicks based on the grid
    x, y = pygame.mouse.get_pos()
    if (x < 600/3) and (y < 600/3) and grid[0] == None:
        space = 1

    elif (x < 600/3*2) and (y < 600/3) and grid[1] == None:
        space = 2

    elif (x < 600) and (y < 600/3) and grid[2] == None:
        space = 3

    elif (x < 600/3) and (y < 600/3*2) and grid[3] == None:
        space = 4

    elif (x < 600/3*2) and (y < 600/3*2) and grid[4] == None:
        space = 5

    elif (x < 600) and (y < 600/3*2) and grid[5] == None:
        space = 6

    elif (x < 600/3) and (y < 600) and grid[6] == None:
        space = 7

    elif (x < 600/3*2) and (y < 600) and grid[7] == None:
        space = 8

    elif (x < 600) and (y < 600) and grid[8] == None:
        space = 9

    else:
        space = None


    display_moves(space, screen) #Places the correct image on the grid
    return check_win(grid) #Checks for a win

def reset_game(): #Runs in the infinite loop to reset the game 
    global grid, winner, X_or_O, draw
    time.sleep(1)
    X_or_O = 'x'
    draw = False
    winner = None
    grid = [None]*9
    launching_window()

launching_window()

while(True):
    whose_turn()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            winner = user_click(screen, grid)
            whose_turn(winner)
            if winner != None or draw:
                reset_game()

    pygame.display.flip()
    clock.tick(fps)
