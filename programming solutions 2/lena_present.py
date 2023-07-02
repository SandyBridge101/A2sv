k=int(input())

def print_row(k,s):
    mat=[' ' for i in range(0,s)]+[str(i) for i in range(0,k)]+[str(i) for i in range(k,-1,-1)]
    return mat

col=print_row(k,0)

for i in col:
    print(*print_row(int(i),k-int(i)))