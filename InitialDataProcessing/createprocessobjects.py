from DataLoading import getjsondata
import pandas


# Function to create process objects from process start and process stop objects
def createprocessobject(ParentLocation):
    # Get the Process Start objects
    processstartobject = getjsondata.getProcessStartObjects(ParentLocation)

    # Get the Process Stop objects
    processstopobject = getjsondata.getProcessStopObjects(ParentLocation)

    # Iterate over the ProcessStart Objects and find the corresponding ProcessStop Object
    print("Creating Process Objects")