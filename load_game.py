#Load Character from file
import start_game

load_name = ""
load_class = ""
load_gender = ""
saved_name = str(start_game.name_option())

def character_check(file_path):
    global load_name
    global load_class
    global load_gender
    
    with open(saved_name.txt, 'r') as file:
        p_info = file.readlines()
    for character_name in p_info:
        if character_name.find("Vyajr") != -1:
            load_name = character_name
    for character_class in p_info:
        if character_class.find ("Paladin") != -1:
            load_class = character_class
    for character_gender in p_info:
        if character_gender.find ("female") != -1:    
            load_gender = character_gender
    print(f"Character Name: {load_name}")
    print(f"Character Class: {load_class}")
    print(f"Character Gender: {load_gender}")
    character_load()
        
    

def character_load():
    print("Welcome", load_name, "to the World")
    