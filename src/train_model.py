import os
import json
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

MODEL_VERSION = "v1"
SEED = 42
HIPERPARAMETERS = {"algorithm": "RandomForestRegressor", "n_estimators": 100}


df = pd.read_csv("data/processed/abalone_clean.csv")
X = df.drop(columns=['Age', 'Rings'])
y = df['Age']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ('escalado', StandardScaler()),
    ('modelo', RandomForestRegressor(n_estimators=100, random_state=42))
])

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

os.makedirs("models", exist_ok=True)
joblib.dump(pipe, "models/model_v1.pkl", compress=3)

os.makedirs("results", exist_ok=True)
metrics_data = {
    "model_version": "v1",
    "seed": 42,
    "hyperparameters": {"algorithm": "RandomForestRegressor", "n_estimators": 100},
    "metrics": {"MAE": round(mae, 4), "RMSE": round(rmse, 4), "R2": round(r2, 4)}
}

with open("results/metrics_v1.json", "w") as f:
    json.dump(metrics_data, f, indent=4)

log_file = "results/experiments_log.csv"
exp_id = "exp_01"
if os.path.exists(log_file):
    log_df = pd.read_csv(log_file,sep=',')
    if not log_df.empty:
        exp_id = log_df.iloc[-1]['experiment_id']
        exp_id = int(exp_id.split('_')[-1]) + 1
        exp_id = f"exp_{exp_id:02d}" 

log_data = pd.DataFrame([{
    "experiment_id": exp_id,
    "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "model_version": "v1",
    "hyperparameters": "RandomForest(n_estimators=100, random_state=42)",
    "metrics": f"MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.2f}"
}])

if not os.path.exists(log_file):
    log_data.to_csv(log_file, index=False,header=True)
else:
    log_data.to_csv(log_file, mode='a', header=False, index=False)

