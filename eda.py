import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load dataset from Excel file."""
    return pd.read_excel(file_path)

def descriptive_statistics(df):
    """Print descriptive statistics of the dataset."""
    print("Descriptive Statistics:")
    print(df.describe(include='all'))

def plot_distributions(df, columns):
    """Plot histograms for specified columns."""
    for col in columns:
        plt.figure(figsize=(8, 4))
        if df[col].dtype == 'object':
            sns.countplot(data=df, x=col)
            plt.title(f'Distribution of {col}')
            plt.xticks(rotation=45)
        else:
            sns.histplot(df[col], kde=True)
            plt.title(f'Distribution of {col}')
        plt.tight_layout()
        plt.show()

def plot_relationships(df, col1, col2):
    """Plot scatterplot and correlation between two numerical columns."""
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=col1, y=col2)
    plt.title(f'Relationship between {col1} and {col2}')
    plt.tight_layout()
    plt.show()
    corr = df[[col1, col2]].corr().iloc[0,1]
    print(f'Correlation between {col1} and {col2}: {corr:.2f}')

def main():
    file_path = "Students_Performance_data_set_cleaned.xlsx"
    df = load_data(file_path)

    descriptive_statistics(df)

    # Example columns to plot distributions
    columns_to_plot = ['Gender', 'Program', 'Current Semester', 'What is your current CGPA?']
    plot_distributions(df, columns_to_plot)

    # Example relationship plot
    plot_relationships(df, 'What was your previous SGPA?', 'What is your current CGPA?')

if __name__ == "__main__":
    main()
