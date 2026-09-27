import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib
import os

print("--- Loading TON_IoT Dataset ---")

# Change the path if your filename is different
df = pd.read_csv("D:\\College\\IOT IDS\\data\\ton\\train_test_network.csv")

print("Original shape:", df.shape)
print("Columns:", df.columns.tolist())

# ---------- 1. Create Binary Target ----------
# TON_IoT uses 'label' (0 = normal, 1 = attack)
if 'label' in df.columns:
    df['target'] = df['label']
else:
    raise ValueError("Column 'label' not found. Check your CSV.")

# ---------- 2. Drop columns that are not useful / too unique ----------
cols_to_drop = [
    'ts', 'src_ip', 'src_port', 'dst_ip', 'dst_port',
    'dns_query', 'http_uri', 'http_referrer', 'http_user_agent',
    'ssl_subject', 'ssl_issuer', 'weird_name', 'weird_addl',
    'type'          # keep only if you want multi-class later
]

# Only drop columns that actually exist
cols_to_drop = [c for c in cols_to_drop if c in df.columns]
df.drop(columns=cols_to_drop, inplace=True, errors='ignore')

# Also drop the original label column after creating target
if 'label' in df.columns:
    df.drop(columns=['label'], inplace=True)

print("Shape after dropping columns:", df.shape)

# ---------- 3. Handle categorical columns ----------
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
print("Categorical columns:", categorical_cols)

encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# ---------- 4. Features and Target ----------
X = df.drop('target', axis=1)
y = df['target']

# ---------- 5. Train / Test Split + Scaling ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("--- Training Random Forest on TON_IoT ---")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_scaled, y_train)

# ---------- 6. Evaluation ----------
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"\nTON_IoT Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ---------- 7. Save Artifacts ----------
os.makedirs("models", exist_ok=True)

joblib.dump(model, 'models/model_toniot.pkl')
joblib.dump(scaler, 'models/scaler_toniot.pkl')
joblib.dump(encoders, 'models/encoders_toniot.pkl')
joblib.dump(X.columns.tolist(), 'models/feature_columns_toniot.pkl')

print("\n--- TON_IoT artifacts saved successfully in models/ folder ---")