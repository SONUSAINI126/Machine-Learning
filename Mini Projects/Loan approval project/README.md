# 🏦 Loan Approval Prediction System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

> A machine learning project that predicts whether a loan application will be **approved or rejected** based on applicant financial and demographic data.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Workflow](#workflow)
- [Technologies Used](#technologies-used)
- [Results](#results)
- [Future Improvements](#future-improvements)

---

## 📖 Overview

Banks and financial institutions receive thousands of loan applications every day. Manually evaluating each one is time-consuming and prone to human bias. This project builds an automated **Loan Approval Prediction System** using machine learning techniques to assist in making data-driven decisions.

The model analyzes key financial and personal attributes of applicants and predicts whether their loan should be **Approved** or **Rejected**.

---

## 📊 Dataset

| Property | Details |
|---|---|
| **File** | `Loan_approval_data.csv` |
| **Records** | 1,000 applicants |
| **Features** | 20 columns |
| **Target** | `Loan_Approved` (Yes / No) |

### Feature Description

| Feature | Type | Description |
|---|---|---|
| `Applicant_ID` | Numeric | Unique identifier for each applicant |
| `Applicant_Income` | Numeric | Monthly income of the applicant |
| `Coapplicant_Income` | Numeric | Monthly income of the co-applicant |
| `Employment_Status` | Categorical | Employed / Self-Employed / Unemployed |
| `Age` | Numeric | Age of the applicant |
| `Marital_Status` | Categorical | Married / Single / Divorced |
| `Dependents` | Numeric | Number of dependents |
| `Credit_Score` | Numeric | Applicant's credit score |
| `Existing_Loans` | Numeric | Number of existing active loans |
| `DTI_Ratio` | Numeric | Debt-to-Income ratio |
| `Savings` | Numeric | Total savings amount |
| `Collateral_Value` | Numeric | Value of collateral provided |
| `Loan_Amount` | Numeric | Requested loan amount |
| `Loan_Term` | Numeric | Loan term in months |
| `Loan_Purpose` | Categorical | Home / Education / Business / Personal etc. |
| `Property_Area` | Categorical | Urban / Semiurban / Rural |
| `Education_Level` | Categorical | Graduate / Not Graduate |
| `Gender` | Categorical | Male / Female |
| `Employer_Category` | Categorical | Government / Private / Self-employed |
| `Loan_Approved` | Target | **Yes** / **No** |

---

## 📁 Project Structure

```
loan-approval-system/
│
├── Loan_approval_System.ipynb   # Main Jupyter Notebook
├── Loan_approval_data.csv       # Dataset
└── README.md                    # Project documentation
```

---

## ✨ Features

- 📥 Data loading and exploration
- 🧹 Data cleaning and preprocessing
- 📊 Exploratory Data Analysis (EDA) with visualizations
- 🔧 Feature engineering
- 🤖 Machine learning model training
- 📈 Model evaluation and performance metrics
- 🔮 Loan approval prediction

---

## ⚙️ Installation

### Prerequisites

Make sure you have **Python 3.8+** installed.

### Clone the Repository

```bash
git clone https://github.com/<your-username>/mini-projects.git
cd mini-projects/loan-approval-system
```

### Install Dependencies

```bash
pip install numpy pandas seaborn matplotlib scikit-learn jupyter
```

Or install all at once:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

1. Make sure `Loan_approval_data.csv` is in the same directory as the notebook.
2. Launch Jupyter Notebook:

```bash
jupyter notebook Loan_approval_System.ipynb
```

3. Run all cells sequentially using **Cell → Run All**.

---

## 🔄 Workflow

```
Data Loading
     ↓
Exploratory Data Analysis (EDA)
     ↓
Data Cleaning & Preprocessing
     ↓
Feature Engineering
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Prediction
```

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Matplotlib / Seaborn** | Data visualization |
| **Scikit-learn** | Machine learning models |
| **Jupyter Notebook** | Interactive development environment |

---

## 📈 Results

> ⚠️ *Model training and evaluation are in progress. Results will be updated once complete.*

| Metric | Score |
|---|---|
| Accuracy | TBD |
| Precision | TBD |
| Recall | TBD |
| F1 Score | TBD |

---

## 🔮 Future Improvements

- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Try multiple models (Random Forest, XGBoost, Logistic Regression)
- [ ] Handle class imbalance with SMOTE
- [ ] Deploy as a web app using Flask or Streamlit
- [ ] Add cross-validation for more robust evaluation

---

## 👨‍💻 Author

**SONU SAINI**
- GitHub: [SONUSAINI126](https://github.com/SONUSAINI126)
- LinkedIn: [sonu-saini-here](https://linkedin.com/in/sonu-saini-here)

---

⭐ *If you found this project helpful, please give it a star!*
