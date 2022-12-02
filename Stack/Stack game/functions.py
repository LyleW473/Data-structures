import pygame, random, urllib.request, sys
from pygame.locals import *
from Menus import Menu
from stack import Stack, Stack2

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
GREY = (79, 79, 79)

# Font
time_font = pygame.font.SysFont("Bahnschrift", 100)
user_input_font = pygame.font.SysFont("Bahnschrift", 40)
question_font = pygame.font.SysFont("Bahnschrift", 50)
score_font = pygame.font.SysFont("Bahnschrift", 30)

# Retrieve words from a website
words_url = "https://www.mit.edu/~ecprice/wordlist.10000"
get_words = urllib.request.urlopen(words_url)
entire_text = get_words.read().decode()
list_of_words = entire_text.splitlines()



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
    player_random_index = random.randrange(0,5)
    
    # In the case that the player spawning index and the goal index is the same, keep generating new indexes for the player
    while player_random_index == random_index:  
        player_random_index = random.randrange(0,5)

    # Create a stack list with 6 elements
    for i in range(0, 6):
        # If the current index is equal to the random plyae rindex we generated earlier, set the item value as 2
        if i == player_random_index:
            item_value = 2

        # If the current index is equal to the random index we generated earlier, set the item value as 1
        elif i == random_index:
            item_value = 1

        # If the current index is not equal to the random index we generated earlier or the player index, set the item value as 0
        else:
            item_value = 0

        # Append the items to the list used in the stack
        stack_list.append(item_value)

    return stack_list

def random_maths_question_generator():
    # Choose a random operation for the question to have
    random_operation = random.randrange(0,4) # 0 = Addition, 1 = Subtraction, 2 = Multiplication, 3 = Division, 4 = MOD

    # Addition
    if random_operation == 0:
        # Generate random numbers
        random_number_1 = random.randrange(0,20)
        random_number_2 = random.randrange(0,20)

        # Store the answer for the question later
        answer = random_number_1 + random_number_2 
        question = f'{random_number_1} + {random_number_2} = ?'

    # Subtraction
    if random_operation == 1:
        # Generate random numbers
        random_number_1 = random.randrange(0,20)
        random_number_2 = random.randrange(0,20)

        # Store the answer for the question later
        answer = random_number_1 - random_number_2 
        question = f'{random_number_1} - {random_number_2} = ?'   

    # Multiplication
    if random_operation == 2:
        # Generate random numbers
        random_number_1 = random.randrange(1,12)
        random_number_2 = random.randrange(0,12)
        
        # Store the answer for the question later
        answer = random_number_1 * random_number_2 
        question = f'{random_number_1} x {random_number_2} = ?'   

    # Division
    if random_operation == 3:
        # Generate random numbers
        random_number_1 = random.randrange(1,50)
        random_number_2 = random.randrange(1,10)

        # In the case that the the first number is not divisible by the second number
        while random_number_1 % random_number_2 != 0:
            # Generate different random numbers
            random_number_1 = random.randrange(1,50)
            random_number_2 = random.randrange(1,10)

        # Store the answer for the question later
        answer = int(random_number_1 / random_number_2)
        question = f'{random_number_1} divided by {random_number_2} = ?'   

    # MOD
    if random_operation == 4:
        random_number_1 = random.randrange(1,50)
        random_number_2 = random.randrange(1,5)
        # In the case that the first number is lower than the second number
        while random_number_1 < random_number_2:
            # Generate different random numbers
            random_number_1 = random.randrange(1,50)
            random_number_2 = random.randrange(1,5)

        # Store the answer for the question later
        answer = random_number_1 % random_number_2 
        question = f'{random_number_1} MOD {random_number_2} = ?'   

    return answer, question

def random_spelling_question_generator(words_list):
    # Generate a random index (this will choose one random word)
    random_word_index = random.randrange(0, len(words_list) - 1)
    answer = words_list[random_word_index]
    question = f'Spell : {answer}'
    # Return the word
    return answer, question

def ask_question(words_list):
    # Check which mode it is
    # The maths mode will keep asking maths questions when the function is called
    if menu.maths_mode == True:
        answer, question = random_maths_question_generator()
    # The spelling mode will keep asking spelling questions when the function is called
    if menu.spelling_mode == True:
        answer, question = random_spelling_question_generator(words_list)
    return answer, question

def reset_game(time_counter, player_score, stack, user_text, starting_setup, permanent_time_decrement):
    # If the game was reset from game 1
    if menu.game_v1 == True:
        # Reset the timer
        time_counter = 30000
    # If the game was reset from game 2
    elif menu.game_v2 == True: 
        # Reset the timer
        time_counter = 8000    
        # Reset the time decrement
        permanent_time_decrement = 0
        # Reset the instances count of Stack2
        Stack2.instances_count = 0
    
    # Note: The following are the same for both games, this is subject to change.
    # Allow for the starting setup again
    starting_setup = True

    # Reset the player score 
    player_score = 0

    # Delete the current stack instance
    del stack
    # Generate a new starting stack instance
    random_stack_list = random_stack_list_generator()
    stack = Stack(random_stack_list)

    # Reset the user input text
    user_text = ""

    return time_counter, player_score, stack, user_text, starting_setup, permanent_time_decrement

