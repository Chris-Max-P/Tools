import os

from util.json_i_o import *
from util.paths_and_data import database

RECEIPES_JSON = os.path.join(database, "receipes.json")
INGR = "ingredients"
INSTR = "instructions"

def output_receipe():
    receipe_name, comma, num_persons = input(f'Enter receipe,num_persons').partition(',')

    receipe = json_file_to_dict(RECEIPES_JSON)
    ingredients = receipe[receipe_name][INGR]
    instructions = receipe[receipe_name][INSTR]
    print("Zutaten:")
    for key, value in ingredients.items():
        print(f'  {key}: {float(value) * float(num_persons)}')

    print(f"\nZubereitung:\n  {instructions}")

def input_receipe():
    receipes = json_file_to_dict(RECEIPES_JSON)

    receipe_name = input("Enter Name:\n")
    receipes[receipe_name] = {}

    ingr_dict = {}
    while True:
        ingredient = input("Neue Zutat: [Name] [Menge in g/ml] ")
        if ingredient == "":
            break
        ingredient = ingredient.split(" ")
        name = ingredient[0]
        amount = ingredient[1]
        ingr_dict[name] = amount
    receipes[receipe_name][INGR] = ingr_dict

    receipes[receipe_name][INSTR] = input("Enter Instructions:\n")

    dict_to_json_file(RECEIPES_JSON, receipes)


