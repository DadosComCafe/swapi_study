import pandas as pd

class StarWarsSearch:
    def __init__(self, field_name, csv_name) -> None:
        self.field_name = field_name
        self.csv_name = csv_name

    def count_distinct_values(self) -> int:
        df = pd.read_csv(self.csv_name)
        return len(pd.unique(df[self.field_name]))


    def count_target_with_more_than_two_elements(self) -> int:
        df = pd.read_csv(self.csv_name)
        return len(df[df[self.field_name].map(len) > 2])

    def planet_with_biggest_value(self) -> tuple:
        df = pd.read_csv(self.csv_name)
        df = df[(df.name != "unknown") & (df[self.field_name] != "unknown")]
        df[self.field_name] = df[self.field_name].astype(int)
        indx_from_biggest = df[self.field_name].idxmax()
        element = df.loc[indx_from_biggest]
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
    planet_name, population_value = question3.planet_with_biggest_value()
    print(f"The planet with the biggest {question3.field_name} is {planet_name} with {population_value}")
