Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/shrut/OneDrive/Documents/music trends/customer churn prediction.py
Logistic Regression Accuracy: 0.765
Logistic Regression ROC AUC: 0.500

Warning (from warnings module):
  File "C:\Users\shrut\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 1731
    _warn_prf(average, modifier, f"{metric.capitalize()} is", result.shape[0])
UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.

Warning (from warnings module):
  File "C:\Users\shrut\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 1731
    _warn_prf(average, modifier, f"{metric.capitalize()} is", result.shape[0])
UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.

Warning (from warnings module):
  File "C:\Users\shrut\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\metrics\_classification.py", line 1731
    _warn_prf(average, modifier, f"{metric.capitalize()} is", result.shape[0])
UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
Logistic Regression Classification Report:
              precision    recall  f1-score   support

           0       0.77      1.00      0.87       153
           1       0.00      0.00      0.00        47

    accuracy                           0.77       200
   macro avg       0.38      0.50      0.43       200
weighted avg       0.59      0.77      0.66       200

Decision Tree Accuracy: 0.710
Decision Tree ROC AUC: 0.471
Decision Tree Classification Report:
              precision    recall  f1-score   support

           0       0.75      0.92      0.83       153
           1       0.08      0.02      0.03        47

    accuracy                           0.71       200
   macro avg       0.42      0.47      0.43       200
weighted avg       0.59      0.71      0.64       200

