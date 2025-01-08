from sklearn.decomposition import PCA

def integrate_ofi(data, ofi_columns):
    """
    Use PCA to integrate multi-level OFIs into a single metric.
    """
    pca = PCA(n_components=1)
    data["Integrated_OFI"] = pca.fit_transform(data[ofi_columns])
    return data
