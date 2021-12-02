import matplotlib.pyplot as plt
from util.json_i_o import *
from datetime import datetime

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


def get_personal_data(data_json):
    data = file_to_dict(data_json)
    html = f"""
            <div><b>Name:</b>       {data['name']}</div>
            <div><b>Geburtstag:</b> {data['birthday']}</div>
            <div><b>Adresse:</b>    {data['address']}</div>
            <div><b>E-Mail:</b>     {data['mail']}</div>
            <div><b>Telefon:</b>    {data['phone']}</div>
            """
    return html

def lebenslauf_to_html(template="Job/lifeline_template.html"):
    main_html = ''
    side_html = ''
    lebenslauf = file_to_dict(json)
    for station in reversed(list(lebenslauf.keys())):
        html = ''
        html += get_html(lebenslauf, station, template=template)

        if not lebenslauf[station]["category"] == "Nebenjob":
            main_html += html
        else:
            side_html += html

    with open(template, 'r') as hf:
        content = hf.read()
        with open(htmlTargetFile, 'w', encoding='utf-8') as target:
            new_content = content.replace('<!--main_html-->', main_html)
            new_content = new_content.replace('<!--side_html-->', side_html)
            new_content = new_content.replace('<!--personal_data-->', get_personal_data(data))
            target.write(new_content)

def get_html(lebenslauf, station, template="timeline"):
    start = datetime.strptime(lebenslauf[station]["start"], "%Y-%m-%d")
    end = datetime.strptime(lebenslauf[station]["end"], "%Y-%m-%d")

    if "timeline" in template:
        html = '<div class="container right">\n' \
                f'    <div class="content">\n' \
                f'        <h3>{start.year}-{start.month } --> {end.year}-{end.month}</h3>\n' \
                f'        <p>{station}</p>\n' \
                f'    </div>\n' \
                '</div>\n'
    else:
        html = f"""
    <div class="station">
        <span class="time"><b>{start.strftime('%m')}/{start.year} – {end.strftime('%m')}/{end.year}</b></span>
        <div class="line">
            <div class="station-heading"><b>{station}</b>
                <div class="experiences">{lebenslauf[station]['experiences'] if 'experiences' in lebenslauf[station] else ''}</div>
            </div>
        </div>
    </div>
            """
    return html


#template = 'Job/lebenslauf_template.html'
template = 'Job/lifeline_template.html'
htmlTargetFile = 'Job/lebenslauf.html'
json = 'Job/Data/lebenslauf.json'
data = 'Job/Data/personal_data.json'
lebenslauf_to_html()