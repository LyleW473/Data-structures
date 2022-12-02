# Import modules
import pygame, sys, random, os
from pygame.locals import *
from functions import *

# Initialise pygame
pygame.init()
clock = pygame.time.Clock()

# Game variables
time_counter = 30000 # 30 seconds in milliseconds
time_counter_2 = 8000 # The time counter for game 2
user_text = "" # Holds the numbers that the user types into the input box 
user_input_rectangle = pygame.Rect((screen_width / 2) - 100, screen_height - 90, 200, 50) # User input box rectangle
player_score = 0 # The score the player currently has
starting_setup = True
answered_correctly = 0 # 1 = Correct, -1 = Incorrect

# Check if a text file called "high_score_1" exists
if os.path.exists('high_score_1.txt'):
    # Read the contents of the file:
    with open('high_score_1.txt', 'r') as high_score_file:
        # Set the high score to be the value inside that file
        high_score = int(high_score_file.read())
# If it doesn't exist
else:
    # Set the high score as 0
    high_score = 0


# Check if a text file called "high_score_2" exists
if os.path.exists('high_score_2.txt'):
    # Read the contents of the file:
    with open('high_score_2.txt', 'r') as high_score_2_file:
        # Set the high score to be the value inside that file
        high_score_2 = int(high_score_2_file.read())
# If it doesn't exist
else:
    # Set the high score as 0
    high_score_2 = 0


# Placeholder values for these items 
stack = 0
current_question = 0
current_question_answer = 0
question_answered_time = 0
threshold_height = 0
threshold_height_tuples = ( (1, 592), (2, 512), (3, 432), (4, 352), (5, 272) )
last_threshold_height = 0
permanent_time_decrement = 0

# Main loop
run = True
while run:
    
    # Limit the FPS to 60
    clock.tick(60)

    # Menu browsing and updating
    if menu.in_game == False:
        # Find the position of the mouse
        pos = pygame.mouse.get_pos()
        # Update the menu, feeding the clicked variable and mouse position into the function
        menu.update(pos) # Set the clicked variable as the returned value from the menu

        # Only if we are in the paused menu, should we draw a "faded" timer
        if menu.show_paused_menu == True:
            # If we paused the game from the "goal element" game
            if menu.game_v1 == True:
                draw_alpha_text(str(round(time_counter / 1000, 2)), time_font, BLACK, 390, 0)   
            # If we paused the game from the "goal height" game
            elif menu.game_v2 == True:
                draw_alpha_text(str(round(time_counter_2 / 1000, 2)), time_font, BLACK, 390, 0)   

        # Check if the player has requested to restart the game
        if menu.reset_game == True:
            # Check which game called the reset function
            if menu.game_v1 == True:
                # Reset all of the game variables
                time_counter, player_score, stack, user_text, starting_setup = reset_game(time_counter, player_score, stack, user_text, starting_setup)
            elif menu.game_v2 == True:
                # Reset all of the game variables
                time_counter_2, player_score, stack, user_text, starting_setup, permanent_time_decrement = reset_game(time_counter_2, player_score, stack, user_text, starting_setup, permanent_time_decrement)

            # Reset the current modes (In case the player wants to try a different mode)
            menu.maths_mode = False
            menu.spelling_mode = False
            menu.game_v1 = False
            menu.game_v2 = False
            
            # Now that the game has been reset, set this variable back to False
            menu.reset_game = False 

    # Game 1 (Reach the goal element)
    if menu.game_v1 == True:
        time_counter, user_text, player_score, starting_setup, answered_correctly, high_score, stack, current_question, current_question_answer, question_answered_time = game_v1(time_counter, user_text, user_input_rectangle, player_score, starting_setup, answered_correctly, high_score, stack, current_question, current_question_answer, question_answered_time)
    
    # Game 2 (Reach the goal height by pushing and popping elements)
    if menu.game_v2 == True:
        time_counter_2, user_text, player_score, starting_setup, answered_correctly, high_score_2, stack, current_question, current_question_answer, question_answered_time, threshold_height, threshold_height_tuples, last_threshold_height, permanent_time_decrement = game_v2(time_counter_2, user_text, user_input_rectangle, player_score, starting_setup, answered_correctly, high_score_2, stack, current_question, current_question_answer, question_answered_time, threshold_height, threshold_height_tuples, last_threshold_height, permanent_time_decrement)
   
    # Event handler
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


    pygame.display.update()
