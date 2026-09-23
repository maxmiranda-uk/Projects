# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 21:08:04 2026

@author: Maxim
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Date Processing
fuel = pd.read_csv('series-180126.csv')

fuel = fuel.rename(columns={
    'Title': 'Period',
    'SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES': 'SPPI'
})

fuel['SPPI'] = pd.to_numeric(fuel['SPPI'], errors='coerce')

# Filter out rows for Year Quarter
process_quarters = fuel['Period'].str.match(r'^\d{4}\sQ[1-4]$', na=False)
fuel_process = fuel[process_quarters].copy()


# Create quarterly datetime index
fuel_process['date'] = pd.PeriodIndex(
    fuel_process['Period'].str.replace(' ', ''),
    freq='Q'
).to_timestamp(how='start')
fuel_process = fuel_process.dropna(subset=['date']).set_index('date').sort_index()

#Time-Series Plot
plt.figure(figsize=(12,4))
fuel_process['SPPI'].plot()
plt.title('Engineering Services SPPI Against Time')
plt.ylabel('SPPI')
plt.xlabel('Date')
plt.show()

#Analysis
print('std is' , fuel_process['SPPI'].std() )
print('mean is' , fuel_process['SPPI'].mean() )

##Comments on Graph:
    ##COVID and 2008 Financial Crisis correspond to a decrease in inflation
    ##Graph suggests high inflation frequently occuring.
    