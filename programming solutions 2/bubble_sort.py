def countSwaps(a):
    swaps=0
    for i in range(0,len(a)):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swaps+=1
    last=a[len(a)-1]
    print(f'Array is sorted in {swaps} swaps.\n'+f'First Element: {a[0]}\n'+f'Last Element: {last}\n')

#n = int(input().strip())

#a = list(map(int, input().rstrip().split()))

a=[6,2,4,3,7,9]

print(countSwaps(a))