import requests

API_URL = "https://kisancreditai.onrender.com/predict"

print("NEW MOCK ENGINE LOADED") 

def compute_recommendation(
    crop,
    state,
    land_area,
    land_ownership=None,
    requested_amount=0,
    **kwargs,
):
    print("compute_recommendation called")
    payload = {
        "year": 2025,
        "month": "January",
        "crop": crop,
        "state": state,
        "land_area": land_area,
        "yield_per_acre": 2.5,
        "cultivation_cost": 180000,
        "loan_amount": requested_amount,
        "interest_rate": 9,
        "tenure_months": 12,
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.ConnectionError:
        return {
            "error": "The backend prediction service is currently offline. Please start the backend API server and try again."
        }
    except requests.exceptions.Timeout:
        return {
            "error": "The backend request timed out. Please try again later."
        }
    except Exception as e:
        return {
            "error": f"Failed to get prediction from backend: {str(e)}"
        }

    if "error" in result:
        return result

    # Risk Mapping
    risk_map = {
        "SAFE": "Low",
        "MODERATE": "Medium",
        "RISKY": "High"
    }

    # Status Mapping
    status_map = {
        "Loan Approved": "eligible",
        "Proceed With Caution": "partly_eligible",
        "Loan Not Recommended": "not_eligible"
    }

    # Scheme
    if result["recommended_loan"] >= 50000:
        scheme = "Kisan Credit Card (KCC)"
        interest = "7% p.a."
    else:
        scheme = "NABARD Allied Activities Loan"
        interest = "8.5% p.a."

    return {
        "approved_amount": int(result["recommended_loan"]),
        "approved_amount_fmt": f"₹{int(result['recommended_loan']):,}",

        "expected_profit": int(result["profit"]),
        "expected_profit_fmt": f"₹{int(result['profit']):,}",

        "risk_level": risk_map[result["risk"]],
        "status": status_map[result["decision"]],

        "scheme_name": scheme,
        "interest_rate": interest,

        "description": (
            result["reason"] + " " + result["advice"]
        ),

        "documents": [
            "doc_aadhaar",
            "doc_land",
            "doc_bank",
            "doc_photo",
            "doc_crop",
        ]
    }