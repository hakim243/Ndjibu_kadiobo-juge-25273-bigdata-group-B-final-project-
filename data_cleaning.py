import pandas as pd

def load_data(file_path):
    """Load dataset from Excel file."""
    return pd.read_excel(file_path)

def check_missing_values(df):
    """Check and print missing values count per column."""
    missing = df.isnull().sum()
    print("Missing values per column:")
    print(missing[missing > 0])

def clean_data(df):
    """Perform basic data cleaning."""
    # Example: Fill missing numerical values with median
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)

    # Example: Fill missing categorical values with mode
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].isnull().any():
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)

    return df

def main():
    file_path = "Students_Performance_data_set.xlsx"
    df = load_data(file_path)
    print("Initial data shape:", df.shape)

    check_missing_values(df)

    df_clean = clean_data(df)
    print("Data shape after cleaning:", df_clean.shape)

    # Save cleaned data to a new file
    df_clean.to_excel("Students_Performance_data_set_cleaned.xlsx", index=False)
    print("Cleaned data saved to 'Students_Performance_data_set_cleaned.xlsx'")

if __name__ == "__main__":
    main()
