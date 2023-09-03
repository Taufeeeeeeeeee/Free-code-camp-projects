import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = (df['weight'] / ((df['height']/100)*(df['height']/100)))
df['overweight'] = 0
df.loc[bmi>25,'overweight'] = 1


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df.loc[df['gluc'] == 1 , 'gluc'] = 0
df.loc[df['cholesterol'] == 1 , 'cholesterol'] = 0
df.loc[df['gluc'] > 1 , 'gluc'] = 1
df.loc[df['cholesterol'] > 1 , 'cholesterol'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='feature', value_name='value')
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='feature')
    
    df_cat.columns = ['cardio', 'feature', 'value']
    df_cat = df_cat.groupby(['feature', 'cardio', 'value']).size().unstack(1).reset_index()

    df_cat.columns = ['feature', 'value', 'Cardio=0', 'Cardio=1']
    # Draw the catplot with 'sns.catplot()'

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.barplot(x='feature', y='Cardio=0', data=df_cat, hue='value', ax=axes[0])
    axes[0].set_title('Cardio=0')
    axes[0].set_xlabel('variable')
    axes[0].set_ylabel('total')
  
    sns.barplot(x='feature', y='Cardio=1', data=df_cat, hue='value', ax=axes[1])
    axes[1].set_title('Cardio=1')
    axes[1].set_xlabel('variable')
    axes[1].set_ylabel('total')
    
    plt.tight_layout()
    
      # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat.loc[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat.loc[df['height'] <= df['height'].quantile(0.975)]
    df_heat = df_heat.loc[df['weight'] >= df['weight'].quantile(0.025)]
    df_heat = df_heat.loc[df['weight'] <= df['weight'].quantile(0.975)]
  
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask =  np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, annot=True, mask = mask, fmt=".1f")
    

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
