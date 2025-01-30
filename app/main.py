#Manage threads into Python
"""
This way the test imports will not be added to the working thread which 
has another way of managing python modules
"""
import threading
import os

#Import the class for data management
from data_scripts_module.data_handler import DataManager

#Create threaded actions
class SetUpTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        #TODO: Insert the set-up actions
        from data_scripts_module.setup_handler import SetUpManager
        os_handler = SetUpManager()
        os_handler.requirements_location = os_handler.os.path.join(os_handler.os.path.dirname(__file__), 'config/requirements.txt')

#Set-Up process into a function to be called at main
def do_installs():
    # Setting up the environment
    installments = SetUpTask()
    installments.start()
    installments.join()
    del installments

#Main thread
if __name__ == "__main__":
    print("Starting excercise...\n")

    # Setting up the environment
    do_installs()

    #TODO: Data Manipulation scripts goes here
    oop_example = DataManager()

    dir_path = os.path.dirname(os.path.realpath(__file__))

    oop_example.database = os.path.join(dir_path, "data\\db\\CarSalesData.db")

    oop_example.filename = os.path.join(dir_path, "data\\excel\\CarSalesDataForReports.xlsx")
    
    oop_example.excel_to_db()
    
    del oop_example