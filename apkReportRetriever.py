import requests
import os
import time


def retrieve(fileName, resource):
    params = {'apikey': '4be7c402ae4840712246a312d01c7f23790fc8314e93a57209154d581da2d1c6', 'resource': str(resource)}
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "gzip,  My Python requests library example client or username"
    }
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
    print(response)
    json_response = response.json()
    print(json_response)
    outputFileName = fileName + '_report.txt'
    textOutput = open(outputFileName, "w")
    textOutput.write(str(json_response))
    textOutput.close()


def traverse(directory):
    cwd = os.getcwd()
    print('Current working directory is: ' + cwd)
    print('Uploading files from directory: ' + directory)
    APKList = os.listdir(directory)
    return APKList


def start():
    directory = input("Please enter the directory of reports you wish to retrieve.\n")
    directoryList = traverse(directory)
    count = 0
    timer = 10
    for files in directoryList:
        timeStart = time.time()
        if files.lower().endswith('.txt'):
            if redundancyCheck(str(directory) + str(files)) == 0:
                print('Retrieving report for: ' + files)
                filePath = directory + str(files)
                status = 0

                reportData = open(str(directory) + str(files), 'r')
                reportDataBuffer = reportData.read()
                resourceData = str(reportDataBuffer)
                strings = resourceData.split(',')
                try:
                    print(strings[2])
                    resource = strings[2].split(':')
                    sanitizedResource = resource[1].split('"')
                    print(sanitizedResource[1])
                    retrieve(files, str(sanitizedResource[1]))
                    status = 1
                except IndexError as error:
                    print("Error retrieving report for " + str(files) + ". Error: " + str(error))
                    return

                timeEnd = time.time()
                if status == 1:
                    print('Retrieving ' + files + ' complete.')
                if timeEnd - timeStart < 60:
                    count = count + 1
                    if count == 4:
                        count = 0
                        time.sleep(60)


def redundancyCheck(fileName):
    status = 0
    if os.path.isfile(str(fileName) + '.txt'):
        status = 1
    return status


print("Welcome to the Report Retriever.\n")
start()


'''
import requests
params = {'apikey': '-YOUR API KEY HERE-', 'resource': '7657fcb7d772448a6d8504e4b20168b8'}
headers = {
  "Accept-Encoding": "gzip, deflate",
  "User-Agent" : "gzip,  My Python requests library example client or username"
  }
response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
  params=params, headers=headers)
json_response = response.json()
'''