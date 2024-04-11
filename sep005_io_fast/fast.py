# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:46:08 2024

@author: AA000139
"""
import pandas as pd
from datetime import datetime

def read_fast_file(file_path: str) -> list[dict]:
   df = pd.read_table(file_path, skiprows=6, dtype=str)
   units_df = df.iloc[0:1].copy()
   units_df.drop(columns="Time", inplace=True)
   df = df.drop(0)
   time = pd.to_numeric(df['Time'], errors='coerce')
   time = time.to_numpy()
   df.index = pd.to_datetime(df["Time"], unit='s')  # Convert index to datetime
   df.drop(columns="Time", inplace=True)

   # Update the index based on fictive_measurement_start_fast
   fictive_measurement_start_fast = datetime(2022, 1, 1)
   df.index = df.index + (fictive_measurement_start_fast - df.index[0])

   # Calculate start_timestamp, fs, and duration
   start_timestamp = df.index[0]
   fs = 1 / (df.index[1] - df.index[0]).total_seconds()  # Sampling frequency in Hz
   duration = (len(df) / fs)

   # Prepare signals list in Sep005 format
   signals = []
   for channel in df.columns:
       units_df[channel] = units_df[channel].str.replace(r'[\(\)]', '', regex=True)
       df[channel] = pd.to_numeric(df[channel], errors='coerce')
       data = df[channel].to_numpy()
       fs_signal = len(data) / duration
       signal = {
              'name': channel,
              'data': data,
              'start_timestamp': str(start_timestamp),
              'fs': fs_signal,
              'unit_str': str(units_df[channel].iloc[0]),
              'time': time
          }
       signals.append(signal)

   return signals

