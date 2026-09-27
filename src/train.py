import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import os

# Define Column Names for NSL-KDD Dataset
columns = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", 
    "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", 
    "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells", 
    "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count", 
    "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", 
    "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", 
    "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", 
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate", 
    "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", 
    "attack_type", "difficulty_level"
]

print("--- Loading Dataset ---")

# Try multiple possible dataset paths
dataset_paths = [
    "data/KDDTrain+.txt",
    "data/raw/KDDTrain+.txt",
    "data/archive/nsl-kdd/KDDTrain+.txt",
    "../data/KDDTrain+.txt"
]

df = None
for path in dataset_paths:
    if os.path.exists(path):
        df = pd.read_csv(path, names=columns, header=None)
        print(f"✅ Dataset loaded from: {path}")
        break

if df is None:
    print("❌ Error: KDDTrain+.txt not found!")
    print("Please place KDDTrain+.txt in the 'data' folder.")
    exit(1)

# Convert to Binary Classification (Normal = 0, Attack = 1)
df['target'] = df['attack_type'].apply(lambda x: 0 if x == 'normal' else 1)
df.drop(['attack_type', 'difficulty_level'], axis=1, inplace=True)

# Encode Categorical Columns
categorical_cols = ['protocol_type', 'service', 'flag']
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features and Target
X = df.drop('target', axis=1)
y = df['target']

# Train-Test Split + Scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("--- Training Random Forest Model ---")
model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)

# Evaluation
y_pred = model.predict(X_test_scaled)
print(f"\n✅ Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save Model Artifacts
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(encoders, 'models/encoders.pkl')
joblib.dump(X.columns.tolist(), 'models/feature_columns.pkl')

print("✅ Training completed! Models saved in 'models/' folder.")