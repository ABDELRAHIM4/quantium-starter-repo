import glob
import sys
import pandas as pd
import pandas
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px


def main():
    data_folder = 'data/'
    files = glob.glob(data_folder + '*.csv')
    all_pink_morsels = pd.DataFrame()
    for file in files:
        df = pd.read_csv(file)
        morsels = df[df['product'].str.lower() == 'pink morsel']
        all_pink_morsels = pd.concat([all_pink_morsels, morsels], ignore_index=True)
        print(all_pink_morsels)
    if not all_pink_morsels.empty:
        all_pink_morsels.to_csv('pink_morsels.csv', index=False)
if __name__ == "__main__":
    main()