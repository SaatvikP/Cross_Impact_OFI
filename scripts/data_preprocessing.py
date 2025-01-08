import os
import pandas as pd
import zstandard as zstd
import io

def load_zst_file(file_path):
    """
    Load a compressed .csv.zst file and return a pandas DataFrame.
    """
    with open(file_path, "rb") as f:
        decompressor = zstd.ZstdDecompressor()
        with decompressor.stream_reader(f) as reader:
            text_stream = io.TextIOWrapper(reader, encoding="utf-8")
            return pd.read_csv(text_stream)

def preprocess_data(data):
    """
    Clean and preprocess the raw data.
    """
    print("Initial data shape:", data.shape)
    print("Initial columns:", data.columns)
    data['ts_recv'] = pd.to_datetime(data['ts_recv'], unit='ns')
    data['ts_event'] = pd.to_datetime(data['ts_event'], unit='ns')

    if 'rtype' in data.columns:
        print("Unique rtype values:", data['rtype'].unique())
        data = data[data['rtype'] == 10]
    else:
        print("Warning: 'rtype' column not found!")

    print("After rtype filtering:", data.shape)

    # Compute imbalance for top levels (1 to 9 in this case)
    for level in range(1, 10):  # Adjust levels based on available data
        bid_sz_col = f'bid_sz_{str(level).zfill(2)}'
        ask_sz_col = f'ask_sz_{str(level).zfill(2)}'
        imbalance_col = f'imbalance_level_{level}'
        if bid_sz_col in data.columns and ask_sz_col in data.columns:
            if (data[bid_sz_col] + data[ask_sz_col]).sum() > 0:
                data[imbalance_col] = (data[bid_sz_col] - data[ask_sz_col]) / (
                    data[bid_sz_col] + data[ask_sz_col] + 1e-9)
                print(f"Calculated {imbalance_col}: Non-NaN count = {data[imbalance_col].notna().sum()}")
            else:
                print(f"No valid values for {bid_sz_col} or {ask_sz_col}. Imbalance not calculated.")
        else:
            print(f"Columns {bid_sz_col} or {ask_sz_col} missing, skipping {imbalance_col}.")

    print("After imbalance calculation:", data.shape)
    columns_to_keep = [col for col in ['symbol', 'ts_recv', 'ts_event', 'price', 'size'] + 
                       [f'imbalance_level_{level}' for level in range(1, 10)] if col in data.columns]
    data = data[columns_to_keep]

    print("Preprocessed data shape:", data.shape)
    return data

def preprocess_directory(input_dir, output_dir, combine=False):
    """
    Process all .csv.zst files in a directory and save results.
    """
    os.makedirs(output_dir, exist_ok=True)
    all_data = []

    for filename in os.listdir(input_dir):
        if filename.endswith(".csv.zst"):
            file_path = os.path.join(input_dir, filename)
            print(f"Processing file: {file_path}")

            raw_data = load_zst_file(file_path)
            print(f"Loaded data shape: {raw_data.shape}")
            processed_data = preprocess_data(raw_data)
            output_file = os.path.join(output_dir, filename.replace(".zst", ""))
            processed_data.to_csv(output_file, index=False)
            print(f"Processed {filename} and saved to {output_file}")
            all_data.append(processed_data)

    if combine and all_data:
        combined_data = pd.concat(all_data, ignore_index=True)
        combined_output_file = os.path.join(output_dir, "combined_processed_data.csv")
        combined_data.to_csv(combined_output_file, index=False)
        print(f"All files combined and saved to {combined_output_file}")
        return combined_data

    return None
