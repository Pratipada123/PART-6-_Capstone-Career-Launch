import pandas as pd

def preprocess_input(data: dict):
    df = pd.DataFrame([data])

    # Encode categorical features
    df["location"] = df["location"].astype("category").cat.codes
    df["property_type"] = df["property_type"].astype("category").cat.codes

    # Ensure columns are in the correct order for the model
    expected_columns = ['area', 'bedrooms', 'bathrooms', 'age', 'floor', 'location', 'property_type']
    df = df[expected_columns]

    return df
