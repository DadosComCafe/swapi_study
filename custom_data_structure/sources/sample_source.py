from models.person import PersonModel
from models.planet import PlanetModel
from models.starship import StarShipModel

# source to PlanetModel
planet_data = {
    "id": 1,
    "name": "Tatooine",
    "rotation_period": "23",
    "orbital_period": "304",
    "diameter": "10465",
    "climate": "arid",
    "gravity": "1 standard",
    "terrain": "desert",
    "surface_water": "1",
    "population": "200000",
    "residents": ["https://swapi.dev/api/people/1/", "https://swapi.dev/api/people/2/"],
    "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/"],
    "created": "2014-12-09T13:50:49.641000Z",
    "edited": "2014-12-15T13:48:16.167217Z",
    "url": "https://swapi.dev/api/planets/1/",
}
sample_planetmodel_instance = PlanetModel(**planet_data)


# source to StarShipModel
starship_data = {
    "id": 1,
    "name": "X-wing",
    "model": "T-65 X-wing",
    "manufacturer": "Incom Corporation",
    "cost_in_credits": "149999",
    "length": "12.5",
    "max_atmosphering_speed": "1050",
    "crew": "1",
    "passengers": "0",
    "cargo_capacity": "110",
    "consumables": "1 week",
    "hyperdrive_rating": "1.0",
    "MGLT": "100",
    "starship_class": "Starfighter",
    "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/"],
    "created": "2014-12-12T11:19:05.340000Z",
    "edited": "2014-12-22T17:35:44.491233Z",
    "url": "https://swapi.dev/api/starships/1/",
}
sample_starshipmodel_instance = StarShipModel(**starship_data)


# Dicionário para PersonModel
person_data = {
    "id": 1,
    "name": "Luke Skywalker",
    "height": "172",
    "mass": "77",
    "hair_color": "blond",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "19BBY",
    "gender": "male",
    "homeworld": sample_planetmodel_instance,
    "films": ["https://swapi.dev/api/films/1/", "https://swapi.dev/api/films/2/"],
    "species": ["https://swapi.dev/api/species/1/"],
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/",
    ],
    "starships": [sample_starshipmodel_instance],
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-20T21:17:56.891000Z",
    "url": "https://swapi.dev/api/people/1/",
}

sample_personmodel_instance = PersonModel(**person_data)
