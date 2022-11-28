# Import modules
import pygame, sys, random
from pygame.locals import *
from Menus import Menu
from stack import Stack


# Initialise pygame
pygame.init()

# Screen
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

# Font
time_font = pygame.font.SysFont("Bahnschrift", 150)

# Game variables
time_counter = 5000 # 5 seconds in milliseconds
spawn_stack = True # Determines whether we create a new stack instance or not

# Instances
menu = Menu(0,0,screen)


def draw_text(text, font, text_colour, x, y):
    image = font.render(text, True, text_colour)
    screen.blit(image, (x, y))


def draw_alpha_text(text, font, text_colour,  x, y):
    alpha_text = font.render(text, True ,text_colour)
    alpha_text.set_alpha(70)
    screen.blit(alpha_text,(x,y))

def random_stack_list_generator():
    stack_list = []
    # Generate a random index, which will represent the index for the element where the player must reach before the time is up.
    random_index = random.randrange(0,5)

    # Create a stack list with 6 elements
    for i in range(0, 6):
        # If the current index is not equal to the random index we generated earlier, set the item value as 0
        if i != random_index:
            item_value = 0
        # Otherwise, set the item value as 1.
        else:
            item_value = 1
        # Append the items to the list used in the stack
        stack_list.append(item_value)

    return stack_list

# Instances

# Main loop
run = True
while run:

    # Menu browsing and updating
    if menu.in_game == False:
        # Find the position of the mouse
        pos = pygame.mouse.get_pos()
        # Update the menu, feeding the clicked variable and mouse position into the function
        menu.update(pos) # Set the clicked variable as the returned value from the menu

        # Only if we are in the paused menu, should we draw a "faded" timer
        if menu.show_paused_menu == True:
            draw_alpha_text(str(round(time_counter / 1000, 2)), time_font, BLACK, 360, 0)


    # INGAME
    if menu.in_game == True:
        screen.fill(BLUE)   

        # Draw the timer at the top of the screen
        draw_text(str(round(time_counter / 1000, 2)), time_font, BLACK, 360, 0)

        # Constantly check the time
        if pygame.time.get_ticks() - menu.entered_game_time > 1:
            # The time should be (the time counter + any time that the player spent in the menu) - (the amount of time that its been since the last check)
            time_counter = (time_counter + menu.menu_times_dictionary["in_menu_time"]) - (pygame.time.get_ticks() - menu.entered_game_time)

            # Reset the values of all the menu times.
            menu.menu_times_dictionary.update({"in_menu_time": 0, "entered_menu_time": 0})

            # Set the current time to now so that we can keep checking the time
            menu.entered_game_time = pygame.time.get_ticks()
            
            # If the time counter has gone below 0, reset it again
            if time_counter <= 0:
                time_counter = 5000

        # Check if we need to spawn a stack.
        if spawn_stack == True:
            # Generate a random list for the stack
            random_stack_list = random_stack_list_generator()
            # Create a new stack instance, feeding in the stack list as a parameter
            stack = Stack(random_stack_list)
            # We no longer need to spawn a stack so reset this variable
            spawn_stack = False

        # Draw the stack
        stack.draw()

    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()

        # Check if the mouse button has been pressed
        if event.type == MOUSEBUTTONDOWN:
            # Check if the mouse button clicked was the left click
            if event.button == 1: # (1 = left, 2 = middle, 3 = right, 4 = scroll up, 5 = scrolldown)
                menu.clicked = True

        # Check if a key has been pressed
        if event.type == KEYDOWN:
            # Check if we are in game
            if menu.in_game == True:    
                # If the ESC key is pressed
                if event.key == K_ESCAPE:
                    # Show the paused menu
                    menu.show_paused_menu = True
                    menu.in_game = False



    pygame.display.update()