def game_v1(time_counter, user_text, user_input_rectangle, player_score, starting_setup, answered_correctly, high_score, stack, current_question, current_question_answer, question_answered_time):

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
            with open("high_score_1.txt", "w") as high_score_file:
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
            print(current_question_answer, current_question)

           
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
        
        # Draw the correct / incorrect text based on if the player answered the question correctly
        if answered_correctly == 1: # Correct
            if pygame.time.get_ticks() - question_answered_time < 1000:
                # Draw the "Correct" text
                draw_text("Correct!", question_font, GREEN, 100, 390)
        elif answered_correctly == -1: # Incorrect
            if pygame.time.get_ticks() - question_answered_time < 1000:
                # Draw the "Incorrect" text
                draw_text("Incorrect!", question_font, RED, 690, 390)            
            
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
        # Note: This has not been removed because the player still needs to be able to click on buttons in the restart menu. Also additional features which involve the mouse may be included later on.
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
                    # Record the time the player answered the question
                    question_answered_time = pygame.time.get_ticks()        

                    # Check if the user input is the same as the answer
                    if menu.maths_mode == True:
                        if int(user_text) == current_question_answer :
                            # Move the player up the stack 
                            stack.travel_up()
                            # Generate a new question
                            current_question_answer, current_question = random_maths_question_generator()
                            # Set the variable answered correctly to 1 (so that the "correct" text can be displayed)
                            answered_correctly = 1
                        else:
                            # Set the variable answered correctly to -1 (so that the "incorrect" text can be displayed)
                            answered_correctly = -1                   
                        
                    elif menu.spelling_mode == True:
                        # Check if the user input is the same as the answer
                        if user_text == current_question_answer:
                            # Move the player down the stack
                            stack.travel_up()
                            # Generate a new question
                            current_question_answer, current_question = random_spelling_question_generator(list_of_words)
                            # Set the variable answered correctly to 1 (so that the "correct" text can be displayed)
                            answered_correctly = 1
                        else:
                            # Set the variable answered correctly to -1 (so that the "incorrect" text can be displayed)
                            answered_correctly = -1   
                              
                    # Reset the user text (regardless if it was correct or incorrect)
                    user_text = ""

                # If the player wants to travel down the stack
                elif event.key == K_HASH and len(user_text) > 0 and user_text != "-":
                    # Record the time the player answered the question
                    question_answered_time = pygame.time.get_ticks()

                    if menu.maths_mode == True:
                        # Check if the user input is the same as the answer
                        if int(user_text) == current_question_answer:
                            # Move the player down the stack
                            stack.travel_down()
                            # Generate a new question
                            current_question_answer, current_question = random_maths_question_generator()
                            # Set the variable answered correctly to 1 (so that the "Correct" text can be displayed)
                            answered_correctly = 1 
                        else:
                            # Set the variable answered correctly to -1 (so that the "Incorrect" text can be displayed)
                            answered_correctly = -1   
                        
                    elif menu.spelling_mode == True:
                        # Check if the user input is the same as the answer
                        if user_text == current_question_answer:
                            # Move the player down the stack
                            stack.travel_down()

                            # Generate a new question
                            current_question_answer, current_question = random_spelling_question_generator(list_of_words)

                            # Set the variable answered correctly to 1 (so that the "Correct" text can be displayed)
                            answered_correctly = 1 
                        else:
                            # Set the variable answered correctly to -1 (so that the "Incorrect" text can be displayed)
                            answered_correctly = -1                    

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
                            # Check that the player hasn't written more than 20 digits
                            if len(user_text) <= 20:
                                # Contacenate the key the user pressed to the user text
                                user_text += event.unicode
    
    return time_counter, user_text, player_score, starting_setup, answered_correctly, high_score, stack, current_question, current_question_answer, question_answered_time


# Specific to the 2nd game
def random_stack_list_generator_2():
    # Generate a random number for the height of the stack (1 to 6)
    initial_height = random.randrange(1, 6)

    # Create a list full of zeros up until the initial height -1. This is because the final element will be the player.
    stack_list = [0 for i in range(0, initial_height - 1)]

    # Append the player to the list
    stack_list.append(2)
    
    return stack_list


def draw_dashed_lines(height):
    for i in range(0, int(screen_width / 40), 2): # Draws at 0, 2, 4, 6, and so on.
        pygame.draw.line(screen, GREEN, (0 + (40 * i), height), (40 + (40 * i), height), 5)


