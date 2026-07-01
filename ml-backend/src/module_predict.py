"""
=========================================================
KisanCredit AI
Module 5 - Backend Integration
=========================================================

This module integrates:

1. Price Prediction Model
2. Financial Engine
3. Risk Prediction Model
4. Recommendation Engine

=========================================================
"""

import os
import sys
import joblib
import pandas as pd

# Get the absolute path of the directory containing this file
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
# Ensure this directory is in the sys.path so modules like revenue_engine can be imported from anywhere
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

BASE_DIR = os.path.dirname(SRC_DIR)

# Temporarily change the current working directory to the BASE_DIR (ml-backend)
# to avoid FileNotFoundError when exchange_rate.py loads data/exchange_rate.csv
old_cwd = os.getcwd()
try:
    os.chdir(BASE_DIR)
    from exchange_rate import usd_to_inr
finally:
    os.chdir(old_cwd)

from revenue_engine import (
    compute_production,
    compute_revenue,
    compute_profit,
    compute_emi,
    compute_profit_margin,
    compute_debt_to_profit_ratio
)

from recommendation_engine import (
    generate_recommendation
)


# -------------------------------------------------------
# Load Models
# -------------------------------------------------------

# Resolve paths to the models and data
price_model_path = os.path.join(BASE_DIR, "models", "price_model.pkl")
risk_model_path = os.path.join(BASE_DIR, "models", "risk_model.pkl")
data_path = os.path.join(BASE_DIR, "data", "ricewheatprice.csv")

price_model = joblib.load(price_model_path)

risk_model = joblib.load(risk_model_path)


# -------------------------------------------------------
# Main Function
# -------------------------------------------------------
# -------------------------------------------------------
# Get Market Data
# -------------------------------------------------------

def get_market_data(year, month):
    """
    Fetch market data for the given year and month.
    """

    market_df = pd.read_csv(data_path)

    record = market_df[
        (market_df["Year"] == year) &
        (market_df["Month"] == month)
    ]

    if record.empty:
        raise ValueError("No market data found for the selected year and month.")

    return record.iloc[0]


def analyze_loan(
    year,
    month,
    land_area,
    yield_per_acre,
    cultivation_cost,
    loan_amount,
    interest_rate,
    tenure_months,
    crop="Wheat",
    state="Punjab",
    price_rice_ton=None,
    price_corn_ton=None,
    inflation_rate=None,
    price_rice_ton_infl=None,
    price_corn_ton_infl=None,
    price_wheat_ton_infl=None
):
    """
    Complete backend pipeline.
    """

    # Fetch market data for the given year and month if any required market variable is missing
    if (price_rice_ton is None or price_corn_ton is None or inflation_rate is None or
            price_rice_ton_infl is None or price_corn_ton_infl is None or price_wheat_ton_infl is None):
        try:
            market = get_market_data(year, month)
            if price_rice_ton is None:
                price_rice_ton = market["Price_rice_ton"]
            if price_corn_ton is None:
                price_corn_ton = market["Price_corn_ton"]
            if inflation_rate is None:
                inflation_rate = market["Inflation_rate"]
            if price_rice_ton_infl is None:
                price_rice_ton_infl = market["Price_rice_ton_infl"]
            if price_corn_ton_infl is None:
                price_corn_ton_infl = market["Price_corn_ton_infl"]
            if price_wheat_ton_infl is None:
                price_wheat_ton_infl = market["Price_wheat_ton_infl"]
        except Exception:
            # If database lookup fails (e.g. year/month not in database), fall back to sensible estimates/defaults
            if price_rice_ton is None:
                price_rice_ton = 25000.0
            if price_corn_ton is None:
                price_corn_ton = 18000.0
            if inflation_rate is None:
                inflation_rate = 5.0
            if price_rice_ton_infl is None:
                price_rice_ton_infl = price_rice_ton * (1 + inflation_rate / 100.0)
            if price_corn_ton_infl is None:
                price_corn_ton_infl = price_corn_ton * (1 + inflation_rate / 100.0)
            if price_wheat_ton_infl is None:
                price_wheat_ton_infl = price_rice_ton_infl * 0.88

    # -----------------------------
    # Price Prediction
    # -----------------------------

    price_input = pd.DataFrame({
        "Year": [year],
        "Month": [month],
        "Price_rice_ton": [price_rice_ton],
        "Price_corn_ton": [price_corn_ton],
        "Inflation_rate": [inflation_rate],
        "Price_wheat_ton_infl": [price_wheat_ton_infl],
        "Price_rice_ton_infl": [price_rice_ton_infl],
        "Price_corn_ton_infl": [price_corn_ton_infl]
    })

    print("\n===== PRICE INPUT =====")
    print(price_input)

    print("\n===== PRICE MODEL OUTPUT =====")
    print(price_model.predict(price_input))


    predicted_price_usd = float(price_model.predict(price_input)[0])

    # The machine learning model predicts prices in USD per ton.
    # To align with the financial calculation engine which operates in Indian Rupees (INR),
    # we convert the predicted USD price to INR using the historical exchange rate 
    # corresponding to the selected prediction year. If the year is not present in our 
    # database, we use the latest available exchange rate.
    predicted_price = usd_to_inr(predicted_price_usd, year)

    # -----------------------------
    # Financial Calculations
    # -----------------------------

    production = compute_production(
        land_area,
        yield_per_acre
    )

    revenue = compute_revenue(
        production,
        predicted_price
    )

    profit = compute_profit(
        revenue,
        cultivation_cost
    )

    emi = compute_emi(
        loan_amount,
        interest_rate,
        tenure_months
    )

    profit_margin = compute_profit_margin(
        profit,
        revenue
    )

    debt_ratio = compute_debt_to_profit_ratio(
        loan_amount,
        profit
    )

    # -----------------------------
    # Risk Prediction
    # -----------------------------

    risk_input = pd.DataFrame({

        "Crop": [crop],
        "State": [state],
        "Land_Area": [land_area],
        "Yield_per_Acre": [yield_per_acre],
        "Predicted_Price": [predicted_price],
        "Cultivation_Cost": [cultivation_cost],
        "Production": [production],
        "Revenue": [revenue],
        "Profit": [profit],
        "Loan_Amount": [loan_amount],
        "Interest_Rate": [interest_rate],
        "Tenure": [tenure_months],
        "EMI": [emi],
        "Profit_Margin": [profit_margin],
        "Debt_to_Profit_Ratio": [debt_ratio]

    })
    risk = risk_model.predict(risk_input)[0]

    # -----------------------------
    # Recommendation
    # -----------------------------

    recommendation = generate_recommendation(
        risk,
        profit,
        revenue,
        emi,
        loan_amount,
        profit_margin,
        debt_ratio
    )

    # -----------------------------
    # Final Output
    # -----------------------------

    result = {

        "predicted_price": round(predicted_price, 2),

        "production": round(production, 2),

        "revenue": round(revenue, 2),

        "profit": round(profit, 2),

        "emi": round(emi, 2),

        "profit_margin": round(profit_margin, 2),

        "debt_ratio": round(debt_ratio, 2),

        "risk": recommendation["risk"],

        "decision": recommendation["decision"],

        "recommended_loan": recommendation["recommended_loan"],

        "reason": recommendation["reason"],

        "advice": recommendation["advice"]

    }

    return result


