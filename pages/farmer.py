"""
pages/farmer.py — KisanCredit AI · Farmer Flow
================================================
5-step loan advisory flow. Renders inside app.py's router.

Step 1: Crop selection    (3×3 emoji card grid)
Step 2: Land + State      (pills, slider, dropdown, ownership)
Step 3: Loan amount       (big display, slider, presets)
Step 4: Analysis          (animated loading, compute, auto-advance)
Step 5: Result            (recommendation card, WhatsApp share)

All navigation is session_state-driven; no Streamlit-page routing used.
"""
from __future__ import annotations

import time
import urllib.parse
import streamlit as st

from utils.locale import CROPS, STATES, crop_label, t
from utils.mock_engine import compute_recommendation

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

_CROP_ROWS: list[list[dict]] = [CROPS[0:3], CROPS[3:6], CROPS[6:9]]

_LAND_PRESETS: list[tuple[float, str]] = [
    (1.0, "1"),
    (2.0, "2"),
    (3.0, "3"),
    (5.0, "4+"),
]

_LOAN_PRESETS: list[int] = [50_000, 1_00_000, 1_50_000, 2_00_000, 3_00_000]

_RISK_PILL: dict[str, dict[str, str]] = {
    "Low":    {"hi": "🟢  सुरक्षित लोन",      "en": "🟢  Safe Loan",      "mr": "🟢  सुरक्षित कर्ज",     "cls": "safety-pill--safe"},
    "Medium": {"hi": "🟡  सोच-समझकर लें",      "en": "🟡  Take Carefully",  "mr": "🟡  विचारपूर्वक घ्या",   "cls": "safety-pill--medium"},
    "High":   {"hi": "🔴  ज़्यादा जोखिम",      "en": "🔴  Higher Risk",     "mr": "🔴  जास्त जोखीम",       "cls": "safety-pill--high"},
}

