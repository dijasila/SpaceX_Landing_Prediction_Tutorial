import pandas as pd
import matplotlib.pyplot as plt

def plot_launch_success(df):
    success_counts = df['success'].value_counts()
    success_counts.plot(kind='bar', color=['green', 'red'])
    plt.title("Launch Success vs Failure")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.show()