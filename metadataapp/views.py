import json, os

import math
from django.http import HttpResponse, JsonResponse

from content_page.models import ContentPage, ContentIndexPage
from metadataapp.models import Plant, Event, Fruit, CropPricing

from .constants import NEPALI_MONTH_INDEX, NO_DAYS_IN_MONTH, EVENT_URL

YEAR = 2073
BASE_TECHNIQUES_URL = "http://barsabharitarkari.org/en/techniques/"


from django.conf import settings 
BASE_DIR = settings.BASE_DIR
LOG_FILE = os.path.join(BASE_DIR, "my_log.txt")


def add_zero_if_less_than_ten(number):
    if number > 10:
        return str(number)
    if not number:
        number += 1
    return "0" + str(number)


def get_date_from_days(total_days):
    """bivu edit test this function"""
    year = math.floor(total_days / 365)
    remainder_days = total_days - year * 365
    month = math.floor(remainder_days / 30)
    # for past month assign next year
    days = round(remainder_days - month * 30)
    # convert 1 to 01 for java date compatibility
    month = add_zero_if_less_than_ten(month)
    days = add_zero_if_less_than_ten(days)
    return "{}/{}/{}".format(month, days, year)


def obtain_english_calendar_from_event(event_object):
    """
    subtract 1 because baisakh 15 is 15 days although baisakh is 1
    subtract 20698 to get english dates
    """
    month_index = NEPALI_MONTH_INDEX[event_object.month]
    days = NO_DAYS_IN_MONTH[event_object.week]

    total_bikram_sambat_days = round(YEAR * 365 + month_index * 30.5 + days)
    total_number_english_days = total_bikram_sambat_days - 20698

    return get_date_from_days(total_number_english_days)


def get_event_url(event_object):
    slug = EVENT_URL[event_object.event_name.strip()]
    return BASE_TECHNIQUES_URL + slug + "/"


def convert_event_into_dict(event_object):
    '''
    outputs dict with keys:
    url, eventDate, name
    '''
    event_dict = {
        'detailURL': get_event_url(event_object),
        'eventDate': obtain_english_calendar_from_event(event_object),
        'name': event_object.event_name,
        'nepaliName': event_object.nepali_event_name
    }
    return event_dict


def get_timeline_for_plant(plant_object):
    plant_pk = plant_object.pk  # pk = 33
    plant_model = Plant.objects.get(pk=plant_pk)
    events = Event.objects.filter(plant_events=plant_model)

    if not events:
        return []

    all_timeline = []

    for event in events:
        all_timeline.append(convert_event_into_dict(event))

    return all_timeline


def generate_unique_name(name):
    return name.replace("-", "_")


def remove_paranthesis(name):
    return name.split("(")[0].strip()


def get_nepali_name(name):
    # bivu edit add function definition
    try:
        return name.split("(")[1].split(")")[0].strip()
    except IndexError:
        return name


def get_json_from_plant(plant):
    import datetime
    try:
        plant_dict = {
            'name': plant.name,
            'plantNepaliName': get_nepali_name(plant.name),
            'season': plant.season,
            'detailURL': plant.detailURL,
            'image': plant.image,
            'unique_name': generate_unique_name(plant.unique_name),
            'timeline': get_timeline_for_plant(plant)
        }
        get_timeline_for_plant(plant)
        return plant_dict
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write("Exception on {}".format(str(datetime.datetime.today())))
            f.write(str(e))
            f.write("\n")
    return False



def check_to_add(name):
    names_to_add = ["Beans", "Cress", "mustard", "Fava", "Colocasia",
                    "Coriander", "Cauliflower", "Bottle", "Sweet"]
    for each_name in names_to_add:
        if each_name in name:
            return True

    return False


def get_json_of_all_plants():
    plants = Plant.objects.all()
    all_plants = []
    for q in plants:
        json_from_plant = get_json_from_plant(q)
        if json_from_plant:
            all_plants.append(get_json_from_plant(q))
    return all_plants


def convert_fruit_into_dict(fruit_object):
    return {
        'name': fruit_object.name,
        'image': fruit_object.image,
        'unique_name': fruit_object.unique_name,
        'detailURL': fruit_object.detailURL
    }


def get_dict_from_technique(technique_object):
    # name = technique_object.title.split('(')[0].strip()
    name = technique_object.title.strip()
    detail_url = "http://barsabharitarkari.org/en/techniques/" + technique_object.slug
    detail_nepali_url = detail_url.replace("/en/", "/ne/")
    try:
        nepali_name = technique_object.title.split("(")[1].split(")")[0].strip()
    except IndexError:
        nepali_name = ""

    return {
        'name': name,
        'detailURL': detail_url,
        'detailNepaliURL': detail_nepali_url,
        'nepaliName': nepali_name
    }


def get_json_of_all_techniques():
    _techniques = ContentIndexPage.objects.get(slug="techniques").get_children()
    all_techniques = []
    for t in _techniques:
        slug = t.slug
        content_page = ContentPage.objects.get(slug=slug)
        if content_page.improved_technique:
            all_techniques.append(get_dict_from_technique(t))
    return all_techniques


def get_json_of_all_fruits():
    fruits = Fruit.objects.all()
    all_fruits = []
    for f in fruits:
        all_fruits.append(convert_fruit_into_dict(f))
    return all_fruits


def get_price_json_one_item(price_object):
    def get_plant_unique_name(plant):
        return plant.split("(")[0].strip().lower().replace(" ", "_")
    return {
        get_plant_unique_name(price_object.name): str(price_object.price)
    }


def get_json_of_all_prices():
    def get_plant_unique_name(plant):
        return plant.strip().split("(")[0].strip().lower().replace(" ", "_")
    all_crops = {}
    for i in CropPricing.objects.all():
        all_crops[get_plant_unique_name(i.name)] = str(i.price)
    return all_crops


def get_plants_data(request):
    all_plants = get_json_of_all_plants()
    all_fruits = get_json_of_all_fruits()
    all_techniques = get_json_of_all_techniques()
    all_prices = get_json_of_all_prices()
    final_json = {
                  "plants": all_plants,
                  "fruits": all_fruits,
                  "techniques": all_techniques,
                  "prices": all_prices
                  }
    return JsonResponse(final_json)
