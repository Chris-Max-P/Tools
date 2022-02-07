from util.json_i_o import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode")
args = parser.parse_args()
mode = args.mode

RECEIPES_JSON = "receipes.json"
INGR = "ingredients"
INSTR = "instructions"

def output_receipe():
    inp = input("Enter [name] [number of persons]:\n").split(" ")
    persons = 1

    if len(inp) > 1:
        persons = inp[1]

    receipe = file_to_dict(RECEIPES_JSON)
    ingredients = receipe[inp[0]][INGR]
    instructions = receipe[inp[0]][INSTR]
    print("Zutaten:")
    for key, value in ingredients.items():
        print(f'  {key}: {float(value) * float(persons)}')

    print(f"\nZubereitung:\n  {instructions}")

def input_receipe():
    receipes = file_to_dict(RECEIPES_JSON)

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

    dict_to_file(RECEIPES_JSON, receipes)


def start():
    if mode == "":
        output_receipe()
    else:
        input_receipe()


start()


