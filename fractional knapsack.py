def fractional_knapsack(values, weights, capacity):
    # Create a list of items with value-to-weight ratios
    items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    max_value = 0
    for value, weight, ratio in items:
        if capacity >= weight:
            # Take the whole item
            max_value += value
            capacity -= weight
        else:
            # Take a fraction of the item
            max_value += value * (capacity / weight)
            break

    return max_value

# User inputs
print("Fractional Knapsack Problem Solver (Greedy Method)")
num_items = int(input("Enter the number of items: "))

values = list(map(int, input("Enter values of the items (comma-separated): ").split(',')))
weights = list(map(int, input("Enter weights of the items (comma-separated): ").split(',')))
capacity = int(input("Enter the capacity of the knapsack: "))

# Validate input
if len(values) != num_items or len(weights) != num_items:
    print("Error: The number of values and weights must match the number of items.")
else:
    max_value = fractional_knapsack(values, weights, capacity)
    print(f"The maximum value of items that can be carried: {max_value:.2f}")
