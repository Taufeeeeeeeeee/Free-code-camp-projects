import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
# Clean data
df = df.loc[df['value']>df['value'].quantile(0.026)]
df = df.loc[df['value']<df['value'].quantile(0.975)]

def draw_line_plot():
    # Draw line plot
    fig,ax = plt.subplots(figsize=(14,6))
    ax.plot(df['date'] , df['value'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['date'] = pd.to_datetime(df_bar['date'])
    
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()
    
    monthly_avg = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    monthly_avg = monthly_avg.reindex(columns=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    monthly_avg.plot(kind='bar', ax=ax)
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily Page Views by Month (Grouped by Year)')
    ax.legend(title='Months', labels=monthly_avg.columns)
    


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['date'] = pd.to_datetime(df_box['date'])
    
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month_name()

    # Draw box plots (using Seaborn)
  
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
  
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],
                order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                       'September', 'October', 'November', 'December'])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    custom_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    axes[1].set_xticklabels(custom_labels)
    axes[1].tick_params(axis='x', rotation=45)
    plt.tight_layout()
    
  
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
