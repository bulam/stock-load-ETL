import os, glob, string
import numpy as np
import pandas as pd
import itertools
from scipy import stats

# 1. Load stock data into a dataframe and prepare for analysis


#1.1 Load close prices
# Set the directory to the directory where the stock data is stored
os.chdir("C:\\Users\\bilgu\\Documents\\Stocks\\lesson\\AllStockData")

# prepare the fileList and dataframe for stock data
fileList = []
df = pd.DataFrame()

# set number of past days to load into dataframe
dataSetSize = 100

# read all file names
for files in glob.glob("*.txt"):

    #ignore empty files
    if os.path.getsize(files) == 0:
        continue

    filename = os.path.basename(files).partition('.')[0]
    fileList.append(filename)

# iterate through files and take close values
for file in glob.glob("*.txt"):

    #ignore empty files
    if os.path.getsize(file) == 0:
        continue

    frame = pd.read_table(file, header = 0, sep = ',', index_col = 0)['Close'].tail(dataSetSize)
    df = df.append(frame)

# change row names to stock ticker symbols
df.index = fileList

# Final clean up! Sort by date, transpose, select latest 100 days, drop null values
df_close = df.sort(axis = 'columns', ascending = False).transpose().head(dataSetSize).dropna(axis=1, how='any')

print('Close prices loaded. Now loading open prices.')



#1.1 Load open prices
# Set the directory to the directory where the stock data is stored
os.chdir("C:\\Users\\bilgu\\Documents\\Stocks\\lesson\\AllStockData")

# prepare the fileList and dataframe for stock data
fileList = []
df_open = pd.DataFrame()

# set number of past days to load into dataframe
dataSetSize = 100

# read all file names
for files in glob.glob("*.txt"):

    #ignore empty files
    if os.path.getsize(files) == 0:
        continue

    filename = os.path.basename(files).partition('.')[0]
    fileList.append(filename)

# iterate through files and take close values
for file in glob.glob("*.txt"):

    #ignore empty files
    if os.path.getsize(file) == 0:
        continue

    frame = pd.read_table(file, header = 0, sep = ',', index_col = 0)['Open'].tail(dataSetSize)
    df_open = df_open.append(frame)

# change row names to stock ticker symbols
df_open.index = fileList

# Final clean up! Sort by date, transpose, select latest 100 days, drop null values
df_open = df_open.sort(axis = 'columns', ascending = False).transpose().head(dataSetSize).dropna(axis=1, how='any')


print('Open prices loaded. Initiating trading algorithm.')