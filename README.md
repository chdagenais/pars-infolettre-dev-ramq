# parse-infolettre-dev-ramq
Outil pour extraire les données des infolettres destinées aux developpeurs de logiciel de pharmacie de la RAMQ

Utilise tabula-py et pandas pour extraire les données des infolettres RAMQ PDF en format CSV ou autre
## Basic setup
Testé avec Python 3.11

1. Clone the repo

2. Create a virtual-env
```
python -m venv venv
. venv/Script/activate  # for windows
source venv/bin/activate  # for linux or mac
```

install requirements in venv
```
pip install -r requirements.txt
```
Sassurer que Java est installé sur votre machine
voir https://tabula-py.readthedocs.io/en/latest/getting_started.html#get-tabula-py-working-windows-10    pour plus d'informations


3. Edit FILEPATH in main.py if needed and Run

`main.py`
