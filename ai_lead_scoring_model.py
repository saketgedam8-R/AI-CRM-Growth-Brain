# 🤖 AI-CRM-Growth-Brain: Lead Scoring Model
# Author: Saket J. Gedam
# Role: AI Product Manager (Aspirant)
# Objective: Predict high-conversion leads based on lead score, industry, and response time.

# --- 1. Import Dependencies ---
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --- 2. Sample Data (Synthetic CRM Leads Dataset) ---
data = {
    'Lead_ID': range(1, 21),
    'Industry': ['Tech', 'Finance', 'Health', 'Edu', 'Tech', 'Finance', 'Retail', 'Edu', 'Health', 'Tech',
                 'Retail', 'Health', 'Edu', 'Finance', 'Tech', 'Retail', 'Health', 'Edu', 'Finance', 'Tech'],
    'Lead_Score': [72, 45, 80, 55, 90, 48, 60, 52, 78, 88, 67, 82, 70, 40, 95, 61, 77, 50, 43, 92],
    'Response_Time_Hrs': [4, 7, 2, 5, 1, 8, 6, 5, 3, 2, 6, 4, 3, 9, 1, 5, 4, 6, 7, 2],
    'Converted': [1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

# --- 3. Preprocess Data ---
df = pd.get_dummies(df, columns=['Industry'], drop_first=True)
X = df.drop(columns=['Converted', 'Lead_ID'])
y = df['Converted']

#---4. Split Data----
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#---5. Train AI Model---
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# --- 6. Evaluate Model ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("AI Lead Scoring Model Trained Successfully!")
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# --- 7. Predict Sample Lead ---
sample = pd.DataFrame({
    'Lead_Score': [85],
    'Response_Time_Hrs': [3],
    'Industry_Finance': [0],
    'Industry_Health': [0],
    'Industry_Retail': [0],
    'Industry_Tech': [1]
})
prediction = model.predict(sample)

if prediction[0] == 1:
    print("🚀 This lead has HIGH conversion potential.")
else:
    print("⚠️ This lead has LOW conversion potential.")
