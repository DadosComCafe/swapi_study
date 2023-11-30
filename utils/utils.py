import requests
import logging
import csv


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


def export_to_csv(list_of_elements_to_be_exported: list[dict], exported_file_name: str) -> str:
    myfile = open(exported_file_name, "w")
    writer = csv.writer(myfile)
    writer.writerow((list_of_elements_to_be_exported[0].keys()))
    for dict_element in list_of_elements_to_be_exported:
        writer.writerow(dict_element.values())
    myfile.close()
    return "The csv file has been exported"
