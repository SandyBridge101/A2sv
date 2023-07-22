from collections import Counter

t=int(input())

for _ in range(t):
    sequence=input()
    set_seq=sorted(set(sequence))
    #print(sequence)
    res=''
    for i in set_seq:
        #print(i,seq_count[i])
        if 2*sequence.count(2*i)!=sequence.count(i):
            res+=i
    print(res)
