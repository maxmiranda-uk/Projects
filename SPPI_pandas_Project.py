# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# docstring - explains what a section of code is for
# comments explain parts of the code
# comments/notes to myself


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pandas getting started tutorial 1

# creates a DataFrame (table) - each dictionary key becomes a column
# the list for each key contains the values in that column

df = pd.DataFrame(
    {
     'Name':[
        'Max',
        'Dan',
        'Euler',],
     
     'Age': [
         10,
         11,
         12,
         ],
     'Sex':[
         'male',
         'male',
         'male',
         ],
     }
    )

print(df)

# creates a Series - basically one column of values
# name gives the Series/column a label and rows have an index

Age = pd.Series([10,11,12], name='Age')
print()

print(Age)

# .max() gives the maximum value in a column/Series

print('max value in table is', df['Name'].max())
print('oldest is', Age.max())

print()

# describe() gives the main summary statistics
# count, mean, std, min, quartiles (25%, 50%, 75%) and max

print(df['Age'].describe())
print(Age.describe())

# reads a csv file into a DataFrame

fuel = pd.read_csv('series-180126.csv')

# .head(n) shows the first n rows
# .tail(n) shows the last n rows

print(fuel.head(3))
print(fuel.tail(3))

# check the datatype pandas has given each column

print(fuel.dtypes)

# to_excel() can save the DataFrame as an Excel file

# index=True includes the row index, index=False leaves it out
#fuel.to_excel('fuel.xlsx', 'sheet_name = spreadsheet', index = False)
# commented this out because it was interfering with the code after it

# info() gives useful details like datatypes, number of entries and memory usage

print(fuel.info())
print(fuel.columns)

# .shape gives the size as (rows, columns)

