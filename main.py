import requests
from bs4 import BeautifulSoup
import json


def get_data():
    # Read the JSON data from the file
    with open('data_structure/date.json', 'r') as file:
        dates_json = json.load(file)

    url = "https://www.integrersciencespo.fr/dates-de-lhistoire-du-monde"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the tag before dates
    target_tag = soup.find('a', href="https://www.integrersciencespo.fr/dates-connaitre")
    target_tag_parent = target_tag.find_parent()

    # Iterate over dates
    html_with_dates = target_tag_parent.find_next_siblings()
    for date in html_with_dates:
        date_clean = str(date).replace('<p>', '').replace('</p>', '').replace('–', '-')
        if '<' not in date_clean and 'Voir aussi' not in date_clean:
            date_split = date_clean.split(' : ')
            year_clean = date_split[0].replace(' ', '')
            event_clean_lower_case = date_split[1].replace('.', '')
            event_clean = event_clean_lower_case[0].upper() + event_clean_lower_case[1:]
            if '-' in year_clean and year_clean[0] != '-':
                split_period('-', year_clean, event_clean, dates_json)
            elif (year_clean[0] != '-') and '-' in year_clean[1:]:
                split_period_avjc(year_clean, event_clean, dates_json)
            else:
                if 'v.' in year_clean:
                    year_clean = year_clean.replace('v.', '')
                new_date = {
                    "year": year_clean,
                    "event": event_clean
                }
                dates_json["dates"].append(new_date)
    print(dates_json)
    with open('output/date.json', 'w') as file:
        json.dump(dates_json, file, indent=4)


def split_period(character, date, event, data):
    years = date.split(character)
    new_date_begin = {
        "year": years[0],
        "event": 'Début ' + event
    }
    new_date_end = {
        "year": years[1],
        "event": 'Fin ' + event
    }
    data["dates"].append(new_date_begin)
    data["dates"].append(new_date_end)


def split_period_avjc(date, event, data):
    years = date[1:].split('-')
    new_date_begin = {
        "year": '-' + years[0],
        "event": 'Début ' + event
    }
    new_date_end = {
        "year": '-' + years[1],
        "event": 'Fin ' + event
    }
    data["dates"].append(new_date_begin)
    data["dates"].append(new_date_end)


# TODO Manage months -> DONE on frontend
# TODO Replace american dashes by french dashes and spaces by void string -> DONE
# TODO Retrieve points and add upper case on first letter -> DONE

# TODO 907 : Chine : le dernier empereur Tang est détrôné. deal with the punctuaction in the middle
# TODO Bug dates with 2 numbers av JC
# TODO Do not delete dates with links

get_data()
