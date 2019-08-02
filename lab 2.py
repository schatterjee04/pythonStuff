import sys
#Base Case
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
f=open("dna.fasta")
#data=f.readlines()
data=f.read()
f.close()

data=data.replace("<<","")
lines=data.split()


#for i in range(0,len(data),1):
#    data[i]=data[i].rstrip('\n')
    
seq1=lines[1]
seq2=lines[3]

print(seq1)
print(seq2)

rows=len(seq1)+1
cols=len(seq2)+1
 
gap=-20
match=5
mismatch=-4
 
T=[]
for i in range(0,rows,1):
    l=[]
    for i in range(0,cols,1):
        l.append(0)
    T.append(l)
    
V=[]
for i in range(0,rows,1):
    l=[]
    for i in range(0,cols,1):
        l.append(0)
    V.append(l)

T[0][0]=''
V[0][0]=0
for i in range(1,cols,1):
    T[0][i]="L"
    V[0][i]=gap*i
for i in range(1,rows,1):
    T[i][0]="U"
    V[i][0]=gap*i
for i in range(0,rows,1):
    print(T[i])

#sys.exit()
for i in range(1,rows):
    for j in range(1,cols):
        if seq1[i-1]==seq2[j-1]:
            d=V[i-1][j-1]+match
        else:
            d=V[i-1][j-1]+mismatch
        l=V[i][j-1]+gap
        u=V[i-1][j]+gap
        if d>=1 and d>=u:
            V[i][j]=d
            T[i][j]='D'
        elif 1>=d and l>=u:
            V[i][j]=1
            T[i][j]='L'
        else:
            V[i][j]=u
            T[i][j]='U'

alignseq1=''
alignseq2=''
i=len(seq1)
j=len(seq2)
while(i!=0 and j!=0):
    if T[i][j]=='L':
        alignseq1='-' +alignseq1
        alignseq2=seq2[j-1]+alignseq2
        j=j-1
    elif T[i][j]=='U':
        alignseq2='-'+alignseq2
        alignseq1=seq[i-1]+alignseq1
        i-i-1
    else:
        alignseq1= seq1[i-1]+alignseq1
        alignseq2=seq2[j-1]+alignseq2
        i=i-1
        j=j-1
    print(alignseq1)
    print(alignseq2)
    print()
 
