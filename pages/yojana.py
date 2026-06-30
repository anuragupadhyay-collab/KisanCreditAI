"""
pages/yojana.py — KisanCredit AI Government Schemes (Yojana)
============================================================
Interactive, mobile-first Government Schemes directory for farmers.
Designed for 40-70 year old users: high contrast, large fonts, solid buttons.
"""
from __future__ import annotations

import streamlit as st
import urllib.parse

# ─────────────────────────────────────────────────────────────────────────────
# YOJANA-SPECIFIC CSS (FARMER-FRIENDLY: HIGH CONTRAST, LARGE TARGETS, NO FLASHY EFFECTS)
# ─────────────────────────────────────────────────────────────────────────────
_YOJANA_CSS = """
/* Filter Container Styling */
.filter-title {
  font-size: 15px;
  font-weight: 800;
  color: #047857;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Custom border wrapper override to style st.container(border=True) as a premium card */
div[data-testid="stVerticalBlockBorderWrapper"] {
  border: 2.5px solid #047857 !important;
  border-radius: 16px !important;
  background-color: #FFFFFF !important;
  padding: 20px !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.04) !important;
  margin-bottom: 16px !important;
}

/* Scheme Card: Simple, Solid, High-Contrast */
.scheme-card {
  background: #FFFFFF;
  border: 2px solid #CBD5E1;
  border-radius: 16px;
  padding: 24px 20px;
  margin-bottom: 16px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.02);
  position: relative;
  overflow: hidden;
}

.scheme-card::before {
  content: "";
  position: absolute;
  top: 0; left: 0;
  width: 6px; height: 100%;
  background: #047857;
}

.scheme-card__header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.scheme-card__icon-wrap {
  width: 52px; height: 52px;
  border-radius: 10px;
  background: #ECFDF5;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  flex-shrink: 0;
  border: 2px solid #047857;
}

.scheme-card__title-box {
  flex: 1;
}

.scheme-card__tag {
  display: inline-block;
  background: #FEF3C7;
  color: #B45309;
  font-size: 11px;
  font-weight: 800;
  padding: 4px 10px;
  border-radius: 6px;
  margin-bottom: 6px;
  border: 1px solid #FDE68A;
  text-transform: uppercase;
}

.scheme-card__title {
  font-size: 20px;
  font-weight: 800;
  color: #0F172A;
  line-height: 1.3;
}

.scheme-card__desc {
  font-size: 15px;
  color: #334155;
  line-height: 1.6;
  margin-bottom: 16px;
  font-weight: 500;
}

/* Detail blocks with clean borders */
.scheme-detail {
  background: #F8FAFC;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 12px;
  border: 1.5px solid #CBD5E1;
}

.scheme-detail__title {
  font-size: 13px;
  font-weight: 800;
  color: #475569;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
  text-transform: uppercase;
}

.scheme-detail__body {
  font-size: 14.5px;
  color: #0F172A;
  line-height: 1.5;
  font-weight: 700;
}

/* Clean Empty State */
.empty-state {
  text-align: center;
  padding: 40px 20px;
  background: #FFFFFF;
  border: 2.5px dashed #CBD5E1;
  border-radius: 16px;
  margin-bottom: 20px;
}

.empty-state__icon {
  font-size: 48px;
  margin-bottom: 12px;
  display: inline-block;
}

.empty-state__title {
  font-size: 18px;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 6px;
}

.empty-state__sub {
  font-size: 14px;
  color: #475569;
  line-height: 1.5;
  font-weight: 500;
  max-width: 280px;
  margin: 0 auto;
}

/* Large Accessible Buttons */
.scheme-btn-primary {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  height: 52px;
  background: #047857;
  color: #FFFFFF !important;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 800;
  text-decoration: none !important;
  border: 2px solid #047857;
  transition: background var(--t-fast);
}

.scheme-btn-primary:hover {
  background: #065f46;
}

.scheme-btn-icon {
  width: 52px; height: 52px;
  border-radius: 12px;
  border: 2px solid #CBD5E1;
  background: #FFFFFF;
  color: #334155;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  cursor: pointer;
  text-decoration: none !important;
  transition: all var(--t-fast);
}

.scheme-btn-icon:hover {
  border-color: #047857;
  color: #047857;
}

.scheme-btn-icon--active {
  background: #FEF3C7 !important;
  border-color: #D97706 !important;
  color: #B45309 !important;
}

/* Columns Bookmark Button styling to match height */
div[data-testid="column"] button {
  height: 52px !important;
  font-size: 20px !important;
  font-weight: 800 !important;
  border-radius: 12px !important;
  border: 2px solid #CBD5E1 !important;
  background: #FFFFFF !important;
  color: #334155 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: all var(--t-fast) !important;
}

div[data-testid="column"] button:hover {
  border-color: #D97706 !important;
  color: #B45309 !important;
  background: #FEF3C7 !important;
}

/* Bookmark filters (Accessible Toggle) */
.bookmark-filter-btn > div > button {
  background: #FFFFFF !important;
  border: 2px solid #CBD5E1 !important;
  color: #334155 !important;
  border-radius: 30px !important;
  height: 44px !important;
  font-size: 14px !important;
  font-weight: 700 !important;
  padding: 0 20px !important;
  width: auto !important;
}

.bookmark-filter-btn-active > div > button {
  background: #FEF3C7 !important;
  border: 2.5px solid #D97706 !important;
  color: #B45309 !important;
  border-radius: 30px !important;
  height: 44px !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  padding: 0 20px !important;
}

/* Streamlit Inputs for Yojana Page */
[data-testid="stSelectbox"] > label, [data-testid="stTextInput"] > label {
  display: none !important;
}
[data-testid="stSelectbox"] > div > div, [data-testid="stTextInput"] > div > div {
  border: 2px solid #CBD5E1 !important;
  border-radius: 12px !important;
  min-height: 48px !important;
  background: #FFFFFF !important;
  font-size: 15px !important;
  font-weight: 600 !important;
  margin-bottom: 12px !important;
}
[data-testid="stSelectbox"] > div > div:focus-within, [data-testid="stTextInput"] > div > div:focus-within {
  border-color: #047857 !important;
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# MOCK SCHEME DATA
# ─────────────────────────────────────────────────────────────────────────────
_SCHEMES = [
    {
        "id": "pm-kisan",
        "icon": "🚜",
        "state": "All States",
        "tags": {
            "hi": "वित्तीय सहायता",
            "mr": "वित्तीय मदत",
            "en": "Financial Help"
        },
        "name": {
            "hi": "PM-KISAN (पीएम किसान सम्मान निधि)",
            "mr": "PM-KISAN (पीएम किसान सन्मान निधी)",
            "en": "PM-KISAN Samman Nidhi"
        },
        "desc": {
            "hi": "भारत सरकार द्वारा छोटे और सीमांत किसानों को आर्थिक मदद देने की योजना।",
            "mr": "लहान व सीमांत शेतकऱ्यांना आर्थिक मदत देण्यासाठी भारत सरकारची योजना।",
            "en": "Central scheme providing income support to landholding farmer families."
        },
        "benefits": {
            "hi": "₹6,000 प्रति वर्ष (₹2,000 की 3 बराबर किश्तों में सीधे खाते में)।",
            "mr": "₹६,००० प्रति वर्ष (₹२,००० च्या ३ हप्त्यांमध्ये थेट खात्यात)।",
            "en": "₹6,000 per year in three equal installments of ₹2,000 directly to bank accounts."
        },
        "eligibility": {
            "hi": "सभी भूमिधारक किसान परिवार जिनके नाम खेती योग्य भूमि है।",
            "mr": "लागवडयोग्य जमीन असलेले सर्व भूमिधारक शेतकरी कुटुंबे।",
            "en": "All landholding farmer families holding cultivable land in their names."
        },
        "apply_url": "https://pmkisan.gov.in/"
    },
    {
        "id": "kcc-loan",
        "icon": "💳",
        "state": "All States",
        "tags": {
            "hi": "कम ब्याज लोन",
            "mr": "कमी व्याज कर्ज",
            "en": "Low Interest Loan"
        },
        "name": {
            "hi": "KCC (किसान क्रेडिट कार्ड)",
            "mr": "KCC (किसान क्रेडिट कार्ड)",
            "en": "KCC (Kisan Credit Card)"
        },
        "desc": {
            "hi": "फसल उत्पादन, फसल कटाई और कृषि रख-रखाव खर्च के लिए लचीला लोन।",
            "mr": "पीक उत्पादन, कापणी आणि शेती देखभालीसाठी सुलभ कर्ज योजना।",
            "en": "Meets financial requirements for cultivation of crops and allied activities."
        },
        "benefits": {
            "hi": "₹3 लाख तक का लोन 7% ब्याज पर (समय पर भुगतान करने पर केवल 4%)।",
            "mr": "₹३ लाखांपर्यंत कर्ज ७% व्याजाने (वेळेवर परतफेड केल्यास केवळ ४%)।",
            "en": "Loans up to ₹3 Lakh at 7% p.a. interest, reduced to 4% p.a. on prompt repayment."
        },
        "eligibility": {
            "hi": "सभी किसान, पट्टेदार, बटाईदार और स्वयं सहायता समूह (SHGs)।",
            "mr": "सर्व शेतकरी, भाडेकरू शेतकरी, भागीदार आणि बचत गट।",
            "en": "All farmers, owner-cultivators, tenant farmers, sharecroppers, and SHGs."
        },
        "apply_url": "https://www.myscheme.gov.in/schemes/kcc"
    },
    {
        "id": "pmfby-insurance",
        "icon": "🛡️",
        "state": "All States",
        "tags": {
            "hi": "फसल सुरक्षा",
            "mr": "पीक विमा",
            "en": "Crop Insurance"
        },
        "name": {
            "hi": "PMFBY (प्रधानमंत्री फसल बीमा योजना)",
            "mr": "PMFBY (पंतप्रधान पीक विमा योजना)",
            "en": "PMFBY (Fasal Bima Yojana)"
        },
        "desc": {
            "hi": "प्राकृतिक आपदाओं, कीटों और बीमारियों के कारण फसल खराब होने की स्थिति में बीमा।",
            "mr": "नैसर्गिक आपत्ती, कीड किंवा रोगांमुळे पीक नुकसानीसाठी विमा संरक्षण।",
            "en": "Comprehensive risk insurance cover against crop failure due to natural calamities."
        },
        "benefits": {
            "hi": "न्यूनतम प्रीमियम दर (खरीफ फसल के लिए 2%, रबी के लिए 1.5%) पर फसल सुरक्षा।",
            "mr": "किमान प्रीमियम (खरीप पिकासाठी २%, रब्बीसाठी १.५%) वर पीक संरक्षण।",
            "en": "Extremely low premium rate (2% for Kharif, 1.5% for Rabi crops) for full coverage."
        },
        "eligibility": {
            "hi": "अधिसूचित क्षेत्रों में अधिसूचित फसलें उगाने वाले सभी किसान।",
            "mr": "अधिसूचित भागात अधिसूचित पिके घेणारे सर्व शेतकरी।",
            "en": "All farmers cultivating notified crops in notified areas."
        },
        "apply_url": "https://pmfby.gov.in/"
    },
    {
        "id": "maha-dbt",
        "icon": "🌾",
        "state": "Maharashtra",
        "tags": {
            "hi": "राज्य सब्सिडी",
            "mr": "राज्य अनुदान",
            "en": "State Subsidy"
        },
        "name": {
            "hi": "महाडीबीटी किसान योजना (महाराष्ट्र)",
            "mr": "महाडीबीटी शेतकरी योजना (महाराष्ट्र)",
            "en": "MahaDBT Farmer Schemes (Maharashtra)"
        },
        "desc": {
            "hi": "कृषि यंत्रों, सिंचाई उपकरणों, बागवानी और बीज पर सब्सिडी प्रदान करने की एकल खिड़की।",
            "mr": "कृषी यंत्रे, सिंचन साधने, फलोत्पादन आणि बियाण्यांवर अनुदान मिळवण्याची सोपी पद्धत।",
            "en": "One-stop portal for Maharashtra state agriculture machinery and irrigation subsidies."
        },
        "benefits": {
            "hi": "ट्रैक्टर, ड्रिप इरिगेशन, स्प्रिंकलर और ग्रीनहाउस उपकरणों पर 50% से 80% तक सब्सिडी।",
            "mr": "ट्रॅक्टर, ठिबक सिंचन, तुषार सिंचन आणि हरितगृह साहित्यावर ५०% ते ८०% पर्यंत अनुदान।",
            "en": "50% to 80% direct subsidy for tractors, drip irrigation, sprinkler units, etc."
        },
        "eligibility": {
            "hi": "केवल महाराष्ट्र के पंजीकृत किसान जिनके पास आधार से जुड़ा बैंक खाता है।",
            "mr": "आधार लिंक असलेले बँक खाते असलेले महाराष्ट्रातील नोंदणीकृत शेतकरी।",
            "en": "Registered farmers of Maharashtra holding valid Aadhaar-linked bank accounts."
        },
        "apply_url": "https://mahadbt.maharashtra.gov.in/"
    },
    {
        "id": "shc-soil",
        "icon": "🧪",
        "state": "All States",
        "tags": {
            "hi": "मिट्टी की जांच",
            "mr": "माती परीक्षण",
            "en": "Soil Testing"
        },
        "name": {
            "hi": "मृदा स्वास्थ्य कार्ड (Soil Health Card)",
            "mr": "मृदा आरोग्य पत्रिका (Soil Health Card)",
            "en": "Soil Health Card Scheme"
        },
        "desc": {
            "hi": "मिट्टी की उपजाऊ क्षमता जानने और सही उर्वरक मात्रा की सलाह देने की योजना।",
            "mr": "जमिनीची सुपीकता तपासण्यासाठी आणि योग्य खतांचे प्रमाण सुचवण्यासाठी योजना।",
            "en": "Assists farmers in identifying soil health and custom nutrient requirements."
        },
        "benefits": {
            "hi": "हर 3 साल में मिट्टी की निःशुल्क जांच और पोषक तत्वों की सुधार रिपोर्ट।",
            "mr": "दर ३ वर्षांनी मोफत माती परीक्षण आणि पोषक तत्वांची सुधारणा अहवाल।",
            "en": "Free soil nutrient analysis and fertilizer dosage cards every 3 years."
        },
        "eligibility": {
            "hi": "देश के सभी खेतों के मालिक किसान।",
            "mr": "देशातील सर्व शेतीधारक शेतकरी।",
            "en": "All farm landholders across India."
        },
        "apply_url": "https://soilhealth.dac.gov.in/"
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# STATE HANDLING
# ─────────────────────────────────────────────────────────────────────────────

def _ensure_state() -> None:
    if "bookmarks" not in st.session_state:
        st.session_state.bookmarks = set()
    if "show_only_bookmarks" not in st.session_state:
        st.session_state.show_only_bookmarks = False


def _get_whatsapp_share_url(scheme_name: str, apply_url: str, lang: str) -> str:
    text = {
        "hi": f"🌾 *सरकारी योजना सूचना*\n\nयोजना का नाम: {scheme_name}\nआवेदन लिंक: {apply_url}\n\nKisanCredit AI से और योजनाएं देखें!",
        "mr": f"🌾 *सरकारी योजना माहिती*\n\nयोजनेचे नाव: {scheme_name}\nअर्ज करण्याची लिंक: {apply_url}\n\nKisanCredit AI वर अधिक योजना पहा!",
        "en": f"🌾 *Government Scheme Update*\n\nScheme Name: {scheme_name}\nApply Link: {apply_url}\n\nCheck out more on KisanCredit AI!"
    }.get(lang, f"Scheme: {scheme_name} | Apply: {apply_url}")
    return f"https://wa.me/?text={urllib.parse.quote(text)}"


# ─────────────────────────────────────────────────────────────────────────────
# RENDER YOJANA SCREEN
# ─────────────────────────────────────────────────────────────────────────────

def render_yojana() -> None:
    _ensure_state()
    st.markdown(f"<style>{_YOJANA_CSS}</style>", unsafe_allow_html=True)

    lang = st.session_state.get("lang", "hi")

    # Header Card
    welcome_title = {"hi": "सरकारी योजनाएं", "en": "Government Schemes", "mr": "सरकारी योजना"}.get(lang)
    welcome_sub = {
        "hi": "भारत सरकार और राज्यों की कृषि कल्याण योजनाएं देखें",
        "en": "Explore central and state farmer benefit schemes",
        "mr": "भारत सरकार आणि राज्य कृषी कल्याण योजना पहा"
    }.get(lang)

    st.markdown(
        f"""
        <div class="chat-welcome" style="margin-bottom: 20px;">
          <div class="chat-welcome__avatar-wrap">
            <div class="chat-welcome__avatar">📋</div>
            <div class="chat-welcome__status-dot"></div>
          </div>
          <div class="chat-welcome__title">{welcome_title}</div>
          <div class="chat-welcome__sub">{welcome_sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Search and Filters Card inside clean st.container(border=True)
    filter_title = {
        "hi": "खोजें और छानें",
        "en": "Search & Filter",
        "mr": "शोधा आणि निवडा"
    }.get(lang)

    with st.container(border=True):
        st.markdown(f'<div class="filter-title">🔍 {filter_title}</div>', unsafe_allow_html=True)

        # Search Box
        search_ph = {"hi": "योजना का नाम खोजें...", "en": "Search schemes...", "mr": "योजना शोधा..."}.get(lang)
        search_query = st.text_input("search_box", placeholder=search_ph, label_visibility="collapsed")

        # State Selector
        state_ph = {"hi": "सभी राज्य", "en": "All States", "mr": "सर्व राज्ये"}.get(lang)
        states_list = [state_ph, "Maharashtra", "Punjab", "Haryana", "Uttar Pradesh", "Gujarat", "Karnataka"]
        state_filter = st.selectbox("state_filter", states_list, label_visibility="collapsed")

        # Bookmark toggle button
        bm_text = {"hi": "⭐ केवल पसंदीदा", "en": "⭐ Bookmarked Only", "mr": "⭐ केवळ आवडत्या"}.get(lang)
        is_bm = st.session_state.show_only_bookmarks
        btn_class = "bookmark-filter-btn-active" if is_bm else "bookmark-filter-btn"

        st.markdown(f'<div class="{btn_class}">', unsafe_allow_html=True)
        if st.button(bm_text, key="bookmark_toggle_action", use_container_width=True):
            st.session_state.show_only_bookmarks = not st.session_state.show_only_bookmarks
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # 2. Filtering Logic
    filtered_schemes = []
    for sc in _SCHEMES:
        name_val = sc["name"].get(lang, sc["name"]["en"]).lower()
        desc_val = sc["desc"].get(lang, sc["desc"]["en"]).lower()
        q = search_query.lower()

        # Match query text
        if q and (q not in name_val and q not in desc_val):
            continue

        # Match state dropdown
        if state_filter != state_ph and sc["state"] != "All States" and sc["state"] != state_filter:
            continue

        # Match bookmarks filter
        if st.session_state.show_only_bookmarks and sc["id"] not in st.session_state.bookmarks:
            continue

        filtered_schemes.append(sc)

    # 3. Render Cards
    if not filtered_schemes:
        # High quality empty state card
        empty_title = {"hi": "कोई योजना नहीं मिली", "en": "No schemes found", "mr": "कोणतीही योजना सापडली नाही"}.get(lang)
        empty_sub = {
            "hi": "कृपया अलग राज्य या कोई अन्य नाम लिखकर दोबारा खोजें",
            "en": "Try adjusting your search filters or clear the bookmark switch",
            "mr": "कृपया भिन्न राज्य किंवा नाव वापरून पुन्हा शोधा"
        }.get(lang)

        st.markdown(
            f"""
            <div class="empty-state">
              <span class="empty-state__icon">🌾</span>
              <div class="empty-state__title">{empty_title}</div>
              <div class="empty-state__sub">{empty_sub}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        for sc in filtered_schemes:
            sc_id = sc["id"]
            name = sc["name"].get(lang, sc["name"]["en"])
            desc = sc["desc"].get(lang, sc["desc"]["en"])
            tag = sc["tags"].get(lang, sc["tags"]["en"])
            benefit_body = sc["benefits"].get(lang, sc["benefits"]["en"])
            elig_body = sc["eligibility"].get(lang, sc["eligibility"]["en"])
            apply_url = sc["apply_url"]

            benefit_title = {
              "hi": "मुख्य लाभ",
              "en": "Key Benefit",
              "mr": "मुख्य लाभ"
            }.get(lang)

            eligibility_title = {
              "hi": "पात्रता",
              "en": "Eligibility",
              "mr": "पात्रता"
            }.get(lang)

            is_bookmarked = sc_id in st.session_state.bookmarks
            bm_star = "★" if is_bookmarked else "☆"

            # Render styled scheme card HTML structure
            st.markdown(
                f"""
                <div class="scheme-card">
                  <div class="scheme-card__header">
                    <div class="scheme-card__icon-wrap">{sc['icon']}</div>
                    <div class="scheme-card__title-box">
                      <span class="scheme-card__tag">{tag}</span>
                      <div class="scheme-card__title">{name}</div>
                    </div>
                  </div>
                  <div class="scheme-card__desc">{desc}</div>

                  <div class="scheme-detail">
                    <div class="scheme-detail__title">
                         🎁 {benefit_title}
                    </div>
                    <div class="scheme-detail__body">
                          {benefit_body}
                    </div>
                  </div>

                  <div class="scheme-detail">
                    <div class="scheme-detail__title">
                       📋 {eligibility_title}
                    </div>
                    <div class="scheme-detail__body">
                        {elig_body}
                    </div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Columns for apply / bookmark / share buttons
            apply_lbl = {"hi": "आवेदन करें ↗", "en": "Apply Now ↗", "mr": "अर्ज करा ↗"}.get(lang)
            wa_share = _get_whatsapp_share_url(name, apply_url, lang)

            c1, c2, c3 = st.columns([3.5, 1, 1], gap="small")
            with c1:
                st.markdown(f'<a href="{apply_url}" target="_blank" class="scheme-btn-primary">{apply_lbl}</a>', unsafe_allow_html=True)
            with c2:
                if st.button(bm_star, key=f"bm_btn_{sc_id}", use_container_width=True):
                    if sc_id in st.session_state.bookmarks:
                        st.session_state.bookmarks.remove(sc_id)
                    else:
                        st.session_state.bookmarks.add(sc_id)
                    st.rerun()
            with c3:
                st.markdown(f'<a href="{wa_share}" target="_blank" class="scheme-btn-icon">📤</a>', unsafe_allow_html=True)

            st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)
