"""

    Welcome to the Smith-Waterman Blosum Comparison and Scoring Tool.
    Substitute relevant file names and extensions for f0, f1, and f2, your
    database, query, and Blosum Matrix file respectively.

"""

import sys

orig_stdout = sys.stdout
f3 = open('output4.txt', 'w')
sys.stdout = f3

f0 = open("database2.txt")
databaseInput = f0.read()
f0.close()

databaseInput = databaseInput.replace("<<", "")
database = databaseInput.split("\n")

f1 = open("query2.txt")
queryInput = f1.read()
f1.close()

queryInput = queryInput.replace("<<", "")
query = queryInput.split("\n")

f2 = open("Blosum_62.txt")
file = f2.readlines()
f2.close()

'''

    We've opened the two primary files, the Blosum Scoring Matrix and the Query file.
    We need to compare each consecutive entry in our list to the first entry and determine a score
    given a match or mismatch using the Blosum Matrix. Now lets create an easy to traverse 2 Dimensional
    array to store the contents of the Blosum Matrix. I'll be reusing code from the NWScoreMatrix.

'''


def swscore(sequence1, sequence2):
    seq1 = sequence1
    seq2 = sequence2
    rows = len(seq1)
    cols = len(seq2)
    swScoreMatrix = [[0 for x in range(cols + 1)] for x in range(rows + 1)]

    for outer in range(0, rows + 1):
        for inner in range(0, cols + 1):
            swScoreMatrix[outer][inner] = "0,0 "

    swScoreMatrix[0][0] = " 0,0  "
    for leftmost in range(1, rows+1, 1):
        something = "U," + str(0) + " "
        swScoreMatrix[leftmost][0] = something

    for topmost in range(1, cols+1, 1):
        anotherSomething = "L," + str(0) + ""
        swScoreMatrix[0][topmost] = anotherSomething

    print()
    for loop1 in range(0, rows):
        for loop2 in range(0, cols):

            if seq1[loop1] == seq2[loop2]:
                for aLoop in range(0, index):
                    if scoreMatrix[0][aLoop] == seq1[loop1]:
                        break
                match = int(scoreMatrix[aLoop][aLoop])
                d = swScoreMatrix[loop1][loop2]
                diagonal = d.strip().split(",")
                diagonalScore = int(diagonal[1])
                tempScore = (diagonalScore+match)
                score = "D," + str(tempScore)
                swScoreMatrix[loop1+1][loop2+1] = score
            else:
                l = swScoreMatrix[loop1+1][loop2]
                u = swScoreMatrix[loop1][loop2+1]
                d = swScoreMatrix[loop1][loop2]

                left = l.strip().split(",")
                upper = u.strip().split(",")
                diagonal = d.strip().split(",")
                leftScore = int(left[1])
                upperScore = int(upper[1])
                diagonalScore = int(diagonal[1])

                for bLoop in range(0, index):
                    if scoreMatrix[0][bLoop] == seq1[loop1]:
                        break
                for cLoop in range(0, index):
                    if scoreMatrix[0][cLoop] == seq2[loop2]:
                        break
                mismatch = int(scoreMatrix[cLoop][bLoop])
                if diagonalScore >= leftScore and diagonalScore >= upperScore and diagonalScore > 0:
                    tempScore = (diagonalScore+mismatch)
                    score = "D," + str(tempScore)

                elif leftScore >= upperScore and leftScore > 0:
                    tempScore = (leftScore+mismatch)
                    score = "L," + str(tempScore)
                else:
                    tempScore = (upperScore+mismatch)
                    score = "U," + str(tempScore)
                swScoreMatrix[loop1+1][loop2+1] = score

    testString = ""
    for m in range(0, rows + 1):
        testString += "\n"
        for n in range(0, cols + 1):
            testString += str(swScoreMatrix[m][n]) + " "

    #print(testString)

    alignseq1 = ''
    alignseq2 = ''
    d = len(seq1)
    e = len(seq2)

    scoreCounter = ""
    gapCounter = 0

    finalScorePotential = swScoreMatrix[d][e]
    finalScoreNumber = finalScorePotential.strip().split(",")
    finalScore = int(finalScoreNumber[1])

    while d >= 0 and e >= 0:
        direction = swScoreMatrix[d][e]

        move = direction[0]
        scorecount = direction.strip().split(",")
        scoreCounter += " " + scorecount[1]
        if move == 'D':
            alignseq1 = seq1[d - 1] + alignseq1
            alignseq2 = seq2[e - 1] + alignseq2
            d -= 1
            e -= 1

        elif move == 'L':
            alignseq1 = '-' + alignseq1
            alignseq2 = seq2[e - 1] + alignseq2
            e -= 1
            gapCounter += 1

        elif move == 'U':
            alignseq2 = '-' + alignseq2
            alignseq1 = seq1[d - 1] + alignseq1
            d -= 1
            gapCounter += 1
        if d == 0 and e == 0:
            break
    print(alignseq1)
    print(alignseq2)
    print("The final calculated score for this alignment is: " + scoreCounter)
    print("Number of gaps: " + str(gapCounter))
    return finalScore


