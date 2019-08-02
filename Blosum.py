f = open("database.fasta")
queryInput = f.read()
f.close()

queryInput = queryInput.replace("<<", "")
query = queryInput.split()

f = open("Blosum_62.txt")
file = f.readlines()
f.close()

for a in range(0, len(file), 1):
    file[a] = file[a].rstrip('\n')

aalist = file[0].split()
length = len(aalist)
print(length)
blosum62 = {}
print(aalist)

for i in range(1, len(file), 1):
    k = file[i].split()
    for j in range(1, len(file), 1):
        key = k[0] + aalist[j-1]
        blosum62[key] = int(k[j])
print(blosum62)
blosumLength = len(blosum62)
print(blosumLength)
# Read Matrix - use a dictionary
'''

def sw_score(seq1, seq2):
    rows = len(seq1)+1
    cols = len(seq2)+1
    v = []
    t = []

    for m in range(0, rows, 1):
        l = []
        for n in range(0, cols, 1):
            l.append(0)
        v.append(l)
        t.append(l)


# Initialization

    for x in range(rows):
        v[x][0] = 0
    for y in range(cols):
        v[0][y] = 0
    maxScore = v[1][1]

# recurrence
    for p in range(1, rows):
        for q in range(1, cols):
            key2 = seq1[p-1] == seq2[q-1]

            d = v[p-1][q-1] + blosum62[key2]
            l = v[p][q-1]
            u = v[p-1][q]
            if d >= l and d >= u and d >= 0:
                v[p][q] = d
                t[p][q] = 'D'
            elif 1 >= d and l >= u and l >= 0:
                v[p][q] = 1
                t[p][q] = 'L'
            elif u >= d and u >= l and u >= 0:
                    v[p][q] = u
                    t[p][q] = 'U'
            else:
                v[p][q] = 0
                t[p][q] = 0
                if v[p][q] >= maxScore:
                    maxScore >= v[p][q]
                    maxP = p
                    maxQ = q

    return maxScore

##Database search
for i in range(1, len(query), 2):
    sw = sw_score(query[1], query[i])
    print(sw)
'''