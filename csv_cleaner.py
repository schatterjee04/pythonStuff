with open('/Users/Sourav/Downloads/cpu_mem_log_v3.csv') as csv:
    tempString = ""
    count = 0

    for line in csv:
        if count < 3:
            count = count + 1
            tempString = tempString + line
        else:
            count = 0
            clean = tempString.replace('\n', '')
            print(tempString)
            tempString = ""

