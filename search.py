import pandas as pd

def count_distinct_values(field_name: str, csv_name: str) -> int:
    df = pd.read_csv(csv_name)
    return len(pd.unique(df[field_name]))

if __name__ == "__main__":
    # how many starships?
    print(count_distinct_values("name", "starships.csv"))
