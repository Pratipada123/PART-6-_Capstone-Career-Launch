import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Create dummy training data
np.random.seed(42)
n_samples = 1000
area = np.random.uniform(500, 5000, n_samples)
bedrooms = np.random.randint(1, 6, n_samples)
bathrooms = np.random.randint(1, 5, n_samples)
age = np.random.randint(0, 50, n_samples)
floor = np.random.randint(1, 20, n_samples)
location = np.random.randint(0, 4, n_samples)  # encoded
property_type = np.random.randint(0, 3, n_samples)  # encoded

# Simple price calculation: base price per sqft + adjustments
price = area * np.random.uniform(2000, 8000, n_samples) + \
        bedrooms * 50000 + \
        bathrooms * 30000 - \
        age * 1000 + \
        floor * 2000 + \
        location * 100000 + \
        property_type * 50000

# Add some noise
price += np.random.normal(0, 50000, n_samples)

# Create dataframe
import pandas as pd
df = pd.DataFrame({
    'area': area,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'age': age,
    'floor': floor,
    'location': location,
    'property_type': property_type,
    'price': price
})

# Train simple model
X = df.drop('price', axis=1)
y = df['price']

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'backend/models/production_model.pkl')
print("Model saved successfully!")