index = len(file)
print(index)

scoreMatrix = [[0 for x in range(index)] for y in range(index)]

for o in range(0, index):
    for p in range(0, index):
        lineData = file[o].split()
        lineLength = len(lineData)
        if lineLength < index:
            scoreMatrix[o][p] = lineData[p-1]
        else:
            scoreMatrix[o][p] = lineData[p]

'''

    You may be wondering why I included a check to see if the length of a line is shorter than the index.
    The reason is as follows, the Blosum file downloaded from the course site, as a text file of extension .txt
    included extra whitespace in the first line for formatting purposes, not a zero or other indicator. As it is
    only whitespace, Python's string split function ignores it. A solution is to include a zero or to check the length.

'''
scoreMatrix[0][0] = "0"
scoreString = ""

for q in range(0, index):
    scoreString += "\n"
    for r in range(0, index):
        cellValue = scoreMatrix[q][r]
        try:
            temp = int(cellValue)
            if 0 <= temp < 10:
                scoreString += "( " + str(cellValue) + " ) "
            else:
                scoreString += "(" + str(cellValue) + " ) "
        except ValueError:
            scoreString += "( " + str(cellValue) + " ) "
print(scoreString)

'''

    Now for the hard part... Reading the first protein sequence from the list, loading the second sequence,
    splitting the sequences by character and comparing to the table.

'''

arrayLength = int(len(database)/2)

proteinSequence = [0 for someLength in range(arrayLength)]
proteinSequenceScores = [0 for anotherLength in range(arrayLength-1)]

counter = 0
anotherCounter = 0
yetAnotherCounter = 0

proteinSequence1 = query[1]

scoreTableWithNamesAndSequences = [0 for arbitraryLength in range(len(database))]
someRandomCounter = 0

for i in range(1, len(database), 2):
    dbseq = database[i]
    output = swscore(proteinSequence1, dbseq)
    scoreTableWithNamesAndSequences[someRandomCounter] = str(output) + " * " + database[i-1] + " * " + dbseq
    someRandomCounter += 1

finalScoreRangeIndex = int(len(scoreTableWithNamesAndSequences)/2)

firstHighest = ""
secondHighest = ""
thirdHighest = ""

firstHighestNum = 0
secondHighestNum = 0
thirdHighestNum = 0

first = 0
second = 0
third = 0

for z in range(0, finalScoreRangeIndex):
    if z < finalScoreRangeIndex:
        tempA = scoreTableWithNamesAndSequences[z].split("*")
    if z < finalScoreRangeIndex-1:
        tempB = scoreTableWithNamesAndSequences[z+1].split("*")
    if z < finalScoreRangeIndex-2:
        tempC = scoreTableWithNamesAndSequences[z+2].split("*")
    first = int(tempA[0])
    second = int(tempB[0])
    third = int(tempC[0])
    tempFirst = firstHighest.split("*")
    tempSecond = secondHighest.split("*")
    tempThird = thirdHighest.split("*")
    if z > 0:
        firstHighestNum = int(tempFirst[0])
    else:
        firstHighest = scoreTableWithNamesAndSequences[z]
    if z > 1:
        secondHighestNum = int(tempSecond[0])
    else:
        secondHighest = scoreTableWithNamesAndSequences[z]
    if z > 2:
        thirdHighestNum = int(tempThird[0])
    else:
        thirdHighest = scoreTableWithNamesAndSequences[z]
    if first >= second and first >= third:
        if first > firstHighestNum:
            firstHighest = scoreTableWithNamesAndSequences[z]
        elif first == firstHighestNum or first > secondHighestNum:
            secondHighest = scoreTableWithNamesAndSequences[z]
        elif first == secondHighestNum or first > thirdHighestNum:
            thirdHighest = scoreTableWithNamesAndSequences[z]
