"""
utils/locale.py — KisanCredit AI Translation Registry
=======================================================
Single source of truth for all UI strings.

Full translations: Hindi (hi), English (en), Marathi (mr)
Stubs (fallback to English): Punjabi (pa), Gujarati (gu),
                              Bengali (bn), Tamil (ta), Telugu (te)
"""
from __future__ import annotations

# ─────────────────────────────────────────────────────────────────────────────
# LANGUAGE METADATA
# (display_name, lang_code, flag_emoji)
# ─────────────────────────────────────────────────────────────────────────────
LANG_META: list[tuple[str, str, str]] = [
    ("हिंदी",    "hi", "🌾"),
    ("English",  "en", "🔤"),
    ("मराठी",    "mr", "🏔️"),
    ("ਪੰਜਾਬੀ",  "pa", "🌻"),
    ("ગુજરાતી", "gu", "🎋"),
    ("বাংলা",   "bn", "🌿"),
    ("தமிழ்",  "ta", "🌺"),
    ("తెలుగు", "te", "🌱"),
]

PRIMARY_LANG_CODES: list[str] = ["hi", "en", "mr"]
VALID_LANG_CODES: set[str] = {code for _, code, _ in LANG_META}

# ─────────────────────────────────────────────────────────────────────────────
# GREETINGS  (greeting_headline, greeting_subtext)
# ─────────────────────────────────────────────────────────────────────────────
_GREETINGS: dict[str, tuple[str, str]] = {
    "hi": ("नमस्ते किसान 👋",          "फसल के लिए सुरक्षित लोन सलाह लें"),
    "en": ("Namaste Kisan 👋",         "Get safe loan advice for your crop"),
    "mr": ("नमस्कार शेतकरी 👋",        "तुमच्या पिकासाठी सुरक्षित कर्ज सल्ला मिळवा"),
    "pa": ("ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਕਿਸਾਨ 👋",  "ਆਪਣੀ ਫਸਲ ਲਈ ਸੁਰੱਖਿਅਤ ਕਰਜ਼ੇ ਦੀ ਸਲਾਹ ਲਓ"),
    "gu": ("નમસ્તે ખેડૂત 👋",           "તમારા પાક માટે સુરક્ષિત લોન સલાહ"),
    "bn": ("নমস্কার কৃষক 👋",           "আপনার ফসলের জন্য নিরাপদ ঋণ পরামর্শ"),
    "ta": ("வணக்கம் விவசாயி 👋",        "உங்கள் பயிருக்கு பாதுகாப்பான கடன் ஆலோசனை"),
    "te": ("నమస్కారం రైతు 👋",          "మీ పంటకు సురక్షితమైన రుణ సలహా పొందండి"),
}

