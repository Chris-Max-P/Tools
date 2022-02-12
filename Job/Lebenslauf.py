import matplotlib.pyplot as plt
from util.json_i_o import *
from datetime import datetime

lebenslauf = json_file_to_dict('Job/Data/lebenslauf.json')

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
    data = json_file_to_dict(data_json)
    html = f"""
            <div><span class="data-title">Name:</span>       <span class="data-field">{data['name']}</span></div>
            <div><span class="data-title">Geburtstag:</span> <span class="data-field">{data['birthday']}</span></div>
            <div><span class="data-title">Adresse:</span>    <span class="data-field">{data['address']}</span></div>
            <div><span class="data-title">E-Mail:</span>     <span class="data-field">{data['mail']}</span></div>
            <div><span class="data-title">Telefon:</span>    <span class="data-field">{data['phone']}</span></div>
            """
    return html

def get_qualifications_html(skills_json):
    skills = json_file_to_dict(skills_json)
    html = ""
    for skill in skills:
        html += f"""
        <div class="station">
            <span class="sub time"><b>{skill}</b></span>
            <div class="line">
                <div class="station-heading">
                    {skills[skill]}
                </div>
            </div>
        </div>
                """
    return html

def lebenslauf_to_html(template="Job/lifeline_template.html"):
    main_html = ''
    side_html = ''
    lebenslauf = json_file_to_dict(json)
    for station in reversed(list(lebenslauf.keys())):
        html = ''
        html += get_station_html(lebenslauf, station, template=template)

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
            new_content = new_content.replace('<!--qualifications-->', get_qualifications_html(skills))
            target.write(new_content)

def get_exp_html(experiences):
    html = """<ul>
                """
    for exp in experiences:
        html += f"""
        <li class="experiences">
            <div> <span class="exp-headline">{exp}:</span> {experiences[exp]['descr'] if 'descr' in experiences[exp] else ''}</div>
            <div> {'<span class="exp-headline">Technologien:</span> ' + experiences[exp]['technologies'] if 'technologies' in experiences[exp] else ''}</div>
            <div> {'<span class="exp-headline">Team-Größe:</span> ' + str(experiences[exp]['team-size']) if 'team-size' in experiences[exp] else ''}</div>
            <div> {'<span class="exp-headline">Rolle:</span> ' + experiences[exp]['role'] if 'role' in experiences[exp] else ''}</div>
        </li>"""
    html += """</ul>
            """
    return html

def get_station_html(lebenslauf, station, template="timeline"):
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
                {get_exp_html(lebenslauf[station]['experiences']) if 'experiences' in lebenslauf[station] else ''}
            </div>
        </div>
    </div>
            """
    return html


template = 'Job/lebenslauf_template.html'
htmlTargetFile = 'Job/lebenslauf.html'
json = 'Job/Data/lebenslauf.json'
data = 'Job/Data/personal_data.json'
skills = 'Job/Data/skills.json'
lebenslauf_to_html(template)
