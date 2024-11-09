def binomial_coefficient(n, k):
    # Create a 2D array to store the binomial coefficients
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate binomial coefficients using dynamic programming
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base case: C(i, 0) = 1 and C(i, i) = 1
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                # Use the recursive relation: C(i, j) = C(i-1, j-1) + C(i-1, j)
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

# User input
print("Binomial Coefficient Calculator using Dynamic Programming")
n, k = map(int, input("Enter n and k (separated by space): ").split())

if k > n:
    print("Error: k cannot be greater than n.")
else:
    result = binomial_coefficient(n, k)
    print(f"The binomial coefficient C({n}, {k}) is: {result}")