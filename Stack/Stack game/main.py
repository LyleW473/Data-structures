# Import modules
import pygame, sys, random, os
from pygame.locals import *
from functions import *

# Initialise pygame
pygame.init()
clock = pygame.time.Clock()

# Game variables
time_counter = 5000 # 30 seconds in milliseconds
user_text = "" # Holds the numbers that the user types into the input box 
user_input_rectangle = pygame.Rect((screen_width / 2) - 100, screen_height - 90, 200, 50) # User input box rectangle
player_score = 0 # The score the player currently has
starting_setup = True
answered_correctly = 0 # 1 = Correct, -1 = Incorrect


# Check if a text file called "high_score" exists
if os.path.exists('high_score.txt'):
    # Read the contents of the file:
    with open('high_score.txt', 'r') as high_score_file:
        # Set the high score to be the value inside that file
        high_score = int(high_score_file.read())
# If it doesn't exist
else:
    # Set the high score as 0
    high_score = 0

# Placeholder values for these items 
stack = 0
current_question = 0
current_question_answer = 0
question_answered_time = 0

# Main loop
run = True
while run:
    
    clock.tick(60)

    # Menu browsing and updating
    if menu.in_game == False:
        # Find the position of the mouse
        pos = pygame.mouse.get_pos()
        # Update the menu, feeding the clicked variable and mouse position into the function
        menu.update(pos) # Set the clicked variable as the returned value from the menu

        # Only if we are in the paused menu, should we draw a "faded" timer
        if menu.show_paused_menu == True:
            draw_alpha_text(str(round(time_counter / 1000, 2)), time_font, BLACK, 390, 0)   

        # Check if the player has requested to restart the game
        if menu.reset_game == True:
            # Reset all of the game variables
            time_counter, player_score, stack, user_text, starting_setup = reset_game(time_counter, player_score, stack, user_text, starting_setup)
            
            # Reset the current modes (In case the player wants to try a different mode)
            menu.maths_mode = False
            menu.spelling_mode = False
            
            # Now that the game has been reset, set this variable back to False
            menu.reset_game = False 

    # Game 1 (Reach the goal element)
    time_counter, user_text, player_score, starting_setup, answered_correctly, high_score, stack, current_question, current_question_answer, question_answered_time = game_v1(time_counter, user_text, user_input_rectangle, player_score, starting_setup, answered_correctly, high_score, stack, current_question, current_question_answer, question_answered_time)


    pygame.display.update()
