import logging
from utils import get_list_all_elements, export_to_csv


if __name__ == "__main__":
    resource_and_filename = [
    {
        "resource": "/people/",
        "filename": "personagens.csv"
    },
    {
        "resource": "/planets/",
        "filename": "planetas.csv"
    },
    {
        "resource": "/starships/",
        "filename": "starships.csv"
    }
    ]
    for dicio in resource_and_filename:
        try:
            list_of_element = get_list_all_elements(resource=dicio["resource"])
            export_to_csv(
                list_of_elements_to_be_exported=list_of_element,
                exported_file_name=dicio["filename"]
            )
            logging.info(f"The data of resource {dicio['resource']} has been colected and the file {dicio['filename']} has been exported!")
        except Exception as e:
            logging.error(f"An error: {e}")
