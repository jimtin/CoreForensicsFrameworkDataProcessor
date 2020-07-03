import json
import pandas as pd
from pathlib import Path

# This library controls all querying of provided JSON objects, then conversion into pandas dataframes

# Function to get the jsonobjects
def getJSONObjects(ParentLocation, ObjectFileName):
    # Turn the file path in a path object
    ParentLocation = Path(ParentLocation)

    # Add the ObjectFileName to the path
    Location = ParentLocation / ObjectFileName

    # Open the file
    with open(Location) as processfile:
        # Load the json into a python data structure
        JSONObject = json.load(processfile)

    # Close the file
    processfile.close()

    # Return the processstart object
    return JSONObject

# Function to get ProcessStart Objects
def getProcessObjects(ParentLocation, ProcessFileName, DataObjectName):
    # Get the initial json file
    processinitial = getJSONObjects(ParentLocation, ProcessFileName)

    # Extract the ProcessStart data
    processobject = processinitial[DataObjectName]

    # Convert into a dataframe
    df = pd.DataFrame(data=processobject)

    # Convert DateTime into a DateTime object
    df['DateTime'] = pd.to_datetime(df['DateTime'])

    # Set the index to be based on time
    df.set_index('DateTime', inplace=True, drop=True)

    # Return the ProcessStart Object
    return df

# Function to get ProcessStart objects
def getProcessStartObjects(ParentLocation):
    # Get the process start objects
    processstart = getProcessObjects(ParentLocation, "processstarts.json", "ProcessStartLogs")

    # Return the outcome
    return processstart

# Function to get the ProcessStop objects
def getProcessStopObjects(ParentLocation):
    # Get the process stop objects
    processstop = getProcessObjects(ParentLocation, "processstops.json", "ProcessStopLogs")

    # Return the outcome
    return processstop