print()
print(firstHighest)
print(secondHighest)
print(thirdHighest)

sys.stdout = orig_stdout
f3.close()

'''

1781 * >sp|P31800|QCR1_BOVIN Cytochrome b-c1 complex subunit 1, mitochondrial OS=Bos taurus GN=UQCRC1 PE=1 SV=2 * MAASAVCRAAGAGTRVLLRTRRSPALLRSSDLRGTATYAQALQSVPETQVSQLDNGLRVASEQSSQPTCTVGVWIDAGSRYESEKNNGAGYFVEHLAFKGTKNRPGNALEKEVESMGAHLNAYSTREHTAYYIKALSKDLPKAVELLADIVQNCSLEDSQIEKERDVILQELQENDTSMRDVVFNYLHATAFQGTPLAQSVEGPSENVRKLSRADLTEYLSRHYKAPRMVLAAAGGLEHRQLLDLAQKHFSGLSGTYDEDAVPTLSPCRFTGSQICHREDGLPLAHVAIAVEGPGWAHPDNVALQVANAIIGHYDCTYGGGAHLSSPLASIAATNKLCQSFQTFNICYADTGLLGAHFVCDHMSIDDMMFVLQGQWMRLCTSATESEVLRGKNLLRNALVSHLDGTTPVCEDIGRSLLTYGRRIPLAEWESRIAEVDARVVREVCSKYFYDQCPAVAGFGPIEQLPDYNRIRSGMFWLRF
1769 * >sp|Q68FY0|QCR1_RAT Cytochrome b-c1 complex subunit 1, mitochondrial OS=Rattus norvegicus GN=Uqcrc1 PE=1 SV=1 * MAASAVCRAACSGTQALLRTCRSPALLRLPALRGTATFVQALQSVPETQVSVLDNGLRVASEQSSHPTCTVGVWIDVGSRYETEKNNGAGYFLEHLAFKGTKNRPGNALEKEVESIGAHLNAYSTREHTAYLIKALSKDLPKVVELLADIVQNISLEDSQIEKERDVILREMQENDASMQNVVFDYLHATAFQGTPLAQAVEGPSENVRRLSRTDLTDYLSRHYKAPRMVLAAAGGVKHQQLLDLAQDHFSSVSQVYEEDAVPSITPCRFTGSEIRHRDDALPLAHVAIAVEGPGWANPDNVALQVANAIIGHYDCTYGGGVHLSSPLASVAVANKLCQSFQTFNISYSETGLLGAHFVCDAMSIDDMIFFLQGQWMRLCTSATESEVTRGKNILRNALISHLDGTTPVCEDIGRSLLTYGRRIPLAEWESRIEEVDAQMVREVCSKYFYDQCPAVAGYGPIEQLSDYNRIRSGMFWLRF
1764 * >sp|Q9CZ13|QCR1_MOUSE Cytochrome b-c1 complex subunit 1, mitochondrial OS=Mus musculus GN=Uqcrc1 PE=1 SV=2 * MAASAVCRAACSGTQVLLRTRRSPALLRLPALRGTATFAQALQSVPETQVSILDNGLRVASEQSSHATCTVGVWIDAGSRYETEKNNGAGYFLEHLAFKGTKNRPGNALEKEVESIGAHLNAYSTREHTAYLIKALSKDLPKVVELLADIVQNSSLEDSQIEKERDVILREMQENDASMQNVVFDYLHATAFQGTPLAQAVEGPSENVRRLSRTDLTDYLNRHYKAPRMVLAAAGGVEHQQLLDLAQKHLSSVSRVYEEDAVPGLTPCRFTGSEIRHRDDALPLAHVAIAVEGPGWANPDNVTLQVANAIIGHYDCTYGGGVHLSSPLASVAVANKLCQSFQTFNISYSDTGLLGAHFVCDAMSIDDMVFFLQGQWMRLCTSATESEVTRGKNILRNALVSHLDGTTPVCEDIGRSLLTYGRRIPLAEWESRIQEVDAQMLRDICSKYFYDQCPAVAGYGPIEQLPDYNRIRSGMFWLRF

'''