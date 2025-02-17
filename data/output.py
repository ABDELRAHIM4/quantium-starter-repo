import glob
import sys
import pandas as pd

def main():
    data_folder = 'data/'
    files = glob.glob(data_folder + '*.csv')
    #print(f"{files}")
    all_pink_morsels = pd.DataFrame()
    for file in files:
        df = pd.read_csv(file)
        morsels = df[df['product'].str.lower() == 'pink morsel']
        all_pink_morsels = pd.concat([all_pink_morsels, morsels], ignore_index=True)
        print(all_pink_morsels)
if __name__ == "__main__":
    main()