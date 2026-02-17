from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# 1. Initialize the FastAPI app
app = FastAPI(title="Property Maintenance AI API")

# 2. Load your trained "brain"
print("Loading model...")
model = joblib.load('real_predictive_model.pkl')

# 3. Define what incoming data should look like
class SensorData(BaseModel):
    air_temp: float
    process_temp: float
    rotational_speed: float
    torque: float
    tool_wear: float

# 4. Create the endpoint (The web address that receives data)
@app.post("/predict")
def predict_failure(data: SensorData):
    
    # Map the incoming JSON data to the exact column names the model expects
    input_data = {
        'Air temperature [K]': [data.air_temp],
        'Process temperature [K]': [data.process_temp],
        'Rotational speed [rpm]': [data.rotational_speed],
        'Torque [Nm]': [data.torque],
        'Tool wear [min]': [data.tool_wear]
    }
    
    # Convert to a pandas DataFrame
    df = pd.DataFrame(input_data)
    
    # Ask the model for a prediction and the probability percentage
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1] # Get probability of '1' (failure)
    
    # Return a clean JSON response
    return {
        "failure_prediction": int(prediction),
        "failure_probability_percentage": round(probability * 100, 2),
        "system_status": "CRITICAL RISK - Trigger Ticket" if prediction == 1 else "Normal Operations"
    }