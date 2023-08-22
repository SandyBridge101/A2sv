t=int(input())

for _ in range(t):
    n=int(input())
    contestants=[]
    winner=0
    maxq=0
    for _ in range(n):
        contestants.append(tuple(list(map(int,input().split()))))
    #print(contestants)
    
    for c in range(len(contestants)):
        if contestants[c][0]<=10:
            if contestants[c][1]>maxq:
                maxq=contestants[c][1]
                winner=c+1

    print(winner)