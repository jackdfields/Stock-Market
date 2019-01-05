# This is going to pull stocks from Apple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('ggplot')

# Create a figure and axes that is only 1x1 as you only have one chart
fig = plt.figure(figsize=(6,4))
ax = fig.gca()


def get_stock_data(interval):
    # Symbol is the company stock abbreviation
    symbol = 'AAPL'

    # IETrading sends their information as json strings
    df_complete_data = pd.read_json('https://api.iextrading.com/1.0/stock/' + symbol + '/chart/1m')

    # Make the date the index as it is more readable 
    df_complete_data.set_index('date', inplace=True)

    # pull out the desired stats
    df_open_to_close = pd.DataFrame(df_complete_data[['high','low','open','close','volume']])
    
    df_open_to_close.sort_index(ascending=False, inplace=True)
    
    print(df_open_to_close.head())
    
    # Clear out previous data
    ax.clear()

    # Plot each of the lines from the dataset
    df_open_to_close.high.plot(color='green', label='High')
    df_open_to_close.low.plot(linestyle = '-', color='red', label='Low')
    df_open_to_close.open.plot(linestyle = ':' , color='blue', label='Open')
    df_open_to_close.close.plot(linestyle = '-.', color='black', label='Close')

    # Grab the most recent data
    fig.suptitle('High: ' + str(df_open_to_close['high'][0]) + '  Low: ' + str(df_open_to_close['low'][0]))
    ax.tick_params(axis='x', rotation=25)

    # set up the chart
    plt.xlabel('Time'); plt.ylabel('Dollar Amount') 
    plt.title("Apple Stock");plt.legend(loc='best')

ani = animation.FuncAnimation(fig, get_stock_data, interval = 86400000)
plt.show()

