import pandas as pd

def count_distinct_values(field_name: str, csv_name: str) -> int:
    df = pd.read_csv(csv_name)
    return len(pd.unique(df[field_name]))


def count_people_with_more_than_two_elements(field_name: str, csv_name: str) -> int:
    df = pd.read_csv(csv_name)
    return len(df[df[field_name].map(len) > 2])


if __name__ == "__main__":
    # how many starships?
    print(count_distinct_values("name", "starships.csv"))

    # how many people with more than 2 starships?
    print(count_people_with_more_than_two_elements("starships", "personagens.csv"))
