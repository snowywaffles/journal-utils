import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, date, timedelta

def get_data():
    num = (date.today() - date(2024, 1, 1)).days + 1
    dates = (np.datetime64("2024-01-01") + np.arange(num, dtype="timedelta64[D]")).astype(str)

    byte_sizes = np.empty(num, dtype=int)

    for i, d in enumerate(dates):
        path = f"/Users/olympus/Documents/journalEntries/{d.replace('-', '.')}.txt"
        if not os.path.exists(path):
            raise ValueError(f"path: {path} does not exist")
        with open(path, "rb") as f:
            byte_sizes[i] = len(f.read())

    return pd.DataFrame({
        "date": dates,
        "byte_size": byte_sizes,
    })

def main():
    use_log_scale = True
    df = get_data()

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    df["sma20"] = df["byte_size"].rolling(window=20, min_periods=1).mean()
    df["sma50"] = df["byte_size"].rolling(window=50, min_periods=1).mean()
    df["sma100"] = df["byte_size"].rolling(window=100, min_periods=1).mean()

    ax = df.plot(
        x="date",
        y=["byte_size", "sma20", "sma50", "sma100"],
        style=[".", "-", "-"],
        markersize=6
    )

    # make individual data points less prominent
    ax.lines[0].set_alpha(0.4)

    if use_log_scale:
        ax.set_yscale("log", base=2)

    ax.set_ylabel("bytes")
    ax.set_title("byte_size vs. time")
    plt.show()

if __name__ == "__main__":
    main()
