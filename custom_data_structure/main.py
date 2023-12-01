from sources import sample_personmodel_instance

if __name__ == "__main__":
    print(f"Information about the person")
    print(sample_personmodel_instance)

    print(f"*" * 50)

    print(f"Informations about its planet")
    print(sample_personmodel_instance.homeworld)

    print(f"*" * 50)

    print(f"Informations about its starship")
    print(sample_personmodel_instance.starships)
