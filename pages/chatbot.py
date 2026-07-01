"""
pages/chatbot.py — KisanCredit AI Chatbot (Kisan AI)
=====================================================
Interactive, production-grade chatbot interface for farmer queries.
Designed for 40-70 year old farmers: high contrast, simple layout.
"""
from __future__ import annotations

import time
import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# CHATBOT-SPECIFIC CSS (FARMER-FRIENDLY & COMPACT)
# ─────────────────────────────────────────────────────────────────────────────
_CHATBOT_CSS = """
/* Profile Header Card */
.chat-welcome {
  background: #FFFFFF;
  border: 2px solid #047857;
  border-radius: 16px;
  padding: 16px 20px;
  margin-bottom: 16px;
  text-align: center;
  box-shadow: 0 4px 10px rgba(0,0,0,0.03);
}

.chat-welcome__avatar-wrap {
  position: relative;
  display: inline-block;
  margin-bottom: 8px;
}

.chat-welcome__avatar {
  width: 56px; height: 56px;
  border-radius: 50%;
  background: #ECFDF5;
  border: 2px solid #047857;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
}

.chat-welcome__status-dot {
  position: absolute;
  bottom: 2px; right: 2px;
  width: 12px; height: 12px;
  background: #10B981;
  border: 2px solid #FFFFFF;
  border-radius: 50%;
}

.chat-welcome__title {
  font-size: 19px;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 2px;
}

.chat-welcome__sub {
  font-size: 13.5px;
  color: #475569;
  line-height: 1.4;
  font-weight: 600;
}

/* Chat bubble styling with proper spacing */
.chat-bubble-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 12px;
  max-width: 85%;
  animation: fadeInUp 0.3s ease both;
}

.chat-bubble-group--user {
  align-self: flex-end;
  align-items: flex-end;
  margin-left: auto;
}

.chat-bubble-group--bot {
  align-self: flex-start;
  align-items: flex-start;
  margin-right: auto;
}

.chat-avatar {
  font-size: 11px;
  font-weight: 700;
  color: #64748B;
  margin-bottom: 2px;
  padding: 0 6px;
  display: block;
}

.chat-bubble {
  padding: 12px 16px;
  border-radius: 14px;
  font-size: 14.5px;
  line-height: 1.5;
  font-weight: 600;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  word-wrap: break-word;
}

.chat-bubble--user {
  background: #047857;
  color: #FFFFFF;
  border-bottom-right-radius: 4px;
  border: 1.5px solid #047857;
}

.chat-bubble--bot {
  background: #FFFFFF;
  color: #0F172A;
  border-bottom-left-radius: 4px;
  border: 1.5px solid #CBD5E1;
}

/* Typing Simulator dots */
.typing-dots {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 6px;
}

.typing-dot {
  width: 7px; height: 7px;
  background: #047857;
  border-radius: 50%;
  animation: bounce-dot 1.4s infinite both;
}

.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes bounce-dot {
  0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
  40% { transform: scale(1.1) translateY(-4px); opacity: 1; }
}

/* Chips and Buttons */
.flow-label {
  display: block;
  font-size: 12px;
  font-weight: 800;
  color: #475569;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 16px 0 8px 4px;
}

/* Global button override for accessibility */
div[data-testid="stButton"] button {
  height: 48px !important;
  font-size: 15px !important;
  font-weight: 800 !important;
  border-radius: 12px !important;
  border: 2px solid #CBD5E1 !important;
  background: #FFFFFF !important;
  color: #0F172A !important;
  transition: all var(--t-fast);
}

div[data-testid="stButton"] button:hover {
  border-color: #047857 !important;
  color: #047857 !important;
  background: #ECFDF5 !important;
}

/* Positioning Chat input cleanly above bottom nav and centering it */
[data-testid="stChatInput"] {
  position: fixed !important;
  bottom: 76px !important;
  z-index: 999 !important;
  background: #F0FDF4 !important;
  padding: 12px 16px !important;
  border-top: 1.5px solid #CBD5E1 !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: 100% !important;
  max-width: 480px !important;
}

/* Adjust general vertical padding of container on chatbot page to prevent overlap */
.main .block-container {
  padding-bottom: 160px !important;
}
"""

