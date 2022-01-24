# Documentation 

## Usage

## Set Up

### Virtual Environment Configuration

To configure a Virtual Environment, the script would look as following:

#### For Windows
```cmd
#Create virtual environment
python -m venv venv

#Install requirements.txt into venv
venv\Scripts\python -m pip install -r config/requirements.tx

#Activate venv
venv\Scripts\Activate.bat
```

#### For Linux or MacOS
```bash
#Create virtual environment
python -m venv venv

#Install requirements.txt into venv
source venv/bin/python3

#Activate venv
venv/bin/python3 -m pip install -r config/requirements.txt
```