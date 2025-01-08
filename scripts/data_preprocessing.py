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
    data = data.dropna()
    data.rename(columns=lambda x: x.strip(), inplace=True)
    return data
