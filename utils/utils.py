import requests
import logging
import csv
from pydantic import BaseModel
from models.person import PersonModel
from models.planet import PlanetModel
from models.starship import StarShipModel

def get_list_all_elements(resource: str) -> list[dict]:
    base_url = "https://swapi.dev/api"
    url = f"{base_url}{resource}?page=1"
    list_of_elements = []
    while url:
        try:
            response = requests.get(url)
            data = response.json()
            url = data.get("next")
            list_of_elements.extend(data["results"])
            logging.info(f"The next url is {url}")
        except Exception as e:
            logging.error(f"An error: {e}")
    return list_of_elements


def export_person_to_csv(list_of_elements_to_be_exported: list[dict], exported_file_name: str) -> str:
    with open(exported_file_name, "w", newline='') as myfile:
        writer = csv.DictWriter(myfile, fieldnames=PersonModel.model_fields.keys())
        writer.writeheader()
        for dict_element in list_of_elements_to_be_exported:
            person_instance = PersonModel(**dict_element)
            person_dict = person_instance.model_dump()
            writer.writerow(person_dict)
    logging.info("The csv file has been exported")


def export_planet_to_csv(list_of_elements_to_be_exported: list[dict], exported_file_name: str) -> str:
    with open(exported_file_name, "w", newline='') as myfile:
        writer = csv.DictWriter(myfile, fieldnames=PlanetModel.model_fields.keys())
        writer.writeheader()
        for dict_element in list_of_elements_to_be_exported:
            planet_instance = PlanetModel(**dict_element)
            planetc_dict = planet_instance.model_dump()
            writer.writerow(planetc_dict)
    logging.info("The csv file has been exported")

def export_starship_to_csv(list_of_elements_to_be_exported: list[dict], exported_file_name: str) -> str:
    with open(exported_file_name, "w", newline='') as myfile:
        writer = csv.DictWriter(myfile, fieldnames=StarShipModel.model_fields.keys())
        writer.writeheader()
        for dict_element in list_of_elements_to_be_exported:
            starship_instance = StarShipModel(**dict_element)
            starship_dict = starship_instance.model_dump()
            writer.writerow(starship_dict)
    logging.info("The csv file has been exported")


def export_generic_model_to_csv(model_class: BaseModel, list_of_elements_to_be_exported: list[dict], exported_file_name: str) -> str:
    with open(exported_file_name, "w", newline='') as myfile:
        writer = csv.DictWriter(myfile, fieldnames=model_class.model_fields.keys())
        writer.writeheader()
        for dict_element in list_of_elements_to_be_exported:
            instance = model_class(**dict_element)
            instance_dict = instance.model_dump()
            writer.writerow(instance_dict)
    logging.info("The CSV file has been exported")