# Import modules
import pygame
from pygame.locals import *

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

class Stack():
    def __init__(self, items_list = [] ):
        self.item_count = len(items_list)
        self.items_list = items_list # If a list isn't passed into the instance when first being instantiated, by default, it will be empty.

        # Find where the player is inside the items list
        for i in range(0, len(self.items_list)):
            if self.items_list[i] == 2:
                # Set the player pointer to be the same as the index in the list
                self.player_pointer = i
        
        self.update_stack_list = False # Determines whether we need to update the stack list

    def travel_up(self):
        # If we are traveling up the stack, we are going left in the list
        
        # If the player is already at the top of the stack
        if self.player_pointer == 0:
            # Do nothing
            pass
        # If the player pointer is any value other than the index at the top of the stack:
        else:
            # If the item isn't the goal element
            if self.items_list[self.player_pointer - 1] != 1:
                # Switch the player item and the item next to it around
                self.items_list[self.player_pointer - 1], self.items_list[self.player_pointer]= self.items_list[self.player_pointer], self.items_list[self.player_pointer - 1]

            # If it is the goal element
            else:
                # Then set the item next to the player to be "overwritten"
                self.items_list[self.player_pointer - 1] = self.items_list[self.player_pointer]
                # Set the item that the player was just at to be nothing
                self.items_list[self.player_pointer] = 0
                # Generate a new stack list (So the player will spawn at a random spot again, and a new goal element will be generated)
                self.update_stack_list = True

            # Decrement the player pointer
            self.player_pointer -= 1
        

    def travel_down(self):
        # If we are traveling down the stack, we are going right in the list

        # If the player pointer is at the bottom of the stack already
        if self.player_pointer == len(self.items_list) -1:
            # Do nothing
            pass
        else:

            # If the item isn't the goal element
            if self.items_list[self.player_pointer + 1] != 1:
                # Switch the player item and the item next to it around
                self.items_list[self.player_pointer + 1], self.items_list[self.player_pointer]= self.items_list[self.player_pointer], self.items_list[self.player_pointer + 1]

            # If it is the goal element
            else:
                # Then set the item next to the player to be "overwritten"
                self.items_list[self.player_pointer + 1] = self.items_list[self.player_pointer]
                # Set the item that the player was just at to be nothing
                self.items_list[self.player_pointer] = 0
                # Generate a new stack list (So the player will spawn at a random spot again, and a new goal element will be generated)
                self.update_stack_list = True

            # Increment the player pointer
            self.player_pointer += 1


    def update_stack(self, stack_list):
        # Set the items list to be the new randomised stack list passed into the method.
        self.items_list = stack_list

        # Find where the player is inside the items list
        for i in range(0, len(self.items_list)):
            if self.items_list[i] == 2:
                # Set the player pointer to be the same as the index in the list
                self.player_pointer = i

    def draw(self):
        # Width and height for the stack element rectangles
        rect_width = 200
        rect_height = 75

        # Border
        pygame.draw.rect(screen, BLACK, (500 - (rect_width / 2) - 5, 200 - 5, rect_width + 10, rect_height * len(self.items_list) + (len(self.items_list) * 5) + 5), 0)   

        # Generate rectangles (one for each stack element)
        for i in range(0, len(self.items_list)):
            # Any other stack item 
            if self.items_list[i] == 0:
                stack_item_colour = WHITE
            # The goal position
            elif self.items_list[i] == 1:
                stack_item_colour = GREEN
            # The player 
            elif self.items_list[i] == 2:
                stack_item_colour = 'purple'

            # Draw the rectangle
            pygame.draw.rect(screen, stack_item_colour, (500 - (rect_width / 2), 200 + (i * (rect_height + 5)), rect_width, rect_height), 0)   

            # Drawing eyes and a mouth on the player
            if self.items_list[i] == 2:
                # Left eye
                pygame.draw.circle(screen, WHITE, (450, 200 + (i * (rect_height + 5)) + (rect_height / 2) ), 25, 50)
                pygame.draw.circle(screen, BLACK, (450, 200 + (i * (rect_height + 5)) + (rect_height / 2) ), 12, 50)
                # Right eye
                pygame.draw.circle(screen, WHITE, (550, 200 + (i * (rect_height + 5)) + (rect_height / 2) ), 25, 50)
                pygame.draw.circle(screen, BLACK, (550, 200 + (i * (rect_height + 5)) + (rect_height / 2) ), 12, 50)
                # Mouth
                pygame.draw.line(screen, BLACK, (480, 225 + (i * (rect_height + 5)) + (rect_height / 2)) , (520, 225 + (i * (rect_height + 5)) + (rect_height / 2)), 3)
        
class Stack2(Stack):
    def __init__(self, items_list = [] ):
        Stack.__init__(self, items_list) # Stack 2 (for the goal height game) inherits Stack(From the goal element game)


    def pop(self):
    
        # If there is greater than 1 item
        if len(self.items_list) > 1:
            # Pop the item underneath the player segment
            self.items_list.pop(self.player_pointer - 1)
            # Decrement the player pointer
            self.player_pointer -= 1

    def push(self):
        if len(self.items_list) < 6:
            # Push the item to the top of the stack
            self.items_list.insert(len(self.items_list) - 1, 0)

            # Increment the player pointer
            self.player_pointer += 1

        print(self.items_list)

    def draw(self):
        # Width and height for the stack element rectangles
        rect_width = 200
        rect_height = 75

        
        # Note: Border (y = 595 - ( 80 *  number of items - 1)), height = 85 + (80 * number of items - 1)  80 = rect width + top outline
        pygame.draw.rect(screen, BLACK, (500 - (rect_width / 2) - 5, 595 - (80 * (len(self.items_list) - 1)) , rect_width + 10, 85 + (80 * (len(self.items_list) - 1)) ) , 0)

        # Generate rectangles (one for each stack element)
        for i in range(0, len(self.items_list)):
            # Any other stack item 
            if self.items_list[i] == 0:
                stack_item_colour = WHITE
            # The player 
            elif self.items_list[i] == 2:
                stack_item_colour = RED

            # Draw the rectangle
            pygame.draw.rect(screen, stack_item_colour, (500 - (rect_width / 2), 600 - (i * (rect_height + 5)), rect_width, rect_height), 0)   

            # Drawing eyes and a mouth on the player
            if self.items_list[i] == 2:
                # Left eye
                pygame.draw.circle(screen, BLACK, (460, 600 - (i * (rect_height + 5)) + (rect_height / 2) ), 10, 50)
                # Right eye
                pygame.draw.circle(screen, BLACK, (540, 600 - (i * (rect_height + 5)) + (rect_height / 2) ), 10, 50)
                # Mouth
                pygame.draw.line(screen, BLACK, (480, 620 - (i * (rect_height + 5)) + (rect_height / 2)) , (520, 620 - (i * (rect_height + 5)) + (rect_height / 2)), 5)