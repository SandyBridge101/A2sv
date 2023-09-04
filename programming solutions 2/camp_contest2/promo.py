def max_free_value(n, q, prices, queries):
    sorted_prices = sorted(prices, reverse=True)
    c_prices = [0] * (n + 1)

    for i in range(1, n + 1):
        c_prices[i] = c_prices[i - 1] + sorted_prices[i - 1]
    print(c_prices)

    results = []
    for query in queries:
        buy, ni_free = query
        pay_for = buy - ni_free
        max_free = c_prices[buy] - c_prices[pay_for]
        results.append(max_free)

    return results

# Read input
n, q = map(int, input().split())
prices = list(map(int, input().split()))
queries = []

for _ in range(q):
    ni_buy, ni_free = map(int, input().split())
    queries.append((ni_buy, ni_free))

results = max_free_value(n, q, prices, queries)

# Output results
for result in results:
    print(result)