from collections import Counter

n=int(input())
arr=list(map(int,input().split()))

most=Counter(arr).most_common(1)[0][1]

print(most,len(set(arr)))