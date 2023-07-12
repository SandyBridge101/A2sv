def arrayTransformation(list1, list2 ):
    tmp1, tmp2=[],[]
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            tmp1.append(list1[i])
            tmp2.append(list2[i])
            for i in range(len(tmp1)):
                tmp1[i] = tmp1[i] + 1
                if tmp1.sort()==tmp2.sort():
                    return 1
                else:
                    return 0

t=int(input())

for _ in range(t):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    print(arrayTransformation(arr1,arr2))