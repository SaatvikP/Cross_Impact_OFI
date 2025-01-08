def compute_ofi(data, levels=5):
    """
    Compute multi-level Order Flow Imbalance (OFI).
    """
    ofi_columns = [f"OFI_Level_{i}" for i in range(1, levels + 1)]
    for i in range(1, levels + 1):
        data[f"OFI_Level_{i}"] = data[f"BidSize_Level_{i}"] - data[f"AskSize_Level_{i}"]
    return data, ofi_columns
