import pandas as pd

def preprocess(df):

    df["Tanggal"] = pd.to_datetime(df["Tanggal"])

    df["Omzet"] = (
        df["Qty"] *
        df["Harga"]
    )

    return df