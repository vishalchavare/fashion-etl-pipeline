import pandas as pd

def transform_data(df):

    try:

        df = df.copy()

        df = df[
            (df["Title"] != "Unknown Product")
            & (df["Rating"] != "Invalid Rating / 5")
            & (df["Rating"] != "Not Rated")
            & (df["Price"] != "Price Unavailable")
        ]

        df = df.drop_duplicates()

        df = df.dropna()

        df["Price"] = (
            df["Price"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .astype(float)
        )

        df["Rating"] = pd.to_numeric(df["Rating"])

        df["Colors"] = pd.to_numeric(df["Colors"])

        return df

    except Exception as e:
        print(f"Transformation Error: {e}")
        return df