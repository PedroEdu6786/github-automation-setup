from src.constants.Colors import Colors
from os import system
from sys import exit

# Project's basic UI
class SetupUI:
    
    # Prints error message with color
    def print_error(self, message):
        print(f'{Colors.FAIL}{message}{Colors.ENDC}')
        
    # Prints white space on command line
    def print_whitespace(self):
        print('\n\n\n\n')
        
    # Clears command line screen
    def clear_screen(self):
        system('cls')
        
    # Exits app
    def dispose_screen(self):
        exit()
        
    # Displays success message
    def success_message(self, message):
        print(f'{Colors.OK_CYAN}{message}{Colors.ENDC}')
        
    # Displays a title in the ui
    def display_title(self, message):
        print(f'{Colors.HEADER}{message}{Colors.ENDC}')
        
    # Displays final message if project has been created successfully
    def display_project_created(self):
        print(f'{Colors.OK_GREEN}Project has been successfully created and deployed on github{Colors.ENDC}')
        
    def success_display(self, message):
        self.clear_screen()
        self.success_message(message)
        self.print_whitespace()
        
    def error_dispose(self, message):
        self.clear_screen()
        self.print_error(message)
        self.dispose_screen()