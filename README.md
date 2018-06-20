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
Navigate into the `/server` directory and run:
```
python setup.py install
```
Then navigate into the `/client` directory and do the same.

Then navigate into the `/server` directory and run the program with:
```
python -m swagger_server
```
