import pandas as pd


def clean_banking_operations(df):
    """Basic cleaning used in the Banking Operations EDA project."""

    df = df.copy()

    # Standardise category names
    df["Product"] = df["Product"].replace({
        "Saving": "Savings",
        "Loans": "Loan"
    })

    df["Region"] = df["Region"].replace({
        "U.K.": "UK"
    })

    # Keep missing regions visible instead of guessing
    df["Region"] = df["Region"].fillna("Unknown")

    # Convert processing time into minutes
    df["Processing_Time_Min"] = (
        df["Processing_Time"].str.extract(r"(\d+)")[0].astype(int)
    )

    # Convert SLA status into a simple 0/1 flag
    df["SLA_Breach_Flag"] = df["SLA_Breach"].map({
        "Yes": 1,
        "No": 0
    })

    # Flag unusual revenue rather than deleting it
    df["Negative_Revenue_Flag"] = df["Revenue"] < 0

    return df.drop_duplicates().copy()
