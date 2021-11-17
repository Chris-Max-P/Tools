import matplotlib.pyplot as plt
from util.json_i_o import *

lebenslauf = file_to_dict('Job/Data/lebenslauf.json')

lebenslauf_list = [key for key in lebenslauf.keys()]  # (key, value) for key, value in lebenslauf
# lebenslauf_list.insert(0, '')

def lebenslauf_to_gantt():
    fig, gnt = plt.subplots()

    gnt.set_xlim(1998, 2021)
    gnt.set_ylim(0, 70)

    gnt.set_xlabel('Jahre')
    gnt.set_ylabel('')

    y_ticks_list = [index*5 for index, _ in enumerate(lebenslauf_list)]
    gnt.set_yticks(y_ticks_list)
    gnt.set_yticklabels(lebenslauf_list)

    gnt.broken_barh([(1999, 6)], (0.5, 0.5), facecolors=('tab:blue'))

    plt.show()

def lebenslauf_to_text(lebenslauf_dict):
    lebenslauf_list = [key for key in lebenslauf.keys()]
    lebenslauf_list.reverse()

















"""from datetime import date
import gantt

Lebenslauf = gantt.Resource('Lebenslauf')

school = gantt.Task(name='Schule', start=date(1999, 9, 15), duration=100, resources=[Lebenslauf])

project_1 = gantt.Project(name='Project 1')
project_1.add_task(school)

project_1.make_svg_for_tasks(
    filename='Project_1.svg',
    today=date(2021, 1, 27),
    start=date(1993, 1, 20),
    end=date(2021, 7, 1)
)"""