import random
f = open("database.fasta")
query=f.readlines()
f.close()
for i in range(0,len(query),1):
    query[i]=query[i].rstrip('\n')

f=open("Blosum_62.txt")
file=f.readlines()
f.close()
for i in range(0,len(file),1):
    file[i]=file[i].rstrip('\n')


aalist=file[0].split()
blosum62={}

for i in range (1,len(file),1):
    l=file[i].split()
    for j in range(1,len(file),1):
        key=l[0] +aalist[j-1]
        blosum62[key]=int(l[j])
print(blosum62)


query=f.readlines()
f.close()
for i in range(0,len(query),1):
    query[0]=query[0].rstrip('\n')
    query[1]=query[1].rstrip('\n')
    
#Read Matrix- use a dictionary
    
def SW_score(seq1,seq2,g):
    rows=len(seq1)+1
    cols=len(seq2)+1
    V=[]
    for i in range(0, rows,1):
        l=[]
        for i in range(0,cols,1):
            l.append(0)
        V.append(l)
            
 #Initiatilization
            
    for i in range(V):
         V[i][0]=0
    for j in range(V):
        V[0][j]=0
    maxscore=V[1][1]
                    
         #recurrence        
    for i in range(1, rows):
        for j in range(1, cols):
            key = seq1[i-1] == seq2[j-1]
            d=V[i-1][j-1]+blosum62[key]
            l=V[i][j-1]+gap
            u=V[i-1][j]+gap
            if d>=l and d>=u and d >=0:
                V[i][j]=d
                T[i][j]='D'
            elif 1>=d and l>=u and l>=0:
                V[i][j]=1
                T[i][j]='L'
            elif u>=d and u>=l and u>=0:
                    V[i][j]=u
                    T[i][j]='U'
            else:
                V[i][j]=0
                T[i][j]=0
                if V[i][j]>= maxscore:
                    maxscore>= V[i][j]
                    max_i=i
                    max_j=j                    
                
    return maxscore
                
##Keeps saying that seq1 and seq2 are out of range     
seq1=query[1]
seq2=query[3]
match=5
gap=-20
mismatch=-4



##Database search
for i in range(1,len(query),2):
    SW=SWscore(query[1],query[i],gap)
    print(SW)
