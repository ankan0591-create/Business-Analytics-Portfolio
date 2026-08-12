# E-Commerce Customer Spending Analysis & Linear Regression

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-EDA-orange)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Linear%20Regression-green)
![Project](https://img.shields.io/badge/Project-Portfolio-purple)

## Overview

This project analyzes customer behaviour data from an e-commerce business and uses **multiple linear regression** to understand and predict **Yearly Amount Spent**.

The project was built as a practical Business Analytics learning project, with an emphasis on moving from:

**Data Quality → EDA → Relationship Analysis → Regression → Model Evaluation → Business Recommendations**

The goal is not only to build a model, but to translate analytical findings into potential business actions.

---

## Business Question

An e-commerce business wants to understand which customer behaviour variables are most closely associated with annual customer spending.

The analysis focuses on:

- Average Session Length
- Time on App
- Time on Website
- Length of Membership

The target variable is:

- **Yearly Amount Spent**

---

## Dataset

The dataset contains **500 customers and 8 columns**.

### Columns

| Column | Description |
|---|---|
| Email | Customer email identifier |
| Address | Customer address |
| Avatar | Customer avatar/color |
| Avg. Session Length | Average in-store style/advice session length |
| Time on App | Average time spent on the mobile app |
| Time on Website | Average time spent on the website |
| Length of Membership | Customer membership duration in years |
| Yearly Amount Spent | Annual customer spending |

### Source

The dataset is the public **E-Commerce Customers** dataset associated with the Kaggle exercise *Focusing on Mobile App or Website*.

Original dataset source:
https://www.kaggle.com/datasets/kolawale/focusing-on-mobile-app-or-website

---

## Analytical Approach

### Phase 1 — Data Quality

- Dataset shape and size
- Data types
- Missing-value check
- Duplicate check
- Descriptive statistics
- Target identification

### Phase 2 — Exploratory Data Analysis

- Outlier analysis using boxplots
- Pairplot
- Correlation matrix
- Jointplots
- Linear relationship visualization

### Phase 3 — Regression

- Feature/target separation
- Train/test split
- Multiple Linear Regression
- Model coefficients
- Predictions
- Actual vs predicted visualization
- MAE
- MSE
- RMSE
- Residual distribution
- Probability plot

### Phase 4 — Business Interpretation

The analytical findings are translated into potential recommendations around:

- Customer retention and loyalty
- Mobile app experience
- Website engagement

---

## Key Findings

### Correlation with Yearly Amount Spent

| Variable | Correlation |
|---|---:|
| Length of Membership | **0.81** |
| Time on App | **0.50** |
| Avg. Session Length | **0.36** |
| Time on Website | **~0.00** |

Length of Membership has the strongest observed linear association with annual spending.

Time on App has a moderate positive association.

Time on Website shows almost no linear correlation with annual spending in this dataset.

---

## Regression Results

The model was trained using:

- 70% training data
- 30% test data
- `random_state=42`

### Model coefficients

| Feature | Coefficient |
|---|---:|
| Avg. Session Length | 25.72 |
| Time on App | 38.60 |
| Time on Website | 0.46 |
| Length of Membership | 61.67 |

The coefficients represent estimated changes in annual spending while holding the other model variables constant.

**Important:** coefficient magnitude should not be treated as a definitive feature-importance ranking because the variables have different scales.

### Test-set error

| Metric | Result |
|---|---:|
| MAE | **8.43** |
| MSE | **103.92** |
| RMSE | **10.19** |

The model's MAE indicates an average absolute prediction error of approximately **8.43 spending units** on the test set.

---

## Business Recommendations

### 1. Strengthen retention and loyalty

Length of Membership has the strongest observed relationship with annual spending.

A structured loyalty and retention strategy could therefore be investigated to increase customer lifetime value.

### 2. Improve the mobile app experience

Time on App shows a meaningful positive relationship with annual spending.

Potential areas for investigation include:

- UX/UI improvements
- Personalization
- Product discovery
- Recommendations
- App engagement journeys

### 3. Treat website findings carefully

Time on Website has almost no linear correlation with annual spending.

This does **not** mean the website is unimportant. It means that **time spent on the website alone is not a useful linear predictor of annual spend in this dataset**.

Additional metrics such as conversion rate, checkout behaviour, bounce rate and customer journey data would be needed before making a major website investment decision.

---

## Important Analytical Limitation

This project demonstrates **association and prediction**, not causation.

For example, the positive relationship between Time on App and Yearly Amount Spent does not prove that increasing app usage will cause customers to spend more.

A production business decision would require additional analysis such as:

- Experimentation / A-B testing
- More customer-level behavioural data
- Cohort analysis
- Causal analysis
- Business KPI impact measurement

---

## Project Status

**Version 1 — Completed**

This version reflects the concepts covered during the current learning stage.

### Planned Regression V2

The next iteration will introduce:

- R²
- Adjusted R²
- Residuals vs predicted values
- Multicollinearity / VIF
- Statistical significance
- Confidence intervals
- Standardized coefficients
- Cross-validation
- Baseline model comparison
- Model comparison using additional algorithms

This will move the project from **basic predictive modelling** toward **more rigorous model validation and statistical analysis**.

---

## Repository Structure

```text
Ecommerce-Customer-Spending-Regression/
│
├── README.md
├── ecommerce_customer_spending_regression.ipynb
├── requirements.txt
├── .gitignore
│
├── data/
│   └── Ecommerce Customers.csv
│
└── images/
    ├── correlation_heatmap.png
    ├── membership_vs_spend.png
    ├── app_time_vs_spend.png
    ├── actual_vs_predicted.png
    └── residual_distribution.png
```

---

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Ecommerce-Customer-Spending-Regression
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch Jupyter

```bash
jupyter lab
```

Open:

```text
ecommerce_customer_spending_regression.ipynb
```

Run the notebook from top to bottom.

---

## Skills Demonstrated

**Python**

- Pandas
- NumPy
- Matplotlib
- Seaborn

**Exploratory Data Analysis**

- Data quality checks
- Descriptive statistics
- Outlier analysis
- Correlation analysis
- Relationship analysis

**Machine Learning**

- Train/test split
- Multiple Linear Regression
- Prediction
- Model error evaluation
- Residual analysis

**Business Analytics**

- Translating analytical findings into business hypotheses
- Connecting customer behaviour to spending
- Identifying areas for further business investigation
- Communicating limitations and avoiding causal overclaims

---

## Author

**Ankan**

Business Analytics / Strategy Portfolio

This project is part of an ongoing portfolio focused on developing practical capabilities across **Python, SQL, Business Analytics, Predictive Modelling, Forecasting and Data Storytelling**.
