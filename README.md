# 🏦 Bank Loan Prediction

A machine learning project to predict whether a bank loan application will be **approved or rejected** based on customer financial and personal information.  
The project is built using **Python**, **Scikit-learn**, and **Streamlit**, and provides an interactive web interface for real-time predictions.

---

## 📌 Project Overview

Banks receive thousands of loan applications every day.  
Manually evaluating each application is time-consuming and prone to errors.  

This project uses **Machine Learning** to automate the loan approval process by analyzing key customer attributes such as income, education, marital status, credit history, and loan amount.

---

## 🎯 Objective

- Predict loan approval status (`Approved / Not Approved`)
- Reduce manual effort in loan evaluation
- Provide a simple and interactive prediction system

---

## 🧠 Machine Learning Approach

- **Problem Type:** Binary Classification  
- **Algorithm Used:** Logistic Regression / Ensemble Model  
- **Target Variable:** `Loan_Status`

---

## 📁 Project Structure

```bash
bank-loan-prediction/
│
├── data/
│ ├── bank_data.csv
│ └── README.md
│
├── app.py
├── Bank_ensemble.ipynb
├── Flowchart_jupyter_Bank.pdf
├── README.md
└── .gitignore
```

---

## 📊 Dataset Description

The dataset contains customer demographic and financial details.

### 🔹 Features

| Feature | Description |
|-------|------------|
| Gender | Gender of the applicant |
| Married | Marital status |
| Education | Education level |
| ApplicantIncome | Applicant's income |
| LoanAmount | Loan amount requested |
| Credit_History | Credit history (1 = Good, 0 = Bad) |
| Loan_Status | Loan approval decision |

📌 **Dataset Location:** `data/bank_data.csv`

---

## ⚙️ Data Preprocessing

- Handling missing values
- Encoding categorical variables
- Feature selection
- Splitting data into training and testing sets

---

## 🌐 Streamlit Web Application

The project includes a **Streamlit-based web app** that allows users to:
- Enter customer details
- Get instant loan approval predictions
- Visualize prediction results

### ▶️ Run the App Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
### 🛠️ Technologies Used

- Python
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Matplotlib / Seaborn (for EDA)
  
---
### 📈 Results

The trained model successfully predicts loan approval outcomes with reliable accuracy and can be used as a decision-support system for banks.

---
🚀 Future Improvements

- Add advanced models (Random Forest, XGBoost)
- Improve feature engineering
- Add model performance metrics
- Deploy the application on cloud platforms

---
### 👩‍💻 Author

- Palak Sharma
- AI/ML Enthusiast
