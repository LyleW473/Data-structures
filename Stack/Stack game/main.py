# Import modules
import pygame, sys, random, os
from pygame.locals import *
#from Menus import Menu
#from stack import Stack
from functions import *

# Initialise pygame
pygame.init()

# Game variables
time_counter = 5000 # 30 seconds in milliseconds
user_text = "" # Holds the numbers that the user types into the input box 
user_input_rectangle = pygame.Rect((screen_width / 2) - 100, screen_height - 90, 200, 50) # User input box rectangle
player_score = 0 # The score the player currently has
starting_setup = True

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

# Main loop
run = True
while run:
    # print("maths", menu.maths_mode)
    # print("spellign",menu.spelling_mode)

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


    # INGAME
    if menu.in_game == True:
        screen.fill(GREY)   
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # TIME
        # Draw the timer at the top of the screen
        draw_text(str(round(time_counter / 1000, 2)), time_font, BLACK, 390, 0)

        # Constantly check the time
        if pygame.time.get_ticks() - menu.entered_game_time > 1:
            # The time should be (the time counter + any time that the player spent in the menu) - (the amount of time that its been since the last check)
            time_counter = (time_counter + menu.menu_times_dictionary["in_menu_time"]) - (pygame.time.get_ticks() - menu.entered_game_time)

            # Reset the values of all the menu times.
            menu.menu_times_dictionary.update({"in_menu_time": 0, "entered_menu_time": 0})

            # Set the current time to now so that we can keep checking the time
            menu.entered_game_time = pygame.time.get_ticks()
            
            # If the time counter has gone below 0
            if time_counter <= 0:
                # The player has lost, so go out of the game and into the restart menu
                menu.in_game = False
                # Show the restart menu
                menu.show_restart_menu = True

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # SCORE
        # If the player's current score is greater than the high score
        if player_score > high_score:
            # Set the high score as the player's current score
            high_score = player_score
            # Write the score into a new file 
            with open("high_score.txt", "w") as high_score_file:
                high_score_file.write(str(high_score))

        # Drawing the high score onto the screen
        draw_text("High score:", score_font, WHITE, 50, 660)
        draw_text(str(high_score), score_font, WHITE, 205, 661)

        # Drawing the score onto the screen
        draw_text("Score:", score_font, WHITE, 50, 710)
        draw_text(str(player_score), score_font, WHITE, 140, 711)
        
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # STACK GAMEPLAY
        # Check if we need to update the stack (The player has reached the goal node)

        if starting_setup == True:
            # Starting stack:
            # Generate a random list for the stack
            random_stack_list = random_stack_list_generator()
            # Create a new stack instance, feeding in the stack list as a parameter
            stack = Stack(random_stack_list)
    
            # Create the starting question 
            current_question_answer, current_question = ask_question(list_of_words)

            starting_setup = False
        
        if stack.update_stack_list == True:
            
            # Increment the score
            player_score += 1

            # Update the stack list (with a new player position and new goal element)
            new_stack_list = random_stack_list_generator()
            stack.update_stack(new_stack_list)  

            # We no longer need to spawn a stack so reset this variable
            stack.update_stack_list = False

        # Draw the stack
        stack.draw()

        # Draw the current question at the top of the screen
        draw_text(current_question, question_font, WHITE, 390, 120)

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # USER INPUT
        text_image = user_input_font.render(user_text, True, BLACK)
        pygame.draw.rect(screen, WHITE, user_input_rectangle, 0)
        pygame.draw.rect(screen, BLACK, user_input_rectangle, 5)
        screen.blit(text_image, (user_input_rectangle.x + 10, user_input_rectangle.y + 8))
        user_input_rectangle.width = max(200, text_image.get_width() + 20)

        # Note: This has been moved out of the event handler so that players can delete their input without pressing the backspace multiple times
        key = pygame.key.get_pressed()
        # If the backspace key is pressed and the user text is not empty
        if key[K_BACKSPACE] and len(user_text) > 0:
            # Wait some time (Otherwise it will seem like the text is being deleted instantly)
            pygame.time.delay(50)
            # Remove the last item inside the text
            user_text = user_text[:-1]

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

                # --------------------------------------------------------------------------------------------------
                # QUESTION INPUT

                # If the player wants to travel up the stack
                if event.key == K_RIGHTBRACKET and len(user_text) > 0 and user_text != "-":
                    # Check if the user input is the same as the answer

                    if menu.maths_mode == True:
                        if int(user_text) == current_question_answer :
                            print("Correct")
                            # Move the player up the stack 
                            stack.travel_up()

                            # Generate a new question
                            current_question_answer, current_question = random_maths_question_generator()

                        else:
                            print("Incorrect")
                        
                        # Reset the user text (regardless if it was correct or incorrect)
                        user_text = ""

                    elif menu.spelling_mode == True:
                        # Check if the user input is the same as the answer
                        if user_text == current_question_answer:
                            print("Correct")

                            # Move the player down the stack
                            stack.travel_up()

                            # Generate a new question
                            current_question_answer, current_question = random_spelling_question_generator(list_of_words)

                        else:
                            print("Incorrect")
                            
                        # Reset the user text (regardless if it was correct or incorrect)
                        user_text = ""

                # If the player wants to travel down the stack
                elif event.key == K_HASH and len(user_text) > 0 and user_text != "-":

                    if menu.maths_mode == True:
                        # Check if the user input is the same as the answer
                        if int(user_text) == current_question_answer:
                            print("Correct")

                            # Move the player down the stack
                            stack.travel_down()

                            # Generate a new question
                            current_question_answer, current_question = random_maths_question_generator()

                        else:
                            print("Incorrect")
                            
                        # Reset the user text (regardless if it was correct or incorrect)
                        user_text = ""
                        
                    elif menu.spelling_mode == True:
                        # Check if the user input is the same as the answer
                        if user_text == current_question_answer:
                            print("Correct")

                            # Move the player down the stack
                            stack.travel_down()

                            # Generate a new question
                            current_question_answer, current_question = random_spelling_question_generator(list_of_words)

                        else:
                            print("Incorrect")
                            
                        # Reset the user text (regardless if it was correct or incorrect)
                        user_text = ""

                # If the player has pressed any other key
                else:   
                    # Check which mode the player is in
                    if menu.maths_mode == True:
                        # Check the unicode number of the key. If it is a number from 0 to 9 or is the "-" symbol
                        if 48 <= event.key <= 57 or event.key == 45:
                            # Check that the player hasn't written more than 20 digits
                            if len(user_text) <= 20:
                                # Contacenate the key the user pressed to the user text
                                user_text += event.unicode
                    
                    elif menu.spelling_mode == True:
                        # Check that the key pressed is in the alphabet (a - z)
                        if 97 <= event.key <= 123:
                            print(event.key)
                            # Check that the player hasn't written more than 20 digits
                            if len(user_text) <= 20:
                                # Contacenate the key the user pressed to the user text
                                user_text += event.unicode






    pygame.display.update()