# ─────────────────────────────────────────────────────────────────────────────
# MOCK QUESTIONS & ANSWERS
# ─────────────────────────────────────────────────────────────────────────────
_CHIPS = {
    "hi": [
        ("🌾 क्या मैं लोन ले सकता हूँ?", "क्या मैं फसल लोन ले सकता हूँ?"),
        ("💰 कितना लोन सुरक्षित है?", "मेरे लिए कितना लोन सुरक्षित है?"),
        ("📈 अपेक्षित लाभ क्या होगा?", "मेरी फसल का अपेक्षित लाभ क्या होगा?"),
        ("🏛 सरकारी योजनाएं दिखाएं", "मुझे प्रमुख सरकारी योजनाएं बताएं"),
    ],
    "mr": [
        ("🌾 मी कर्ज घेऊ शकतो का?", "मी पीक कर्ज घेऊ शकतो का?"),
        ("💰 किती कर्ज सुरक्षित आहे?", "माझ्यासाठी किती कर्ज सुरक्षित आहे?"),
        ("📈 अपेक्षित नफा किती असेल?", "माझ्या पिकाचा अपेक्षित नफा किती असेल?"),
        ("🏛 सरकारी योजना दाखवा", "मला प्रमुख सरकारी योजना सांगा"),
    ],
    "en": [
        ("🌾 Can I take a crop loan?", "Can I take a crop loan?"),
        ("💰 How much loan is safe?", "How much loan is safe?"),
        ("📈 Expected profit?", "What will be my expected profit?"),
        ("🏛 Show government schemes", "Show government schemes"),
    ]
}

