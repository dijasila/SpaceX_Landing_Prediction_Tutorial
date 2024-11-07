import pandas as pd

def analyze_data(df):
    print("Total launches:", df.shape[0])
    print("Successful launches:", df[df['success'] == True].shape[0])
    print("Launch success rate:", df['success'].mean())