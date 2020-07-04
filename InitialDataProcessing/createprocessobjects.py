from DataLoading import getjsondata
import pandas


# Function to create process objects from process start and process stop objects
def combineProcessStartProcessStop(ParentLocation):
    # Get the Process Start objects
    processstartobject = getjsondata.getProcessStartObjects(ParentLocation)

    # Get the Process Stop objects
    processstopobject = getjsondata.getProcessStopObjects(ParentLocation)

    # Process object DataFrame
    proclist = []

    # Iterate over the ProcessStart Objects and find the corresponding ProcessStop Object
    for data in processstartobject.iterrows():
        # Get the content of the row
        row = data[1]

        # Get the ProcessId to be searched on
        ProcessId = str(row["ProcessId"])

        # Get the start time of the process
        starttime = row.DateTime

        # Update the ProcessStopObjects to only include items after the process start
        procstopobjects = processstopobject.loc[processstopobject.index > pandas.to_datetime(starttime)]

        # Search for the ProcessId in the ProcessStop Logs
        procstopobjects = procstopobjects.query(f'ProcessId=={ProcessId}')

        # If data returned from procstopobject search, create the combined process object
        if procstopobjects.empty == True:
            processobject = {
                "ParentProcessId": row.ParentProcessId,
                "DateTime": row.DateTime,
                "ProcessStartTime": row.DateTime,
                "TargetLogonId": row.TargetLogonId,
                "TargetAccountName": row.TargetAccountName,
                "ProcessId": row.ProcessId,
                "TokenElevationType": row.TokenElevationType,
                "ParentProcessPath": row.ParentProcessPath,
                "ProcessStartEventLogRecordId": row.EventLogRecordId,
                "TargetAccountDomain": row.TargetAccountDomain,
                "ProcessStartCreatorAccountName": row.CreatorAccountName,
                "ProcessCommandLine": row.ProcessCommandLine,
                "ProcessStartCreatorLogonID": row.CreatorLogonID,
                "Source": row.Source,
                "TargetSecurityId": row.TargetSecurityId,
                "ProcessStartCreatorAccountDomain": row.CreatorAccountDomain,
                "ProcessStartPath": row.ProcessStartPath,
                "Target": row.Target,
                "SecurityID": row.SecurityID,
                "CreatorSecurityID": row.CreatorSecurityID,
                "ProcessExitStatus": "NoProcessStopObject",
                "ProcessStopLogs": False,
                "ProcessStartLogs": True,
                "ProcessStopEventLogRecordID": "NoProcessStopObject",
                "ProcessStopAccountDomain": "NoProcessStopObject",
                "ProcessStopLogonID": "NoProcessStopObject",
                "ProcessStopAccountName": "NoProcessStopObject",
                "ProcessStopTime": "NoProcessStopObject",
                "HostHunterObject": "ProcessStartProcessStopObject"
            }

            # Append the output to the proclist
            proclist.append(processobject)
        else:
            # Only get data after the start time
            procstopobjects = procstopobjects.loc[procstopobjects.index > pandas.to_datetime(starttime)]

            # Select the first occurrence as this is associated with the process start
            procstop = procstopobjects.head(1)

            # Join the two objects together
            processobject = {
                "ParentProcessId": row.ParentProcessId,
                "DateTime": row.DateTime,
                "ProcessStartTime": row.DateTime,
                "TargetLogonId": row.TargetLogonId,
                "TargetAccountName": row.TargetAccountName,
                "ProcessId": row.ProcessId,
                "TokenElevationType": row.TokenElevationType,
                "ParentProcessPath": row.ParentProcessPath,
                "ProcessStartEventLogRecordId": row.EventLogRecordId,
                "TargetAccountDomain": row.TargetAccountDomain,
                "ProcessStartCreatorAccountName": row.CreatorAccountName,
                "ProcessCommandLine": row.ProcessCommandLine,
                "ProcessStartCreatorLogonID": row.CreatorLogonID,
                "Source": row.Source,
                "TargetSecurityId": row.TargetSecurityId,
                "ProcessStartCreatorAccountDomain": row.CreatorAccountDomain,
                "ProcessStartPath": row.ProcessStartPath,
                "Target": row.Target,
                "SecurityID": row.SecurityID,
                "CreatorSecurityID": row.CreatorSecurityID,
                "ProcessExitStatus": procstop.ProcessExitStatus,
                "ProcessStopLogs": True,
                "ProcessStartLogs": True,
                "ProcessStopEventLogRecordID": procstop.EventLogRecordId,
                "ProcessStopAccountDomain": procstop.AccountDomain,
                "ProcessStopLogonID": procstop.LogonID,
                "ProcessStopAccountName": procstop.AccountName,
                "ProcessStopTime": procstop.DateTime[0],
                "HostHunterObject": "ProcessStartProcessStopObject"
            }

            # Append the output to the proclist
            proclist.append(processobject)
    # Turn proc list back into a Dataframe
    procdf = pandas.DataFrame(proclist)

    # Convert DateTime into a DateTime object
    procdf['DateTime'] = pandas.to_datetime(procdf['DateTime'])

    # Set the index to be based on time
    procdf.set_index('DateTime', inplace=True, drop=False)

    return procdf

