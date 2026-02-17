import requests
import sqlite3
import time
import random

# The URL of your running FastAPI server
API_URL = "http://127.0.0.1:8000/predict"

def log_ticket_to_crm(property_id, risk_percentage):
    """Connects to the database and automatically creates a maintenance ticket."""
    conn = sqlite3.connect('crm.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO Maintenance_Tickets (Property_ID, Status, Risk_Percentage)
        VALUES (?, ?, ?)
    ''', (property_id, 'OPEN - URGENT', risk_percentage))
    
    conn.commit()
    conn.close()
    print(f"--> [CRM AUTOMATION] Ticket auto-generated for {property_id}\n")

print("Starting AI Integration Agent...")
print("Monitoring properties for maintenance risks (Press Ctrl+C to stop)\n")

# Continuous monitoring loop
while True:
    # 1. Simulate reading sensor data from a random property boiler
    property_id = f"Property_{random.randint(100, 999)}"
    
    # We generate random data, occasionally pushing numbers high to trigger a failure
    sensor_data = {
        "air_temp": random.uniform(295.0, 310.0),
        "process_temp": random.uniform(305.0, 320.0),
        "rotational_speed": random.uniform(1200.0, 2800.0),
        "torque": random.uniform(10.0, 80.0), 
        "tool_wear": random.uniform(0.0, 250.0) 
    }

    # 2. Send the data to your API
    try:
        response = requests.post(API_URL, json=sensor_data)
        result = response.json()
        
        print(f"[{property_id}] Status: {result['system_status']} | Risk: {result['failure_probability_percentage']}%")
        
        # 3. THE INTEGRATION LOGIC: If the AI predicts failure, log a ticket!
        if result['failure_prediction'] == 1:
            print(f"!!! CRITICAL ALERT !!! AI detected failure risk for {property_id}.")
            log_ticket_to_crm(property_id, result['failure_probability_percentage'])
            
    except Exception as e:
        print("Error connecting to API. Make sure your FastAPI server is running!")
        break
        
    # Wait 3 seconds before checking the next property
    time.sleep(3)