def NWScore(sequence1, sequence2, m, mm, g):
    gap = g
    match = m
    mismatch = mm
    seq1 = sequence1
    seq2 = sequence2

    print()

    print("Sequences loaded!")
    print(seq1)
    print(seq2)
    print()
    rows = len(seq1)
    cols = len(seq2)
    print("Sequence lengths:")
    print(rows)
    print(cols)

    scoreMatrix = [[0 for x in range(cols + 1)] for x in range(rows + 1)]
    for o in range(0, rows + 1):
        for p in range(0, cols + 1):
            scoreMatrix[o][p] = "0,0 "

    '''

        scoreArray and sumArray have 4 cells, u, l, d. u or 0 denotes upper sum, l or 1 denotes
        left sum, d or 2 denotes diagonal sum. Summations are performed using best available value.

    '''
    scoreMatrix[0][0] = " 0,0  "
    outputString = ""

    gapcount = 0
    for i in range(1, rows+1, 1):
        gapcount += gap
        something = "U," + str(gapcount) + " "
        scoreMatrix[i][0] = something

    gapcount = 0
    for j in range(1, cols+1, 1):
        gapcount += gap
        anotherSomething = "L," + str(gapcount) + ""
        scoreMatrix[0][j] = anotherSomething

    print()

    '''

        A note on scoring, since it was not clearly denoted in the slides/notes, I referred to the wikipedia article here:

        https://en.wikipedia.org/wiki/Needleman–Wunsch_algorithm

        Accordingly, for each cell in the matrix, there is a U, L and D score denoting the sum of the cell score given
        an upper to lower, a left to right, or a diagonal summation.

    '''
    for i in range(0, rows):
        for j in range(0, cols):
            if seq1[i] == seq2[j]:
                outputString += "(" + str(i) + "," + str(j) + ") " + seq1[i] + seq2[j] + " Match \n"

                d = scoreMatrix[i][j]
                diagonal = d.strip().split(",")
                diagonalScore = int(diagonal[1])
                tempScore = (diagonalScore+match)
                score = "D," + str(tempScore)
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

                if diagonalScore >= leftScore and diagonalScore >= upperScore:
                    if j == 0 and i == 0:
                        tempScore = (diagonalScore+mismatch)
                    else:
                        tempScore = (diagonalScore+mismatch)
                    score = "D," + str(tempScore)

                elif leftScore >= upperScore:
                    tempScore = (leftScore+gap)
                    score = "L," + str(tempScore)
                else:
                    tempScore = (upperScore+gap)
                    score = "U," + str(tempScore)

                scoreMatrix[i+1][j+1] = score
    print(outputString)

    testString = ""
    for m in range(0, rows + 1):
        testString += "\n"
        for n in range(0, cols + 1):
            testString += str(scoreMatrix[m][n]) + " "

    print(testString)
    print()

    alignseq1 = ''
    alignseq2 = ''
    i = len(seq1)
    j = len(seq2)

    while i >= 0 and j >= 0:
        direction = scoreMatrix[i][j]
        tempDirection = direction.strip().split(",")
        move = direction[0]
        if move == 'D':
            alignseq1 = seq1[i - 1] + alignseq1
            alignseq2 = seq2[j - 1] + alignseq2
            i -= 1
            j -= 1

        elif move == 'L':
            alignseq1 = '-' + alignseq1
            alignseq2 = seq2[j - 1] + alignseq2
            j -= 1

        elif move == 'U':
            alignseq2 = '-' + alignseq2
            alignseq1 = seq1[i - 1] + alignseq1
            i -= 1
        if i == 0 and j == 0:
            break

    print(alignseq1)
    print(alignseq2)

    NWSCTemp = scoreMatrix[rows][cols]
    NWScoreA = NWSCTemp.strip().split(",")
    NWScoreOutput = int(NWScoreA[1])
    return NWScoreOutput


def main():
    print("Welcome!")
    seq1 = input("Please enter sequence 1: ")
    seq2 = input("Please enter sequence 2: ")
    try:
        m = int(input("Please enter the match score: "))
        mm = int(input("Please enter the mismatch score: "))
        gap = int(input("Please enter the gap penalty: "))
    except (TypeError, ValueError):
        print("Please enter numbers!")
        main()
    finally:
        print("Onwards and upwards!")
        print()
        score = NWScore(seq1,seq2,m,mm,gap)
        print()
        print("The final computed NW Score is: ")
        print(score)

try:
    main()
except UnboundLocalError:
    print("You did something wrong but everything seems to have \n"
          "completed. Just in case something did go horribly wrong, \n"
          "we can run the program again. Would you like us to run the program again?\n")
    choice = input("Please enter Y or N:\n ")
    if choice == 'Y' or choice == 'y' or choice == "yes" or choice == "Yes" or choice == "YES":
        main()
    elif choice == 'N' or choice == 'n' or choice == "no" or choice == "No" or choice == "NO":
        print("Thank you for your patience, good bye!")
    else:
        print("You are a terrible person for fucking with me for no reason. \n"
              "You had two choices! Y or N! FOR FUCKS SAKE! FUCK YOU AND GOOD DAY!\n")