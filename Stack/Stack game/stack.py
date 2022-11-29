# Import modules
import pygame

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
        for i in range(0, len(self.items_list)):
            if self.items_list[i] == 2:
                self.player_pointer = i

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

            # --------------------------------- ADD CODE HERE FOR GENERATING A NEW GOAL ELEMENT
              
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

                # --------------------------------- ADD CODE HERE FOR GENERATING A NEW GOAL ELEMENT

            # Increment the player pointer
            self.player_pointer += 1

    def update_stack(self):
        pass

    def draw(self):
        # Width and height for the stack element rectangles
        rect_width = 200
        rect_height = 75
        
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
                stack_item_colour = RED

            # Draw the rectangle
            pygame.draw.rect(screen, stack_item_colour, (500 - (rect_width / 2), 200 + (i * (rect_height + 5)), rect_width, rect_height), 0)