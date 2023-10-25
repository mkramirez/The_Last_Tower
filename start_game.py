##Start Game Interface
import os
import load_game
import player_setup

name_option = ""
class_option = ""
gender_option = ""

             
                 
def start_game_check():
    os.system('cls')
    print('Please Enter your Characters Name')
    option = input("> ")
    global name_option
    name_option = option
    character_exists(r'Player_list.txt', option)


def character_exists(file_path, player_name):
    
    with open(file_path, 'r') as file:
        p_names = file.read() 
    if player_name in p_names:
        os.system('cls')
        print ('Character Found')
        load_game()
    elif not player_name in p_names:
        character_creation(file_path, True)
    
def character_creation(file_path, player_selection):
    with open('Character_Classes.txt', 'r') as file:
        class_names = file.read()
    
    os.system('cls')
    print(class_names)
    character_creation_class()

def character_creation_class():
    option = input("> ")
    global class_option
    class_option = option

    if option == '1':
        with open('Paladin.txt', 'r') as file:
            p_selection = file.read()
        os.system('cls')
        print(p_selection)
        while True:
            print("Do you want to pick this class? (Yes/No)")
            option = input("> ")
            if option.lower() == "yes":
                class_option = "Paladin"
                character_creation_gender()
                break
            elif option.lower() == "no":
                character_creation()
                break
   
def character_creation_gender():
    os.system('cls')
    global gender_option
    while True:
        print("Please pick a gender (Male, Female, Nonbinary)")
        option = input("> ")
        if option.lower() in ["male", "female", "nonbinary"]:
            gender_option = option
            character_creation_finalize()
            break


def character_creation_finalize():
    os.system('cls')
    print(f"Character Name: {name_option}")
    print(f"Character Class: {class_option}")
    print(f"Character Gender: {gender_option}")
    while True:
        print("Do you want to create this character?")
        option = input ("> ")
        if option.lower == ("yes"):
            character_file = open(name_option.lower,".txt", "wt")
            character_content = "Character: ", name_option,'/n', "Gender: ", gender_option, "n", "Class: ", class_option
            n = character_file.write(character_content)
            load_game.character_check() #not working?
            break
        elif option.lower == ("no"):
            character_creation() #not working?
            break

    
