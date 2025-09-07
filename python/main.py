import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, date, timedelta

def main():
    choice = input(
        "Choose an option.\n"
        "1: occurrences of a string over time\n"
        "2: data of journal sizes\n"
        "--> "
    )

    if choice == "1":
        pass
    elif choice == "2":
        basic_stats()

def basic_stats():
    days = (date.today() - date(2024, 1, 1)).days + 1
    byte_sizes = np.zeros(days)

    for i in range(days):

        dt = datetime(2024, 1, 1) + timedelta(days=i)
        formatted_date = dt.strftime("%Y.%m.%d")
        path = f"/Users/olympus/Documents/journalEntries/{formatted_date}.txt"

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            byte_sizes[i] = len(text.encode("utf-8"))

        else:
            print("uh oh... missing a journal entry somewhere")

    # ChatGPT boilerplate

    valid_sizes = byte_sizes[byte_sizes > 0]
    mean_size = np.mean(valid_sizes)
    median_size = np.median(valid_sizes)
    min_size = np.min(valid_sizes)
    std_size = np.std(valid_sizes)

    # Basic stats
    print("\n Journal Entry Statistics")
    print(f"Mean size: {mean_size:.2f} bytes")
    print(f"Median size: {median_size:.2f} bytes")
    print(f"Standard deviation: {std_size:.2f} bytes")
    print(f"Total entries: {len(valid_sizes)} / {days} days recorded")

    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(byte_sizes[byte_sizes > 0], bins=50, edgecolor='black', alpha=0.7)
    plt.title("Distribution of Journal Entry Sizes (in bytes)", fontsize=16)
    plt.xlabel("Byte Size", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.axvline(mean_size, color='red', linestyle='-', linewidth=2, label=f"Mean: {mean_size:.0f}")
    plt.axvline(median_size, color='green', linestyle='-', linewidth=2, label=f"Median: {median_size:.0f}")
    plt.axvline(min_size, color='orange', linestyle='-', linewidth=2, label=f"Min: {min_size:.0f}")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
