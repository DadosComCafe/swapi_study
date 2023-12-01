import pandas as pd

class StarWarsSearch:
    def __init__(self, field_name: str, csv_name: str) -> None:
        """The classe will be use to get some informations about the starwars csv's containing in this repository.
        This class uses pandas to handle dataframes with the csv values.

        Args:
            field_name (str): The csv column to be used in the search
            csv_name (str): The csv filename.
        """
        self.field_name = field_name
        self.csv_name = csv_name
        self.df = pd.read_csv(self.csv_name)
        self.df = self.df[(self.df.name != "unknown") & (self.df[self.field_name] != "unknown")]

    def count_distinct_values(self) -> int:
        """Count the number of distinct values in the given csv and field_name. 

        Returns:
            int: The number of unique values be found in the given field name. 
        """
        return len(pd.unique(self.df[self.field_name]))


    def count_target_with_more_than_two_elements(self) -> int:
        """This method compares the value of the given field in the given csv file
        and count the number of records that have more than 2 occurrence in the . 
        Example: I would like to now how many names in the `personagens.csv` has more than 2 films. 
        In this case I need to use csv_name=`personagens.csv` and  field_name=`films`.

        Returns:
            int: The number of names has more than 2 elements in the field. 
        """
        return len(self.df[self.df[self.field_name].map(len) > 2])

    def target_with_biggest_value(self) -> tuple:
        """Found the biggest value of the given `field_name` in the given csv.

        Returns:
            tuple: A tuple with the (value of field `name` and value of field given `field_name`)
        """
        self.df[self.field_name] = self.df[self.field_name].astype(int)
        indx_from_biggest = self.df[self.field_name].idxmax()
        element = self.df.loc[indx_from_biggest]
        return element["name"],element[self.field_name]


if __name__ == "__main__":
    # how many starships?
    question1 = StarWarsSearch("name", "starships.csv")
    print(f"There are {question1.count_distinct_values()} starships!")

    # how many people with more than 2 starships?
    question2 = StarWarsSearch("starships", "personagens.csv")
    print(f"There are {question2.count_target_with_more_than_two_elements()} people with more than 2 starships")

    # what is the planet with biggest population?
    question3 = StarWarsSearch("population", "planetas.csv")
    planet_name, population_value = question3.target_with_biggest_value()
    print(f"The planet with the biggest {question3.field_name} is {planet_name} with {population_value}")
