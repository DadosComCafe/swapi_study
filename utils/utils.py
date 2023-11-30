import requests
import logging
import csv
from pydantic import BaseModel


def get_list_all_elements(resource: str) -> list[dict]:
    """Get a list of dictionaries from the given endpoint by resource.

    Args:
        resource (str): The path of endpoint where you want to make the get request to retrieve the data.

    Returns:
        list[dict]: List of dictionary from the api.
    """
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


def export_generic_model_to_csv(model_class: BaseModel, list_of_elements_to_be_exported: list[dict], exported_file_name: str):
    """Carries out export of containing values in the given list of elements, using the given Pydantic model
    to ensure the output format.     

    Args:
        model_class (BaseModel): A pydantic BaseModel of the given list_of_elements modules
        list_of_elements_to_be_exported (list[dict]): A list that be taken from `get_list_all_elements` function
        exported_file_name (str): The name of file that will be exported.

    """
    with open(exported_file_name, "w", newline='') as myfile:
        writer = csv.DictWriter(myfile, fieldnames=model_class.model_fields.keys())
        writer.writeheader()
        for dict_element in list_of_elements_to_be_exported:
            instance = model_class(**dict_element)
            instance_dict = instance.model_dump()
            writer.writerow(instance_dict)
    logging.info("The CSV file has been exported")