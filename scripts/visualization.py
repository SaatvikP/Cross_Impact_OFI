import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the results directory exists
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def save_plot(filename):
    """
    Save the current plot to the results directory.
    """
    file_path = os.path.join(RESULTS_DIR, filename)
    plt.savefig(file_path, bbox_inches='tight')
    print(f"Plot saved to {file_path}")

def plot_r2_scores(results_df):
    """
    Plot R² scores for all stocks and save to the results folder.
    """
    results_df = results_df.sort_values(by="r2_score", ascending=False)
    plt.figure(figsize=(10, 6))
    plt.bar(results_df['symbol'], results_df['r2_score'], color='skyblue')
    plt.xlabel("Stock Symbol")
    plt.ylabel("R² Score")
    plt.title("R² Scores for Integrated OFI vs. Price Changes by Stock")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    save_plot("r2_scores_plot.png")
    plt.close()

def plot_scatter(stock_data, x_column, y_column, stock_symbol, title, filename):
    """
    Create a scatter plot for a specific stock and save to the results folder.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(stock_data[x_column], stock_data[y_column], alpha=0.7, color='purple')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.grid(alpha=0.3)
    save_plot(filename)
    plt.close()

def plot_heatmap(data, stock_symbol):
    """
    Plot a heatmap of correlations for the selected stock and save to the results folder.
    """
    # Filter numeric columns only
    numeric_data = data.select_dtypes(include=['number'])

    if numeric_data.empty:
        print(f"No numeric data available for {stock_symbol}. Skipping heatmap.")
        return

    # Compute correlation matrix
    correlation_matrix = numeric_data.corr()

    # Create heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(f"Correlation Heatmap for {stock_symbol}")
    
    # Save plot
    filename = f"results/heatmap_{stock_symbol}.png"
    plt.savefig(filename)
    plt.close()
    print(f"Heatmap saved to {filename}")
