import pandas as pd

def main():
    # Load the dataset
    file_path = "Students_Performance_data_set.xlsx"
    df = pd.read_excel(file_path)

    # Print basic information about the dataset
    print("Dataset Overview:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\nColumns and data types:")
    print(df.dtypes)
    print("\nFirst 5 rows:")
    print(df.head())

if __name__ == "__main__":
    main()
