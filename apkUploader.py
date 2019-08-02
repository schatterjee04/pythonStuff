import requests
import os
import time


def upload(fileName):
    params = {'apikey': '4be7c402ae4840712246a312d01c7f23790fc8314e93a57209154d581da2d1c6'}
    files = {'file': (fileName, open(fileName, 'rb'))}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files,params=params)
    print(response)
    path = '/Users/Sourav/Desktop/Receipts/'
    outputFileName = path + fileName + '.txt'
    textOutput = open(outputFileName, "w")
    textOutput.write(response.text)
    textOutput.close()


def traverse(directory):
    cwd = os.getcwd()
    print('Current working directory is: ' + cwd)
    print('Uploading files from directory: ' + directory)
    APKList = os.listdir(directory)
    return APKList


def start():
    directory = input("Please enter the directory of APKs you wish to upload.\n")
    directoryList = traverse(directory)
    count = 0
    timer = 10
    for files in directoryList:
        timeStart = time.time()
        if files.lower().endswith('.apk'):
            if redundancyCheck(str(directory) + str(files)) == 0:
                print('Uploading: ' + files)
                filePath = directory + str(files)
                status = 0
                try:
                    upload(filePath)
                    status = 1
                except IOError as e:
                    print("Error : " + str(e) + "Upload failed!")

                timeEnd = time.time()
                if status == 1:
                    print('Uploading ' + files + ' complete.')
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


print("Welcome to the uploader.\n")
start()

'''

Now that we have the directory, we need to iterate through this directory respecting the 4 upload per minute timeout. 

**** API Key for reference: c30b92a15eb6744cacad49e9cfbeb8e8772afcb6c3f2b4d9d84e30f2e0fe5128 ****

Once a file is uploaded, we need to store the file name and the scan ID from the response as well as the status. 
If the status or "Response Code" is 1 for: 'verbose_msg': 

'Scan request successfully queued, come back later for the report',

we will need to request the scan report periodically until it is available, retrieved and safely store in our output 
file with the associated ID and file nae for human readability.

This polling will need to be handled on a rolling timeout so as to not bog down their system or ours.

'''

'''

import requests
params = {'apikey': '-YOUR API KEY HERE-'}
files = {'file': ('myfile.exe', open('myfile.exe', 'rb'))}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()

*** SAMPLE SCAN REQUEST AND RESPONSE ***

{
  'permalink': 'https://www.virustotal.com/file/d140c...244ef892e5/analysis/1359112395/',
  'resource': u'd140c244ef892e59c7f68bd0c6f74bb711032563e2a12fa9dda5b760daecd556',
  'response_code': 1,
  'scan_id': 'd140c244ef892e59c7f68bd0c6f74bb711032563e2a12fa9dda5b760daecd556-1359112395',
  'verbose_msg': 'Scan request successfully queued, come back later for the report',
  'sha256': 'd140c244ef892e59c7f68bd0c6f74bb711032563e2a12fa9dda5b760daecd556'
}

'''

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


*** SAMPLE REPORT REQUEST AND RESPONSE ***

{
 'response_code': 1,
 'verbose_msg': 'Scan finished, scan information embedded in this object',
 'resource': '99017f6eebbac24f351415dd410d522d',
 'scan_id': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c-1273894724',
 'md5': '99017f6eebbac24f351415dd410d522d',
 'sha1': '4d1740485713a2ab3a4f5822a01f645fe8387f92',
 'sha256': '52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c',
 'scan_date': '2010-05-15 03:38:44',
 'positives': 40,
 'total': 40,
 'scans': {
    'nProtect': {'detected': true, 'version': '2010-05-14.01', 'result': 'Trojan.Generic.3611249', 'update': '20100514'},
    'CAT-QuickHeal': {'detected': true, 'version': '10.00', 'result': 'Trojan.VB.acgy', 'update': '20100514'},
    'McAfee': {'detected': true, 'version': '5.400.0.1158', 'result': 'Generic.dx!rkx', 'update': '20100515'},
    'TheHacker': {'detected': true, 'version': '6.5.2.0.280', 'result': 'Trojan/VB.gen', 'update': '20100514'},
    .
    .
    .
    'VirusBuster': {'detected': true, 'version': '5.0.27.0', 'result': 'Trojan.VB.JFDE', 'update': '20100514'},
    'NOD32': {'detected': true, 'version': '5115', 'result': 'a variant of Win32/Qhost.NTY', 'update': '20100514'},
    'F-Prot': {'detected': false, 'version': '4.5.1.85', 'result': null, 'update': '20100514'},
    'Symantec': {'detected': true, 'version': '20101.1.0.89', 'result': 'Trojan.KillAV', 'update': '20100515'},
    'Norman': {'detected': true, 'version': '6.04.12', 'result': 'W32/Smalltroj.YFHZ', 'update': '20100514'},
    'TrendMicro-HouseCall': {'detected': true, 'version': '9.120.0.1004', 'result': 'TROJ_VB.JVJ', 'update': '20100515'},
    'Avast': {'detected': true, 'version': '4.8.1351.0', 'result': 'Win32:Malware-gen', 'update': '20100514'},
    'eSafe': {'detected': true, 'version': '7.0.17.0', 'result': 'Win32.TRVB.Acgy', 'update': '20100513'}
  },
 'permalink': 'https://www.virustotal.com/file/52d3df0ed60c46f336c131bf2ca454f73bafdc4b04dfa2aea80746f5ba9e6d1c/analysis/1273894724/'
}

'''