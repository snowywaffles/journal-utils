import pandas as pd
import numpy as np
import requests as requests
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    data = requests.get("https://www.njbrown.com/posts.json")
    # print(data.text)
    df = pd.read_json(data.text)
    df['date'] = pd.to_datetime(df['date'])
    df['url'] = df['url'].str.extract(r'/blog/(\d+)/').astype(int)
    cleaned = df[['date', 'url']]
    print(cleaned)
    plt.scatter(x=cleaned['date'], y=cleaned['url']) 
    plt.show()

if __name__ == "__main__":
    main()
