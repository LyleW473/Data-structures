import pygame, sys, random, os
from pygame.locals import *
from Menus import Menu
from stack import Stack


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