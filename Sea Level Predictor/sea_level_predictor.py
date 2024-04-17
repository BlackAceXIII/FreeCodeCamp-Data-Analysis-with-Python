import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df4 = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    plt.scatter(df4['Year'], df4['CSIRO Adjusted Sea Level'], s=8, marker='D', color='b')

    # Create first line of best fit
    line1 = linregress(df4['Year'], df4['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df4['Year'].min(), 2051, 1)
    y1 = line1.intercept + line1.slope*x1
    plt.plot(x1,y1,color='firebrick')

    # Create second line of best fit
    df5 = df4[df4['Year']>=2000]
    line2 = linregress(df5['Year'], df5['CSIRO Adjusted Sea Level'])
    x2 = np.arange(df5['Year'].min(), 2051, 1)
    y2 = line2.intercept + line2.slope*x2
    plt.plot(x2,y2,color='mediumseagreen')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()