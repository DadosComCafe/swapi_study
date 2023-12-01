# STARWARS API -> Study

## HOW TO USE 

* __1. Clone the repository__:
    - `git clone https://github.com/DadosComCafe/swapi_study.git`

* __2. Create a virtualenv__:
    - `python -m venv .venv`
    - `source .venv/bin/activate`

* __3. Install dependencies__:
    - `pip install -r requirements.txt`

* __4. Run python to get the csv file__:
    - `python export_csv/main.py`
    - `You need to wait a moment while the get request is be doing.`

* __5. Make a search in the exported csv__:
    - `One there are the csv files exported in the previous step, you can analize them`
    - `python search/search.py`

* __6. Take a look in the data with pydantic models__:
    - `No csv file is necessary in this step, once all the used data is placed in sources/ directory`
    - `python custom_data_structure/main.py`