# ─────────────────────────────────────────────────────────────────────────────
# MAIN TRANSLATION TABLE
# ─────────────────────────────────────────────────────────────────────────────
_T: dict[str, dict[str, str]] = {

    # ── Hindi ─────────────────────────────────────────────────────────────────
    "hi": {
        # Hero
        "tagline":              "आपकी फसल, आपकी सुरक्षा",
        "hero_sub":             "किसान क्रेडिट कार्ड · NABARD · PM-KISAN",

        # Stats
        "stat_farmers":         "10 लाख+",
        "stat_farmers_label":   "किसान",
        "stat_loans":           "₹500 Cr+",
        "stat_loans_label":     "लोन स्वीकृत",
        "stat_states":          "17",
        "stat_states_label":    "राज्य",

        # Language section
        "choose_lang":          "अपनी भाषा चुनें",
        "more_languages":       "+ अधिक भाषाएँ",
        "fewer_languages":      "कम दिखाएं",

        # CTA card
        "cta_card_title":       "लोन सलाह लें",
        "cta_card_sub":         "फसल और जमीन देखकर सबसे सुरक्षित लोन जानें — मुफ़्त",
        "cta_btn":              "लोन जाँचें",
        "cta_badge":            "30 सेकंड में जानें",

        # Trust section
        "why_trust":            "किसान क्यों भरोसा करते हैं",
        "trust_easy_title":     "उपयोग में आसान",
        "trust_easy_body":      "बिना बैंक जाए समझें",
        "trust_free_title":     "मुफ़्त सलाह",
        "trust_free_body":      "कोई छुपा शुल्क नहीं",
        "trust_crop_title":     "फसल आधारित",
        "trust_crop_body":      "आपकी फसल के हिसाब से",
        "trust_secure_title":   "100% सुरक्षित",
        "trust_secure_body":    "डेटा पूरी तरह सुरक्षित",

        # How it works
        "how_title":            "कैसे काम करता है",
        "step1_title":          "भाषा चुनें",
        "step1_body":           "अपनी पसंदीदा भाषा में जारी रखें",
        "step2_title":          "जानकारी भरें",
        "step2_body":           "फसल, जमीन और राज्य",
        "step3_title":          "सलाह पाएं",
        "step3_body":           "तुरंत लोन रिपोर्ट देखें",

        # Footer
        "footer_tagline":       "भारत के किसानों के लिए",
        "footer_powered":       "AI द्वारा संचालित · NABARD दिशानिर्देश",
        "footer_disclaimer":    "यह केवल जानकारी के लिए है। बैंक की शर्तें लागू होंगी।",

        # Bottom nav
        "nav_home":             "होम",
        "nav_ask":              "किसान AI",
        "nav_yojana":           "योजना",

        # Farmer screen
        "farmer_screen_title":  "लोन विश्लेषक",
        "farmer_screen_body":   "अपनी फसल, जमीन और लोन जानकारी भरें और तुरंत सलाह पाएं।",

        # Ask screen
        "ask_screen_title":     "किसान AI से पूछें",
        "ask_screen_body":      "KCC लोन, ब्याज दर और दस्तावेज़ों के बारे में अपनी भाषा में जवाब पाएँ।",

        # Yojana screen
        "yojana_screen_title":  "सरकारी योजनाएँ",
        "yojana_screen_body":   "PM-KISAN, Kisan Credit Card, PMFBY और अन्य सक्रिय योजनाएँ देखें।",

        # Common
        "back":                 "वापस",
        "coming_soon":          "जल्द आ रहा है",

        # Farmer form
        "select_crop":          "फसल चुनें",
        "select_state":         "राज्य चुनें",
        "land_area":            "जमीन का क्षेत्रफल (एकड़)",
        "land_ownership":       "जमीन का प्रकार",
        "loan_amount":          "लोन राशि (₹)",
        "get_advice":           "सलाह लें",
        "doc_aadhaar":          "आधार कार्ड",
        "doc_land":             "जमीन के दस्तावेज़",
        "doc_bank":             "बैंक पासबुक",
        "doc_photo":            "पासपोर्ट फ़ोटो",
        "doc_crop":             "फसल बुआई प्रमाण",
    },

    # ── English ───────────────────────────────────────────────────────────────
    "en": {
        # Hero
        "tagline":              "Your Crop, Your Safety",
        "hero_sub":             "Kisan Credit Card · NABARD · PM-KISAN",

        # Stats
        "stat_farmers":         "10 Lakh+",
        "stat_farmers_label":   "Farmers",
        "stat_loans":           "₹500 Cr+",
        "stat_loans_label":     "Loans Approved",
        "stat_states":          "17",
        "stat_states_label":    "States",

        # Language section
        "choose_lang":          "Choose Your Language",
        "more_languages":       "+ More Languages",
        "fewer_languages":      "Show Less",

        # CTA card
        "cta_card_title":       "Get Loan Advice",
        "cta_card_sub":         "Discover the safest loan for your crop and land — free",
        "cta_btn":              "Check My Loan",
        "cta_badge":            "Know in 30 seconds",

        # Trust section
        "why_trust":            "Why Farmers Trust Us",
        "trust_easy_title":     "Easy to Use",
        "trust_easy_body":      "No bank visit needed",
        "trust_free_title":     "Free Advice",
        "trust_free_body":      "No hidden charges",
        "trust_crop_title":     "Crop Based",
        "trust_crop_body":      "Tailored to your crop",
        "trust_secure_title":   "100% Secure",
        "trust_secure_body":    "Your data is safe",

        # How it works
        "how_title":            "How It Works",
        "step1_title":          "Choose Language",
        "step1_body":           "Continue in your preferred language",
        "step2_title":          "Fill Details",
        "step2_body":           "Crop, land and state",
        "step3_title":          "Get Advice",
        "step3_body":           "See instant loan report",

        # Footer
        "footer_tagline":       "For farmers of India",
        "footer_powered":       "Powered by AI · NABARD Guidelines",
        "footer_disclaimer":    "For informational purposes only. Bank terms apply.",

        # Bottom nav
        "nav_home":             "Home",
        "nav_ask":              "Ask Kisan",
        "nav_yojana":           "Yojana",

        # Farmer screen
        "farmer_screen_title":  "Loan Analyzer",
        "farmer_screen_body":   "Fill in your crop, land and loan details to get instant advice.",

        # Ask screen
        "ask_screen_title":     "Ask Kisan AI",
        "ask_screen_body":      "Get answers on KCC loans, interest rates and required documents — in your language.",

        # Yojana screen
        "yojana_screen_title":  "Government Schemes",
        "yojana_screen_body":   "Browse PM-KISAN, Kisan Credit Card, PMFBY and other active schemes for farmers.",

        # Common
        "back":                 "Back",
        "coming_soon":          "Coming Soon",

        # Farmer form
        "select_crop":          "Select Crop",
        "select_state":         "Select State",
        "land_area":            "Land Area (acres)",
        "land_ownership":       "Land Type",
        "loan_amount":          "Loan Amount (₹)",
        "get_advice":           "Get Advice",
        "doc_aadhaar":          "Aadhaar Card",
        "doc_land":             "Land Documents",
        "doc_bank":             "Bank Passbook",
        "doc_photo":            "Passport Photo",
        "doc_crop":             "Crop Sowing Proof",
    },

    # ── Marathi ───────────────────────────────────────────────────────────────
    "mr": {
        # Hero
        "tagline":              "तुमचे पीक, तुमची सुरक्षा",
        "hero_sub":             "किसान क्रेडिट कार्ड · NABARD · PM-KISAN",

        # Stats
        "stat_farmers":         "10 लाख+",
        "stat_farmers_label":   "शेतकरी",
        "stat_loans":           "₹500 कोटी+",
        "stat_loans_label":     "कर्ज मंजूर",
        "stat_states":          "17",
        "stat_states_label":    "राज्ये",

        # Language section
        "choose_lang":          "आपली भाषा निवडा",
        "more_languages":       "+ अधिक भाषा",
        "fewer_languages":      "कमी दाखवा",

        # CTA card
        "cta_card_title":       "कर्ज सल्ला घ्या",
        "cta_card_sub":         "पीक आणि जमिनीवर आधारित सुरक्षित कर्ज जाणा — मोफत",
        "cta_btn":              "कर्ज तपासा",
        "cta_badge":            "30 सेकंदात जाणा",

        # Trust section
        "why_trust":            "शेतकरी का विश्वास ठेवतात",
        "trust_easy_title":     "वापरण्यास सोपे",
        "trust_easy_body":      "बँकेत न जाता समजा",
        "trust_free_title":     "मोफत सल्ला",
        "trust_free_body":      "कोणताही छुपा शुल्क नाही",
        "trust_crop_title":     "पीक आधारित",
        "trust_crop_body":      "तुमच्या पिकानुसार",
        "trust_secure_title":   "100% सुरक्षित",
        "trust_secure_body":    "डेटा पूर्णपणे सुरक्षित",

        # How it works
        "how_title":            "कसे काम करते",
        "step1_title":          "भाषा निवडा",
        "step1_body":           "आपल्या पसंतीच्या भाषेत पुढे जा",
        "step2_title":          "माहिती भरा",
        "step2_body":           "पीक, जमीन आणि राज्य",
        "step3_title":          "सल्ला मिळवा",
        "step3_body":           "त्वरित कर्ज अहवाल पाहा",

        # Footer
        "footer_tagline":       "भारतातील शेतकऱ्यांसाठी",
        "footer_powered":       "AI द्वारे चालित · NABARD मार्गदर्शक तत्त्वे",
        "footer_disclaimer":    "केवळ माहितीसाठी. बँकेच्या अटी लागू होतील.",

        # Bottom nav
        "nav_home":             "होम",
        "nav_ask":              "किसान AI",
        "nav_yojana":           "योजना",

        # Farmer screen
        "farmer_screen_title":  "कर्ज विश्लेषक",
        "farmer_screen_body":   "पीक, जमीन आणि कर्जाची माहिती भरा आणि त्वरित सल्ला मिळवा.",

        # Ask screen
        "ask_screen_title":     "Kisan AI ला विचारा",
        "ask_screen_body":      "KCC कर्ज, व्याज दर आणि कागदपत्रांबद्दल आपल्या भाषेत उत्तरे मिळवा.",

        # Yojana screen
        "yojana_screen_title":  "सरकारी योजना",
        "yojana_screen_body":   "PM-KISAN, KCC, PMFBY आणि इतर सक्रिय योजना पाहा.",

        # Common
        "back":                 "मागे",
        "coming_soon":          "लवकरच येत आहे",

        # Farmer form
        "select_crop":          "पीक निवडा",
        "select_state":         "राज्य निवडा",
        "land_area":            "जमिनीचे क्षेत्रफळ (एकर)",
        "land_ownership":       "जमिनीचा प्रकार",
        "loan_amount":          "कर्ज रक्कम (₹)",
        "get_advice":           "सल्ला मिळवा",
        "doc_aadhaar":          "आधार कार्ड",
        "doc_land":             "जमीन कागदपत्रे",
        "doc_bank":             "बँक पासबुक",
        "doc_photo":            "पासपोर्ट फोटो",
        "doc_crop":             "पीक पेरणी पुरावा",
    },
}