def _map_keys(d):
    """
    Map keys from input_data to standard parameter names of analyze_loan.
    """
    mapping = {
        'year': 'year',
        'Year': 'year',
        'month': 'month',
        'Month': 'month',
        'land_area': 'land_area',
        'Land_Area': 'land_area',
        'land_ownership': 'land_ownership',
        'Land_Ownership': 'land_ownership',
        'yield_per_acre': 'yield_per_acre',
        'Yield_per_Acre': 'yield_per_acre',
        'cultivation_cost': 'cultivation_cost',
        'Cultivation_Cost': 'cultivation_cost',
        'loan_amount': 'loan_amount',
        'Loan_Amount': 'loan_amount',
        'interest_rate': 'interest_rate',
        'Interest_Rate': 'interest_rate',
        'tenure_months': 'tenure_months',
        'tenure': 'tenure_months',
        'Tenure': 'tenure_months',
        'Tenure_Months': 'tenure_months',
        'crop': 'crop',
        'Crop': 'crop',
        'state': 'state',
        'State': 'state',
        'price_rice_ton': 'price_rice_ton',
        'Price_rice_ton': 'price_rice_ton',
        'price_corn_ton': 'price_corn_ton',
        'Price_corn_ton': 'price_corn_ton',
        'inflation_rate': 'inflation_rate',
        'Inflation_rate': 'inflation_rate',
        'price_rice_ton_infl': 'price_rice_ton_infl',
        'Price_rice_ton_infl': 'price_rice_ton_infl',
        'price_corn_ton_infl': 'price_corn_ton_infl',
        'Price_corn_ton_infl': 'price_corn_ton_infl',
        'price_wheat_ton_infl': 'price_wheat_ton_infl',
        'Price_wheat_ton_infl': 'price_wheat_ton_infl',
    }
    mapped = {}
    for k, v in d.items():
        if k in mapping:
            mapped[mapping[k]] = v
        else:
            mapped[k] = v
    return mapped


def predict(input_data):
    """
    Public prediction API endpoint.
    Accepts input_data as a dictionary, a pandas DataFrame, or a list of dictionaries.
    Returns the prediction result(s) from the pipeline.
    """
    if isinstance(input_data, pd.DataFrame):
        records = input_data.to_dict(orient="records")
        results = [analyze_loan(**_map_keys(rec)) for rec in records]
        return results
    elif isinstance(input_data, list):
        results = [analyze_loan(**_map_keys(rec)) for rec in input_data]
        return results
    elif isinstance(input_data, dict):
        return analyze_loan(**_map_keys(input_data))
    else:
        raise TypeError("input_data must be a dictionary, list of dictionaries, or pandas DataFrame.")


# -------------------------------------------------------
# Test
# -------------------------------------------------------

if __name__ == "__main__":

    result = analyze_loan(

        year=2025,

        month="January",

        price_rice_ton=25000,

        price_corn_ton=18000,

        inflation_rate=5.2,

        price_rice_ton_infl=26250,

        price_corn_ton_infl=18900,

        land_area=5,

        yield_per_acre=2.5,

        cultivation_cost=180000,

        loan_amount=200000,

        interest_rate=9,

        tenure_months=12,

        crop="Wheat",

        state="Punjab"

    )

    print(result)