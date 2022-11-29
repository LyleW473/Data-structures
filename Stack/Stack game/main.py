# Import modules
import pygame, sys, random, os
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
GREY = (79, 79, 79)

# Font
time_font = pygame.font.SysFont("Bahnschrift", 100)
user_input_font = pygame.font.SysFont("Bahnschrift", 40)
question_font = pygame.font.SysFont("Bahnschrift", 50)
score_font = pygame.font.SysFont("Bahnschrift", 30)

# Game variables
time_counter = 5000 # 30 seconds in milliseconds
user_text = "" # Holds the numbers that the user types into the input box 
user_input_rectangle = pygame.Rect((screen_width / 2) - 100, screen_height - 90, 200, 50) # User input box rectangle
player_score = 0 # The score the player currently has


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
    

def random_spelling_question_generator():
    pass


def reset_game(time_counter, player_score, stack, current_question_answer, current_question, user_text):
    # Reset the timer
    time_counter = 30000

    # Reset the player score 
    player_score = 0

    # Delete the current stack instance
    del stack
    # Generate a new starting stack instance
    random_stack_list = random_stack_list_generator()
    stack = Stack(random_stack_list)

    # Generate a new starting question
    current_question_answer, current_question = random_maths_question_generator()
    # Reset the user input text
    user_text = ""

    return time_counter, player_score, stack, current_question_answer, current_question, user_text


# Instances
menu = Menu(0,0,screen)

# Starting stack:
# Generate a random list for the stack
random_stack_list = random_stack_list_generator()
# Create a new stack instance, feeding in the stack list as a parameter
stack = Stack(random_stack_list)
# Create the starting question 
current_question_answer, current_question = random_maths_question_generator()


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
            draw_alpha_text(str(round(time_counter / 1000, 2)), time_font, BLACK, 390, 0)   

        # Check if the player has requested to restart the game
        if menu.reset_game == True:
            # Reset all of the game variables
            time_counter, player_score, stack, current_question_answer, current_question, user_text = reset_game(time_counter, player_score, stack, current_question_answer, current_question, user_text)
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

                # If the player wants to push an item onto the stack
                if event.key == K_u and len(user_text) > 0:
                    # Check if the user input is the same as the answer
                    if int(user_text) == current_question_answer:
                        print("Correct")
                        # Move the player up the stack 
                        stack.travel_up()

                        # Generate a new question
                        current_question_answer, current_question = random_maths_question_generator()

                    else:
                        print("Incorrect")
                        
                    # Reset the user text (regardless if it was correct or incorrect)
                    user_text = ""

                # If the player wants to pop an item off the stack
                elif event.key == K_j and len(user_text) > 0:
                    # Check if the user input is the same as the answer
                    if int(user_text) == current_question_answer:
                        print("Correct")

                        # Move the player down the stack
                        stack.travel_down()

                        # Generate a new question
                        current_question_answer, current_question = random_maths_question_generator()

                        # Reset the user text
                        user_text = ""

                    else:
                        print("Incorrect")
                        
                    # Reset the user text (regardless if it was correct or incorrect)
                    user_text = ""

                # If the player has pressed any other key
                else:   
                    # Check the unicode number of the key. If it is a number from 0 to 9 or is the "-" symbol
                    if 48 <= event.key <= 57 or event.key == 45:
                        # Check that the player hasn't written more than 20 digits
                        if len(user_text) <= 20:
                            # Contacenate the key the user pressed to the user text
                            user_text += event.unicode





    pygame.display.update()
