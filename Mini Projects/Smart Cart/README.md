# 🛒 ShopSmart — Online Purchase Intent Predictor

> A machine learning project that predicts whether an e-commerce session will end in a purchase — built with Decision Trees, scikit-learn Pipelines, and GridSearchCV.

---

## 📌 Problem Statement

E-commerce platforms lose millions of potential customers every day to **cart abandonment**. This project tackles that challenge by building a classifier that analyzes user session behavior and predicts whether a visitor is likely to **make a purchase** — enabling smarter, real-time interventions.

---

## 📊 Dataset

**File:** `shop_smart_ecommerce.csv`  
**Rows:** 12,330 sessions  
**Target:** `Revenue` (True = purchase made, False = no purchase)  
**Class distribution:** ~84.7% No Purchase | ~15.3% Purchase (imbalanced)

### Features

| Feature | Description |
|---|---|
| `Administrative`, `Administrative_Duration` | Admin pages visited & time spent |
| `Informational`, `Informational_Duration` | Info pages visited & time spent |
| `ProductRelated`, `ProductRelated_Duration` | Product pages visited & time spent |
| `BounceRates` | % of visitors who leave after one page |
| `ExitRates` | % of exits from a specific page |
| `PageValues` | Average value of pages visited before transaction |
| `SpecialDay` | Closeness to a special day (e.g., Valentine's Day) |
| `Month` | Month of the session |
| `OperatingSystems`, `Browser`, `Region`, `TrafficType` | Technical & traffic metadata |
| `VisitorType` | New vs returning visitor |
| `Weekend` | Whether the session was on a weekend |

---

## 🧠 Approach

### 1. Preprocessing Pipeline
- **Numerical features** → `StandardScaler`
- **Categorical features** → `OneHotEncoder` (handles unknown categories)
- Combined using `ColumnTransformer`

### 2. Model
- **Decision Tree Classifier** with:
  - `max_depth=6` — prevents overfitting
  - `min_samples_leaf=30` — smooths decision boundaries
  - `class_weight="balanced"` — handles class imbalance

### 3. Hyperparameter Tuning
- `GridSearchCV` with 5-fold cross-validation
- Scoring metric: **F1 Score** (best for imbalanced datasets)
- Search space:
  - `max_depth`: [4, 6, 8]
  - `min_samples_leaf`: [20, 30, 50]

---

## 🗂️ Project Structure

```
shop_smart/
│
├── shop_smart.ipynb            # Main notebook
├── shop_smart_ecommerce.csv    # Dataset
└── README.md                   # You are here
```

---

## ⚙️ Setup & Usage

### Prerequisites
```bash
pip install pandas numpy scikit-learn
```

### Run the Notebook
```bash
jupyter notebook shop_smart.ipynb
```

### Key Steps in the Notebook
1. Load and explore the dataset
2. Split into train/test (80/20, stratified)
3. Build preprocessing + model pipeline
4. Evaluate with F1 score, classification report & confusion matrix
5. Tune hyperparameters with GridSearchCV

---

## 📈 Evaluation Metrics

The model is evaluated using:
- **F1 Score** — primary metric (handles class imbalance)
- **Classification Report** — precision, recall, F1 per class
- **Confusion Matrix** — visualize true/false positives & negatives

> F1 is chosen over accuracy because the dataset is imbalanced (~85% non-purchase) — a model that always predicts "no purchase" would still get 85% accuracy but be completely useless.

---

## 🔮 Future Improvements

- [ ] Try ensemble models (Random Forest, XGBoost)
- [ ] Add SHAP values for feature importance & explainability
- [ ] Deploy as a REST API using FastAPI or Flask
- [ ] Build a real-time dashboard for session monitoring

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data-green?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)

---

## 👤 Author

Made with ❤️ as a minor ML project.  
Feel free to fork, star ⭐, and build on top of it!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
