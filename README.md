# Data Analysis with Python

No exclusive GNU utilities usage.

Solution developed on **Windows**.

## How to use ? :smiley:

To run this program, do one of the following :arrow_down:

### Only for Windows visitors

For more information about how to install Makefile into your computer, direct to:

- For a more detailed description: [Chocolatey Overview Repo](https://github.com/miguelestradam36/chocolatey-for-windows)
- For a quick set-up: [Other project that uses Chocolatey and Make GNU](https://github.com/miguelestradam36/python-skillset-01)

### For Linux and MacOS visitors

#### For Linux users

```bash
#Update the package installer
sudo apt-get update
#Make sure you have the build-essentials package to make use of tools like:
#GCC for example.
sudo apt-get install build-essential

#At last, let's be 100% sure.
sudo apt-get -y install make
```

#### For MacOS users

```bash
#Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
#Run this command
brew install make
```

### First-Use Instructions

First steps to use this project into your computer.

#### Manual Execution

- If you want to run this app directly on your **Operating System**
  - `python app/main.py` *or* `python3 app/main.py`

- If you want to run it upon a Virtual Environment:
  1. First run
     - `python -m venv venv`
  2. Then active your virtual environment:
     - For **Linux** or **MacOS**: `source venv/bin/python3` *or* `venv/bin/activate`
     - For **Windows**: 
       - from **CMD** `venv\Scripts\Activate.bat` *or* `ven\Scripts\activate`
       - from **Git Bash**, the same commands as on Linux.

#### Automatic Execution

## Documentation Overview :arrow_down:

Quick overview over some of the functionalities of this project.

Consult the documentation folder for more information: [Documentation](docs/)

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