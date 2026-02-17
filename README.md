# Predictive Property Maintenance & CRM AI Integration

An end-to-end Artificial Intelligence and automation pipeline designed to predict property infrastructure failures (e.g., HVAC, boilers) using IoT sensor data and automatically log urgent maintenance tickets into a mock CRM system.

This project demonstrates the practical application of machine learning, RESTful API development, and automated workflow integration within the PropTech and real estate sectors.

## 🚀 Features
* **Predictive Machine Learning:** Utilizes a Random Forest Classifier trained on the real-world [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset) to identify patterns of equipment failure. Handles imbalanced data natively.
* **RESTful API Deployment:** The trained ML model is served via a FastAPI web server, allowing external applications to send JSON sensor data and receive real-time failure probability scores.
* **Automated CRM Integration:** A continuous integration agent simulates live IoT data streams, queries the API, and automatically triggers SQL database inserts (ticket creation) when risk thresholds are exceeded.
* **Manual API Testing:** Fully compatible with Postman for manual endpoint verification and JSON payload testing.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Machine Learning:** `scikit-learn`, `pandas`, `numpy`, `joblib`
* **API & Web Framework:** `FastAPI`, `uvicorn`, `pydantic`
* **Database:** `SQLite`
* **Integration & Testing:** `requests`, Postman

## 🏗️ Project Architecture
1. **`train_real_model.py`**: Cleans the Kaggle dataset, drops data-leaking columns, trains the Random Forest model using balanced class weights, and exports it as `real_predictive_model.pkl`.
2. **`api.py`**: A FastAPI application that loads the `.pkl` model and exposes a POST endpoint (`/predict`) to evaluate live sensor data.
3. **`setup_db.py`**: Initializes a lightweight SQLite database (`crm.db`) to act as the backend CRM for property managers.
4. **`integration_agent.py`**: An automation script that continuously generates simulated boiler data, sends it to the API, and automatically logs an "OPEN - URGENT" ticket in the database if the AI detects a critical failure risk.

## ⚙️ Installation & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/YourUsername/Predictive-Maintenance-API.git](https://github.com/YourUsername/Predictive-Maintenance-API.git)
cd Predictive-Maintenance-API