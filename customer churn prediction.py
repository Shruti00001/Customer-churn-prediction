# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score, roc_auc_score, classification_report,
    roc_curve
)

# Step 2: Generate synthetic churn dataset
np.random.seed(42)
n_samples = 1000

df = pd.DataFrame({
    'Tenure': np.random.randint(1, 72, n_samples),
    'MonthlyCharges': np.random.uniform(20, 120, n_samples),
    'ContractType': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples),
    'InternetService': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples),
    'SupportCalls': np.random.poisson(2, n_samples),
    'PaymentMethod': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_samples),
    'Churn': np.random.choice([0, 1], n_samples, p=[0.75, 0.25])  # 25% churn rate
})

# Step 3: Preprocess data
X = df.drop('Churn', axis=1)
y = df['Churn']
X = pd.get_dummies(X, drop_first=True)

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train models
logreg = LogisticRegression(max_iter=1000)
dtree = DecisionTreeClassifier(max_depth=5, random_state=42)

logreg.fit(X_train, y_train)
dtree.fit(X_train, y_train)

# Step 6: Make predictions
y_pred_logreg = logreg.predict(X_test)
y_pred_dtree = dtree.predict(X_test)

# Step 7: Evaluation function
def evaluate_model(y_true, y_pred, model_name):
    acc = accuracy_score(y_true, y_pred)
    roc_auc = roc_auc_score(y_true, y_pred)
    print(f"{model_name} Accuracy: {acc:.3f}")
    print(f"{model_name} ROC AUC: {roc_auc:.3f}")
    print(f"{model_name} Classification Report:\n{classification_report(y_true, y_pred)}")

# Step 8: Evaluate both models
evaluate_model(y_test, y_pred_logreg, "Logistic Regression")
evaluate_model(y_test, y_pred_dtree, "Decision Tree")

# Step 9: Plot ROC curves
plt.figure(figsize=(8,6))
for model, y_pred_prob in zip(
    ['Logistic Regression', 'Decision Tree'],
    [logreg.predict_proba(X_test)[:,1], dtree.predict_proba(X_test)[:,1]]
):
    fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
    plt.plot(fpr, tpr, label=f'{model} (AUC = {roc_auc_score(y_test, y_pred_prob):.3f})')

plt.plot([0,1], [0,1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Customer Churn Prediction')
plt.legend()
plt.show()

# Step 10: Top churn drivers from Logistic Regression
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': logreg.coef_[0]
}).sort_values(by='Coefficient', key=abs, ascending=False)

print("\nTop churn drivers (Logistic Regression coefficients):")
print(feature_importance.head(10))

# Step 11: Top churn drivers from Decision Tree
dt_feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dtree.feature_importances_
}).sort_values(by='Importance', ascending=False)

print("\nTop churn drivers (Decision Tree feature importances):")
print(dt_feature_importance.head(10))
