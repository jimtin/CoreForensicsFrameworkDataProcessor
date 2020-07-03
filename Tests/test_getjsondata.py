"""
Unit tests for loading data into memory space
"""

from DataLoading import getjsondata
import os
import pandas as pd
from pathlib import Path

class TestDataLoading:

    # Set up some variables for test
    ## Get the Current Working Directory as the 'ParentLocation' for tests
    ParentLocation = os.getcwd()

    # Turn the ParentLocation into a Path
    ParentLocation = Path(ParentLocation)

    ## Update the Current Working Directory to take account of the Tests folder
    ParentLocation = ParentLocation / "Tests"

    # Test ability to convert json into a dictionary
    def test_jsontodictconversion(self):
        # Load test data
        processdict = getjsondata.getJSONObjects(TestDataLoading.ParentLocation, "processstarts.json")

        # Assert positive outcome
        assert type(processdict) == dict

    # Test getProcessObjects returns a dataframe
    def test_dicttodataframeconversion(self):
        # Load test data
        dataframe = getjsondata.getProcessObjects(TestDataLoading.ParentLocation, "processstarts.json", "ProcessStartLogs")

        # Assert the returned result
        assert type(dataframe) == pd.DataFrame

    # Test getProcessStartObjects returns the correct data
    def test_getProcessStartObjectsReturnCorrectData(self):
        # Load the test data
        procstartobject = getjsondata.getProcessStartObjects(TestDataLoading.ParentLocation)

        # Assert positive outcome
        assert procstartobject.head(1).CreatorAccountDomain.values[0] == "FAKEWORKGROUP"

    # Test getProcessStartObjects does not return the wrong data
    def test_getProcessStartObjectsnotReturnIncorrectData(self):
        # Load the test data
        procstartobject = getjsondata.getProcessStartObjects(TestDataLoading.ParentLocation)

        # Assert negative outcome
        assert procstartobject.head(1).CreatorAccountDomain.values[0] != "FAKEWORKGROUPS"

    # Test getProcessStopObjects returns the correct data
    def test_getProcessStopObjectsReturnCorrectData(self):
        # Load the test data
        procstopobject = getjsondata.getProcessStopObjects(TestDataLoading.ParentLocation)

        # Assert positive outcome
        assert procstopobject.head(1).AccountDomain.values[0] == "FAKEWORKGROUP"

    # Test getProcessStopObjects does not return incorrect data
    def test_getProcessStopObjectsnotReturnIncorrectData(self):
        # Load the test data
        procstopobject = getjsondata.getProcessStopObjects(TestDataLoading.ParentLocation)

        # Assert negative outcome
        assert procstopobject.head(1).AccountDomain.values[0] != "FAKEWORKGROUPS"
