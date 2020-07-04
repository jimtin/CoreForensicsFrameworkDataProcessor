"""
Unit tests for loading data into memory space
"""

# Python Dictionaries
import os
import pandas as pd
from pathlib import Path

# My functions to test
from DataLoading import getjsondata
from InitialDataProcessing import createprocessobjects

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

    # Test combineProcessStartProcessStop function can combine ProcessStart and ProcessStop objects
    def test_combineProcessStartProcessStop(self):
        # Load the test data
        processobject = createprocessobjects.combineProcessStartProcessStop(TestDataLoading.ParentLocation)

        # Assert that the result is a process object
        assert processobject.head(1).HostHunterObject.values[0] == "ProcessStartProcessStopObject"

    # Test combineProcessStartProcessStop function selects the stop object directly after process start
    def test_combineProcessStartProcessStopfirstStop(self):
        # Load the test data
        processobject = createprocessobjects.combineProcessStartProcessStop(TestDataLoading.ParentLocation)

        # Assert that the stop time is "2020-06-22T18:30:38.925157+10:00"
        assert str(processobject.head(1).ProcessStopTime.values[0]) == "2020-06-22T18:30:38.925157+10:00"

    # Test combineProcessStartProcessStop function creates no more than the count of the ProcessStart events
    def test_combineProcessStartProcessStopcount(self):
        # Load the test data
        processobject = createprocessobjects.combineProcessStartProcessStop(TestDataLoading.ParentLocation)

        # Get a count of the number of ProcessStart objects
        procstart = getjsondata.getProcessStartObjects(TestDataLoading.ParentLocation)

        # Assert dataframe count is no more than number of process start objects
        assert processobject.shape[0] <= procstart.shape[0]

    # Test combineProcessStartProcessStop function returns a 'No Process Stop Found' when given a process which hasn't exited
    def test_combineProcessStartProcessStopnotexited(self):
        # Load the test data
        processobject = createprocessobjects.combineProcessStartProcessStop(TestDataLoading.ParentLocation)

        # Get the ProcessObject with no related stop object
        ProcessIdNoStop = [2192000]
        testobject = processobject[processobject.ProcessId.isin(ProcessIdNoStop)]

        # Assert that the value of ProcessStopsLogs is false
        assert testobject.ProcessStopLogs.values[0] == False
