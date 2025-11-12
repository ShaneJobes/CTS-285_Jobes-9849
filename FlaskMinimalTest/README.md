## Flask Quickstart Setup
Setup flask on a virtual environment to run web apps

## Setup Virtual Environment
In terminal
python3 -m venv .venv
Activate venv with:
. .venv/bin/activate

## Intall Flask 
pip install flask
verify install:
flask --version

## Run flask
flask --app minimal run
Press ctrl+c to quit app

## Notes
make sure you are in the correct directory before running venv
make sure you have flask installed with flask --version command
flask --app minimal run --debug to open debugging page