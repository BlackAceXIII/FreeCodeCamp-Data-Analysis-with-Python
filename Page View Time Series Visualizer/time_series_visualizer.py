import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df3 = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df3 = df3[(df3['value']>df3['value'].quantile(0.025)) & ((df3['value']<df3['value'].quantile(0.975)))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18,6))
    plt.plot(df3,color='m')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df3_bar = df3.copy(deep=True)
    df3_bar['year'] = df3_bar.index.year
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    df3_bar['month'] = df3_bar.index.month_name()
    df3_bar['month'] = pd.Categorical(df3_bar['month'], categories=months)
    df3_bar_pivot = pd.pivot_table(df3_bar,values="value",index="year",columns="month",aggfunc=np.mean)

    # Draw bar plot
    fig = df3_bar_pivot.plot(kind='bar').get_figure()
    fig.set_figheight(6)
    fig.set_figwidth(8)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df3_box = df3.copy()
    df3_box.reset_index(inplace=True)
    df3_box['year'] = [d.year for d in df3_box.date]
    df3_box['month'] = [d.strftime('%b') for d in df3_box.date]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    df3_box['month'] = pd.Categorical(df3_box['month'], categories=months)

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(18,6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df3_box['year'], y=df3_box['value']).get_figure()
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df3_box['month'], y=df3_box['value']).get_figure()
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
