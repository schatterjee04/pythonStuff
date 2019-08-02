import random
import sys
import os
import subprocess

f = open("training.txt")
train = f.readlines()
f.close()
for i in range(0, len(train), 1):
    train[i] = train.rstrip("\n")

avg = 0
gap =-30 #optimal gap penalty
gapcount=0
for i in range(0,len(train),1):
    gapcount+=gap
accuracy= gapcount/len(train)
print(accuracy)
for i in range(0, len(train), 1):

#compute NW alignment of train[i]
    os.system("python NWblosum.py " + train[i] + " nw.fasta -20")

    ref = train[i].replace(".unaligned", "")

    os.system('./qscore -test nw.fasta -ref ' + ref ' > qscore_out')
    f.open('qscore_out')
    l = f.readlines().split(';')[2].replace('Q=', '')
    avg+=float(l)
#    print(l)
    
avg = avg/len(train)
print(avg)
#get qscore
#    proc = subprocess.Popen('./qscore -test nw.fasta -ref ' + ref, stdout=subprecess.Pipe)
#    output = proc.stdout.read()
#    print(output)
    
gapscore=-100
##depends on how large the sequence, bigger the length, smalled gapy penalty is needed. although this score should be pretty good for these sequences
