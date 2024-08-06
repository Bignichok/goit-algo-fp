import random
import matplotlib.pyplot as plt

# Number of simulations
num_simulations = 1_000_000

# Possible sums and their counts
sum_counts = {sum_: 0 for sum_ in range(2, 13)}

# Simulate the dice rolls
for _ in range(num_simulations):
    roll_sum = random.randint(1, 6) + random.randint(1, 6)
    sum_counts[roll_sum] += 1

# Calculate probabilities
simulated_probabilities = {sum_: count / num_simulations for sum_, count in sum_counts.items()}

# Analytical probabilities (from the provided table)
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36, 
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Print results for comparison
print("Sum\tSimulated Probability\tAnalytical Probability")
for sum_ in range(2, 13):
    print(f"{sum_}\t{simulated_probabilities[sum_]:.4%}\t\t{analytical_probabilities[sum_]:.4%}")

# Plot the probabilities
sums = list(range(2, 13))
simulated_probs = [simulated_probabilities[sum_] for sum_ in sums]
analytical_probs = [analytical_probabilities[sum_] for sum_ in sums]

plt.figure(figsize=(10, 6))
plt.plot(sums, simulated_probs, label='Simulated Probabilities', marker='o')
plt.plot(sums, analytical_probs, label='Analytical Probabilities', marker='x')
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability')
plt.title('Comparison of Simulated and Analytical Probabilities')
plt.legend()
plt.grid(True)
plt.show()
