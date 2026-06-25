def store_to_csv(df):
    try:
        output_file = "fashion_product_cleaned.csv"

        df.to_csv(output_file, index=False)

        print(f"Data successfully saved to {output_file}")

        return True

    except Exception as e:
        print(f"Error saving CSV: {e}")
        return False