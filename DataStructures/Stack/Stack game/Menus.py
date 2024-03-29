# Import modules
import pygame, sys

# Initialise pygame
pygame.init()

# Screen
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Fonts
menu_font = pygame.font.SysFont("Bahnschrift", 20)

# Load images 
# Most buttons are (400 x 125) pixels
play_image = pygame.image.load('graphics/Buttons/play_button.png').convert()
controls_image = pygame.image.load('graphics/Buttons/controls_button.png').convert()
quit_image = pygame.image.load('graphics/Buttons/quit_button.png').convert()
back_image = pygame.image.load('graphics/Buttons/back_button.png').convert()
return_to_main_menu_image = pygame.image.load('graphics/Buttons/return_to_main_menu_button.png').convert()
continue_image = pygame.image.load('graphics/Buttons/continue_button.png').convert()

maths_image = pygame.image.load('graphics/Buttons/maths_button.png').convert()
spelling_image = pygame.image.load('graphics/Buttons/spelling_button.png').convert()

goal_element_image = pygame.image.load('graphics/Buttons/goal_element_button.png').convert()
goal_height_image = pygame.image.load('graphics/Buttons/goal_height_button.png').convert()

game_over_display = pygame.image.load('graphics/Buttons/game_over_display.png').convert()
controls_display = pygame.image.load('graphics/Buttons/controls_display.png').convert_alpha()


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


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, pos):
        mouse_over_button = False
        # Check for a collision between the button and the current mouse position
        if self.rect.collidepoint(pos):
            mouse_over_button = True

        # Draw the button
        screen.blit(self.image, self.rect)

        # Return the clicked variable to the menu
        return mouse_over_button