print(fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES'].shape)

# select more than one column with a list of column names, then use head()

print(fuel[['Title','SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES']].head(14))

# use comparisons such as >, <, == or != to filter rows

fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES'] = pd.to_numeric(fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES'], errors = 'coerce')
# had an error here because the column contained strings as well as numbers
# pd.to_numeric converts the values to numbers so they can be compared
# errors='coerce' turns anything that can't be converted into NaN
filter_ed = fuel[fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES']>100]
print(filter_ed.head())

# .isin() can be used to find rows containing particular values

value = fuel[fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES'].isin([101,103])]
print('value wanting to be found are in', value)

# select rows that meet a condition, then return a particular column

specific_by_name = fuel.loc[fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES']>102,'Title']
print('the columns that fit condition >102 are', specific_by_name)
# .loc works with labels/column names and conditions

#specific_by_number = fuel.iloc[2:5,0:1]
#specific_by_number = pd.to_numeric(specific_by_number.squeeze(), errors = 'coerce')
#print('between rows 1 and 3 for column 1 is', specific_by_number)

# this iloc attempt didn't work with the way I was slicing the data
# iloc uses integer positions rather than labels
# loc is more useful for what I'm doing here
# kept the failed attempt commented out for reference

# quick plot to visually check the data

# pandas does the plotting here and matplotlib displays/customises it
fuel.plot()
plt.title('Quick visual check')
plt.show()

# plot one specific column

fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES'].plot()
plt.title('plot one column SPPI')
plt.show()

# scatter plot to compare data - lower alpha makes the points more transparent

# quarter data is different from the other entries, so don't mix them up
x_process = fuel['Title']
x = []
filtered_df = fuel[fuel['Title'].astype(str).str.contains('Q1')]
# change Q1 here if I want to look at a different quarter
for i in x_process:
    
    date = str(i).split()
 #   print(date[0]) # useful for checking what was extracted
    if date[0].isdigit() and len(date)>=2 and date[1].startswith('Q1'):
# change Q1 here if I want to look at a different quarter
            #print data and see that the order is different
            #ensures right amount of years is used
            x.append(date[0])
    #len returns number of items in this list so filter 1s with not just date
#print(fuel)
#

print(len(x))
       
y = filtered_df['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES'] 
# y is taken from the filtered quarter data, so non-quarter values aren't included
# print('x is', x) # useful for checking x

        
plt.scatter(x, y,alpha = 0.5)
plt.show()

# box plot attempt - kept commented out for reference

# x = []
# filtered_df = fuel[fuel['Title'].astype(str).str.contains('Q1')]
# y = filtered_df['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES']
# # print(fuel['Title'])
# for i in fuel['Title']:
#     date = str(i).split()
#     if date[0].isdigit() and len(date)>=2 and date[1].startswith('Q1'):
#         x.append(date[0])
# # print(x)

# fuel.plot.box()
# plt.show()

# subplots can be used to split plots into separate axes

#print(fuel)
x_process = fuel['Title']
for i in x_process:
    date = str(i).split()
    if date[0].isdigit() and len(date)>=2 and date[1].startswith('Q1'):
        x.append(date[0])
filtered_df = fuel[fuel['Title'].astype(str).str.contains('Q1')]
y = filtered_df['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES']
fuel.plot.area(subplots=True)
plt.show()
        
# use matplotlib to customise things like axis labels and save the figure

x_process = fuel['Title']
for i in x_process:
    date = str(i).split()
    if date[0].isdigit() and len(date)>=2 and date[1].startswith('Q1'):
        x.append(date[0])
filtered_df = fuel[fuel['Title'].astype(str).str.contains('Q1')]
y = filtered_df['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES']
fig, axs = plt.subplots()
fuel.plot.area(ax=axs)
axs.set_ylabel('SPPI')
axs.set_xlabel('Date')
fig.savefig('SPPI_vs_Date.png')
plt.show()

# creating new columns

# multiplying a column by a number applies it to every value in the column

#fuel['New Columnn Years'] = fuel['Title']*10
#print(fuel)

# calculate a ratio using columns and save it as a new column

#for i in fuel['Title']:
   # column_one = str(i).split()
  #  if i.startswith('20'):
 #       fuel['Title'].append(i)
#print(fuel)
        


fuel['year'] = (
    fuel['Title'].astype(str).str.extract('^(20\d{2})')
    .astype('Int64')
    )
fuel['sppi values'] = pd.to_numeric( 
    fuel['SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES'], errors = 'coerce'
    )

fuel['ratio'] = fuel['year'] / fuel['sppi values']
print(fuel['ratio'])

# rename columns to make the names shorter/easier to use

rename_fuel = fuel.rename(
    columns = {
    'Title': 'Name',
    'SPPI: 7112000000: ENGINEERING SERVICES & RELATED SERVICES': 'SPPI',
    }
    )
print(rename_fuel)


# summary statistics

print(fuel['ratio'].mean())
print(fuel['ratio'].median())

print(fuel['ratio'].describe())
print(fuel.agg(
    {
     'ratio':['min','max'],
      'sppi values':['min','max'],
     }
    )
    )
print(fuel[['Title','ratio']].groupby('Title').mean())

 # value_counts() tells me how often each value appears
 
print(fuel['ratio'].value_counts())

# sorting / reshaping the data

# sort one column from smallest to biggest

print(fuel.sort_values(by='ratio').head())

# sort using more than one column (ascending=False gives biggest to smallest)

print(fuel.sort_values(by=['sppi values','ratio'], ascending = False).head())

# filter down to the data I want before reshaping/plotting

#print(fuel)
filtered_year = fuel[fuel['Title'] == '2018']
filtered_year_subset = filtered_year.groupby(['SPPI']).head()
#print(filtered_year_subset)
filtered_year_subset.pivot(columns = 'Title', values = 'ratio').plot()

# handling time-series data
# Title has mixed formats, so I need to clean the dates before treating it as time-series data
# if the dates were already clean I could use the normal pandas approach

print(fuel)
fuel['Title'] = fuel['Title'].astype(str)

# first check the minimum and maximum values in Title
print(fuel['Title'].min())
print(fuel['Title'].max())

# Title also contains words/non-date values, so I can't convert everything directly
# need to filter/handle the non-date values first

fuel_copy = fuel.copy()

# identify values that look like year + quarter

filtered_dates = fuel['Title'].astype(str).str.match(r'\d{4}\sQ[1-4]?$', na=False)
# \d{4} means 4 digits
# \s means a space/whitespace
# $ means the pattern has to end there
# na=False means NaN values are treated as not matching
fuel_copy = fuel.copy()

# convert the valid date values to datetime

# separate quarter entries from year-only entries because they need different conversion
look_at_quarters = fuel_copy['Title'].str.contains(r'\sQ[1-4]$')
fuel_copy.loc[~look_at_quarters, 'date'] = pd.to_datetime(
    fuel_copy.loc[~look_at_quarters, 'Title'], format ='%Y', errors ='coerce')
fuel_copy.loc[look_at_quarters, 'date'] = pd.PeriodIndex(fuel.loc[look_at_quarters,'Title'].str.replace(' ',''), freq = 'Q').to_timestamp(how='start')
fuel_copy['ratio'] = pd.to_numeric(fuel['ratio'], errors = 'coerce')
# make sure ratio is numeric - anything invalid becomes NaN
print('min date', fuel_copy['date'].min())
print('max date', fuel_copy['date'].max())

# now work with the quarter data as a time series

# can make a new column from parts of the datetime, e.g. month or year
# using month here

print(fuel_copy)
fuel_copy['Year Quarter'] = fuel_copy['date'].dt.month
# .dt lets me access datetime parts such as month
print(fuel_copy['Year Quarter'])
print(fuel_copy.groupby([fuel_copy['date'].dt.month, 'Title'])['ratio'].mean())

# plot the ratio grouped by month

fig, axs = plt.subplots(figsize = (12,4))
fuel_copy.groupby([fuel_copy['date'].dt.month, 'Title'])['ratio'].mean().plot(
    kind = 'bar',
    rot = 0,
    ax=axs,
    )
plt.xlabel('month')
plt.ylabel('ratio')

# setting date as the index makes date slicing much easier

print(fuel_copy['date'])

fuel_copy = fuel_copy.dropna(subset=['date']).set_index('date').sort_index()
fuel_copy.loc['2010-01-01':'2011-10-01','ratio'].plot()
