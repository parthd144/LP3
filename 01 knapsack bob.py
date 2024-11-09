def knapsack_dynamic_programming(weights, values, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value that can be attained
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # The maximum value that can be achieved is stored in dp[n][capacity]
    return dp[n][capacity]

# User inputs
num_items = int(input("Enter the number of items: "))

weights = list(map(int, input("Enter the weights of the items (comma-separated): ").split(',')))
values = list(map(int, input("Enter the values of the items (comma-separated): ").split(',')))
capacity = int(input("Enter the capacity of the knapsack: "))

# Validate input
if len(weights) != num_items or len(values) != num_items:
    print("Error: The number of weights and values must match the number of items.")
else:
    result = knapsack_dynamic_programming(weights, values, capacity)
    print(f"The maximum value that can be attained is: {result}")
