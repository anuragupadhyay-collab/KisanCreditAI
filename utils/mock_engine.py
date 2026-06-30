"""
utils/mock_engine.py — KisanCredit AI Mock Recommendation Engine
=================================================================
Pure rule-based heuristics that produce realistic loan recommendations
from farmer input. Zero backend, zero ML, zero database.

Design contract:
  compute_recommendation(**kwargs) → dict
  All callers depend on the keys documented in Returns below.
"""

from __future__ import annotations
from typing import Any

# ── Crop lookup tables ─────────────────────────────────────────────────────────

# Base eligible loan per acre (₹) — drawn from KCC scheme norms
_CROP_LOAN_PER_ACRE: dict[str, int] = {
    "paddy":      25_000,
    "wheat":      22_000,
    "cotton":     40_000,
    "sugarcane":  55_000,
    "maize":      18_000,
    "soybean":    20_000,
    "groundnut":  30_000,
    "vegetables": 35_000,
    "pulses":     15_000,
}

# Expected net profit per acre (₹) — indicative, post input costs
_CROP_PROFIT_PER_ACRE: dict[str, int] = {
    "paddy":      18_000,
    "wheat":      16_000,
    "cotton":     32_000,
    "sugarcane":  42_000,
    "maize":      13_000,
    "soybean":    14_000,
    "groundnut":  20_000,
    "vegetables": 26_000,
    "pulses":     11_000,
}

# Intrinsic crop risk (weather sensitivity + market volatility)
_CROP_BASE_RISK: dict[str, str] = {
    "paddy":      "Medium",   # rain-dependent
    "wheat":      "Low",      # stable demand
    "cotton":     "High",     # price volatile
    "sugarcane":  "Low",      # long-cycle, FRP support
    "maize":      "Low",      # diversified use
    "soybean":    "Medium",   # global price linkage
    "groundnut":  "Medium",   # drought-sensitive
    "vegetables": "High",     # perishable, price crash risk
    "pulses":     "Low",      # MSP support
}

# State-level credit multiplier (reflects state-specific agri productivity
# and banking penetration; source: NABARD District Credit Plan heuristics)
_STATE_MULTIPLIER: dict[str, float] = {
    "Punjab":          1.20,
    "Haryana":         1.15,
    "Maharashtra":     1.10,
    "Karnataka":       1.10,
    "Tamil Nadu":      1.10,
    "Andhra Pradesh":  1.05,
    "Telangana":       1.05,
    "Gujarat":         1.05,
    "Uttar Pradesh":   1.00,
    "Kerala":          1.00,
    "West Bengal":     0.95,
    "Madhya Pradesh":  0.95,
    "Bihar":           0.90,
    "Rajasthan":       0.90,
    "Uttarakhand":     0.92,
    "Chhattisgarh":    0.88,
    "Odisha":          0.88,
}
_DEFAULT_STATE_MULT: float = 1.00

# ── Scheme catalogue ───────────────────────────────────────────────────────────

_SCHEMES: dict[str, dict[str, str]] = {
    "KCC": {
        "name":     "Kisan Credit Card (KCC)",
        "rate":     "7% p.a.  (2% Govt. interest subvention)",
        "desc":     (
            "Short-term revolving credit for crop production, post-harvest "
            "expenses, and allied activities. Backed by RBI / NABARD mandated "
            "coverage under PM-KISAN Samman Nidhi."
        ),
    },
    "AGRI_TERM": {
        "name":     "Agricultural Term Loan",
        "rate":     "9% p.a.",
        "desc":     (
            "Medium to long-term financing for agricultural equipment, "
            "land development, and irrigation infrastructure."
        ),
    },
    "NABARD_ALLIED": {
        "name":     "NABARD Allied Activities Loan",
        "rate":     "8.5% p.a.",
        "desc":     (
            "For allied agri activities including horticulture, animal "
            "husbandry, and fisheries, under NABARD refinance scheme."
        ),
    },
}

# KCC upper cap as per revised 2023 RBI circular
_KCC_LIMIT: int = 3_00_000   # ₹3,00,000

# ── Risk visual helpers ────────────────────────────────────────────────────────

_RISK_FG: dict[str, str] = {
    "Low":    "#388E3C",
    "Medium": "#F57F17",
    "High":   "#E64A19",
}
_RISK_BG: dict[str, str] = {
    "Low":    "#E8F5EC",
    "Medium": "#FFF8E1",
    "High":   "#FBE9E7",
}
_RISK_EMOJI: dict[str, str] = {
    "Low":    "🟢",
    "Medium": "🟡",
    "High":   "🔴",
}


# ── Indian numeral formatting ──────────────────────────────────────────────────

