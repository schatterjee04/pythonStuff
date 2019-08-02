import sys

# My experience with python is limited, if any errors or omissions are found, please correct accordingly.

# I don't know exactly why I'm importing sys as my IDE is ignoring it... I may look into this later.

# Ah, according to my IDE, pyCharm, we never use anything from sys so importing it is pointless.

# So a single line comment in python is denoted by a "#"

# I wonder what standard notation for multi-line comments are...

'''

    AH-HA!Found it. Apparently it is, quite simply, three apostrophes!
    Just keep going with your comments and none of it will print!
    Interesting tidbit, there is a cool website for notes on this:

        http://www.afterhoursprogramming.com/tutorial/Python/Comments/

    This just helps to keep things neater I guess...
    Any who, let's continue.

'''

# OK. The following is vestigial code that's been commented out by the last person to work on this.

# Base Case
##V[0][0]=0
##for i=0 to length(seq):
##    V[i][0]+gap*i
##for j=0 to length(seq2):
##    V[0][j]=gap*j
##
##Main loop
##for i=0 to length(seq1):
##    for j=0 to length(seq2)
##    V[i][j]=max V[i-0][j-1],V[i-0][j],V[i][j-1]



# Here begins the actual program:

try:
    f = open("dna.fasta")
except IOError:
    print("There was an error with the requisite file!")
finally:
    print("Let's begin, shall we?")

'''

    OK. So here it seems that we are creating some arbitrary object variable called "f".
    "f" is now set to whatever is being read from "dna.fasta" which seems to be an odd
    file extension. The contents appear to be plain text.

    IN the event that the file is not found or ends unexpectedly, the program will tell us.
    Regardless, the application will try to continue.

'''

# data=f.readlines()

'''

    I guess you tried to create a new object variable called data to store the lines of f?
    Not so simple? I guess you realized that and commented it out.

'''

data = f.read()
f.close()

'''

    Again, an object variable named data. Read contents of "f"
        Close "f"
    Work with a new string array, ala data. Clearly I'm a little
    fuzzy on variable data types in python.

'''


print()
print(data)
print()

data = data.replace("<<", "")
lines = data.split()

'''

    Removed excess fluff from the input file...

'''

# for i in range(0,len(data),1):
#    data[i]=data[i].rstrip('\n')

'''

    More stuff...

'''
seq1 = lines[1]
seq2 = lines[3]

print(seq1)
print(seq2)

rows = len(seq1) + 1
cols = len(seq2) + 1

'''

    Here we will define the scores for gaps, matches and mismatches:
    Gap = -20
    Match = 5
    Mismatch = -4

'''
gap = -20
match = 5
mismatch = -4

'''

    T is the traceback matrix ? In this instance it is empty.

'''
print()
print("Below is the matrix of T and V")
print()
T = []
for i in range(0, rows, 1):
    l = []
    for i in range(0, cols, 1):
        l.append(000)
    T.append(l)

V = []
for i in range(0, rows, 1):
    l = []
    for i in range(0, cols, 1):
        l.append(0)
    V.append(l)

T[0][0] = ' '
V[0][0] = 0
for i in range(1, cols, 1):
    T[0][i] = "L"
    V[0][i] = gap * i
for i in range(1, rows, 1):
    T[i][0] = "U"
    V[i][0] = gap * i
for i in range(0, rows, 1):
    print(T[i])
    print(V[i])

print()

output = " "

# sys.exit()
for i in range(1, rows):
    print(output)
    output = ""
    for j in range(1, cols):
        if seq1[i - 1] == seq2[j - 1]:
            d = V[i - 1][j - 1] + match
            print(d)
        else:
            d = V[i - 1][j - 1] + mismatch
            print(d)

        l = V[i][j - 1] + gap
        u = V[i - 1][j] + gap
        if d >= 1 and d >= u:
            V[i][j] = d
            T[i][j] = 'D'
            output += " D "
        elif 1 >= d and l >= u:
            V[i][j] = 1
            T[i][j] = 'L'
            output += " L "
        else:
            V[i][j] = u
            T[i][j] = 'U'
            output += " U "
print()
alignseq1 = ''
alignseq2 = ''
i = len(seq1)
j = len(seq2)
rowScore1 = 0
rowScore2 = 0

while (i != 0 and j != 0):
    if T[i][j] == 'D':
        alignseq1 = seq1[i - 1] + alignseq1
        alignseq2 = seq2[j - 1] + alignseq2
        i = i - 1
        j = j - 1
        rowScore1 += match

    elif T[i][j] == 'L':
        alignseq1 = '-' + alignseq1
        alignseq2 = seq2[j - 1] + alignseq2
        j = j - 1
        rowScore1 += gap
        rowScore2 += mismatch
        print()
    elif T[i][j] == 'U':
        alignseq2 = '-' + alignseq2
        alignseq1 = seq1[i - 1] + alignseq1
        i = i - 1
        rowScore1 += gap
        rowScore2 += mismatch
        print()

    print(alignseq1)
    print(alignseq2)
    print()
numTab = ""
for i in range(1,rows):
    numTab += "\n"
    for j in range(1,cols):
        numTab += " " + str(V[i][j])
print(numTab)

print(T)
print(V)

