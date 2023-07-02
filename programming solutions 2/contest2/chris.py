def can_sort_cubes(n, volumes):
    max_exchanges = ((n * (n - 1)) // 2) - 1

    # Check if the array is already non-decreasing
    if all(volumes[i] <= volumes[i + 1] for i in range(n - 1)):
        return "YES"

    # Check if the maximum number of exchanges is sufficient
    for i in range(n - 1):
        if volumes[i] > volumes[i + 1]:
            break
    else:
        return "NO"

    return "YES" if max_exchanges >= n - 1 else "NO"


# Read the number of test cases
t = int(input())

# Read all the test cases
test_cases = []
for _ in range(t):
    # Read the number of cubes
    n = int(input())

    # Read the volumes of the cubes
    volumes = list(map(int, input().split()))

    test_cases.append((n, volumes))

# Process each test case and print the result
for n, volumes in test_cases:
    result = can_sort_cubes(n, volumes)
    print(result)

