from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import time

def run_regression(data, target_column, feature_columns):
    """
    Run regression analysis using Random Forest with optimizations.
    """
    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' not found in data.")
    missing_features = [col for col in feature_columns if col not in data.columns]
    if missing_features:
        raise ValueError(f"Feature columns {missing_features} not found in data.")
    data_sample = data.sample(frac=0.1, random_state=42)  # Use 10% of the data
    X = data_sample[feature_columns].fillna(0)
    y = data_sample[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Starting Random Forest training...")
    start_time = time.time()
    model = RandomForestRegressor(n_estimators=50, random_state=42, n_jobs=-1)  # Reduce trees, enable parallelism
    model.fit(X_train, y_train)
    end_time = time.time()
    print(f"Training completed in {end_time - start_time:.2f} seconds.")

    score = model.score(X_test, y_test)
    print(f"Random Forest R^2 Score: {score}")

    return model, score
