"""
app.py — KisanCredit AI
========================
Single-page app with query-param routing.

Screens: home | farmer | ask | yojana

Run:
    streamlit run app.py
"""
from __future__ import annotations

import streamlit as st
from pathlib import Path

from utils.locale import (
    LANG_META,
    PRIMARY_LANG_CODES,
    VALID_LANG_CODES,
    t,
    greeting_pair,
)
from pages.farmer import render_farmer as _render_farmer_impl
from pages.chatbot import render_chatbot as _render_chatbot_impl
from pages.yojana import render_yojana as _render_yojana_impl

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="KisanCredit AI",
    page_icon="🌱",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
def _load_css() -> None:
    css_path = Path(__file__).parent / "styles" / "main.css"
    css = css_path.read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE + QUERY PARAM SYNC
# ─────────────────────────────────────────────────────────────────────────────
def _init_state() -> None:
    defaults: dict = {
        "lang":           "hi",
        "screen":         "home",
        "show_all_langs": False,
        "crop":           None,
        "land_area":      2.0,
        "land_ownership": "Owned",
        "state":          None,
        "loan_amount":    100_000,
        "result":         None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    lang_p = st.query_params.get("lang", "")
    if lang_p in VALID_LANG_CODES:
        st.session_state.lang = lang_p

    screen_p = st.query_params.get("screen", "")
    if screen_p in {"home", "farmer", "ask", "yojana"}:
        st.session_state.screen = screen_p

    all_langs_p = st.query_params.get("all_langs", "0")
    st.session_state.show_all_langs = all_langs_p == "1"


# ─────────────────────────────────────────────────────────────────────────────
# HOME SCREEN
# ─────────────────────────────────────────────────────────────────────────────
def render_home() -> None:
    lang     = st.session_state.lang
    show_all = st.session_state.show_all_langs
    greet, sub = greeting_pair(lang)

    # ── 1. HERO ───────────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="hero">
          <div class="hero__badge">
            <span class="hero__badge-dot"></span>
            AI Powered · Free
          </div>
          <span class="hero__logo">🌱</span>
          <div class="hero__app-name">KisanCredit AI</div>
          <div class="hero__tagline">{t(lang, 'tagline')}</div>
          <div class="hero__sub">{t(lang, 'hero_sub')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── 2. STATS STRIP ────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="stats-strip">
          <div class="stat-item">
            <span class="stat-item__value">{t(lang, 'stat_farmers')}</span>
            <span class="stat-item__label">{t(lang, 'stat_farmers_label')}</span>
          </div>
          <div class="stats-divider"></div>
          <div class="stat-item">
            <span class="stat-item__value">{t(lang, 'stat_loans')}</span>
            <span class="stat-item__label">{t(lang, 'stat_loans_label')}</span>
          </div>
          <div class="stats-divider"></div>
          <div class="stat-item">
            <span class="stat-item__value">{t(lang, 'stat_states')}</span>
            <span class="stat-item__label">{t(lang, 'stat_states_label')}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── 3. GREETING ───────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="greeting">
          <div class="greeting__avatar">👨‍🌾</div>
          <div>
            <div class="greeting__text">{greet}</div>
            <div class="greeting__sub">{sub}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── 4. LANGUAGE SELECTION ─────────────────────────────────────────────────
    st.markdown(
        f'<span class="section-label">{t(lang, "choose_lang")}</span>',
        unsafe_allow_html=True,
    )

    if not show_all:
        _render_primary_lang_pills(lang)
    else:
        _render_full_lang_grid(lang)

    # ── 5. PRIMARY CTA CARD ───────────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="cta-section">
          <a href="?screen=farmer&lang={lang}"
             target="_self"
             class="cta-card"
             role="button"
             aria-label="{t(lang, 'cta_card_title')}">
            <div class="cta-card__header">
              <span class="cta-card__icon">👨‍🌾</span>
              <div class="cta-card__meta">
                <div class="cta-card__badge">⚡ {t(lang, 'cta_badge')}</div>
                <div class="cta-card__title">{t(lang, 'cta_card_title')}</div>
                <div class="cta-card__sub">{t(lang, 'cta_card_sub')}</div>
              </div>
            </div>
            <div class="cta-card__btn">
              <span class="cta-card__btn-icon">🌾</span>
              {t(lang, 'cta_btn')}
              <span class="cta-card__arrow">→</span>
            </div>
          </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── 6. HOW IT WORKS ───────────────────────────────────────────────────────
    st.markdown(
        f'<span class="section-label">{t(lang, "how_title")}</span>',
        unsafe_allow_html=True,
    )

    steps = [
        ("🌐", t(lang, "step1_title"), t(lang, "step1_body")),
        ("📋", t(lang, "step2_title"), t(lang, "step2_body")),
        ("✅", t(lang, "step3_title"), t(lang, "step3_body")),
    ]

    steps_html = '<div class="how-section"><div class="how-steps">'
    for i, (icon, title, body) in enumerate(steps):
        steps_html += f"""
        <div class="how-step">
          <div class="how-step__num">{i + 1}</div>
          <div class="how-step__icon">{icon}</div>
          <div class="how-step__text">
            <div class="how-step__title">{title}</div>
            <div class="how-step__body">{body}</div>
          </div>
        </div>"""
    steps_html += "</div></div>"
    st.markdown(steps_html, unsafe_allow_html=True)

    # ── 7. TRUST SECTION ──────────────────────────────────────────────────────
    st.markdown(
        f'<span class="section-label">{t(lang, "why_trust")}</span>',
        unsafe_allow_html=True,
    )

    trust_items = [
        ("✅", t(lang, "trust_easy_title"), t(lang, "trust_easy_body")),
        ("🎁", t(lang, "trust_free_title"), t(lang, "trust_free_body")),
        ("🌾", t(lang, "trust_crop_title"), t(lang, "trust_crop_body")),
        ("🔒", t(lang, "trust_secure_title"), t(lang, "trust_secure_body")),
    ]

    cards_html = '<div class="trust-section"><div class="trust-grid">'
    for icon, title, body in trust_items:
        cards_html += f"""
        <div class="trust-card">
          <div class="trust-card__icon-wrap">{icon}</div>
          <div class="trust-card__title">{title}</div>
          <div class="trust-card__body">{body}</div>
        </div>"""
    cards_html += "</div></div>"
    st.markdown(cards_html, unsafe_allow_html=True)

    # ── 8. SCHEME BANNER ──────────────────────────────────────────────────────
    st.markdown(
        """
        <div class="scheme-banner">
          <span class="scheme-banner__icon">🏛️</span>
          <div class="scheme-banner__text">
            <div class="scheme-banner__label">Government Backed</div>
            <div class="scheme-banner__title">PM-KISAN · KCC · PMFBY</div>
            <div class="scheme-banner__sub">Official scheme guidelines</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── 9. FOOTER ─────────────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="app-footer">
          <div class="footer__divider"></div>
          <div class="footer__row">
            <span class="footer__brand">🌱 KisanCredit AI</span>
            <span class="footer__sep">·</span>
            <span class="footer__tagline">{t(lang, 'footer_tagline')}</span>
          </div>
          <div class="footer__powered">{t(lang, 'footer_powered')}</div>
          <div class="footer__disclaimer">{t(lang, 'footer_disclaimer')}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_primary_lang_pills(lang: str) -> None:
    pills_html = '<div class="lang-pills">'
    for name, code, _ in LANG_META:
        if code not in PRIMARY_LANG_CODES:
            continue
        active  = code == lang
        cls     = "lang-pill lang-pill--active" if active else "lang-pill"
        check   = '<span class="lang-pill__check">✓</span>' if active else ""
        pressed = "true" if active else "false"
        pills_html += (
            f'<a href="?lang={code}&screen=home&all_langs=0"'
            f'   target="_self" class="{cls}"'
            f'   aria-label="{name}" aria-pressed="{pressed}">'
            f"  {check}{name}"
            f"</a>"
        )
    pills_html += "</div>"

    more_label = t(lang, "more_languages")
    pills_html += (
        f'<div class="more-langs-wrap">'
        f'  <a href="?lang={lang}&screen=home&all_langs=1"'
        f'     target="_self" class="more-langs-link"'
        f'     aria-label="{_more_langs_aria(lang)}">'
        f"    {more_label}"
        f"  </a>"
        f"</div>"
    )
    st.markdown(pills_html, unsafe_allow_html=True)


def _render_full_lang_grid(lang: str) -> None:
    grid_html = '<div class="lang-grid">'
    for name, code, emoji in LANG_META:
        active  = code == lang
        cls     = "lang-card lang-card--active" if active else "lang-card"
        check   = '<span class="lang-card__check">✓</span>' if active else ""
        pressed = "true" if active else "false"
        grid_html += (
            f'<a href="?lang={code}&screen=home&all_langs=1"'
            f'   target="_self" class="{cls}"'
            f'   aria-label="{name}" aria-pressed="{pressed}">'
            f"  {check}"
            f'  <span class="lang-card__icon">{emoji}</span>'
            f'  <span class="lang-card__name">{name}</span>'
            f"</a>"
        )
    grid_html += "</div>"

    fewer_label = t(lang, "fewer_languages")
    grid_html += (
        f'<div class="more-langs-wrap">'
        f'  <a href="?lang={lang}&screen=home&all_langs=0"'
        f'     target="_self" class="more-langs-link">'
        f"    ‹ {fewer_label}"
        f"  </a>"
        f"</div>"
    )
    st.markdown(grid_html, unsafe_allow_html=True)


def _more_langs_aria(lang: str) -> str:
    labels = {
        "hi": "सभी भाषाएँ देखें",
        "en": "See all languages",
        "mr": "सर्व भाषा पाहा",
    }
    return labels.get(lang, labels["en"])


# ─────────────────────────────────────────────────────────────────────────────
# FARMER SCREEN  →  delegated to pages/farmer.py
# ─────────────────────────────────────────────────────────────────────────────
def render_farmer() -> None:
    _render_farmer_impl()


# ─────────────────────────────────────────────────────────────────────────────
# CHATBOT SCREEN  →  delegated to pages/chatbot.py
# ─────────────────────────────────────────────────────────────────────────────
def render_chatbot() -> None:
    _render_chatbot_impl()


# ─────────────────────────────────────────────────────────────────────────────
# YOJANA SCREEN  →  delegated to pages/yojana.py
# ─────────────────────────────────────────────────────────────────────────────
def render_yojana() -> None:
    _render_yojana_impl()


# ─────────────────────────────────────────────────────────────────────────────
# BOTTOM NAVIGATION  (fixed)
# ─────────────────────────────────────────────────────────────────────────────
def render_bottom_nav() -> None:
    lang = st.session_state.lang
    cur  = st.session_state.screen
    home_active = cur in {"home", "farmer"}

    def _tab(screen: str, icon: str, label: str, active: bool) -> str:
        cls     = "nav-tab nav-tab--active" if active else "nav-tab"
        current = "page" if active else "false"
        return (
            f'<a href="?screen={screen}&lang={lang}&all_langs=0"'
            f'   target="_self" class="{cls}"'
            f'   aria-label="{label}" aria-current="{current}">'
            f'  <span class="nav-tab__icon">{icon}</span>'
            f'  <span class="nav-tab__label">{label}</span>'
            f"</a>"
        )

    nav_html = (
        '<nav class="bottom-nav" role="navigation" aria-label="Main navigation">'
        + _tab("home",   "🏠", t(lang, "nav_home"),   home_active)
        + _tab("ask",    "💬", t(lang, "nav_ask"),    cur == "ask")
        + _tab("yojana", "📋", t(lang, "nav_yojana"), cur == "yojana")
        + "</nav>"
    )
    st.markdown(nav_html, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ROUTER
# ─────────────────────────────────────────────────────────────────────────────
def main() -> None:
    _init_state()
    _load_css()

    screen = st.session_state.screen

    if screen == "home":
        render_home()
    elif screen == "farmer":
        render_farmer()
    elif screen == "ask":
        render_chatbot()
    elif screen == "yojana":
        render_yojana()
    else:
        render_home()

    render_bottom_nav()


if __name__ == "__main__":
    main()
