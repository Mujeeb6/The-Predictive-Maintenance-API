import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ---------------------------------------------------------
# 1. LOAD THE KAGGLE DATASET
# ---------------------------------------------------------
print("Loading the AI4I 2020 dataset...")
# Ensure your CSV file is named exactly like this, or change the string below
df = pd.read_csv('ai4i2020.csv') 

# ---------------------------------------------------------
# 2. PREPARE & CLEAN THE DATA
# ---------------------------------------------------------
print("Cleaning data and selecting features...")

# The dataset has some columns we DON'T need for predicting, like ID numbers.
# We also drop specific failure modes (TWF, HDF, etc.) to prevent "data leakage" 
# (giving the model the answer before it guesses).
# Update the columns_to_drop list to match the dataset
columns_to_drop = ['UDI', 'Product ID', 'Type', 'Machine failure', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF']

# 'X' is the data we use to predict (the sensor readings)
X = df.drop(columns=columns_to_drop)

# 'y' is the answer we are trying to guess (Did it fail? 1 = Yes, 0 = No)
y = df['Machine failure']

# Split the data: 80% to train the model, 20% to test it
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------------------------------------------------
# 3. TRAIN THE "BRAIN"
# ---------------------------------------------------------
print("Training the Random Forest model on real sensor data...")
# We use class_weight='balanced' because machine failures are rare in real life, 
# and this helps the AI pay more attention to the failures.
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# ---------------------------------------------------------
# 4. TEST THE MODEL
# ---------------------------------------------------------
print("Evaluating model performance...")
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\n--- Results ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Report (Look at how well it predicts the '1's - the failures):")
print(classification_report(y_test, predictions))

# ---------------------------------------------------------
# 5. SAVE THE MODEL FOR THE API
# ---------------------------------------------------------
joblib.dump(model, 'real_predictive_model.pkl')
print("\nSuccess! Model saved as 'real_predictive_model.pkl'. Ready for the API!")