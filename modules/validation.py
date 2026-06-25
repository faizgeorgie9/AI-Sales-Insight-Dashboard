import pandas as pd

required_columns = [
    "Tanggal",
    "Customer",
    "Produk",
    "Kategori",
    "Qty",
    "Harga",
    "Sales",
    "Target Sales",
    "Kota"
]


def validate_data(df):

    errors = []

    missing_cols = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_cols:
        errors.append(
            f"Kolom tidak ditemukan : {missing_cols}"
        )

    if df.isnull().sum().sum() > 0:
        errors.append(
            "Masih terdapat missing value"
        )

    if (df["Qty"] <= 0).any():
        errors.append(
            "Qty tidak boleh <= 0"
        )

    if (df["Harga"] <= 0).any():
        errors.append(
            "Harga tidak boleh <= 0"
        )

    return errors