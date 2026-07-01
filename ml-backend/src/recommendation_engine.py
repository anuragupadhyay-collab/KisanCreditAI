"""
=========================================================
KisanCredit AI
Module 4 - Recommendation Engine
=========================================================

This module generates financial recommendations
based on the farmer's predicted financial status.

Author: Soil and Soul
=========================================================
"""


# =========================================================
# Calculate Safe Loan Amount
# =========================================================

def calculate_safe_loan_amount(profit, revenue):
    """
    Calculate the maximum recommended loan amount.

    Rule:
        Safe Loan = minimum(
            40% of Profit,
            25% of Revenue
        )
    """

    if profit <= 0 or revenue <= 0:
        return 0

    return round(min(0.40 * profit, 0.25 * revenue), 2)


# =========================================================
# Recommendation Generator
# =========================================================

def generate_recommendation(
    risk,
    profit,
    revenue,
    emi,
    loan_amount,
    profit_margin,
    debt_ratio
):
    """
    Generate recommendation for farmer.

    Returns:
        Dictionary containing

        - Risk
        - Decision
        - Reason
        - Recommended Loan
        - Advice
    """

    safe_loan = calculate_safe_loan_amount(
        profit,
        revenue
    )

    # ---------------- SAFE ---------------- #

    if risk == "SAFE":

        decision = "Loan Approved"

        reason = (
            "Expected profit comfortably covers "
            "loan repayment."
        )

        advice = (
            "Proceed with the loan. Financial "
            "position appears healthy."
        )

    # ---------------- MODERATE ---------------- #

    elif risk == "MODERATE":

        decision = "Proceed With Caution"

        reason = (
            "Profit is sufficient, but debt "
            "burden is relatively high."
        )

        advice = (
            "Consider reducing the requested "
            "loan amount or increasing "
            "expected production."
        )

    # ---------------- RISKY ---------------- #

    else:

        decision = "Loan Not Recommended"

        reason = (
            "Expected profit is too low to "
            "comfortably repay the loan."
        )

        advice = (
            "Reduce the loan amount, decrease "
            "cultivation cost, or improve "
            "expected yield before applying."
        )

    return {

        "risk": risk,

        "decision": decision,

        "reason": reason,

        "recommended_loan": safe_loan,

        "advice": advice

    }


# =========================================================
# Test Module
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("KisanCredit AI - Recommendation Engine")
    print("=" * 60)

    # -----------------------------------------------------

    safe_case = generate_recommendation(

        risk="SAFE",

        profit=200000,

        revenue=500000,

        emi=15000,

        loan_amount=100000,

        profit_margin=40,

        debt_ratio=0.50

    )

    print("\nSAFE CASE\n")

    for key, value in safe_case.items():
        print(f"{key} : {value}")

    # -----------------------------------------------------

    moderate_case = generate_recommendation(

        risk="MODERATE",

        profit=90000,

        revenue=300000,

        emi=18000,

        loan_amount=150000,

        profit_margin=30,

        debt_ratio=1.8

    )

    print("\n" + "=" * 60)

    print("\nMODERATE CASE\n")

    for key, value in moderate_case.items():
        print(f"{key} : {value}")

    # -----------------------------------------------------

    risky_case = generate_recommendation(

        risk="RISKY",

        profit=15000,

        revenue=100000,

        emi=22000,

        loan_amount=200000,

        profit_margin=10,

        debt_ratio=8

    )

    print("\n" + "=" * 60)

    print("\nRISKY CASE\n")

    for key, value in risky_case.items():
        print(f"{key} : {value}")

    print("\n" + "=" * 60)