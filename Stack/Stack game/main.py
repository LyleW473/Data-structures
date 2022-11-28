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
time_font = pygame.font.SysFont("Bahnschrift", 100)
user_input_font = pygame.font.SysFont("Bahnschrift", 40)
question_font = pygame.font.SysFont("Bahnschrift", 50)

# Game variables
time_counter = 5000 # 5 seconds in milliseconds
generate_new_questions = True # Determines whether we need to generate a new question or not

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
    player_random_index = random.randrange(0,5)
    print("random", random_index)
    print("player", random_index)
    
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

def random_question_generator():
    # random_operation = random.randrange(0,3) # Add = 0, Subtract = 1, Multiply = 2, Division = 3 , could add MOD
    random_operation = 0
    # Note: Maybe define these random numbers in the random operation sections. That way we can have harder addition questions but easier multiplication questions.
    random_number_1 = random.randrange(0,50)
    random_number_2 = random.randrange(0,50)
    # Addition
    if random_operation == 0:
        # Store the answer for the question later
        answer = random_number_1 + random_number_2 
        question = f'{random_number_1} + {random_number_2} = ?'

    return answer, question


# variables (move up later)
user_text = "" # Holds the numbers that the user types into the input box 
user_input_rectangle = pygame.Rect((screen_width / 2) - 100, screen_height - 70, 200, 50) # User input box rectangle

# Instances

# Generate a random list for the stack
random_stack_list = random_stack_list_generator()
# Create a new stack instance, feeding in the stack list as a parameter
stack = Stack(random_stack_list)

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
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # TIME
        # Draw the timer at the top of the screen
        draw_text(str(round(time_counter / 1000, 2)), time_font, BLACK, 410, 0)
        

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

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # STACK GAMEPLAY
        # Check if we need to spawn a stack.
        if generate_new_questions == True:

            # We no longer need to spawn a stack so reset this variable
            generate_new_questions = False

            # Generate a question 
            current_question_answer, current_question = random_question_generator()
            print(current_question_answer, current_question)
            print(stack.items_list)

        # Draw the stack
        stack.draw()

        # Draw the current question at the top of the screen
        draw_text(current_question, question_font, RED, 400, 120)

        # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # USER INPUT
        text_image = user_input_font.render(user_text, True, RED)
        pygame.draw.rect(screen, WHITE, user_input_rectangle, 5)
        screen.blit(text_image, (user_input_rectangle.x + 5, user_input_rectangle.y + 10))
        user_input_rectangle.width = max(200, text_image.get_width() + 10)

        
    
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

                # If the backspace key is pressed
                if event.key == K_BACKSPACE:
                    # Remove the last item inside the text
                    user_text = user_text[:-1]

                # If the player wants to push an item onto the stack
                elif event.key == K_j and len(user_text) > 0:
                    # Check if the user input is the same as the answer
                    if int(user_text) == current_question_answer:
                        print("Correct")
                        # ---- ADD CODE TO TRAVEL UP THE STACK  
                        stack.travel_up()
                    else:
                        print("Incorrect")
                        

                # If the player wants to pop an item off the stack
                elif event.key == K_k and len(user_text) > 0:
                    # Check if the user input is the same as the answer
                    if int(user_text) == current_question_answer:
                        print("Correct")
                        stack.travel_down()
                        # ---- ADD CODE TO TRAVEL DOWN THE STACK

                    else:
                        print("Incorrect")

                # If the player has pressed any other key
                else:   
                    # Check the unicode number of the key and if it is a number from 0 to 9
                    if 48 <= event.key <= 57:
                        # Check that the player hasn't written more than 20 digits
                        if len(user_text) <= 20:
                            # Contacenate the key the user pressed to the user text
                            user_text += event.unicode





    pygame.display.update()
