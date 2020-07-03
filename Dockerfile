# Get the image
FROM python:3

# Change working directory to usr directory
WORKDIR /usr/src/app

# Download the latest github
ADD https://github.com/jimtin/CoreForensicsFrameworkDataProcessor/archive/master.zip /usr/src/app/DataProcessor.zip

# Unzip the file
RUN unzip DataProcessor.zip

# Change working directory to HostHunterDataProcessor
WORKDIR /usr/src/app/CoreForensicsFrameworkDataProcessor-master

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

