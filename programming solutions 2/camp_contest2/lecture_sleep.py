def max_theorems(n, k, theorems, behavior):
    sum = 0
    for i in range(n):
        if behavior[i] == 1:
            sum += theorems[i]

    m = 0
    tmp = 0

    for i in range(k):
        if behavior[i] == 0:
            tmp += theorems[i]

    m = tmp

    for i in range(k, n):
        if behavior[i] == 0:
            tmp += theorems[i]

        if behavior[i - k] == 0:
            tmp -= theorems[i - k]

        m = max(m, tmp)

    return m + sum


n, k = map(int, input().split())
theorems = list(map(int, input().split()))
behavior = list(map(int, input().split()))

result = max_theorems(n, k, theorems, behavior)
print(result)