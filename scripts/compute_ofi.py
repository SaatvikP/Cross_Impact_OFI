def compute_ofi(data, levels=9):
    """
    Compute multi-level Order Flow Imbalance (OFI) for the given data.
    """
    ofi_columns = []
    
    for level in range(1, levels + 1):
        imbalance_col = f'imbalance_level_{level}'
        ofi_col = f'OFI_level_{level}'
        
        if imbalance_col in data.columns:
            data[ofi_col] = data[imbalance_col] * data['size']  # Example calculation
            ofi_columns.append(ofi_col)
            print(f"Calculated {ofi_col}: Non-NaN count = {data[ofi_col].notna().sum()}")
        else:
            print(f"Column {imbalance_col} missing, skipping {ofi_col}.")
    
    return data, ofi_columns
