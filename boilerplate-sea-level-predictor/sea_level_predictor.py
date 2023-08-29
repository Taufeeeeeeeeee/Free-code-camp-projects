import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    
    # Create scatter plot
    fig,ax = plt.subplots()
    ax.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    

    # Create first line of best fit
    res1 = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    
    x = np.linspace(df['Year'].min(),2050,2050 - df['Year'].min() +1)
    y = x*res1[0] + res1[1]
    ax.plot(x,y)
  
    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000 , ['Year','CSIRO Adjusted Sea Level' ]]
    
    res2 = linregress(new_df['Year'],new_df['CSIRO Adjusted Sea Level'])
    new_x = np.linspace(new_df['Year'].min(),2050,2050 - new_df['Year'].min() +1)
    new_y = new_x*res2[0] + res2[1]
    
    ax.plot(new_x,new_y)
  

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()