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

import joblib
import pandas as pd

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

price_model = joblib.load("../models/price_model.pkl")

risk_model = joblib.load("../models/risk_model.pkl")


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

    market_df = pd.read_csv("../data/ricewheatprice.csv")

    record = market_df[
        (market_df["Year"] == year) &
        (market_df["Month"] == month)
    ]

    if record.empty:
        raise ValueError("No market data found for the selected year and month.")

    return record.iloc[0]
 market = get_market_data(year, month)

price_rice_ton = market["Price_rice_ton"]
price_corn_ton = market["Price_corn_ton"]
inflation_rate = market["Inflation_rate"]
price_rice_ton_infl = market["Price_rice_ton_infl"]
price_corn_ton_infl = market["Price_corn_ton_infl"]   

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
    state="Punjab"
):
    """
    Complete backend pipeline.
    """

    # -----------------------------
    # Price Prediction
    # -----------------------------

    price_input = pd.DataFrame({
        "Year": [year],
        "Month": [month],
        "Price_rice_ton": [price_rice_ton],
        "Price_corn_ton": [price_corn_ton],
        "Inflation_rate": [inflation_rate],
        "Price_rice_ton_infl": [price_rice_ton_infl],
        "Price_corn_ton_infl": [price_corn_ton_infl]
    })

    predicted_price = float(price_model.predict(price_input)[0])

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