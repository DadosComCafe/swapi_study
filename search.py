import pandas as pd

def count_distinct_values(field_name: str, csv_name: str) -> int:
    df = pd.read_csv(csv_name)
    return len(pd.unique(df[field_name]))


def count_people_with_more_than_two_elements(field_name: str, csv_name: str) -> int:
    df = pd.read_csv(csv_name)
    return len(df[df[field_name].map(len) > 2])

def planet_with_biggest_value(field_name: str, csv_name: str) -> str:
    df = pd.read_csv(csv_name)
    df = df[(df.name != "unknown") & (df[field_name] != "unknown")]
    df[field_name] = df[field_name].astype(int)
    indice_maior_populacao = df[field_name].idxmax()
    planeta = df.loc[indice_maior_populacao]
    return f"O planeta com o maior {field_name} é {planeta['name']}, com um {field_name} de {planeta[field_name]}"


if __name__ == "__main__":
    # how many starships?
    print(count_distinct_values("name", "starships.csv"))

    # how many people with more than 2 starships?
    print(count_people_with_more_than_two_elements("starships", "personagens.csv"))

    # what is the planet with biggest population?
    print(planet_with_biggest_value("population", "planetas.csv"))