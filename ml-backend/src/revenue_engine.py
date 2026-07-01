"""
=========================================================
KisanCredit AI
Module 2 - Financial Calculation Engine
=========================================================

This module calculates:

1. Crop Production
2. Revenue
3. Profit
4. Monthly EMI
5. Profit Margin
6. Debt-to-Profit Ratio

Author: Soil and Soul
=========================================================
"""

import math


# =========================================================
# 1. Production
# =========================================================
def compute_production(land_area, yield_per_acre):
    """
    Calculate total crop production.

    Formula:
        Production = Land Area × Yield per Acre
    """

    if land_area < 0 or yield_per_acre < 0:
        raise ValueError("Land area and yield must be positive.")

    return round(land_area * yield_per_acre, 2)


# =========================================================
# 2. Revenue
# =========================================================
def compute_revenue(production, predicted_price):
    """
    Calculate total revenue.

    Formula:
        Revenue = Production × Predicted Price
    """

    if production < 0 or predicted_price < 0:
        raise ValueError("Production and price must be positive.")

    return round(production * predicted_price, 2)


# =========================================================
# 3. Profit
# =========================================================
def compute_profit(revenue, cultivation_cost):
    """
    Calculate net profit.

    Formula:
        Profit = Revenue − Cultivation Cost
    """

    return round(revenue - cultivation_cost, 2)


# =========================================================
# 4. EMI Calculation
# =========================================================
def compute_emi(loan_amount, annual_interest_rate, tenure_months):
    """
    Calculate Monthly EMI.

    Parameters
    ----------
    loan_amount : float
    annual_interest_rate : float
    tenure_months : int

    Returns
    -------
    float
    """

    monthly_rate = annual_interest_rate / (12 * 100)

    if monthly_rate == 0:
        return round(loan_amount / tenure_months, 2)

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** tenure_months
    ) / (
        (1 + monthly_rate) ** tenure_months - 1
    )

    return round(emi, 2)


# =========================================================
# 5. Profit Margin
# =========================================================
def compute_profit_margin(profit, revenue):
    """
    Calculate Profit Margin.

    Formula:
        Profit Margin = Profit / Revenue
    """

    if revenue <= 0:
        return 0

    return round((profit / revenue) * 100, 2)


# =========================================================
# 6. Debt-to-Profit Ratio
# =========================================================
def compute_debt_to_profit_ratio(loan_amount, profit):
    """
    Calculate Debt-to-Profit Ratio.

    Formula:
        Loan Amount / Profit
    """

    if profit <= 0:
        return 999

    return round(loan_amount / profit, 2)

# =========================================================
# Test Module
# =========================================================
if __name__ == "__main__":

    print("=" * 55)
    print("KisanCredit AI - Financial Engine Test")
    print("=" * 55)

    # Farmer Details
    land_area = 5                # acres
    yield_per_acre = 2.5         # tons/acre

    predicted_price = 24000      # ₹ per ton

    cultivation_cost = 180000    # ₹

    loan_amount = 200000         # ₹

    annual_interest_rate = 9     # %

    tenure_months = 12

    # Calculations
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
        annual_interest_rate,
        tenure_months
    )

    margin = compute_profit_margin(
        profit,
        revenue
    )

    debt_ratio = compute_debt_to_profit_ratio(
        loan_amount,
        profit
    )

    # Output
    print(f"Land Area                : {land_area} acres")
    print(f"Yield per Acre           : {yield_per_acre} tons")

    print("-" * 55)

    print(f"Production               : {production} tons")
    print(f"Predicted Price          : ₹{predicted_price}")

    print("-" * 55)

    print(f"Revenue                  : ₹{revenue}")
    print(f"Cultivation Cost         : ₹{cultivation_cost}")
    print(f"Profit                   : ₹{profit}")

    print("-" * 55)

    print(f"Loan Amount              : ₹{loan_amount}")
    print(f"Monthly EMI              : ₹{emi}")

    print("-" * 55)

    print(f"Profit Margin            : {margin}%")
    print(f"Debt to Profit Ratio     : {debt_ratio}")

    print("=" * 55)