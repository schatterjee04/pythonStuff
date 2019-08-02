import os

def traverse(directory):
    cwd = os.getcwd()
    print('Current working directory is: ' + cwd)
    print('Uploading files from directory: ' + directory)
    APKList = os.listdir(directory)
    return APKList


def start():
    directory = input("Please enter the directory of reports you wish to retrieve.\n")
    directoryList = traverse(directory)
    for files in directoryList:
        if files.lower().endswith('.txt'):
            if redundancyCheck(str(directory) + str(files)) == 0:
                print('Retrieving report for: ' + files)
                reportData = open(str(directory) + str(files), 'r')
                reportDataBuffer = reportData.read()
                resourceData = str(reportDataBuffer)
                strings = resourceData.split(',')
                try:
                    resource = strings[2].split(':')
                    sanitizedResource = resource[1].split('"')
                    print(sanitizedResource[1])
                except IndexError as error:
                    print("Error retrieving report for " + str(files) + ". Error: " + str(error))
                    return


def redundancyCheck(fileName):
    status = 0
    if os.path.isfile(str(fileName) + '_report.txt'):
        status = 1
    return status


print("Welcome to the Report Retriever.\n")
start()