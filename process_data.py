#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

# Fix Danish headers first
df = pd.read_csv('22153912.csv', sep=';', skiprows=1, encoding="ISO-8859-1")
print(df)

# Prepare data: Fix danish chars, weird decimal chars etc.
df.rename(columns={'Værdi(KWH)': 'kWh'}, inplace=True)
df['Datetime'] = pd.to_datetime(df['Dato'])
df['Date'] = df['Datetime'].dt.date
df["WeekendFlag"] = df['Datetime'].dt.dayofweek > 4
df['kWh'] = df['kWh'].str.replace(',', '.')
df['kWh'] = pd.to_numeric(df['kWh'])

# Set index
df.set_index('Datetime', inplace=True)
df.drop(columns=['Dato'], inplace=True)

# Plot averages
averages = ['1D', '7D', '28D']
fig, ax = plt.subplots()
for avg in averages:
    _df_plot = df
    # _df_plot = df.query('WeekendFlag == False').copy()
    _df_plot = _df_plot[['kWh']].rolling(avg, min_periods=7, center=True).median().rename(columns={'kWh': f'kWh_{avg}_median'})
    _df_plot.plot(ax=ax, grid=True)
ax.set_xlabel('')
ax.set_ylabel('kWh')

# Calculate rolling means
print(df)
print(df.describe())
print(df.query('WeekendFlag == True').describe())
print(df.query('WeekendFlag == False').describe())

plt.show()