def _fmt_inr(amount: int) -> str:
    """Format integer as ₹1,20,000 (Indian numbering system)."""
    if amount <= 0:
        return "₹0"
    s = str(abs(amount))
    if len(s) <= 3:
        return f"₹{s}"
    last3 = s[-3:]
    rest = s[:-3]
    parts: list[str] = []
    while len(rest) > 2:
        parts.append(rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.append(rest)
    parts.reverse()
    return "₹" + ",".join(parts) + "," + last3


# ── Core recommendation function ───────────────────────────────────────────────

def compute_recommendation(
    crop: str,
    state: str,
    land_area: float,
    land_ownership: str = "Owned",
    requested_amount: float = 0.0,
    annual_income: float = 0.0,
) -> dict[str, Any]:
    """
    Compute a mock loan recommendation from farmer inputs.

    Parameters
    ----------
    crop            : Crop key (must exist in _CROP_LOAN_PER_ACRE)
    state           : State name (used for credit multiplier)
    land_area       : Farm size in acres  (0.5 – 500)
    land_ownership  : "Owned" | "Leased"
    requested_amount: Loan amount the farmer wants (₹), 0 means unspecified
    annual_income   : Optional annual farm income (₹)

    Returns
    -------
    dict with keys:
        status              : "eligible" | "partly_eligible" | "not_eligible"
        approved_amount     : int  (₹)
        approved_amount_fmt : str  (₹1,20,000)
        expected_profit     : int  (₹)
        expected_profit_fmt : str
        risk_level          : "Low" | "Medium" | "High"
        risk_fg             : hex colour string
        risk_bg             : hex colour string
        risk_emoji          : emoji string
        scheme_name         : str
        interest_rate       : str
        description         : str
        documents           : list[str]  (locale token keys)
        inputs_summary      : dict  (echoes key inputs for share card)
    """

    # ── Guard: unknown crop ────────────────────────────────────────────────────
    if crop not in _CROP_LOAN_PER_ACRE:
        return _error_result("Unknown crop selected")

    # ── 1. Base eligible amount ────────────────────────────────────────────────
    base_rate    = _CROP_LOAN_PER_ACRE[crop]
    state_mult   = _STATE_MULTIPLIER.get(state, _DEFAULT_STATE_MULT)
    # Leased land → bank applies a 15% haircut (no title security)
    ownership_adj = 0.85 if land_ownership == "Leased" else 1.00
    raw_eligible = base_rate * land_area * state_mult * ownership_adj
    approved     = int(min(raw_eligible, _KCC_LIMIT))

    # ── 2. Expected profit ─────────────────────────────────────────────────────
    profit_rate     = _CROP_PROFIT_PER_ACRE.get(crop, 15_000)
    expected_profit = int(profit_rate * land_area * state_mult)

    # ── 3. Risk assessment ─────────────────────────────────────────────────────
    risk = _CROP_BASE_RISK.get(crop, "Medium")
    # Leased land → one notch higher risk (no collateral security)
    if land_ownership == "Leased":
        risk = _bump_risk(risk)
    # Very small farms → higher weather sensitivity
    if land_area < 1.0 and risk == "Low":
        risk = "Medium"

    # ── 4. Eligibility verdict ─────────────────────────────────────────────────
    if land_area < 0.5:
        status   = "not_eligible"
        approved = 0
    elif requested_amount > 0 and requested_amount > approved * 1.4:
        # Farmer wants significantly more than eligible → partial
        status = "partly_eligible"
    else:
        status = "eligible"

    # ── 5. Scheme selection ────────────────────────────────────────────────────
    if approved <= 50_000:
        scheme_key = "NABARD_ALLIED"
    elif approved <= _KCC_LIMIT:
        scheme_key = "KCC"
    else:
        scheme_key = "AGRI_TERM"
    scheme = _SCHEMES[scheme_key]

    # ── 6. Document checklist tokens ──────────────────────────────────────────
    documents = ["doc_aadhaar", "doc_land", "doc_bank", "doc_photo", "doc_crop"]

    return {
        "status":               status,
        "approved_amount":      approved,
        "approved_amount_fmt":  _fmt_inr(approved),
        "expected_profit":      expected_profit,
        "expected_profit_fmt":  _fmt_inr(expected_profit),
        "risk_level":           risk,
        "risk_fg":              _RISK_FG[risk],
        "risk_bg":              _RISK_BG[risk],
        "risk_emoji":           _RISK_EMOJI[risk],
        "scheme_name":          scheme["name"],
        "interest_rate":        scheme["rate"],
        "description":          scheme["desc"],
        "documents":            documents,
        "inputs_summary": {
            "crop":           crop,
            "state":          state,
            "land_area":      land_area,
            "land_ownership": land_ownership,
        },
    }


def _bump_risk(risk: str) -> str:
    """Move risk one notch upward: Low → Medium → High."""
    return {"Low": "Medium", "Medium": "High", "High": "High"}.get(risk, risk)


def _error_result(msg: str) -> dict[str, Any]:
    return {
        "status":               "not_eligible",
        "approved_amount":      0,
        "approved_amount_fmt":  "₹0",
        "expected_profit":      0,
        "expected_profit_fmt":  "₹0",
        "risk_level":           "High",
        "risk_fg":              _RISK_FG["High"],
        "risk_bg":              _RISK_BG["High"],
        "risk_emoji":           _RISK_EMOJI["High"],
        "scheme_name":          "—",
        "interest_rate":        "—",
        "description":          msg,
        "documents":            [],
        "inputs_summary":       {},
    }
