import logging
from utils import get_list_all_elements, export_generic_model_to_csv
from models.person import PersonModel
from models.planet import PlanetModel
from models.starship import StarShipModel

if __name__ == "__main__":
    list_dict_resource_filename = [
        {
            "resource": "/people/",
            "model_class": PersonModel,
            "filename": "personagens.csv",
        },
        {
            "resource": "/planets/",
            "model_class": PlanetModel,
            "filename": "planetas.csv",
        },
        {
            "resource": "/starships/",
            "model_class": StarShipModel,
            "filename": "starships.csv",
        },
    ]

    for dicio in list_dict_resource_filename:
        try:
            list_of_element = get_list_all_elements(dicio["resource"])
            export_generic_model_to_csv(
                model_class=dicio["model_class"],
                list_of_elements_to_be_exported=list_of_element,
                exported_file_name=dicio["filename"],
            )
            logging.info(
                f"The data of resource {dicio['resource']} has been colected and the file {dicio['filename']} has been exported!"
            )
        except Exception as e:
            logging.error(f"An error: {e}")
