import random
import matplotlib.pyplot as plt

def flip_coin(num_trials=10000, flips_per_trial=10):
    counts = {i: 0 for i in range(flips_per_trial + 1)}
    for _ in range(num_trials):
        heads = sum(random.choice([0, 1]) for _ in range(flips_per_trial))
        counts[heads] += 1
    return {k: round(v / num_trials * 100, 2) for k, v in counts.items()}

def draw_gaussian_distribution_graph(distribution):
    x = list(distribution.keys())
    y = list(distribution.values())
    plt.bar(x, y, color='skyblue')
    plt.xlabel('Number of Heads in 10 Flips')
    plt.ylabel('Percentage (%)')
    plt.title('Distribution of Heads Count in 10 Coin Flips')
    plt.xticks(x)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

distribution = flip_coin()
print(distribution)
draw_gaussian_distribution_graph(distribution)
