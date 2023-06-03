import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = range(1880, 2051)
    y_values = slope * x_values + intercept
    plt.plot(x_values, y_values, 'r', label='Best Fit Line')

    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    recent_slope, recent_intercept, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    recent_x_values = range(2000, 2051)
    recent_y_values = recent_slope * recent_x_values + recent_intercept
    plt.plot(recent_x_values, recent_y_values, 'g', label='Recent Best Fit Line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