class Menu():
    def __init__(self, x, y, surface):
        # Surface that the menu will be drawn onto
        self.surface = surface
        # Buttons
        self.button_list = []
        self.clicked = False # Used to track whenever the buttons on the menus are clicked

        # Game states
        self.show_main_menu = True # Determines whether we show the main menu or not
        self.show_controls_menu = False # Determines whether we show the controls menu or not
        self.in_game = False # Determines whether we are in game or not
        self.show_paused_menu = False # Determines whether we show the paused menu or not
        self.show_restart_menu = False # Determines whether we show the restart menu or not
        self.reset_game = False # Determines whether we should call the reset_game function inside the main file
        self.last_menu_visited = 0 # 1 = Main menu, 2 = Paused menu

        self.show_choose_mode_menu = False # Determines whether we should show the menu where the player can choose what mode they want to play
        # Game modes:
        self.spelling_mode = False
        self.maths_mode = False

        self.show_choose_game_menu = False # Determines whether we should show the menu where the player can choose which game they want to play
        # Games
        self.game_v1 = False # Goal element game
        self.game_v2 = False # Goal height game

        # Time tracking
        self.menu_times_dictionary = {"in_menu_time": 0, "entered_menu_time": 0}

    def update(self, pos):

        # MAIN MENU
        if self.show_main_menu == True:
            # Fill the screen with a white background
            screen.fill("dodgerblue4")

            # PLAY BUTTON
            # If the mouse is over the play button and is the mouse button is clicked
            if play_button.update(pos) == True and self.clicked == True: 
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False
                
                # Display the mode chooser menu
                self.show_main_menu = False
                self.show_choose_mode_menu = True


            # CONTROLS BUTTON
            if controls_button.update(pos) == True and self.clicked == True: 
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False

                # Display the show controls menu
                self.show_controls_menu = True
                self.show_main_menu = False

                # Set the last menu visited from the controls menu to be the paused menu
                self.last_menu_visited = 1

            # QUIT BUTTON
            # If the mouse is over the quit button and is the mouse button is clicked
            if quit_button.update(pos) == True and self.clicked == True:
                # Quit the game
                pygame.quit()
                sys.exit()

            # If none of the buttons above are True, that means the player clicked on empty space
            elif play_button.update(pos) == False and quit_button.update(pos) == False and self.clicked == True: 
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False


        # CONTROLS MENU
        if self.show_controls_menu == True:
            screen.fill("dodgerblue4")

            # Display the controls onto the screen
            screen.blit(controls_display, (75, 0))

            # BACK BUTTON
            if back_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False

                # Go back to the last menu 
                if self.last_menu_visited == 1: # MAIN MENU
                    self.show_main_menu = True

                elif self.last_menu_visited == 2: # PAUSED MENU
                    self.show_paused_menu = True

                # Don't show the controls menu
                self.show_controls_menu = False

            # If none of the buttons above are True, that means the player clicked on empty space
            elif back_button.update(pos) == False and self.clicked == True: 
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False

        # PAUSED MENU
        if self.show_paused_menu == True:
            screen.fill("dodgerblue4")

            # Check if the value inside "entered menu time" key in the menu times dictionary is 0
            if self.menu_times_dictionary["entered_menu_time"] == 0:
                # If it is, this means that the player has entered the paused menu, so record the current time.
                self.menu_times_dictionary["entered_menu_time"] = pygame.time.get_ticks()
            
            # CONTINUE BUTTON
            if continue_button.update(pos) == True and self.clicked == True: 
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False

                # Calculate the time that the player was in the menu
                self.menu_times_dictionary["in_menu_time"] = pygame.time.get_ticks() - self.menu_times_dictionary["entered_menu_time"] 

                # Go back to the main game
                self.in_game = True
                self.show_paused_menu = False

            # CONTROLS BUTTON
            if controls_button_2.update(pos) == True and self.clicked == True: 
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False

                # Display the show controls menu
                self.show_controls_menu = True
                self.show_paused_menu = False   
                
                # Set the last menu visited from the controls menu to be the paused menu
                self.last_menu_visited = 2

            # QUIT BUTTON
            # If the mouse is over the quit button and is the mouse button is clicked
            if quit_button_2.update(pos) == True and self.clicked == True:
                # Quit the game
                pygame.quit()
                sys.exit()

            # If none of the buttons above are True, that means the player clicked on empty space
            elif continue_button.update(pos) == False and controls_button_2.update(pos) == False and quit_button_2.update(pos) == False and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False             

        # RESTART MENU
        if self.show_restart_menu == True:
            screen.fill("dodgerblue4")

            # Display the game over text onto the screen
            screen.blit(game_over_display, (200, 80))

            # RETURN TO MAIN MENU BUTTON
            if return_to_main_menu_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False
                # Go back to the main menu  
                self.show_main_menu = True
                # Stop showing the restart menu
                self.show_restart_menu = False
                # Call the reset game function
                self.reset_game = True
                # Set the last menu visited to be the main menu (so that if the player enters the controls menu, they'll be back in the main menu)
                self.last_menu_visited = 1

            # QUIT BUTTON
            # If the mouse is over the quit button and is the mouse button is clicked
            if quit_button_3.update(pos) == True and self.clicked == True:
                # Quit the game
                pygame.quit()
                sys.exit()

            # If none of the buttons above are True, that means the player clicked on empty space
            elif return_to_main_menu_button.update(pos) == False and quit_button_3.update(pos) == False and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False

        # CHOOSE MODE MENU
        if self.show_choose_mode_menu == True:

            # Fill the screen with a white background
            screen.fill("dodgerblue4") 
            # Borders for the maths and spelling buttons
            pygame.draw.rect(screen, BLACK, (195, 195, 260, 260), 5)
            pygame.draw.rect(screen, BLACK, (545, 195, 260, 260), 5)

            # Display guide text
            draw_text("Answer maths questions!", menu_font, WHITE, 210, 500)
            draw_text("Correctly spell the given word!", menu_font, WHITE, 538, 500)

            # If the maths mode was clicked
            if maths_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    

                # Set the mode to be the maths mode
                self.maths_mode = True

                # Set the mode menu to stop showing and show the choose game menu
                self.show_choose_mode_menu = False
                self.show_choose_game_menu = True
            
            # If the spelling mode was clicked
            if spelling_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    

                # Set the mode to be the spelling mode
                self.spelling_mode = True

                # Set the mode menu to stop showing and show the choose game menu
                self.show_choose_mode_menu = False
                self.show_choose_game_menu = True

            # If the back button was clicked
            if back_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    

                # Go back to the main menu
                self.show_main_menu = True
                self.show_choose_mode_menu = False
            
            # If none of these buttons were clicked, then the player clicked on empty space
            elif maths_button.update(pos) == False and spelling_button.update(pos) == False and back_button.update(pos) == False and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    


        # CHOOSE GAME MENU
        if self.show_choose_game_menu == True:
            screen.fill("dodgerblue4")

            # Borders for the two game buttons
            pygame.draw.rect(screen, BLACK, (145, 155, 310, 310), 5)
            pygame.draw.rect(screen, BLACK, (545, 155, 310, 310), 5)

            # Display guide text
            draw_text("Reach the goal element!", menu_font, WHITE, 190, 510)
            draw_text("Reach the goal height!", menu_font, WHITE, 593, 510)


            # If the goal element game was pressed
            if goal_element_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    
                # Set the game to be loaded to be the goal element game
                self.game_v1 = True
                # Set the time that the player entered the game to be now
                self.entered_game_time = pygame.time.get_ticks()
                # Set the mode menu to stop showing and start the game
                self.show_choose_game_menu = False
                self.in_game = True

            if goal_height_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    
                # Set the game to be loaded to be the goal height game
                self.game_v2 = True
                # Set the time that the player entered the game to be now
                self.entered_game_time = pygame.time.get_ticks()
                # Set the mode menu to stop showing and start the game
                self.show_choose_game_menu = False
                self.in_game = True

            # If the back button was clicked
            if back_button.update(pos) == True and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    
                # Go back to the choose mode menu
                self.show_choose_mode_menu = True
                self.show_choose_game_menu = False

            # If none of the buttons were clicked, the player clicked on empty space
            elif goal_element_button.update(pos) == False and goal_height_button.update(pos) == False and back_button.update(pos) == False and self.clicked == True:
                # Reset the clicked variable to default so more clicks can be detected
                self.clicked = False    


# Button instances

# Main menu
play_button = Button(300, 200 , play_image)
controls_button = Button(300, 400, controls_image)
quit_button = Button(300, 600, quit_image)

# Controls menu
back_button = Button(300, 600, back_image)

# Paused menu
continue_button = Button(300, 200, continue_image)
controls_button_2 = Button(300, 400, controls_image)
quit_button_2 = Button(300, 600, quit_image)

# Restart menu
return_to_main_menu_button = Button(300, 350, return_to_main_menu_image)
quit_button_3 = Button(300, 550, quit_image)

# Choose mode menu
maths_button = Button(200, 200, maths_image)
spelling_button = Button(800 - 250, 200, spelling_image)
back_button_2 = Button(300, 600, back_image)

# Choose game menu
goal_element_button = Button(150, 160, goal_element_image)
goal_height_button = Button(850 - 300, 160, goal_height_image)
back_button_3 = Button(300, 600, back_image)