def game_v2(time_counter_2, user_text, user_input_rectangle, player_score, starting_setup, answered_correctly, high_score_2, stack, current_question, current_question_answer, question_answered_time, threshold_height, threshold_height_tuples, last_threshold_height, permanent_time_decrement):

    # INGAME
    if menu.in_game == True:
        screen.fill(GREY)   
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # TIME
        # Draw the timer at the top of the screen
        draw_text(str(round(time_counter_2 / 1000, 2)), time_font, BLACK, 390, 0)

        # Constantly check the time
        if pygame.time.get_ticks() - menu.entered_game_time > 1:
            # The time should be (the time counter + any time that the player spent in the menu) - (the amount of time that its been since the last check)
            time_counter_2 = (time_counter_2 + menu.menu_times_dictionary["in_menu_time"]) - (pygame.time.get_ticks() - menu.entered_game_time)

            # Reset the values of all the menu times.
            menu.menu_times_dictionary.update({"in_menu_time": 0, "entered_menu_time": 0})

            # Set the current time to now so that we can keep checking the time
            menu.entered_game_time = pygame.time.get_ticks()
            
        # If the time counter has gone below 0
        if time_counter_2 <= 0:

            # Check if the height that the player is at matches with the threshold height generated earlier
            if threshold_height_tuples[len(stack.items_list) - 2][1] == threshold_height:

                # Generate a new threshold height that is different from the last key
                threshold_height = threshold_height_tuples[random.randrange(1,5)][1] 
                
                # In the case that the threshold height is the same as the last height
                while threshold_height == last_threshold_height:
    
                    # Keep generating another random height until they aren't the same
                    threshold_height = threshold_height_tuples[random.randrange(1,5)][1]

                # Set the last threshold height to be the current threshold height
                last_threshold_height = threshold_height


                # Limit the time decrement to be 2 seconds. This means that the player will have 6 seconds no even after 10 "rounds"
                if permanent_time_decrement < 2000:
                    # Increase the time decrement to 0.20 seconds
                    permanent_time_decrement += 200 # Milliseconds
                 
                # Reset the timer and add the permanent time decrement (this is to increase difficulty as time goes on)
                time_counter_2 = 8000 - permanent_time_decrement

                # Generate a new question 
                current_question_answer, current_question = ask_question(list_of_words) 

                # Reset the user text
                user_text = ""

                # Increment the score 
                player_score += 1
                
            else:
                # The player has lost, so go out of the game and into the restart menu
                menu.in_game = False
                # Show the restart menu
                menu.show_restart_menu = True

        # Only do the following if the starting stack has already been spawned
        if Stack2.instances_count > 0:
            # Check if the player is already at the height (This is so that the player isn't just sitting there for several seconds whilst already at the height)
            if threshold_height_tuples[len(stack.items_list) - 2][1] == threshold_height:
                # Generate a new threshold height that is different from the last key
                threshold_height = threshold_height_tuples[random.randrange(1,5)][1] 
                    
                # In the case that the threshold height is the same as the last height
                while threshold_height == last_threshold_height:
        
                    # Keep generating another random height until they aren't the same
                    threshold_height = threshold_height_tuples[random.randrange(1,5)][1]

                # Set the last threshold height to be the current threshold height
                last_threshold_height = threshold_height


                # Limit the time decrement to be 2 seconds. This means that the player will have 6 seconds no even after 10 "rounds"
                if permanent_time_decrement < 2000:
                    # Increase the time decrement to 0.20 seconds
                    permanent_time_decrement += 200 # Milliseconds
                    
                # Reset the timer and add the permanent time decrement (this is to increase difficulty as time goes on)
                time_counter_2 = 8000 - permanent_time_decrement

                # Generate a new question 
                current_question_answer, current_question = ask_question(list_of_words) 

                # Reset the user text
                user_text = ""

                # Increment the score 
                player_score += 1

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # SCORE
        # If the player's current score is greater than the high score
        if player_score > high_score_2:
            # Set the high score as the player's current score
            high_score_2 = player_score
            # Write the score into a new file 
            with open("high_score_2.txt", "w") as high_score_2_file:
                high_score_2_file.write(str(high_score_2))

        # Drawing the high score onto the screen
        draw_text("High score:", score_font, WHITE, 50, 660)
        draw_text(str(high_score_2), score_font, WHITE, 205, 661)

        # Drawing the score onto the screen
        draw_text("Score:", score_font, WHITE, 50, 710)
        draw_text(str(player_score), score_font, WHITE, 140, 711)
        
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # STACK GAMEPLAY
        # Check if we need to update the stack (The player has reached the goal node)

        # The starting set-up 
        if starting_setup == True:
            # Starting stack:
            # Generate a random list for the stack
            random_stack_list = random_stack_list_generator_2()
            # Create a new stack instance, feeding in the stack list as a parameter
            stack = Stack2(random_stack_list)
    
            # Create the starting question 
            current_question_answer, current_question = ask_question(list_of_words)
            print(current_question_answer, current_question)
            
            # Generate a random starting threshold height
            threshold_height = threshold_height_tuples[random.randrange(1,5)][1]

            # Set the previous height to be this one (this is so that later on, we don't get the same height generated twice in a row)
            last_threshold_height = threshold_height

            # The starting set-up is now complete
            starting_setup = False

        if stack.update_stack_list == True:
            
            # Increment the score
            player_score += 1

            # Update the stack list (with a random initial height)
            new_stack_list = random_stack_list_generator_2()
            stack.update_stack(new_stack_list)  

            # We no longer need to spawn a stack so reset this variable
            stack.update_stack_list = False

        # Draw the stack
        stack.draw()

        # Draw the dashed lines that the stack height must be at
        #pygame.draw.line(screen, GREEN, (0, threshold_height), (screen_width , threshold_height) , 5)
        draw_dashed_lines(threshold_height)

        # Draw the current question at the top of the screen
        draw_text(current_question, question_font, WHITE, 390, 120)
        
        # Draw the correct / incorrect text based on if the player answered the question correctly
        if answered_correctly == 1: # Correct
            if pygame.time.get_ticks() - question_answered_time < 1000:
                # Draw the "Correct" text
                draw_text("Correct!", question_font, GREEN, 100, 390)
        elif answered_correctly == -1: # Incorrect
            if pygame.time.get_ticks() - question_answered_time < 1000:
                # Draw the "Incorrect" text
                draw_text("Incorrect!", question_font, RED, 690, 390)            
            
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
        # Note: This has not been removed because the player still needs to be able to click on buttons in the restart menu. Also additional features which involve the mouse may be included later on.
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
                    # Record the time the player answered the question
                    question_answered_time = pygame.time.get_ticks()        

                    # Check if the user input is the same as the answer
                    if menu.maths_mode == True:
                        if int(user_text) == current_question_answer :
                            # Move the player up the stack 
                            stack.push()
                            # Generate a new question
                            current_question_answer, current_question = random_maths_question_generator()
                            # Set the variable answered correctly to 1 (so that the "correct" text can be displayed)
                            answered_correctly = 1
                        else:
                            # Set the variable answered correctly to -1 (so that the "incorrect" text can be displayed)
                            answered_correctly = -1                   
                        
                    elif menu.spelling_mode == True:
                        # Check if the user input is the same as the answer
                        if user_text == current_question_answer:
                            # Move the player down the stack
                            stack.push()
                            # Generate a new question
                            current_question_answer, current_question = random_spelling_question_generator(list_of_words)
                            # Set the variable answered correctly to 1 (so that the "correct" text can be displayed)
                            answered_correctly = 1
                        else:
                            # Set the variable answered correctly to -1 (so that the "incorrect" text can be displayed)
                            answered_correctly = -1   
                              
                    # Reset the user text (regardless if it was correct or incorrect)
                    user_text = ""

                # If the player wants to travel down the stack
                elif event.key == K_HASH and len(user_text) > 0 and user_text != "-":
                    # Record the time the player answered the question
                    question_answered_time = pygame.time.get_ticks()

                    if menu.maths_mode == True:
                        # Check if the user input is the same as the answer
                        if int(user_text) == current_question_answer:
                            # Move the player down the stack
                            stack.pop()
                            # Generate a new question
                            current_question_answer, current_question = random_maths_question_generator()
                            # Set the variable answered correctly to 1 (so that the "Correct" text can be displayed)
                            answered_correctly = 1 
                        else:
                            # Set the variable answered correctly to -1 (so that the "Incorrect" text can be displayed)
                            answered_correctly = -1   
                        
                    elif menu.spelling_mode == True:
                        # Check if the user input is the same as the answer
                        if user_text == current_question_answer:
                            # Move the player down the stack
                            stack.pop()

                            # Generate a new question
                            current_question_answer, current_question = random_spelling_question_generator(list_of_words)

                            # Set the variable answered correctly to 1 (so that the "Correct" text can be displayed)
                            answered_correctly = 1 
                        else:
                            # Set the variable answered correctly to -1 (so that the "Incorrect" text can be displayed)
                            answered_correctly = -1                    

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
                            # Check that the player hasn't written more than 20 digits
                            if len(user_text) <= 20:
                                # Contacenate the key the user pressed to the user text
                                user_text += event.unicode
    
    return time_counter_2, user_text, player_score, starting_setup, answered_correctly, high_score_2, stack, current_question, current_question_answer, question_answered_time, threshold_height, threshold_height_tuples, last_threshold_height, permanent_time_decrement    

# Instances
menu = Menu(0,0,screen)
