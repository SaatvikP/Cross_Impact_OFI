import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(data, correlation_columns):
    """
    Plot a heatmap of correlations.
    """
    correlation_matrix = data[correlation_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

def scatter_plot(data, x_column, y_column):
    """
    Create a scatter plot.
    """
    plt.scatter(data[x_column], data[y_column])
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{x_column} vs {y_column}")
    plt.show()
