#Manage threads into Python
"""
This way the test imports will not be added to the working thread which 
has another way of managing python modules
"""
import threading

#Import the class for data management
from scripts.data_handler import DataManager

#Create threaded actions
class SetUpTask(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        #TODO: Insert the set-up actions
        from scripts.setup_handler import SetUpManager
        os_handler = SetUpManager()
        os_handler.requirements_location = 'config/requirements.txt'

#Set-Up process into a function to be called at main
def do_installs():
    # Setting up the environment
    installments = SetUpTask()
    installments.start()
    #installments.join() is not used, since if I were to join the threads I would be causing the imports problem I try to avoid
    del installments

def main():
    oop_example = DataManager()
    oop_example.filename = 'data/CarSalesDataForReports.xlsx'
    oop_example.database = 'database/CarSalesData.db'

#Main thread
if __name__ == "__main__":
    print("Starting excercise...")

    # Setting up the environment
    do_installs()

    #TODO: Data Manipulation scripts goes here
    main()

