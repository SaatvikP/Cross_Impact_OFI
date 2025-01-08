# Cross Impact OFI Analysis

This repository contains the code and data for analyzing the **cross-impact dynamics of Order Flow Imbalance (OFI)** in equity markets. The project integrates multi-level OFI metrics, applies dimensionality reduction, and evaluates their predictive power for price changes across various stocks.

Read **Cross_Analysis_OFI.pdf** for more info
---

## Features
- **Data Preprocessing**: Handles raw `.csv.zst` files and extracts relevant features.
- **Order Flow Imbalance (OFI) Computation**: Calculates multi-level OFI metrics.
- **PCA Integration**: Reduces multi-level OFI dimensions to a single feature.
- **Regression Analysis**: Explores the relationship between OFI and price changes.
- **Visualizations**: Heatmaps and scatter plots for key insights.

---

## Installation
1. Clone the repository:
   git clone https://github.com/your-username/Cross_Impact_OFI.git

2. Navigate to the project directory:
   cd Cross_Impact_OFI

3. Install dependencies:
   pip install -r requirements.txt

---

## Usage
1. Preprocess the data:
   python scripts/data_preprocessing.py

2. Run analysis:
   python main.py

3. View results in the `results/` folder.

---

## Results
- Regression analysis R² scores are available in `results/stock_specific_regression_results.csv`.
- Heatmaps and scatter plots for individual stocks are saved in the `results/` folder.

---

## Acknowledgments
- [Databento](https://www.databento.com/) for providing the dataset.
- Contributors: [Saatvik Pradhan](https://github.com/SaatvikP)
