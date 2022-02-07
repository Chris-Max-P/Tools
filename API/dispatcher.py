import argparse
from receipes import start

switch = {
    "receipe": start,
    "number": start
}

parser = argparse.ArgumentParser()
parser.add_argument("domain")

args = parser.parse_args()

domain = args.domain

switch[domain]()

# todo
# generic database adder / remover / updater
# check structure of json + adapt input etc
