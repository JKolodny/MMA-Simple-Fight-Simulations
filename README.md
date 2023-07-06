# Fighter Data Simulation and Visualization

This project consists of three main Python functions designed to simulate fight data for a number of fighters, visualize the distribution of win percentages, and display the distribution of wins and losses. Here's a brief summary of each function:

__generate_fighter_data(number_of_fighters):__ This function simulates fight data for a given number of fighters, each fighter having a varying number of fights and outcomes. It returns a pandas DataFrame with each row representing a fighter, and columns representing the number of wins and losses.

__plot_fighter_data(number_of_fighters):__ This function first generates fighter data using the generate_fighter_data function. It then calculates the win percentage for each fighter and plots a histogram of these win percentages. The color coding of the histogram bars is done by height.

__plot_win_loss_distribution(number_of_fighters):__ Similar to plot_fighter_data, this function first generates fighter data. It then calculates the counts of wins and losses, sorts these counts, and displays them in a bar plot.

# Usage

Here is how you can use these functions:

## Generate and visualize data for 1000 fighters
plot_fighter_data(number_of_fighters=1000)

## Generate and visualize win-loss distribution for 1000 fighters
plot_win_loss_distribution(number_of_fighters=1000)

# Requirements
This project requires Python 3.6+ and the following Python libraries installed:

numpy
pandas
matplotlib

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.
