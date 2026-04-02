import pandas as pd

import os

df = pd.read_csv("data/processed/cleaned_data.csv")


# -------------------------------
# Load Data
# -------------------------------
def load_data():
    csv_path = "data/raw/traffic.csv"
    excel_path = "data/raw/Traffic_Violations_raw.xlsx"

    if os.path.exists(csv_path):
        print("Loading from CSV...")
        df = pd.read_csv(csv_path)
    else:
        print("Loading from Excel...")
        df = pd.read_excel(excel_path)
        df.to_csv(csv_path, index=False)
        print("CSV created")

    return df


# -------------------------------
# Cleaning Functions
# -------------------------------
def clean_datetime(df):
    df['Date Of Stop'] = pd.to_datetime(df['Date Of Stop'], errors='coerce')

    df['Time Of Stop'] = df['Time Of Stop'].astype(str)
    df['Time Of Stop'] = df['Time Of Stop'].str.replace('.', ':', regex=False)

    df['Stop DateTime'] = pd.to_datetime(
        df['Date Of Stop'].dt.strftime('%Y-%m-%d') + ' ' + df['Time Of Stop'],
        errors='coerce'
    )
    return df


def clean_booleans(df):
    bool_cols = [
        'Accident', 'Belts', 'Personal Injury', 'Property Damage', 'Fatal',
        'Commercial License', 'HAZMAT', 'Commercial Vehicle', 'Alcohol', 'Work Zone'
    ]

    for col in bool_cols:
        df[col] = df[col].astype(str).str.upper().map({'YES': True, 'NO': False})

    return df


def clean_search_columns(df):
    search_cols = [
        'Search Disposition', 'Search Outcome', 'Search Reason',
        'Search Type', 'Search Arrest Reason'
    ]

    for col in search_cols:
        df[col] = df[col].fillna("Not Applicable")

    return df


def clean_duplicates(df):
    df = df.drop_duplicates(subset=['SeqID', 'Charge'])
    df['Violation Count'] = df.groupby('SeqID')['Charge'].transform('count')
    return df


def feature_engineering(df):
    def classify_violation_count(x):
        if x == 1:
            return "Single"
        elif x <= 3:
            return "Low Multiple"
        elif x <= 6:
            return "Medium Multiple"
        else:
            return "High Risk"

    df['Violation Category'] = df['Violation Count'].apply(classify_violation_count)

    df['Hour'] = pd.to_datetime(df['Stop DateTime']).dt.hour
    df['Weekday'] = pd.to_datetime(df['Stop DateTime']).dt.day_name()
    df['Month'] = pd.to_datetime(df['Stop DateTime']).dt.month_name()

    return df


def clean_make(df):
    df['Make'] = df['Make'].str.upper().str.strip()
    df['Make'] = df['Make'].replace({
        'CHEV': 'CHEVROLET',
        'CHEVY': 'CHEVROLET',
        'MERCRUY': 'MERCURY',
        'MECURY': 'MERCURY',
        'INFNITY': 'INFINITI'
    })
    return df


def clean_location(df):
    df['Location'] = df['Location'].str.replace('@', '/')
    df['Location'] = df['Location'].str.upper().str.strip()
    return df


def validate_coordinates(df):
    return df[(df['Latitude'] != 0) & (df['Longitude'] != 0)]


def optimize_types(df):
    cat_cols = ['Race','Gender','State','VehicleType','Violation Category']
    for col in cat_cols:
        df[col] = df[col].astype('category')
    return df


# -------------------------------
# Main Pipeline
# -------------------------------
def main():
    print("Loading data...")
    df = load_data()

    print("Cleaning datetime...")
    df = clean_datetime(df)

    print("Cleaning booleans...")
    df = clean_booleans(df)

    print("Cleaning search columns...")
    df = clean_search_columns(df)

    print("Removing duplicates...")
    df = clean_duplicates(df)

    print("Feature engineering...")
    df = feature_engineering(df)

    print("Cleaning Make...")
    df = clean_make(df)

    print("Cleaning Location...")
    df = clean_location(df)

    print("Validating coordinates...")
    df = validate_coordinates(df)

    print("Optimizing data types...")
    df = optimize_types(df)

    print("Saving cleaned data...")
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned_data.csv", index=False)

    print("Done ✅")


# -------------------------------
if __name__ == "__main__":
    main()


