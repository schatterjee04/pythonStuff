import os

'''

    Potential Gap scores:
    {0, -1, -2, -5, -10, -15, -20, -25, -30}

'''

f = open("training.txt")
train = f.readlines()
f.close()

gap = 0
avg = 0
gapcount = 0

'''

    at some point i need to keep track of scores relative to gap penalty

'''

accuracy = gapcount/len(train)
print(accuracy)
for i in range(0, len(train), 1):

    #os.system("python NWblosum.py " + train[i] + " nw.fasta -20")
    ref = train[i].replace(".unaligned", "")
    os.system('./qscore -test nw.fasta -ref ' + ref + ' > qscore_out')
    #f.open('qscore_out')
    #l = f.readlines().split(';')[2].replace('Q=', '')
    #avg += float(l)
    #print(l)

avg /= len(train)
print(avg)
#get qscore
#    proc = subprocess.Popen('./qscore -test nw.fasta -ref ' + ref, stdout=subprocess.Pipe)
#    output = proc.stdout.read()
#    print(output)

gapscore = -100
##depends on how large the sequence, bigger the length, smalled gapy penalty is needed. although this score should be pretty good for these sequences
