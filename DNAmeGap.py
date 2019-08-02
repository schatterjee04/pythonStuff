try:
    f = open("dna.fasta")
    print("File opened and read!")
except IOError:
    print("There was an error with the requisite file!")
finally:
    print("Let's begin, shall we?")

data = f.read()
f.close()
print("File loaded into memory and closed.")
print()
print(data)
print()

data = data.replace("<<", "")
lines = data.split()

seq1 = lines[1]
seq2 = lines[3]
print("Sequences loaded!")
print(seq1)
print(seq2)

rows = len(seq1)
cols = len(seq2)
print("Sequence lengths:")
print(rows)
print(cols)

gap = -20
match = 5
mismatch = -4

scoreMatrix = [[0 for x in range(cols + 1)] for x in range(rows + 1)]
for o in range(0, rows + 1):
    for p in range(0, cols + 1):
        scoreMatrix[o][p] = "0,0 "

'''

    scoreArray and sumArray have 4 cells, u, l, d. u or 0 denotes upper sum, l or 1 denotes
    left sum, d or 2 denotes diagonal sum. Summations are performed using best available value.

'''
scoreMatrix[0][0] = "0,0 "
outputString = " "
gapcount = 0
for i in range(1, rows+1, 1):
    gapcount += gap
    something = "U," + str(gapcount) + " "
    scoreMatrix[i][0] = something
print()
gapcount = 0
for j in range(1, cols+1, 1):
    gapcount += gap
    anotherSomething = "L," + str(gapcount) + " "
    scoreMatrix[0][j] = anotherSomething

colGapCount = 0
tally = 0
gapcost = 0
print()

'''

    A note on scoring, since it was not clearly denoted in the slides/notes, I referred to the wikipedia article here:

    https://en.wikipedia.org/wiki/Needleman–Wunsch_algorithm

    Accordingly, for each cell in the matrix, there is a U, L and D score denoting the sum of the cell score given
    an upper to lower, a left to right, or a diagonal summation.

'''
count = 0
tempScore = 0
for i in range(0, rows):
    # print(seq1[i])
    colGapCount = 0
    for j in range(0, cols):
        if seq1[i] == seq2[j]:
            outputString += "(" + str(i) + "," + str(j) + ") " + seq1[i] + seq2[j] + " Match \n"

            l = scoreMatrix[i+1][j]
            u = scoreMatrix[i][j+1]
            d = scoreMatrix[i][j]

            left = l.strip().split(",")
            upper = u.strip().split(",")
            diagonal = d.strip().split(",")
            leftScore = int(left[1])
            upperScore = int(upper[1])
            diagonalScore = int(diagonal[1])

            if i != j:
                if i > j:
                    gapcost = (i-j)*gap
                else:
                    gapcost = (j-i)*gap
            else:
                gapcost = 0

            if j and i >= 0:
                if diagonalScore >= leftScore:
                    if diagonalScore >= upperScore:
                        tempScore = (diagonalScore+match+gapcost)
                        score = "D," + str(tempScore)
                    else:
                        tempScore = (upperScore+match+gapcost)
                        score = "U," + str(tempScore)
                elif leftScore >= upperScore:
                    tempScore = (leftScore+match+gapcost)
                    score = "L," + str(tempScore)
                else:
                    tempScore = (upperScore+match)
                    score = "U," + str(tempScore)
            elif j > 0 and i == 0:
                tempScore = (leftScore+match+gapcost)
                score = "L," + str(tempScore)
            else:
                tempScore = (upperScore+match+gapcost)
                score = "U," + str(tempScore)
            scoreMatrix[i+1][j+1] = score

        else:
            outputString += "(" + str(i) + "," + str(j) + ") " + seq1[i] + seq2[j] + " Mismatch\n"
            l = scoreMatrix[i+1][j]
            u = scoreMatrix[i][j+1]
            d = scoreMatrix[i][j]

            left = l.strip().split(",")
            upper = u.strip().split(",")
            diagonal = d.strip().split(",")
            leftScore = int(left[1])
            upperScore = int(upper[1])
            diagonalScore = int(diagonal[1])

            if i and j > 0:
                if diagonalScore >= leftScore:
                    if diagonalScore >= upperScore:
                        if j == 0 and i == 0:
                            tempScore = (diagonalScore+mismatch+gapcost)
                        else:
                            tempScore = (diagonalScore+mismatch+gapcost)
                        score = "D," + str(tempScore)
                    else:
                        tempScore = (upperScore+mismatch+gapcost)
                        score = "U," + str(tempScore)
                elif leftScore >= upperScore:
                    tempScore = (leftScore+mismatch+gapcost)
                    score = "L," + str(tempScore)
                else:
                    tempScore = (upperScore+mismatch+gapcost)
                    score = "U," + str(tempScore)
            elif j > 0 and i == 0:
                tempScore = (leftScore+mismatch+gapcost)
                score = "L," + str(tempScore)
            else:
                tempScore = (upperScore+mismatch+gapcost)
                score = "U," + str(tempScore)
            scoreMatrix[i+1][j+1] = score

            score = mismatch+count
print(outputString)

testString = ""
for m in range(0, rows + 1):
    testString += "\n"
    for n in range(0, cols + 1):
        testString += str(scoreMatrix[m][n]) + " "
print(testString)
