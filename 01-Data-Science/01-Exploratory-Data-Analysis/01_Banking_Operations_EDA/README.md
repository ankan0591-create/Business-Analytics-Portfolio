# Banking Operations — Exploratory Data Analysis

## Project 01 | Business Analytics Portfolio

This is the first project in a progressive Python EDA portfolio.

The objective is to explore banking operations data, clean common data-quality issues, analyse operational performance and translate the findings into simple business recommendations.

## Business Questions

- What does the dataset look like?
- Are there data-quality issues?
- Which products take the longest to process?
- Which products have more errors or SLA breaches?
- Do processing time and errors appear to be related?
- Are there unusual revenue values?

## Dataset

The dataset contains banking transaction records covering:

- Transaction ID
- Customer ID
- Product
- Region
- Processing Time
- Error Count
- SLA Breach
- Cost per Transaction
- Revenue

## Analysis Covered

1. Dataset inspection
2. Missing-value checks
3. Duplicate checks
4. Category standardisation
5. Processing-time conversion
6. Product analysis
7. Error analysis
8. SLA analysis
9. Regional analysis
10. Processing time vs. errors
11. Revenue anomaly check
12. Business findings and recommendations

## Key Findings

- Mortgage has the longest average processing time in the sample.
- Mortgage also has the highest average error count.
- SLA breaches are concentrated in the higher-processing-time products.
- Regional processing times vary, although the sample is small.
- A negative revenue transaction requires business investigation.
- The dataset contains several basic data-quality issues that need to be addressed before analysis.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Repository Structure

```text
01_Banking_Operations_EDA/
│
├── README.md
├── Banking_Operations_EDA.ipynb
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── banking_operations_raw.csv
│   └── processed/
│       └── banking_operations_clean.csv
│
├── outputs/
│   └── figures/
│
└── src/
    └── data_cleaning.py
```

## Learning Progression

This project intentionally focuses on **fundamental EDA skills**.

Later projects will progressively introduce:
- deeper statistical analysis
- more sophisticated anomaly detection
- stronger data storytelling
- more complex business questions
- more advanced modelling

The goal is to show genuine progression rather than making the first project look artificially advanced.
