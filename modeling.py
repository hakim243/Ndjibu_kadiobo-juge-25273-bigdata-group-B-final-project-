import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_data(file_path):
    """Load dataset from Excel file."""
    return pd.read_excel(file_path)

def preprocess_data(df):
    """Preprocess data for modeling."""
    # Select features and target
    features = ['University Admission year', 'Gender', 'Age', 'H.S.C passing year',
                'Program', 'Current Semester', 'Do you have meritorious scholarship ?',
                'Do you use University transportation?', 'How many hour do you study daily?',
                'How many times do you seat for study in a day?', 'What is your preferable learning mode?',
                'Do you use smart phone?', 'Do you have personal Computer?',
                'How many hour do you spent daily in social media?', 'Status of your English language proficiency',
                'Average attendance on class', 'Did you ever fall in probation?', 'Did you ever got suspension?',
                'Do you attend in teacher consultancy for any kind of academical problems?',
                'What are the skills do you have ?', 'How many hour do you spent daily on your skill development?',
                'What is you interested area?', 'What is your relationship status?', 'Are you engaged with any co-curriculum activities?',
                'With whom you are living with?', 'Do you have any health issues?', 'What was your previous SGPA?',
                'Do you have any physical disabilities?', 'How many Credit did you have completed?', 'What is your monthly family income?']

    target = 'What is your current CGPA?'

    X = df[features].copy()
    y = df[target]

    # Encode categorical variables
    for col in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        # Convert all values to string to avoid mixed types error
        X[col] = le.fit_transform(X[col].astype(str))

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

def train_model(X, y):
    """Train a linear regression model."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Model Evaluation:")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R-squared: {r2:.4f}")

def main():
    file_path = "Students_Performance_data_set_cleaned.xlsx"
    df = load_data(file_path)

    X, y = preprocess_data(df)
    train_model(X, y)

if __name__ == "__main__":
    main()
