## TKG Beacon
For wrapping Translator Knowledge Graph compliant Neo4j databases

### Getting started
Create a fresh virtual environment
```
virtualenv -p python3.5 venv
source venv/bin/activate
```

Install the project requirements:
```
pip install -r requirements.txt
```

Setup the config file by copying the sample file:
```
cp config.sample.yaml config.yaml
``` 
Change the database settings in `config.yaml` to match the address and credentials of the wanted neo4j database.

Navigate into the `/server` directory and run:
```
python setup.py install
```

Then navigate into the `/ontology` and `/client` directories and do the same.

Then navigate into the `/server` directory and run the program with:
```
python -m swagger_server
```

The Swagger UI can be found at `{basepath}/ui/`, e.g. `localhost:8080/ui/`

### Configuring the beacon
Settings should be in `config.yaml`.
Change the database address (bolt protocol), username, and password to the Neo4j database you would like to wrap.

Setting `filter_biolink` to `True` will ignore all categories that are non-Biolink compliant if a concept has more than one category. If only one category exists for a particular concept, the concept will be reported by the beacon as `"named thing"`.
