# Data Analysis with Python

No exclusive GNU utilities usage.

Solution developed on **Windows**.

## How to use ? :smiley:

To run this program, do one of the following :arrow_down:

### First-Use Instructions

- If you want to run this app directly on your **Operating System**
  - `python app/main.py` *or* `python3 app/main.py`

- If you want to run it upon a Virtual Environment:
  1. First run
     - `python -m venv venv`
  2. Install the dependencies:
     - For **Linux** or **MacOS**: `venv/bin/python3 -m pip install -r config/requirements.txt`
     - For **Windows**: `venv/Scripts/python -m pip install -r config/requirements.txt`
  3. Then active your virtual environment:
     - For **Linux** or **MacOS**: `source venv/bin/python3` *or* `venv/bin/activate`
     - For **Windows**: 
       - from **CMD** `venv\Scripts\Activate.bat` *or* `ven\Scripts\activate`
       - from **Git Bash**, the same commands as on Linux.

Consult the scripts at the documentation: [Documentation README](docs/README.md)

## About this project

Some of the details of the project are listed below :arrow_down:

### Data Diagram

Dataset to use during this exercise.

![Data Diagram Image](docs/Images/marked-diagram.jpg "Developed using DbDiagram.io")

For more information about the data used, please refer to: [Excel File](app/data/CarSalesDataForReports.xlsx)

**Note**
You will not be able to open it on Github... :sweat_smile:

### Data Transformations

The data transformations will be carried out with help of Python scripts, which will use the modules `pandas` and `sqlite3`.

For more information about the data used, please refer to: [Scripts Python Module](app/scripts/)

### Author

Miguel Estrada: 