_ANSWERS = {
    "hi": {
        "crop_loan": (
            "🌾 *फसल लोन (KCC) पात्रता:*\n\n"
            "हाँ, भारत का कोई भी किसान जो अपनी जमीन पर खेती करता है, पट्टे (lease) पर खेती करता है, "
            "या बटाईदार है, वह **किसान क्रेडिट कार्ड (KCC)** लोन ले सकता है।\n\n"
            "इसके लिए आपके पास जमीन के कागजात (खतौनी/7-12) और आधार कार्ड होना आवश्यक है।"
        ),
        "safe_loan": (
            "💰 *सुरक्षित लोन सीमा:*\n\n"
            "आमतौर पर प्रति एकड़ **₹25,000 से ₹55,000** तक का लोन सुरक्षित माना जाता है।\n\n"
            "छोटे किसानों को सलाह दी जाती है कि वे शुरुआती दौर में ₹50,000 से ₹1,00,000 तक का ही लोन लें "
            "ताकि फसल बेचने के बाद ब्याज चुकाना आसान रहे।"
        ),
        "profit": (
            "📈 *अपेक्षित लाभ विवरण:*\n\n"
            "यह आपकी फसल के प्रकार पर निर्भर करता है। उदाहरण के लिए:\n"
            "- **धान/गेहूं:** ₹15,000 - ₹18,000 प्रति एकड़ मुनाफा।\n"
            "- **गन्ना:** ₹40,000 - ₹45,000 प्रति एकड़ मुनाफा।\n\n"
            "उत्पादन लागत और मौसम की स्थिति के आधार पर यह घट-बढ़ सकता है।"
        ),
        "schemes": (
            "🏛 *प्रमुख सरकारी योजनाएं:*\n\n"
            "1. **KCC (किसान क्रेडिट कार्ड):** 7% की कम ब्याज दर पर लोन (समय पर चुकाने पर 4% ही)।\n"
            "2. **PM-KISAN:** सालाना ₹6,000 सीधे बैंक खाते में।\n"
            "3. **PMFBY (फसल बीमा):** प्राकृतिक आपदाओं से फसल नुकसान पर सुरक्षा कवच।"
        ),
        "fallback": (
            "🌾 मैं समझ गया। कृपया मुझे अपनी फसल, एकड़ जमीन और राज्य का नाम बताएं ताकि मैं सही लोन और योजना की जानकारी दे सकूं।"
        )
    },
    "mr": {
        "crop_loan": (
            "🌾 *पीक कर्ज (KCC) पात्रता:*\n\n"
            "होय, भारतातील कोणताही शेतकरी जो स्वतःच्या जमिनीवर किंवा भाडेपट्ट्याने शेती करतो, "
            "तो **किसान क्रेडिट कार्ड (KCC)** अंतर्गत कर्ज घेऊ शकतो।\n\n"
            "यासाठी तुमच्याकडे ७/१२ उतारा आणि आधार कार्ड असणे आवश्यक आहे।"
        ),
        "safe_loan": (
            "💰 *सुरक्षित कर्ज मर्यादा:*\n\n"
            "साधारणपणे प्रति एकर **₹२५,००० ते ₹५५,०००** पर्यंतचे कर्ज सुरक्षित मानले जाते।\n\n"
            "शेतकऱ्यांनी गरजेपेक्षा जास्त कर्ज घेणे टाळावे जेणेकरून पीक विकल्यानंतर परतफेड सोपी होईल।"
        ),
        "profit": (
            "📈 *अपेक्षित नफा:*\n\n"
            "नफा हा तुमच्या पिकावर आणि हवामानावर अवलंबून असतो. सरासरी नफा:\n"
            "- **भात/गहू:** ₹१५,००० - ₹१८,००० प्रति एकर नफा।\n"
            "- **ऊस:** ₹४०,००० - ₹४२,००० प्रति एकर नफा।\n\n"
            "बाजारातील भावानुसार नफा बदलू शकतो।"
        ),
        "schemes": (
            "🏛 *महत्त्वाच्या सरकारी योजना:*\n\n"
            "1. **KCC (किसान क्रेडिट कार्ड):** ७% कमी व्याजदराने कर्ज (वेळेवर भरल्यास केवळ ४%)।\n"
            "2. **PM-KISAN:** वर्षाला ₹६,००० थेट खात्यात।\n"
            "3. **PMFBY (पीक विमा):** नैसर्गिक आपत्तीमुळे होणाऱ्या नुकसानापासून सुरक्षा।"
        ),
        "fallback": (
            "🌾 मला समजले. कृपया तुमचे पीक, जमिनीचे क्षेत्रफळ आणि राज्याची माहिती द्या, जेणेकरून मी अचूक माहिती देऊ शकेन।"
        )
    },
    "en": {
        "crop_loan": (
            "🌾 *Crop Loan (KCC) Eligibility:*\n\n"
            "Yes! Any farmer (owner, tenant farmer, or sharecropper) engaged in crop cultivation is eligible "
            "for a **Kisan Credit Card (KCC)** loan.\n\n"
            "Required documents include Land ownership proof (7/12 Utara or Patta) and Aadhaar card."
        ),
        "safe_loan": (
            "💰 *Safe Loan Guidelines:*\n\n"
            "Typically, a loan of **₹25,000 to ₹55,000 per acre** is considered safe and standard under RBI norms.\n\n"
            "Borrowing aligned strictly with your acreage helps prevent high debt traps."
        ),
        "profit": (
            "📈 *Expected Profit Heuristics:*\n\n"
            "Net income varies by crop under standard conditions:\n"
            "- **Paddy/Wheat:** ₹15,000 - ₹18,000 net profit per acre.\n"
            "- **Sugarcane:** ₹40,000 - ₹45,000 net profit per acre.\n\n"
            "Input cost fluctuations and weather play a major role in final earnings."
        ),
        "schemes": (
            "🏛 *Key Government Schemes:*\n\n"
            "1. **Kisan Credit Card (KCC):** Loans at 7% p.a., with prompt payment reducing it to 4% p.a.\n"
            "2. **PM-KISAN Samman Nidhi:** Direct benefit transfer of ₹6,000 annually.\n"
            "3. **Pradhan Mantri Fasal Bima Yojana (PMFBY):** Highly subsidized crop insurance protection."
        ),
        "fallback": (
            "🌾 I understand. Please provide details like crop type, land size, or state to help me advise you better."
        )
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# STATE HANDLING & LOGIC
# ─────────────────────────────────────────────────────────────────────────────

def _ensure_state() -> None:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "chat_loading" not in st.session_state:
        st.session_state.chat_loading = False


def _get_reply(query: str, lang: str) -> str:
    query_l = query.lower()
    ans = _ANSWERS.get(lang, _ANSWERS["en"])

    if any(k in query_l for k in ["crop", "loan", "ले सकता", "घेऊ", "कर्ज", "लोन"]):
        return ans["crop_loan"]
    elif any(k in query_l for k in ["safe", "how much", "कितना", "किती", "सुरक्षित"]):
        return ans["safe_loan"]
    elif any(k in query_l for k in ["profit", "expected", "लाभ", "नफा", "अपेक्षित"]):
        return ans["profit"]
    elif any(k in query_l for k in ["scheme", "government", "योजना", "सरकारी"]):
        return ans["schemes"]
    else:
        return ans["fallback"]


# ─────────────────────────────────────────────────────────────────────────────
# CHAT RENDERER
# ─────────────────────────────────────────────────────────────────────────────

def render_chatbot() -> None:
    _ensure_state()
    st.markdown(f"<style>{_CHATBOT_CSS}</style>", unsafe_allow_html=True)

    lang = st.session_state.get("lang", "hi")
    welcome_title = {"hi": "किसान AI आपके साथ है", "en": "Kisan AI is here to help you", "mr": "किसान AI तुमच्या सोबत आहे"}.get(lang, "Kisan AI is here")
    welcome_sub = {"hi": "लोन, ब्याज दरों या योजनाओं के बारे में कुछ भी पूछें", "en": "Ask anything about KCC loans, rates or schemes", "mr": "कर्ज, व्याजदर किंवा योजनांबद्दल काहीही विचारा"}.get(lang, "Ask anything")

    # Header Card
    st.markdown(
        f"""
        <div class="chat-welcome">
          <div class="chat-welcome__avatar-wrap">
            <div class="chat-welcome__avatar">🌱</div>
            <div class="chat-welcome__status-dot"></div>
          </div>
          <div class="chat-welcome__title">{welcome_title}</div>
          <div class="chat-welcome__sub">{welcome_sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 1. Clear chat row (Standard button rendering, no split div wraps!)
    if st.session_state.chat_history:
        clear_lbl = {"hi": "🗑️ चैट साफ करें", "en": "🗑️ Clear Chat", "mr": "🗑️ चॅट साफ करा"}.get(lang, "🗑️ Clear")
        if st.button(clear_lbl, key="clear_chat_action", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.chat_loading = False
            st.rerun()

    # 2. Quick Question Chips (Render if history is empty)
    if not st.session_state.chat_history:
        suggest_lbl = {"hi": "सुझाए गए प्रश्न", "en": "Suggested Questions", "mr": "सुचवलेले प्रश्न"}.get(lang, "Suggested")
        st.markdown(f'<span class="flow-label">{suggest_lbl}</span>', unsafe_allow_html=True)

        chips = _CHIPS.get(lang, _CHIPS["en"])
        cols = st.columns(2, gap="small")
        for idx, (label, query) in enumerate(chips):
            col = cols[idx % 2]
            with col:
                if st.button(label, key=f"chip_{idx}", use_container_width=True):
                    st.session_state.chat_history.append({"role": "user", "text": query})
                    st.session_state.chat_loading = True
                    st.rerun()

    # 3. Render Chat History (Self-contained templates, no split wraps!)
    if st.session_state.chat_history:
        for msg in st.session_state.chat_history:
            role = msg["role"]
            text = msg["text"]
            cls = "chat-bubble--user" if role == "user" else "chat-bubble--bot"
            align_cls = "chat-bubble-group--user" if role == "user" else "chat-bubble-group--bot"
            sender_name = "👨‍🌾 Kisan" if role == "user" else "🌱 Kisan AI"
            formatted_text = text.replace('\\n', '<br>').replace('\n', '<br>')

            st.markdown(
                f"""
                <div class="chat-bubble-group {align_cls}">
                  <span class="chat-avatar">{sender_name}</span>
                  <div class="chat-bubble {cls}">
                    {formatted_text}
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # 4. Simulate Bot Reply (Typing Animation)
    if st.session_state.chat_loading:
        typing_slot = st.empty()
        typing_slot.markdown(
            """
            <div class="chat-bubble-group chat-bubble-group--bot">
              <span class="chat-avatar">🌱 Kisan AI</span>
              <div class="chat-bubble chat-bubble--bot">
                <div class="typing-dots">
                  <span class="typing-dot"></span>
                  <span class="typing-dot"></span>
                  <span class="typing-dot"></span>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        time.sleep(1.0)
        typing_slot.empty()

        # Get reply and update history
        last_user_query = st.session_state.chat_history[-1]["text"]
        bot_reply = _get_reply(last_user_query, lang)

        st.session_state.chat_history.append({"role": "bot", "text": bot_reply})
        st.session_state.chat_loading = False
        st.rerun()

    # 5. Chat Input Widget
    chat_ph = {"hi": "सवालों को यहाँ लिखें...", "en": "Ask Kisan AI a question...", "mr": "येथे प्रश्न लिहा..."}.get(lang, "Ask a question...")
    user_input = st.chat_input(chat_ph)

    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        st.session_state.chat_loading = True
        st.rerun()
