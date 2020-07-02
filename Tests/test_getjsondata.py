"""
Unit tests for loading data into memory space
"""

from DataLoading import getjsondata
import os
import pandas as pd

class TestDataLoading:

    # Set up some variables for test
    ## Get the Current Working Directory as the 'ParentLocation' for tests
    ParentLocation = os.getcwd()

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
    #def test_getProcessStartObjectsReturnData(self):
        # Load the test data
    #    procstartobject = getjsondata.getProcessStartObjects(TestDataLoading.ParentLocation)

