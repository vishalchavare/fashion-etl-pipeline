import pandas as pd
from utils.transform import transform_data
from utils.load import store_to_csv

def main():
    try:
        print("Loading CSV file...")

        df = pd.read_csv("fashion_product.csv")

        print("Original Data:")
        print(df.head())

        df = transform_data(df)

        print("\nTransformed Data:")
        print(df.head())

        store_to_csv(df)

        print("\nETL Process Completed Successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()