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
        self.head_pointer = self.item_count - 1 # Set the head pointer (the pointer for the item at the top of the stack) (If it is empty, the pointer will be -1)
        self.items_list = items_list # If a list isn't passed into the instance when first being instantiated, by default, it will be empty.

    def push(self, item):
        # Increment the head pointer 
        self.head_pointer += 1
        # Add the item onto the stack
        self.items_list.append(item)

    def pop(self):
        # If the stack is empty, then don't do anything
        if self.isEmpty() == True:
            print("Unable to pop items when the stack is empty")
        else:
            print(f'{self.items_list[self.head_pointer]} has been popped off the stack')
            # Pop the item off the stack
            self.items_list.pop(self.head_pointer)
            # Decrement the head pointer
            self.head_pointer -= 1

    def isEmpty(self):
        # If the length of the list is greater than 0
        if len(self.items_list) > 0:
            # Then it isn't empty so return False
            return False
        # Otherwise return True
        return True

    def peek(self):
        if self.isEmpty() == False:
            print(f'The topmost element of the stack is {self.items_list[self.head_pointer]}')
        else:
            print("The stack is currently empty.")
    
    def size(self):
        print(f'There are {len(self.items_list)} items in the stack')


    def update_stack(self):
        pass

    def draw(self):
        rect_width = 200
        rect_height = 75

        for i in range(0, 6):
            if self.items_list[i] == 0:
                stack_item_colour = WHITE
            else:
                stack_item_colour = GREEN

            pygame.draw.rect(screen, stack_item_colour, (500 - (rect_width / 2), 200 + (i * (rect_height + 5)), rect_width, rect_height), 0)