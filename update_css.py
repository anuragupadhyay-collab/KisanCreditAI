import re
with open('pages/farmer.py', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
/* ── Premium Farmer Flow CSS ───────────────────────────────────────────── */
.farmer-back-btn > div > button {
  background: transparent !important; border: none !important; box-shadow: none !important;
  color: #059669 !important; font-size: 15px !important; font-weight: 700 !important;
  height: 40px !important; min-height: 0 !important; padding: 0 4px 0 16px !important;
  width: auto !important; text-align: left !important; letter-spacing: 0 !important;
  transition: opacity 0.2s;
}
.farmer-back-btn > div > button:hover { opacity: 0.7; }

/* ── Step header (Glassmorphic & Fluid) ────────────────────────────────── */
.step-header {
  background: linear-gradient(135deg, #047857 0%, #059669 50%, #10B981 100%);
  padding: 24px 24px 32px; position: relative; overflow: hidden;
  border-bottom-left-radius: 32px; border-bottom-right-radius: 32px;
  box-shadow: 0 12px 32px rgba(4, 120, 87, 0.15); margin-bottom: 16px;
}
.step-header::before, .step-header::after {
  content: ''; position: absolute; border-radius: 50%; filter: blur(30px);
}
.step-header::before { width: 150px; height: 150px; background: rgba(255,255,255,0.15); top: -50px; right: -20px; }
.step-header::after { width: 200px; height: 200px; background: rgba(16,185,129,0.5); bottom: -100px; left: -50px; }
.step-header__meta { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; position: relative; z-index: 1; }
.step-header__badge { background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); color: #fff; font-size: 11px; font-weight: 800; padding: 4px 12px; border-radius: 9999px; letter-spacing: 0.5px; border: 1px solid rgba(255,255,255,0.3); }
.step-header__dots { display: flex; gap: 6px; }
.step-dot { height: 4px; border-radius: 999px; flex: 1; background: rgba(255,255,255,0.25); min-width: 32px; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
.step-dot--done { background: rgba(255,255,255,0.6); }
.step-dot--active { background: #fff; box-shadow: 0 0 10px rgba(255,255,255,0.5); }
.step-header__title { color: #fff; font-size: 24px; font-weight: 800; line-height: 1.2; margin-top: 16px; margin-bottom: 4px; position: relative; z-index: 1; text-shadow: 0 2px 12px rgba(0,0,0,0.1); letter-spacing: -0.5px; }
.step-header__sub { color: rgba(255,255,255,0.9); font-size: 14px; line-height: 1.5; font-weight: 500; position: relative; z-index: 1; }

.flow-label { display: block; font-size: 12px; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 1px; margin: 24px 0 12px; }

/* ── Default Base Buttons (Premium styling) ────────────────────────────── */
[data-testid="stBaseButton-secondary"] {
  background: rgba(255,255,255,0.7) !important; backdrop-filter: blur(10px) !important; -webkit-backdrop-filter: blur(10px) !important;
  border: 1px solid rgba(226,232,240,0.8) !important; color: #475569 !important; border-radius: 16px !important;
  height: 56px !important; font-size: 16px !important; font-weight: 700 !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important; box-shadow: 0 2px 8px rgba(15,23,42,0.03) !important;
}
[data-testid="stBaseButton-secondary"]:hover {
  border-color: #059669 !important; background: #fff !important; color: #059669 !important;
  transform: translateY(-2px) !important; box-shadow: 0 12px 24px rgba(15,23,42,0.06) !important;
}
[data-testid="stBaseButton-primary"] {
  background: linear-gradient(135deg, #059669 0%, #10B981 100%) !important; color: #fff !important;
  border: none !important; border-radius: 16px !important; height: 60px !important;
  font-size: 18px !important; font-weight: 800 !important; letter-spacing: 0.5px !important;
  box-shadow: 0 12px 28px rgba(5,150,105,0.25) !important; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
[data-testid="stBaseButton-primary"]:hover { transform: translateY(-3px) scale(1.02) !important; box-shadow: 0 20px 40px rgba(5,150,105,0.35) !important; }
[data-testid="stBaseButton-primary"]:active { transform: translateY(0) scale(0.98) !important; }

/* ── Specific Button overrides based on columns ────────────────────────── */
div[data-testid="stHorizontalBlock"]:has(> div:nth-child(3)):not(:has(> div:nth-child(4))) > div [data-testid="stBaseButton-secondary"] {
  height: 110px !important; border-radius: 20px !important; font-size: 14px !important; padding: 12px 4px !important;
  background: #fff !important; box-shadow: 0 4px 12px rgba(15,23,42,0.04) !important;
}
div[data-testid="stHorizontalBlock"]:has(> div:nth-child(3)):not(:has(> div:nth-child(4))) > div [data-testid="stBaseButton-primary"] {
  height: 110px !important; border-radius: 20px !important; font-size: 14px !important; padding: 12px 4px !important;
  background: #fff !important; color: #047857 !important; border: 2px solid #059669 !important;
  box-shadow: 0 0 0 4px rgba(5,150,105,0.1), 0 8px 24px rgba(5,150,105,0.2) !important;
}
div[data-testid="stHorizontalBlock"]:has(> div:nth-child(4)):not(:has(> div:nth-child(5))) > div [data-testid="stBaseButton-secondary"] { height: 60px !important; border-radius: 9999px !important; font-size: 15px !important; }
div[data-testid="stHorizontalBlock"]:has(> div:nth-child(4)):not(:has(> div:nth-child(5))) > div [data-testid="stBaseButton-primary"] { height: 60px !important; border-radius: 9999px !important; font-size: 15px !important; }
div[data-testid="stHorizontalBlock"]:not(:has(> div:nth-child(3))) > div [data-testid="stBaseButton-primary"] { background: #ECFDF5 !important; border: 2px solid #059669 !important; color: #047857 !important; box-shadow: none !important; }
div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) > div [data-testid="stBaseButton-secondary"] { height: 48px !important; border-radius: 9999px !important; font-size: 13px !important; }
div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) > div [data-testid="stBaseButton-primary"] { height: 48px !important; border-radius: 9999px !important; font-size: 13px !important; }

/* ── Slider & Selectbox ────────────────────────────────────────────────── */
[data-testid="stSlider"] > label { display: none !important; }
[data-testid="stSlider"] > div > div > div > div { background: #059669 !important; }
[data-testid="stThumbValue"] { color: #059669 !important; font-weight: 800 !important; font-family: 'Outfit', sans-serif !important; }
[data-testid="stSelectbox"] > label { display: none !important; }
[data-testid="stSelectbox"] > div > div {
  border: 1px solid rgba(226,232,240,0.8) !important; border-radius: 16px !important; min-height: 56px !important;
  background: rgba(255,255,255,0.8) !important; backdrop-filter: blur(10px) !important; font-size: 16px !important;
  font-weight: 600 !important; box-shadow: 0 4px 12px rgba(15,23,42,0.03) !important; padding-left: 16px !important;
}
[data-testid="stSelectbox"] > div > div:focus-within { border-color: #059669 !important; box-shadow: 0 0 0 4px rgba(5,150,105,0.15) !important; }

/* ── Loan Big Display ──────────────────────────────────────────────────── */
.loan-display { text-align: center; padding: 24px 0 12px; }
.loan-display__amount { font-size: 56px; font-weight: 800; color: #059669; line-height: 1; letter-spacing: -2px; font-family: 'Outfit', sans-serif; text-shadow: 0 4px 12px rgba(5,150,105,0.1); }
.loan-display__hint { font-size: 13px; color: #94A3B8; margin-top: 8px; font-weight: 500; }
.loan-info-banner { background: rgba(240,253,244,0.7); backdrop-filter: blur(8px); border-left: 4px solid #059669; border-radius: 0 12px 12px 0; padding: 12px 16px; font-size: 13px; color: #0F172A; font-weight: 500; margin: 16px 0 12px; }
.validation-msg { background: #FEF2F2; border: 1px solid #FECACA; border-radius: 12px; padding: 12px 16px; font-size: 14px; color: #DC2626; font-weight: 700; margin-bottom: 16px; box-shadow: 0 4px 12px rgba(220,38,38,0.1); }

/* ── Loading Screen ────────────────────────────────────────────────────── */
.loading-screen { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 68vh; padding: 40px 24px; text-align: center; gap: 20px; }
.loading-screen__icon { font-size: 80px; line-height: 1; animation: farmerBounce 2s ease-in-out infinite; filter: drop-shadow(0 8px 16px rgba(0,0,0,0.1)); }
@keyframes farmerBounce { 0%, 100% { transform: translateY(0); } 48% { transform: translateY(-12px); } }
.loading-screen__title { font-size: 20px; font-weight: 800; color: #0F172A; line-height: 1.45; }
.loading-screen__sub { font-size: 14px; color: #475569; line-height: 1.6; max-width: 260px; font-weight: 500; }
.loading-bar { width: 220px; height: 6px; background: rgba(226,232,240,0.8); border-radius: 9999px; overflow: hidden; box-shadow: inset 0 2px 4px rgba(0,0,0,0.05); }
.loading-bar__fill { height: 100%; background: linear-gradient(90deg, #10B981, #34D399); border-radius: 9999px; animation: barFill 1.8s cubic-bezier(0.16, 1, 0.3, 1) infinite; }
@keyframes barFill { 0% { width: 4%; } 65% { width: 90%; } 100% { width: 95%; } }

/* ── Result Card ───────────────────────────────────────────────────────── */
.result-card { border-radius: 24px; overflow: hidden; box-shadow: 0 24px 48px rgba(15,23,42,0.12); margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.8); }
.result-card__header { background: linear-gradient(135deg, #047857 0%, #059669 50%, #10B981 100%); padding: 32px 24px; text-align: center; position: relative; }
.result-card__header--partial { background: linear-gradient(135deg, #B45309 0%, #D97706 50%, #F59E0B 100%); }
.result-card__header--rejected { background: linear-gradient(135deg, #9F1239 0%, #E11D48 50%, #FB7185 100%); }
.result-card__header::after { content: ''; position: absolute; width: 200px; height: 200px; background: rgba(255,255,255,0.1); border-radius: 50%; top: -100px; right: -50px; filter: blur(20px); }
.result-card__label { color: rgba(255,255,255,0.8); font-size: 12px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px; }
.result-card__amount { color: #fff; font-size: 56px; font-weight: 800; line-height: 1; letter-spacing: -2px; font-family: 'Outfit', sans-serif; text-shadow: 0 4px 16px rgba(0,0,0,0.2); margin-bottom: 12px; position: relative; z-index: 1; }
.result-card__scheme { display: inline-block; background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); color: #fff; font-size: 14px; font-weight: 700; padding: 6px 16px; border-radius: 9999px; border: 1px solid rgba(255,255,255,0.3); position: relative; z-index: 1; }

.safety-row { padding: 16px 0 12px; }
.safety-pill { display: inline-flex; align-items: center; gap: 8px; padding: 10px 24px; border-radius: 9999px; font-size: 15px; font-weight: 800; box-shadow: 0 4px 12px rgba(15,23,42,0.05); }
.safety-pill--safe { background: #ECFDF5; color: #047857; border: 1px solid #A7F3D0; }
.safety-pill--medium { background: #FEF3C7; color: #D97706; border: 1px solid #FDE68A; }
.safety-pill--high { background: #FEF2F2; color: #DC2626; border: 1px solid #FECACA; }

.result-explain { background: rgba(255,255,255,0.7); backdrop-filter: blur(12px); border-left: 4px solid #059669; border-radius: 0 16px 16px 0; padding: 16px 20px; font-size: 15px; color: #0F172A; line-height: 1.6; margin: 12px 0 20px; font-weight: 500; box-shadow: 0 4px 12px rgba(15,23,42,0.03); }
.docs-card { background: #fff; border: 1px solid rgba(226,232,240,0.8); border-radius: 24px; padding: 20px; margin-bottom: 24px; box-shadow: 0 12px 32px rgba(15,23,42,0.06); }
.docs-card__hdr { font-size: 15px; font-weight: 800; color: #0F172A; margin-bottom: 16px; }
.doc-row { display: flex; align-items: flex-start; gap: 12px; font-size: 14px; color: #475569; padding: 10px 0; border-bottom: 1px solid #F1F5F9; font-weight: 500; }
.doc-row__check { color: #059669; font-weight: 800; }
.docs-note { font-size: 12px; color: #94A3B8; margin-top: 12px; font-style: italic; font-weight: 500; }

.btn-wa { display: flex; align-items: center; justify-content: center; gap: 10px; height: 64px; background: linear-gradient(135deg, #10B981 0%, #059669 100%); color: #fff !important; border-radius: 16px; font-size: 18px; font-weight: 800; text-decoration: none !important; box-shadow: 0 12px 28px rgba(16,185,129,0.3); transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); margin-bottom: 12px; letter-spacing: 0.5px; }
.btn-wa:hover { transform: translateY(-3px) scale(1.02); box-shadow: 0 20px 40px rgba(16,185,129,0.4); }
.btn-outline-row { display: flex; gap: 12px; }
.btn-outline { flex: 1; display: flex; align-items: center; justify-content: center; gap: 8px; height: 56px; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); color: #059669 !important; border: 1.5px solid #059669; border-radius: 16px; font-size: 15px; font-weight: 800; text-decoration: none !important; transition: all 0.2s; box-shadow: 0 4px 12px rgba(5,150,105,0.05); }
.btn-outline:hover { background: #059669; color: #fff !important; transform: translateY(-2px); box-shadow: 0 12px 24px rgba(5,150,105,0.2); }
.step-gap { margin: 0; padding: 0; height: 16px; }
.step-gap-sm { height: 8px; }
.content-pad { padding: 0 20px; }
'''

content = re.sub(r'_FARMER_CSS\s*=\s*\"\"\"[\s\S]*?\"\"\"', f'_FARMER_CSS = \"\"\"\n{new_css}\n\"\"\"', content)
with open('pages/farmer.py', 'w', encoding='utf-8') as f:
    f.write(content)
