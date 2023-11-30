import logging
from utils import get_list_all_elements, export_person_to_csv, export_planet_to_csv, export_starship_to_csv


if __name__ == "__main__":
    try:
        list_of_element = get_list_all_elements(resource="/people/")
        export_person_to_csv(
            list_of_elements_to_be_exported=list_of_element,
            exported_file_name="personagens.csv"
        )
        logging.info(f"The data of resource '/people/' has been colected and the file 'personagens.csv' has been exported!")
    except Exception as e:
        logging.error(f"An error: {e}")
    
    try:
        list_of_element = get_list_all_elements(resource="/planets/")
        export_planet_to_csv(
            list_of_elements_to_be_exported=list_of_element,
            exported_file_name="planetas.csv"
        )
        logging.info(f"The data of resource '/planets/' has been colected and the file 'planetas.csv' has been exported!")
    except Exception as e:
        logging.error(f"An error: {e}")
    
    try:
        list_of_element = get_list_all_elements(resource="/starships/")
        export_starship_to_csv(
            list_of_elements_to_be_exported=list_of_element,
            exported_file_name="starships.csv"
        )
        logging.info(f"The data of resource '/starships/' has been colected and the file 'starships.csv' has been exported!")
    except Exception as e:
        logging.error(f"An error: {e}")