# Unsupported languages fall back to English
for _code in ("pa", "gu", "bn", "ta", "te"):
    _T[_code] = _T["en"]

# ─────────────────────────────────────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────────────────────────────────────

def t(lang: str, key: str) -> str:
    """Return translated string for lang+key. Falls back to English."""
    return _T.get(lang, _T["en"]).get(key, _T["en"].get(key, key))


def greeting_pair(lang: str) -> tuple[str, str]:
    """Return (headline, subtext) greeting for lang."""
    return _GREETINGS.get(lang, _GREETINGS["en"])


# ─────────────────────────────────────────────────────────────────────────────
# CROP DATA  (used by farmer screen)
# ─────────────────────────────────────────────────────────────────────────────
CROPS: list[dict] = [
    {"key": "paddy",      "icon": "🌿", "hi": "धान",     "en": "Paddy",      "mr": "धान"},
    {"key": "wheat",      "icon": "🌾", "hi": "गेहूँ",   "en": "Wheat",      "mr": "गहू"},
]


def crop_label(crop_key: str, lang: str) -> str:
    """Return localised crop name for a given crop key."""
    for crop in CROPS:
        if crop["key"] == crop_key:
            return crop.get(lang, crop["en"])
    return crop_key


# ─────────────────────────────────────────────────────────────────────────────
# STATES  (used by farmer screen)
# ─────────────────────────────────────────────────────────────────────────────
STATES: list[str] = [
    "Andhra Pradesh", "Bihar", "Chhattisgarh", "Gujarat",
    "Haryana", "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Odisha", "Punjab", "Rajasthan",
    "Tamil Nadu", "Telangana", "Uttar Pradesh", "Uttarakhand",
    "West Bengal",
]

# ─────────────────────────────────────────────────────────────────────────────
# BACKWARD-COMPATIBILITY ALIASES  (for any code that imported old names)
# ─────────────────────────────────────────────────────────────────────────────
LANGUAGES: dict[str, str] = {name: code for name, code, _ in LANG_META}
TRANSLATIONS: dict[str, dict[str, str]] = _T
STATES_AND_DISTRICTS: dict[str, list[str]] = {s: [] for s in STATES}
