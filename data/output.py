import glob
import sys
import pandas as pd
import logging
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Process CSV files in the data folder to extract pink morsels data and save to a single CSV file."""

    data_folder = 'data/'
    files = glob.glob(data_folder + '*.csv')
    
    if not files:
        logging.warning("No CSV files found in the data folder")
        return

    all_pink_morsels = pd.DataFrame()
    
    for file in files:
        try:
            logging.info(f"Processing file: {file}")
            df = pd.read_csv(file)
            morsels = df[df['product'].str.lower() == 'pink morsel']
            all_pink_morsels = pd.concat([all_pink_morsels, morsels], ignore_index=True)
            logging.info(f"Processed {len(morsels)} rows from {file}")
        except Exception as e:
            logging.error(f"Error processing file {file}: {str(e)}")
            continue

    if not all_pink_morsels.empty:
        try:
            all_pink_morsels.to_csv('pink_morsels.csv', index=False)
            logging.info(f"Successfully saved {len(all_pink_morsels)} rows to pink_morsels.csv")
        except Exception as e:
            logging.error(f"Error saving output file: {str(e)}")

if __name__ == "__main__":
    main()