_DOC_COPY: dict[str, dict[str, str]] = {
    "doc_aadhaar": {
        "hi": "आधार कार्ड (असली + फोटोकॉपी)",
        "en": "Aadhaar Card (original + copy)",
        "mr": "आधार कार्ड (मूळ + छायाप्रत)",
    },
    "doc_land": {
        "hi": "ज़मीन के कागज़ — 7/12 उतारा",
        "en": "Land Records — 7/12 Utara",
        "mr": "जमीन नोंदी — 7/12 उतारा",
    },
    "doc_bank": {
        "hi": "बैंक पासबुक (पिछले 6 महीने)",
        "en": "Bank Passbook (last 6 months)",
        "mr": "बँक पासबुक (शेवटचे 6 महिने)",
    },
    "doc_photo": {
        "hi": "पासपोर्ट साइज़ फोटो — 2 नग",
        "en": "Passport-size Photos × 2",
        "mr": "पासपोर्ट साईज फोटो × 2",
    },
    "doc_crop": {
        "hi": "फसल बोने का प्रमाण पत्र",
        "en": "Crop Sowing Certificate",
        "mr": "पीक पेरणी प्रमाणपत्र",
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# FARMER-SPECIFIC CSS  (injected at render time)
# ─────────────────────────────────────────────────────────────────────────────

_FARMER_CSS = """
/* ── Farmer Flow Custom Styling ── */
div[data-testid="stVerticalBlock"] > div[data-testid="element-container"]:first-child button {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  color: var(--c-green) !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  height: 40px !important;
  min-height: 0 !important;
  padding: 0 4px 0 16px !important;
  width: auto !important;
  text-align: left !important;
  transition: opacity 0.2s;
}
div[data-testid="stVerticalBlock"] > div[data-testid="element-container"]:first-child button:hover {
  opacity: 0.7;
}

/* Step Header */
.step-header {
  background: linear-gradient(160deg, var(--c-green-xdk) 0%, var(--c-green-dk) 50%, var(--c-green) 100%);
  padding: 28px 24px 32px;
  position: relative;
  overflow: hidden;
  border-bottom-left-radius: var(--r-xl);
  border-bottom-right-radius: var(--r-xl);
  box-shadow: var(--sh-md);
  margin-bottom: var(--sp-4);
}
.step-header::before {
  content: "";
  position: absolute;
  width: 180px; height: 180px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
  top: -60px; right: -40px;
  pointer-events: none;
}
.step-header__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
  position: relative;
  z-index: 1;
}
.step-header__badge {
  background: rgba(255, 255, 255, 0.18);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  padding: 4px 14px;
  border-radius: var(--r-pill);
  letter-spacing: 0.5px;
  border: 1px solid rgba(255, 255, 255, 0.25);
}
.step-header__dots {
  display: flex;
  gap: 6px;
}
.step-dot {
  height: 4px;
  border-radius: var(--r-pill);
  background: rgba(255, 255, 255, 0.25);
  min-width: 32px;
  transition: all var(--t-base) var(--ease);
}
.step-dot--done {
  background: rgba(255, 255, 255, 0.6);
}
.step-dot--active {
  background: #fff;
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.6);
}
.step-header__title {
  color: #fff;
  font-size: 24px;
  font-weight: 800;
  line-height: 1.2;
  margin-top: 12px;
  text-shadow: 0 2px 10px rgba(0,0,0,0.1);
  letter-spacing: -0.5px;
}
.step-header__sub {
  color: rgba(255, 255, 255, 0.85);
  font-size: 13px;
  line-height: 1.4;
  font-weight: 500;
  margin-top: 6px;
}

/* Input Cards */
.input-card {
  background: var(--c-surface);
  border: 1.5px solid var(--c-border);
  border-radius: var(--r-xl);
  padding: var(--sp-5);
  box-shadow: var(--sh-sm);
  margin-bottom: var(--sp-4);
  transition: border-color var(--t-fast);
}
.input-card:focus-within {
  border-color: var(--c-border-strong);
}
.input-card__title {
  font-size: 15px;
  font-weight: 800;
  color: var(--c-text-1);
  margin-bottom: var(--sp-3);
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Streamlit Widget Styling Overrides */
[data-testid="stBaseButton-secondary"] {
  background: var(--c-card) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border: 1.5px solid var(--c-border) !important;
  color: var(--c-text-2) !important;
  border-radius: var(--r-md) !important;
  height: 54px !important;
  font-size: 15px !important;
  font-weight: 700 !important;
  transition: all var(--t-fast) var(--ease-spring) !important;
  box-shadow: var(--sh-xs) !important;
}
[data-testid="stBaseButton-secondary"]:hover {
  border-color: var(--c-green) !important;
  background: var(--c-surface) !important;
  color: var(--c-green-dk) !important;
  transform: translateY(-2px) !important;
  box-shadow: var(--sh-sm) !important;
}
[data-testid="stBaseButton-secondary"]:active {
  transform: scale(0.97) !important;
}
[data-testid="stBaseButton-primary"] {
  background: linear-gradient(135deg, var(--c-green-dk) 0%, var(--c-green) 50%, var(--c-green-md) 100%) !important;
  color: #fff !important;
  border: none !important;
  border-radius: var(--r-md) !important;
  height: 56px !important;
  font-size: 17px !important;
  font-weight: 800 !important;
  letter-spacing: 0.3px !important;
  box-shadow: var(--sh-green) !important;
  transition: all var(--t-fast) var(--ease) !important;
}
[data-testid="stBaseButton-primary"]:hover {
  transform: translateY(-2px) scale(1.01) !important;
  box-shadow: var(--sh-green-lg) !important;
}
[data-testid="stBaseButton-primary"]:active {
  transform: scale(0.98) !important;
}

/* Crop Grid Button Adjustments */
div[data-testid="stHorizontalBlock"] > div [data-testid="stBaseButton-secondary"] {
  height: 90px !important;
  border-radius: var(--r-lg) !important;
}
div[data-testid="stHorizontalBlock"] > div [data-testid="stBaseButton-primary"] {
  height: 90px !important;
  border-radius: var(--r-lg) !important;
  background: var(--c-surface) !important;
  color: var(--c-green-dk) !important;
  border: 2.5px solid var(--c-green) !important;
  box-shadow: var(--sh-green) !important;
}

/* Slider and Selectbox styling */
[data-testid="stSlider"] > label {
  display: none !important;
}
[data-testid="stSlider"] > div > div > div > div {
  background: var(--c-green) !important;
}
[data-testid="stThumbValue"] {
  color: var(--c-green) !important;
  font-weight: 800 !important;
  font-size: 16px !important;
}
[data-testid="stSelectbox"] > label {
  display: none !important;
}
[data-testid="stSelectbox"] > div > div {
  border: 1.5px solid var(--c-border) !important;
  border-radius: var(--r-md) !important;
  min-height: 54px !important;
  background: var(--c-surface) !important;
  font-size: 15px !important;
  font-weight: 600 !important;
  box-shadow: var(--sh-xs) !important;
  padding-left: 12px !important;
}
[data-testid="stSelectbox"] > div > div:focus-within {
  border-color: var(--c-green) !important;
  box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.15) !important;
}

/* Custom Displays */
.loan-display {
  text-align: center;
  padding: var(--sp-4) 0;
}
.loan-display__amount {
  font-size: 52px;
  font-weight: 900;
  color: var(--c-green);
  line-height: 1.1;
  letter-spacing: -1.5px;
  text-shadow: 0 2px 8px rgba(5,150,105,0.08);
}
.loan-display__hint {
  font-size: 12px;
  color: var(--c-text-off);
  margin-top: 6px;
  font-weight: 600;
}

.validation-msg {
  background: #FEF2F2;
  border: 1.5px solid #FCA5A5;
  border-radius: var(--r-md);
  padding: 12px 16px;
  font-size: 14px;
  color: #DC2626;
  font-weight: 700;
  margin-bottom: var(--sp-4);
  box-shadow: 0 4px 12px rgba(220,38,38,0.06);
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Loading Screen */
.loading-screen {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  padding: var(--sp-8) var(--sp-5);
  text-align: center;
  gap: var(--sp-4);
}
.loading-screen__icon {
  font-size: 72px;
  line-height: 1;
  animation: float 4s ease-in-out infinite;
}

/* Result Screen */
.result-card {
  border-radius: var(--r-xl);
  overflow: hidden;
  box-shadow: var(--sh-lg);
  margin-bottom: var(--sp-4);
  border: 1.5px solid var(--c-border);
}
.result-card__header {
  background: linear-gradient(135deg, var(--c-green-xdk) 0%, var(--c-green-dk) 50%, var(--c-green) 100%);
  padding: 32px 24px;
  text-align: center;
  position: relative;
}
.result-card__header--partial {
  background: linear-gradient(135deg, var(--c-amber) 0%, var(--c-gold) 100%);
}
.result-card__header--rejected {
  background: linear-gradient(135deg, #BE123C 0%, #E11D48 100%);
}
.result-card__label {
  color: rgba(255,255,255,0.75);
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: var(--sp-2);
}
.result-card__amount {
  color: #fff;
  font-size: 52px;
  font-weight: 900;
  line-height: 1.1;
  letter-spacing: -1.5px;
  margin-bottom: var(--sp-3);
  text-shadow: 0 4px 16px rgba(0,0,0,0.15);
}
.result-card__scheme {
  display: inline-block;
  background: rgba(255,255,255,0.18);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: #fff;
  font-size: 13px;
  font-weight: 700;
  padding: 6px 18px;
  border-radius: var(--r-pill);
  border: 1px solid rgba(255,255,255,0.25);
}

.safety-row {
  padding: 12px 0;
}
.safety-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 18px;
  border-radius: var(--r-pill);
  font-size: 13px;
  font-weight: 800;
  box-shadow: var(--sh-xs);
}
.safety-pill--safe {
  background: var(--c-green-lt);
  color: var(--c-green-dk);
  border: 1px solid rgba(5,150,105,0.2);
}
.safety-pill--medium {
  background: var(--c-gold-lt);
  color: var(--c-gold-dk);
  border: 1px solid rgba(245,158,11,0.2);
}
.safety-pill--high {
  background: #FEF2F2;
  color: #DC2626;
  border: 1px solid rgba(220,38,38,0.2);
}

.result-explain {
  background: var(--c-card);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border-left: 4px solid var(--c-green);
  border-radius: 0 var(--r-md) var(--r-md) 0;
  padding: 16px var(--sp-5);
  font-size: 14px;
  color: var(--c-text-2);
  line-height: 1.5;
  margin: var(--sp-2) 0 var(--sp-4);
  font-weight: 500;
  box-shadow: var(--sh-xs);
}

.docs-card {
  background: var(--c-surface);
  border: 1.5px solid var(--c-border);
  border-radius: var(--r-xl);
  padding: 20px;
  margin-bottom: var(--sp-5);
  box-shadow: var(--sh-sm);
}
.docs-card__hdr {
  font-size: 15px;
  font-weight: 800;
  color: var(--c-text-1);
  margin-bottom: var(--sp-3);
}
.doc-row {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
  color: var(--c-text-2);
  padding: 10px 0;
  border-bottom: 1px solid var(--c-border);
  font-weight: 500;
}
.doc-row:last-of-type {
  border-bottom: none;
}
.doc-row__check {
  color: var(--c-green);
  font-weight: 900;
  font-size: 14px;
}
.docs-note {
  font-size: 11px;
  color: var(--c-text-off);
  margin-top: 12px;
  font-style: italic;
  font-weight: 600;
}

.btn-wa {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  height: 56px;
  background: linear-gradient(135deg, #10B981 0%, #059669 100%);
  color: #fff !important;
  border-radius: var(--r-md);
  font-size: 16px;
  font-weight: 800;
  text-decoration: none !important;
  box-shadow: var(--sh-green);
  transition: all var(--t-fast) var(--ease);
  margin-bottom: 12px;
}
.btn-wa:hover {
  transform: translateY(-2px);
  box-shadow: var(--sh-green-lg);
}
.btn-outline-row {
  display: flex;
  gap: 12px;
}
.btn-outline {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  height: 50px;
  background: var(--c-surface);
  color: var(--c-green) !important;
  border: 1.5px solid var(--c-green);
  border-radius: var(--r-md);
  font-size: 14px;
  font-weight: 800;
  text-decoration: none !important;
  transition: all var(--t-fast) var(--ease);
  box-shadow: var(--sh-xs);
}
.btn-outline:hover {
  background: var(--c-green-lt);
  transform: translateY(-2px);
}
.step-gap {
  height: 12px;
}
.content-pad {
  padding: 0 4px;
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def _fmt_inr(n: int) -> str:
    if n <= 0:
        return "₹0"
    s = str(abs(n))
    if len(s) <= 3:
        return f"₹{s}"
    last3 = s[-3:]
    rest   = s[:-3]
    parts: list[str] = []
    while len(rest) > 2:
        parts.append(rest[-2:])
        rest = rest[:-2]
    if rest:
        parts.append(rest)
    parts.reverse()
    return "₹" + ",".join(parts) + "," + last3


def _short_inr(n: int) -> str:
    if n >= 1_00_000:
        lakh = n / 1_00_000
        return f"₹{int(lakh)}L" if lakh == int(lakh) else f"₹{lakh:.1f}L"
    if n >= 1_000:
        return f"₹{n // 1_000}K"
    return f"₹{n}"


def _tx(lang: str, d: dict[str, str]) -> str:
    return d.get(lang, d.get("en", next(iter(d.values()))))


def _whatsapp_url(result: dict, lang: str, crop_name: str, land_area: float) -> str:
    tmpl = {
        "hi": (
            f"🌾 *KisanCredit AI की सलाह*\n\n"
            f"फसल: {crop_name}\n"
            f"जमीन: {land_area} एकड़\n"
            f"सुझाया लोन: *{result['approved_amount_fmt']}*\n"
            f"योजना: {result['scheme_name']}\n\n"
            f"अपनी सलाह लें → https://kisancredit.ai"
        ),
        "mr": (
            f"🌾 *KisanCredit AI चा सल्ला*\n\n"
            f"पीक: {crop_name}\n"
            f"जमीन: {land_area} एकर\n"
            f"सुचवलेले: *{result['approved_amount_fmt']}*\n"
            f"योजना: {result['scheme_name']}\n\n"
            f"तुमचा सल्ला → https://kisancredit.ai"
        ),
        "en": (
            f"🌾 *KisanCredit AI Advice*\n\n"
            f"Crop: {crop_name}\n"
            f"Land: {land_area} acres\n"
            f"Recommended: *{result['approved_amount_fmt']}*\n"
            f"Scheme: {result['scheme_name']}\n\n"
            f"Get your advice → https://kisancredit.ai"
        ),
    }
    body = tmpl.get(lang, tmpl["en"])
    return f"https://wa.me/?text={urllib.parse.quote(body)}"


def _plain_result(result: dict, lang: str, crop_key: str, land_area: float) -> str:
    name      = crop_label(crop_key, lang)
    amount    = result["approved_amount_fmt"]
    requested = _fmt_inr(int(st.session_state.get("loan_amount", 0)))
    status    = result.get("status", "eligible")

    if status == "eligible":
        return {
            "hi": f"आपकी {land_area} एकड़ {name} की फसल के लिए <strong>{amount}</strong> का लोन सुरक्षित है। फसल बेचने के बाद आप इसे आसानी से वापस कर सकते हैं।",
            "mr": f"तुमच्या {land_area} एकर {name} पिकासाठी <strong>{amount}</strong> चे कर्ज सुरक्षित आहे। पीक विकल्यानंतर तुम्ही ते सहज परत करू शकता।",
            "en": f"A loan of <strong>{amount}</strong> is safe for your {land_area}-acre {name} crop. You can comfortably repay after the harvest.",
        }.get(lang, f"Loan of <strong>{amount}</strong> is safe for {land_area} acres of {name}.")

    if status == "partly_eligible":
        return {
            "hi": f"आपने {requested} माँगा है, लेकिन आपकी {land_area} एकड़ {name} की फसल के लिए <strong>{amount}</strong> ज़्यादा सुरक्षित रहेगा।",
            "mr": f"तुम्ही {requested} मागितले, परंतु {land_area} एकर {name} साठी <strong>{amount}</strong> अधिक सुरक्षित आहे।",
            "en": f"You requested {requested}, but <strong>{amount}</strong> is safer for your {land_area}-acre {name} crop.",
        }.get(lang, f"<strong>{amount}</strong> is safer than {requested} for {land_area} acres.")

    return {
        "hi": "0.5 एकड़ से कम जमीन पर KCC लोन नहीं मिलता। अधिक जानकारी के लिए Kisan AI से पूछें।",
        "mr": "0.5 एकरपेक्षा कमी जमिनीवर KCC कर्ज मिळत नाही। Kisan AI ला विचारा।",
        "en": "KCC loans are not available for farms under 0.5 acres. Ask Kisan AI to learn more.",
    }.get(lang, "Not eligible for KCC at this land size.")


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────

def _ensure_state() -> None:
    defaults: dict = {
        "farmer_step":      1,
        "crop":             None,
        "land_area":        2.0,
        "land_ownership":   "Owned",
        "state":            None,
        "loan_amount":      1_00_000,
        "result":           None,
        "show_val_err":     False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# STEP HEADER
# ─────────────────────────────────────────────────────────────────────────────

def _step_header(lang: str, step: int, title: str, subtitle: str, total: int = 3) -> None:
    badge = {"hi": f"चरण {step} / {total}", "en": f"Step {step} of {total}", "mr": f"पाऊल {step} / {total}"}.get(lang, f"Step {step}/{total}")

    dots = ""
    for i in range(1, total + 1):
        if   i < step:  dots += '<div class="step-dot step-dot--done"></div>'
        elif i == step: dots += '<div class="step-dot step-dot--active"></div>'
        else:           dots += '<div class="step-dot"></div>'

    st.markdown(
        f"""
        <div class="step-header">
          <div class="step-header__meta">
            <div class="step-header__dots">{dots}</div>
            <span class="step-header__badge">{badge}</span>
          </div>
          <div class="step-header__title">{title}</div>
          <div class="step-header__sub">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _back_btn(lang: str, target_step: int) -> bool:
    label = {"hi": "← वापस", "en": "← Back", "mr": "← मागे"}.get(lang, "← Back")
    return st.button(label, key=f"back_to_{target_step}")


# ─────────────────────────────────────────────────────────────────────────────
# STEP 1 — CROP SELECTION
# ─────────────────────────────────────────────────────────────────────────────

def _step_crop(lang: str) -> None:
    title = {"hi": "आपकी फसल कौन सी है?",    "en": "Which is your crop?",        "mr": "तुमचे पीक कोणते आहे?"}.get(lang, "Select your crop")
    sub   = {"hi": "नीचे से अपनी फसल चुनें", "en": "Tap your crop below",         "mr": "खाली तुमचे पीक निवडा"}.get(lang, "Tap a crop below")
    _step_header(lang, 1, title, sub)

    st.markdown('<div class="step-gap"></div>', unsafe_allow_html=True)

    selected = st.session_state.get("crop")

    # Render Crop Cards in 3x3 Grid
    for row_idx, row in enumerate(_CROP_ROWS):
        cols = st.columns(3, gap="small")
        for col, crop_data in zip(cols, row):
            with col:
                key  = crop_data["key"]
                icon = crop_data["icon"]
                name = crop_data.get(lang, crop_data["en"])
                active = selected == key
                lbl  = f"{'✓ ' if active else ''}{icon}\n{name}"
                if st.button(
                    lbl,
                    key=f"crop_{key}",
                    use_container_width=True,
                    type="primary" if active else "secondary",
                ):
                    st.session_state.crop         = key
                    st.session_state.farmer_step  = 2
                    st.session_state.show_val_err = False
                    st.rerun()

    st.markdown('<div class="step-gap"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2 — LAND + STATE + OWNERSHIP
# ─────────────────────────────────────────────────────────────────────────────

def _step_land(lang: str) -> None:
    title = {"hi": "आपकी जमीन के बारे में",     "en": "Tell us about your land",  "mr": "जमिनीबद्दल सांगा"}.get(lang, "About your land")
    sub   = {"hi": "जमीन का आकार और राज्य चुनें", "en": "Select land size and state", "mr": "जमिनीचा आकार व राज्य निवडा"}.get(lang, "Select size and state")

    if _back_btn(lang, 1):
        st.session_state.farmer_step = 1
        st.rerun()

    _step_header(lang, 2, title, sub)

    land      = float(st.session_state.get("land_area", 2.0))
    ownership = st.session_state.get("land_ownership", "Owned")
    acres_lbl = {"hi": "एकड़", "en": "acres", "mr": "एकर"}.get(lang, "acres")

    # 1. Land Area Card
    st.markdown(
        f"""
        <div class="input-card">
          <div class="input-card__title">
            <span>📐</span> {t(lang, 'land_area')}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    pill_cols = st.columns(4, gap="small")
    for col, (val, disp) in zip(pill_cols, _LAND_PRESETS):
        with col:
            active = abs(land - val) < 0.05
            if st.button(
                f"{disp}\n{acres_lbl}",
                key=f"land_pill_{val}",
                use_container_width=True,
                type="primary" if active else "secondary",
            ):
                st.session_state.land_area = val
                st.rerun()

    fine_hint = {"hi": "या खिसकाकर दर्ज करें", "en": "Or slide for exact amount", "mr": "किंवा सरकवून दर्ज करा"}.get(lang, "Or drag to fine-tune")
    st.markdown(f'<span style="font-size:11px;color:var(--c-text-off);padding-left:4px;font-weight:600;">{fine_hint}</span>', unsafe_allow_html=True)

    new_land = st.slider(
        "land_slider_fine",
        min_value=0.5,
        max_value=20.0,
        value=land,
        step=0.5,
        key="land_fine",
        label_visibility="collapsed",
        format="%.1f",
    )
    if abs(new_land - land) > 0.01:
        st.session_state.land_area = new_land
        st.rerun()

    st.markdown(
        f'<p style="text-align:center;font-size:22px;font-weight:800;color:var(--c-green);margin:2px 0 16px;">'
        f'{new_land:.1f} {acres_lbl}</p>',
        unsafe_allow_html=True,
    )

    # 2. State Selection Card
    state_ph = {"hi": "→ राज्य चुनें", "en": "→ Select your state", "mr": "→ राज्य निवडा"}.get(lang, "Select state")
    st.markdown(
        f"""
        <div class="input-card">
          <div class="input-card__title">
            <span>📍</span> {t(lang, 'select_state')}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cur_state = st.session_state.get("state")
    options   = [state_ph] + STATES
    cur_idx   = (STATES.index(cur_state) + 1) if cur_state in STATES else 0
    chosen    = st.selectbox("state_sel", options, index=cur_idx, label_visibility="collapsed", key="state_box")
    st.session_state.state = chosen if chosen != state_ph else None

    # 3. Land Ownership Card
    st.markdown(
        f"""
        <div class="input-card" style="margin-top: 12px;">
          <div class="input-card__title">
            <span>🏡</span> {t(lang, 'land_ownership')}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    own_opts = [
        ("Owned",  {"hi": "🏡  अपनी जमीन",   "en": "🏡  My Land",     "mr": "🏡  स्वतःची"}.get(lang, "🏡 Owned")),
        ("Leased", {"hi": "🤝  किराए की",    "en": "🤝  Rented Land",  "mr": "🤝  भाड्याची"}.get(lang, "🤝 Rented")),
    ]
    own_cols = st.columns(2, gap="small")
    for col, (val, lbl) in zip(own_cols, own_opts):
        with col:
            if st.button(
                lbl,
                key=f"own_{val}",
                use_container_width=True,
                type="primary" if ownership == val else "secondary",
            ):
                st.session_state.land_ownership = val
                st.rerun()

    st.markdown('<div class="step-gap"></div>', unsafe_allow_html=True)

    # Validation Error Banner
    if st.session_state.get("show_val_err"):
        v_msg = {"hi": "⚠️  पहले अपना राज्य चुनें", "en": "⚠️  Please select your state first", "mr": "⚠️  आधी राज्य निवडा"}.get(lang, "⚠️ Select state")
        st.markdown(f'<div class="validation-msg"><span>⚠️</span> {v_msg}</div>', unsafe_allow_html=True)

    # Submit Button
    cont_lbl = {"hi": "आगे बढ़ें  →", "en": "Continue  →", "mr": "पुढे जा  →"}.get(lang, "Continue →")
    if st.button(cont_lbl, key="to_step3", use_container_width=True, type="primary"):
        if not st.session_state.get("state"):
            st.session_state.show_val_err = True
            st.rerun()
        else:
            st.session_state.show_val_err = False
            st.session_state.farmer_step  = 3
            st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# STEP 3 — LOAN AMOUNT
# ─────────────────────────────────────────────────────────────────────────────

def _step_loan(lang: str) -> None:
    title = {"hi": "आप कितना लोन चाहते हैं?",    "en": "How much loan do you need?",   "mr": "तुम्हाला किती कर्ज हवे?"}.get(lang, "Loan amount")
    sub   = {"hi": "खिसकाकर या नीचे से जल्दी चुनें", "en": "Slide or pick a quick amount", "mr": "सरकवा किंवा झटपट निवडा"}.get(lang, "Slide or pick")

    if _back_btn(lang, 2):
        st.session_state.farmer_step = 2
        st.rerun()

    _step_header(lang, 3, title, sub)

    loan = int(st.session_state.get("loan_amount", 1_00_000))

    # 1. Large Input Card for Display
    st.markdown(
        f"""
        <div class="input-card">
          <div class="input-card__title">
            <span>💰</span> {t(lang, 'loan_amount')}
          </div>
          <div class="loan-display">
            <div class="loan-display__amount">{_fmt_inr(loan)}</div>
            <div class="loan-display__hint">
              {"खिसकाकर राशि बदलें" if lang == "hi" else "Drag slider to change"}
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Slider
    new_loan = st.slider(
        "loan_range",
        min_value=10_000,
        max_value=3_00_000,
        value=loan,
        step=5_000,
        key="loan_slider",
        label_visibility="collapsed",
        format="₹%d",
    )
    if new_loan != loan:
        st.session_state.loan_amount = new_loan
        st.rerun()

    # Preset Options Row
    quick_lbl = {"hi": "या जल्दी चुनें", "en": "Or Quick pick", "mr": "झटपट निवडा"}.get(lang, "Quick pick")
    st.markdown(f'<span class="flow-label content-pad">{quick_lbl}</span>', unsafe_allow_html=True)

    preset_cols = st.columns(len(_LOAN_PRESETS), gap="small")
    for col, pval in zip(preset_cols, _LOAN_PRESETS):
        with col:
            active = abs(loan - pval) < 100
            if st.button(
                _short_inr(pval),
                key=f"preset_{pval}",
                use_container_width=True,
                type="primary" if active else "secondary",
            ):
                st.session_state.loan_amount = pval
                st.rerun()

    # Info banner
    info = {"hi": "ℹ️  KCC लोन की अधिकतम सीमा <strong>₹3 लाख</strong> है।", "en": "ℹ️  KCC loan maximum limit is <strong>₹3 lakh</strong>.", "mr": "ℹ️  KCC कर्जाची कमाल मर्यादा <strong>₹3 लाख</strong> आहे."}.get(lang, "Max KCC limit is ₹3L")
    st.markdown(f'<div class="loan-info-banner">{info}</div>', unsafe_allow_html=True)

    st.markdown('<div class="step-gap"></div>', unsafe_allow_html=True)

    # Submit
    cta = {"hi": "🌟  मेरी सलाह दिखाएं", "en": "🌟  Show My Advice", "mr": "🌟  माझा सल्ला दाखवा"}.get(lang, "🌟 Show Advice")
    if st.button(cta, key="get_advice", use_container_width=True, type="primary"):
        st.session_state.farmer_step = 4
        st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# STEP 4 — ANALYSIS / LOADING
# ─────────────────────────────────────────────────────────────────────────────

def _step_loading(lang: str) -> None:
    loading_title = {
        "hi": "आपकी सलाह तैयार हो रही है...",
        "en": "Preparing your advice...",
        "mr": "तुमचा सल्ला तयार होत आहे...",
    }.get(lang, "Preparing...")

    loading_sub = {
        "hi": "आपकी फसल और जमीन देखकर<br>सबसे सुरक्षित लोन ढूंढ रहे हैं",
        "en": "Analyzing your crop and land<br>to find the safest loan",
        "mr": "तुमचे पीक व जमीन पाहून<br>सुरक्षित कर्ज शोधत आहोत",
    }.get(lang, "Analyzing...")

    slot = st.empty()
    slot.markdown(
        f"""
        <div class="loading-screen">
          <div class="loading-screen__icon">🌾</div>
          <div class="loading-bar"><div class="loading-bar__fill"></div></div>
          <div class="loading-screen__title">{loading_title}</div>
          <div class="loading-screen__sub">{loading_sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    time.sleep(1.2)

    result = compute_recommendation(
        crop            = st.session_state.get("crop") or "wheat",
        state           = st.session_state.get("state") or "Maharashtra",
        land_area       = float(st.session_state.get("land_area", 2.0)),
        land_ownership  = st.session_state.get("land_ownership", "Owned"),
        requested_amount= float(st.session_state.get("loan_amount", 1_00_000)),
    )

    slot.empty()
    st.session_state.result      = result
    st.session_state.farmer_step = 5
    st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# STEP 5 — RESULT
# ─────────────────────────────────────────────────────────────────────────────

def _step_result(lang: str) -> None:
    result = st.session_state.get("result")
    if not result:
        st.session_state.farmer_step = 1
        st.rerun()
        return

    crop_key  = st.session_state.get("crop", "wheat")
    land_area = float(st.session_state.get("land_area", 2.0))
    status    = result.get("status", "eligible")
    risk      = result.get("risk_level", "Medium")

    advice_title = {
        "eligible":        {"hi": "✅  आपकी लोन सलाह", "en": "✅  Your Loan Advice",   "mr": "✅  तुमचा कर्ज सल्ला"},
        "partly_eligible": {"hi": "⚠️  आपकी लोन सलाह", "en": "⚠️  Your Loan Advice",   "mr": "⚠️  तुमचा कर्ज सल्ला"},
        "not_eligible":    {"hi": "❌  लोन सलाह",       "en": "❌  Loan Advice",         "mr": "❌  कर्ज सल्ला"},
    }.get(status, {"hi": "आपकी सलाह", "en": "Your Advice", "mr": "तुमचा सल्ला"})

    if _back_btn(lang, 3):
        st.session_state.farmer_step = 3
        st.rerun()

    _step_header(lang, 3, _tx(lang, advice_title), "", total=3)
    st.markdown('<div class="step-gap"></div>', unsafe_allow_html=True)

    # 1. Result Header Card
    hdr_cls = {
        "eligible":        "result-card__header",
        "partly_eligible": "result-card__header result-card__header--partial",
        "not_eligible":    "result-card__header result-card__header--rejected",
    }.get(status, "result-card__header")

    rec_label  = {"hi": "हमारी सलाह", "en": "Our Recommendation", "mr": "आमचा सल्ला"}.get(lang, "Recommendation")
    amount_txt = result.get("approved_amount_fmt", "₹0")
    scheme_txt = result.get("scheme_name", "KCC")

    st.markdown(
        f"""
        <div class="result-card">
          <div class="{hdr_cls}">
            <div class="result-card__label">{rec_label}</div>
            <div class="result-card__amount">{amount_txt}</div>
            <div class="result-card__scheme">{scheme_txt}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Safety Indicator
    pill_info = _RISK_PILL.get(risk, _RISK_PILL["Medium"])
    pill_text = _tx(lang, {k: v for k, v in pill_info.items() if k != "cls"})
    pill_cls  = pill_info["cls"]
    st.markdown(
        f'<div class="safety-row"><span class="safety-pill {pill_cls}">{pill_text}</span></div>',
        unsafe_allow_html=True,
    )

    # Plain text explanation
    explain_cls = {
        "eligible":        "result-explain",
        "partly_eligible": "result-explain result-explain--partial",
        "not_eligible":    "result-explain result-explain--rejected",
    }.get(status, "result-explain")
    explanation = _plain_result(result, lang, crop_key, land_area)
    st.markdown(f'<div class="{explain_cls}">{explanation}</div>', unsafe_allow_html=True)

    # Document Checklist Card
    docs_hdr  = {"hi": "📋  बैंक में ये कागज़ लेकर जाएं", "en": "📋  Take these to the bank", "mr": "📋  बँकेत ही कागदपत्रे न्या"}.get(lang, "📋 Documents")
    docs_note = {"hi": "📌 हर कागज़ की एक फोटोकॉपी साथ रखें।", "en": "📌 Keep one photocopy of each.", "mr": "📌 प्रत्येकाची एक छायाप्रत ठेवा."}.get(lang, "Keep photocopies.")

    docs_rows = ""
    for doc_key in result.get("documents", []):
        doc_text = _DOC_COPY.get(doc_key, {}).get(lang, _DOC_COPY.get(doc_key, {}).get("en", doc_key))
        docs_rows += f'<div class="doc-row"><span class="doc-row__check">✓</span><span>{doc_text}</span></div>'

    st.markdown(
        f"""
        <div class="docs-card">
          <div class="docs-card__hdr">{docs_hdr}</div>
          {docs_rows}
          <div class="docs-note">{docs_note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Actions Row
    crop_name  = crop_label(crop_key, lang)
    wa_url     = _whatsapp_url(result, lang, crop_name, land_area)
    yojana_url = f"?screen=yojana&lang={lang}&all_langs=0"
    share_lbl  = {"hi": "📤  WhatsApp पर भेजें",  "en": "📤  Share on WhatsApp", "mr": "📤  WhatsApp वर पाठवा"}.get(lang, "📤 Share")
    retry_lbl  = {"hi": "🔄  दोबारा जाँचें",       "en": "🔄  Check Again",       "mr": "🔄  पुन्हा तपासा"}.get(lang, "🔄 Retry")
    yojana_lbl = {"hi": "🏛️  योजना देखें",        "en": "🏛️  Govt Schemes",      "mr": "🏛️  योजना पाहा"}.get(lang, "🏛️ Yojana")

    st.markdown(f'<a href="{wa_url}" target="_blank" class="btn-wa">{share_lbl}</a>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="small")
    with c1:
        if st.button(retry_lbl, key="retry_btn", use_container_width=True):
            st.session_state.farmer_step = 1
            st.session_state.crop        = None
            st.session_state.result      = None
            st.rerun()
    with c2:
        st.markdown(f'<a href="{yojana_url}" target="_self" class="btn-outline">{yojana_lbl}</a>', unsafe_allow_html=True)

    st.markdown('<div class="step-gap"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY POINT  (called from app.py router)
# ─────────────────────────────────────────────────────────────────────────────

def render_farmer() -> None:
    _ensure_state()
    st.markdown(f"<style>{_FARMER_CSS}</style>", unsafe_allow_html=True)

    lang = st.session_state.get("lang", "hi")
    step = st.session_state.get("farmer_step", 1)

    if   step == 1: _step_crop(lang)
    elif step == 2: _step_land(lang)
    elif step == 3: _step_loan(lang)
    elif step == 4: _step_loading(lang)
    elif step == 5: _step_result(lang)
    else:           _step_crop(lang)
