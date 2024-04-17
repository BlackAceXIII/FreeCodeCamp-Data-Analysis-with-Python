import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df2 = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
#df2['overweight'] = None
BMI = df2['weight']/((df2['height']/100)**2)
df2['overweight'] = (BMI > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df2['cholesterol'] = df2['cholesterol'].replace([1, 2, 3], [0, 1, 1])
df2['gluc'] = df2['gluc'].replace([1, 2, 3], [0, 1, 1])

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df2_cat_plot = pd.melt(df2, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df2_cat_plot_2 = pd.DataFrame(df2_cat_plot.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total'))


    # Draw the catplot with 'sns.catplot()'
    catplot = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df2_cat_plot, kind='bar')


    # Get the figure for the output
    fig = catplot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df2_heat_map = df2[(df2['ap_lo'] <= df2['ap_hi'])
    & (df2['height'] >= df2['height'].quantile(0.025))
    & (df2['height'] <= df2['height'].quantile(0.975))
    & (df2['weight'] >= df2['weight'].quantile(0.025))
    & (df2['weight'] <= df2['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df2_heat_map.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, linewidths=.5, annot=True, fmt='.1f', mask=mask, square=True, center=0, vmin=-0.1, vmax=0.25, cbar_kws={'shrink': .45,'format': '%.2f'})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig