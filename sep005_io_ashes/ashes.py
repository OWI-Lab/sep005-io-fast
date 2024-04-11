# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:38:12 2024

@author: AA000139
"""

import pandas as pd
from datetime import datetime
import numpy as np
import os

def read_ashes_file(filepaths: str) -> list[dict]:
    
    # Initialize an empty list to store DataFrames
    dfs = []
    units = []

    # Loop through each file and read data into DataFrame with appropriate skiprows
    for key, filepath in filepaths.items():
        if os.path.exists(filepath):
            if key in ['Sensor Mooring line']:
                # For Mooring file, skip 12 rows and drop 6 rows
                df = pd.read_table(filepath, skiprows=12, dtype=str)
                df.drop(range(6), inplace=True)
                df.reset_index(drop=True, inplace=True)
                dfs.append(df)
            elif key in ['Sensor Blade [Time] [Blade 1]']:
                # For Blade file, skip 12 rows and drop 12 rows
                df = pd.read_table(filepath, skiprows=12, dtype=str)
                df.drop(range(6), inplace=True)
                df.reset_index(drop=True, inplace=True)
                dfs.append(df)
            elif key in ['Sensor Node [Node Hub Hub]']:
                # For Node file, skip 11 rows and drop 17 rows
                df = pd.read_table(filepath, skiprows=11, dtype=str)
                df.drop(range(17), inplace=True)
                df.reset_index(drop=True, inplace=True)
                dfs.append(df)
            elif key in ['Sensor Beam element [Element 1 Tubular tower]']:
                # For Node file, skip 11 rows and drop 17 rows
                df = pd.read_table(filepath, skiprows=11, dtype=str)
                df.drop(range(12), inplace=True)
                df.reset_index(drop=True, inplace=True)
                dfs.append(df)
            else:
                # For other files, skip 11 rows and drop 6 rows
                df = pd.read_table(filepath, skiprows=11, dtype=str)
                df.drop(range(6), inplace=True)
                df.reset_index(drop=True, inplace=True)
                dfs.append(df)
            # Rename columns if it's Sensor Rotor or Sensor Beam element to
            # avoid duplicated columns with other sensors
            if key == 'Sensor Rotor':
                df.columns = [f"{col}_rotor" if col != 'Time [s]' else col for col in df.columns]
            elif key == 'Sensor Beam element [Element 1 Tubular tower]':
                df.columns = [f"{col}_beam" if col != 'Time [s]' else col for col in df.columns]
                
    # Combine all DataFrames in one Dataframe along the columns axis
    combined_df = pd.concat(dfs, axis=1)

    # Extract units from column headers
    for column in combined_df.columns:
        unit = column.split('[')[-1].split(']')[0]
        units.append(unit)
    units_df = pd.DataFrame([units], columns=combined_df.columns)

    # Extract the first encounter of Time [s] column and set it as the index
    time_column_index = next((i for i, col in enumerate(combined_df.columns) if col == 'Time [s]'), None)
    if time_column_index is not None:
        combined_df.index = pd.to_datetime(combined_df.iloc[:, time_column_index], unit='s')
        combined_df = combined_df.drop(columns=[col for col in combined_df.columns if 'Time [s]' in col])
        units_df = units_df.drop(columns=[col for col in units_df.columns if 'Time [s]' in col])

    # Define a fictive measurement start datetime for Ashes data
    fictive_measurement_start_ashes = datetime(2022, 1, 1)
    combined_df.index += (fictive_measurement_start_ashes - combined_df.index[0])

    # Initialize an empty list to store the time vector
    start_timestamp = combined_df.index[0]
    time_seconds = []
    # Extract time vector from the datetime index
    for timestamp in combined_df.index:
        time_seconds.append((timestamp - start_timestamp).total_seconds())
    time = np.array(time_seconds, dtype=float)

    # Clean dataframe's columns 
    combined_df.columns = combined_df.columns.str.replace(r'\[.*?\]', '', regex=True).str.strip()
    units_df.columns = units_df.columns.str.replace(r'\[.*?\]', '', regex=True).str.strip()

    # Write in Sep005 format
    fs = 1 / (combined_df.index[1] - combined_df.index[0]).total_seconds()  # Sampling frequency in Hz
    duration = (len(combined_df) / fs)
    signals = []
        
    for channel in combined_df.columns:
        combined_df[channel] = pd.to_numeric(combined_df[channel], errors='coerce')
        data = combined_df[channel].to_numpy()
        fs_signal = len(data) / duration
        signal = {
            'name': channel,
            'data': data,
            'start_timestamp': str(start_timestamp),
            'fs': fs_signal,
            'unit_str': str(units_df[channel].iloc[0]),
        }
        signals.append(signal)


    return signals
