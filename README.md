📉 Customer Churn Prediction

 🔍 Overview  
This project analyzes customer churn in a telecom company using predictive modeling. The goal is to identify key factors contributing to churn and build a model that helps the business proactively retain customers, reduce losses, and improve profitability.

---

🧠 Problem Statement  
Customer churn is a major challenge for subscription-based businesses. By predicting which customers are likely to leave, companies can take targeted actions to improve retention. This project uses synthetic telecom data to build a classification model that flags high-risk customers.

---

📊 Dataset  
- Source: Synthetic dataset simulating telecom customer behavior  
- Features: Demographics, service usage, contract type, tenure, billing, and payment method  
- Target: `Churn` (Yes/No)

---

 🛠️ Tools & Technologies  
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Jupyter Notebook

---

 🧪 Methodology  
1. Data Cleaning & Preprocessing 
   - Handled missing values  
   - Encoded categorical variables  
   - Scaled numerical features  

2. Exploratory Data Analysis (EDA)
   - Visualized churn distribution  
   - Analyzed feature correlations  
   - Identified key churn drivers

3. Modeling 
   - Logistic Regression  
   - Decision Tree Classifier  
   - Compared performance using accuracy, precision, recall, and ROC AUC

4. Interpretability 
   - Feature importance analysis  
   - ROC curve visualization  
   - Business recommendations based on model insights

---

 📈 Results  
- Achieved 85% ROC AUC with Decision Tree  
- Identified top churn indicators: contract type, tenure, monthly charges  
- Proposed retention strategies based on model outputs

---

🖼️ Visualizations  
Embed your charts here to showcase model performance and insights. Example:

```markdown
![ROC Curve](results/charts/churn_roc_curve.png)
*Figure: ROC Curve showing model performance*
```

You can also add:
- Confusion matrix  
- Feature importance bar chart  
- Churn distribution pie chart

---

 📁 Project Structure  
Customer-churn-prediction/
│
├── data/                  # Dataset files
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── scripts/               # Python scripts for cleaning and visualization
├── results/               # Charts and model outputs
│   └── charts/
│       └── churn_roc_curve.png
├── README.md              # Project overview
├── requirements.txt       # Dependencies
└── LICENSE                # License info
```

🚀 How to Run  
pip install -r requirements.txt
jupyter notebook notebooks/Customer_Churn_Analysis.ipynb
```

---

 📌 Highlights  
- Built a churn prediction pipeline from scratch  
- Delivered actionable insights for customer retention  
- Structured for easy reuse and extension

---

📬 Contact  
Shruti
📧 shruti.email@example.com  
🔗 [LinkedIn](https://www.linkedin.com/in/shruti00001)  
🔗 [GitHub](https://github.com/Shruti00001)

