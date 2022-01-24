# Documentation 

## Usage

First run the transformation scripts by executing the python file at the: [python main script of the app](../app/main.py)

## Set Up

In this case, the setup is done automatically by the python scripts.

## Extras

### Virtual Environment Configuration

To configure a Virtual Environment, the script would look as following:

#### For Windows
```cmd
#Create virtual environment
python -m venv venv

#Activate venv
venv\Scripts\Activate.bat
```

#### For Linux or MacOS
```bash
#Create virtual environment
python -m venv venv

#Activate venv
source venv/bin/python3
```

### Create context with SQL

In this excercise due to time matters, the Database was not created solely with SQL.

But one good approach of doing so, could be found at: [SQL Example](examples/create_context.sql)