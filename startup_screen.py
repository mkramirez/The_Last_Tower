##Start up Screen
import os
import sys
import sysconfig
import start_game
import display_setup

os.getcwd()

def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        start_game.start_game_check()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sysconfig.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please Enter a Command")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()
            
def title_screen():
    os.system('cls')
    print('###########whaddup kids###########')
    print('Play')
    print('Help')
    print('Quit')
    title_screen_selection()
    
def help_menu():
    print('bruh why you need help already?')
    title_screen_selection()