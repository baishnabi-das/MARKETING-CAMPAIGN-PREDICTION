# 📊 Marketing Campaign Prediction using Random Forest

## 📌 Project Overview
This project focuses on predicting whether a customer will respond positively to a marketing campaign using Machine Learning. 

The model is built using the **Random Forest Classifier**, an ensemble learning algorithm that improves prediction accuracy by combining multiple decision trees.

The goal is to help businesses:
- Identify potential customers
- Improve marketing efficiency
- Reduce campaign costs
- Increase conversion rates

---

## 🎯 Problem Statement
Marketing campaigns often target a large customer base, but only a small percentage responds positively. Predicting customer responses beforehand can significantly improve ROI.

This project builds a classification model to predict:
> Will the customer respond to the marketing campaign? (Yes / No)

---

## 🧠 Machine Learning Approach

- Type: **Supervised Learning**
- Task: **Binary Classification**
- Algorithm Used: **Random Forest Classifier**

Random Forest was chosen because:
- It handles both categorical and numerical data well
- It reduces overfitting
- It provides feature importance
- It performs well on structured/tabular data

---

## 📂 Dataset Description

The dataset contains customer information such as:
- Age
- Job
- Marital Status
- Education
- Balance
- Contact Type
- Campaign details
- Previous campaign outcome
- Target variable (Response)

Target Variable:
- `1` → Customer responded positively
- `0` → Customer did not respond

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- Jupyter Notebook

---

## ⚙️ Project Workflow

1. Data Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Encoding
5. Train-Test Split
6. Model Training (Random Forest)
7. Model Evaluation
8. Feature Importance Analysis

---

### 📌 Evaluation Metrics Used

- **Accuracy** – Overall correctness of the model  
- **Precision** – How many predicted positives are actually positive  
- **Recall** – How many actual positives were correctly identified  
- **F1-Score** – Balance between Precision and Recall  

---

## 📊 Feature Importance

Random Forest provides feature importance scores which help identify which features influence predictions the most.

---

## 📈 Results

- The Random Forest model achieved strong classification performance.
- Important customer attributes influencing campaign success were identified.
- The model can help businesses target customers more effectively and improve marketing ROI.

---

## 🚀 How to Run the Project

1️⃣ Clone the repository:

```bash
git clone https://github.com/baishnabi-das/MARKETING-CAMPAIGN-PREDICTION.git
```

2️⃣ Navigate to the project folder:

```bash
cd MARKETING-CAMPAIGN-PREDICTION
```

3️⃣ Run the Jupyter Notebook.

---

## 🔮 Future Improvements

- Perform Hyperparameter Tuning (GridSearchCV / RandomizedSearchCV)
- Handle Class Imbalance using SMOTE
- Compare with other models (Logistic Regression, XGBoost)
- Deploy the model using Flask or Streamlit
- Implement Cross-Validation

---

## 🤝 Conclusion

This project demonstrates how Machine Learning can be applied to real-world marketing problems. By leveraging the Random Forest algorithm, businesses can predict customer responses and make smarter, data-driven marketing decisions.

---

## 📬 Contact

If you have suggestions or would like to collaborate, feel free to connect!
