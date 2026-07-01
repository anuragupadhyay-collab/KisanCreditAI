# KisanCredit AI — Low-Fidelity Wireframes
**Version:** 1.0
**Viewport:** Mobile-First (360px primary)
**Compatibility:** Streamlit layout-compatible
**Format:** ASCII wireframes — no code

---

## Legend & Notation

```
╔═══╗ / ┌───┐   Page boundary / Card boundary
║   ║ / │   │   Interior content area
[   ]               Button / Tappable element
( )  /  (●)         Radio button / Selected radio
[x]                 Selected checkbox
▾                   Dropdown chevron
●                   Slider thumb (active position)
─ / ━               Divider / Section separator
▓▓▓                 Selected / highlighted tile
...                 Placeholder / dynamic content
🌾                  Icon (descriptive, not literal emoji)
```

---
---

# PAGE 1 — LOAN ANALYZER
## Mobile View  |  360px width

```
╔═════════════════════════════════════════╗
║              HEADER  56dp               ║
║                                         ║
║  [🌱]    KisanCredit AI    [हिं ▾]     ║
║                                         ║
╚═════════════════════════════════════════╝
   ^Logo                         ^Lang pill
   32x32dp, left pad 16dp        White border, 14sp
   App name: 18sp Bold, White    Right pad 16dp


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PAGE TITLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🌾 अपनी फसल जानकारी भरें            ← H1, 22sp Bold, #1A2E1C
     Fill in your crop details         ← Subtitle, 14sp, #4A5E4C

  ──────────────────────────────────────


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 1 — CROP SELECTOR GRID
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  फसल चुनें / Select Crop              ← Section label, 12sp SemiBold

  ┌──────────┬──────────┬──────────┐
  │          │          │          │
  │   🌾     │   🌿     │   🪢     │   ← Row 1 — icons 40x40dp, centered
  │  Paddy   │  Wheat   │  Cotton  │   ← Labels 12sp SemiBold below icon
  │          │          │          │
  └──────────┴──────────┴──────────┘

  ┌──────────┬──────────┬──────────┐
  │          │          │          │
  │   🎋     │   🌽     │   🫘     │   ← Row 2
  │Sugarcane │  Maize   │ Soybean  │
  │          │          │          │
  └──────────┴──────────┴──────────┘

  ┌──────────┬──────────┬──────────┐
  │▓▓▓▓▓▓▓▓▓▓│          │          │
  │▓         ▓│          │          │
  │▓   🥜   ▓│   🥦     │   🫛     │   ← ▓▓▓ = SELECTED TILE
  │▓Groundnut▓│   Veg.   │  Pulses  │     Green border 2.5dp + light bg
  │▓         ▓│          │          │
  └──────────┴──────────┴──────────┘

  [+ Show More Crops ▾]                 ← Secondary link, only if >9 crops
                                          Tiles: 100×100dp each
                                          Grid: 3 col, gap 8dp, pad 16dp


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 2 — FARM SIZE PICKER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  जमीन का आकार / Farm Size             ← Section label, 12sp SemiBold

  ┌─────────────────────────────────────┐
  │                                     │
  │   [  −  ]       2.5       [  +  ]   │   ← (−) and (+): 56×56dp buttons
  │                                     │       Central value: 24sp Bold
  │             Acres                   │   ← Unit label, 14sp below value
  │                                     │
  └─────────────────────────────────────┘

  ┌────────────┬─────────────┬──────────┐
  │   Acres    │    Bigha    │ Hectares │   ← Unit tab switcher
  │  [ACTIVE]  │             │          │     Underline active tab
  └────────────┴─────────────┴──────────┘
                                            Min: 0.5 | Max: 500 | Step: 0.5


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 3 — LOCATION DROPDOWNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  राज्य / State                         ← Field label, 12sp SemiBold
  ┌─────────────────────────────────────┐
  │   Select your state             ▾   │   ← Dropdown, 56dp height
  └─────────────────────────────────────┘   border 1.5dp, radius 10dp

  जिला / District                       ← Field label, 12sp SemiBold
  ┌─────────────────────────────────────┐
  │   Select district (choose state) ▾  │   ← DISABLED until State chosen
  └─────────────────────────────────────┘   Greyed placeholder when locked


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 4 — LAND OWNERSHIP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  भूमि स्वामित्व / Land Ownership       ← Section label, 12sp SemiBold

  ┌─────────────────────────────────────┐
  │                                     │
  │   (●)  Owned   (खुद की)             │   ← Selected radio, 48dp tap area
  │   ( )  Leased  (किराए की)           │   ← Unselected radio
  │                                     │
  └─────────────────────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 5 — ANNUAL INCOME
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  सालाना आय / Annual Income  (Optional) ← Label + Optional tag

  ┌─────────────────────────────────────┐
  │   ₹  Enter amount (e.g. 80,000)     │   ← Text input, numeric keyboard
  └─────────────────────────────────────┘

  [Skip this step →]                    ← Secondary link, 14sp, #1565C0


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PRIMARY CTA BUTTON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────────────────────────────┐
  │                                     │
  │    🔍   लोन विश्लेषण करें           │   ← Full width, 56dp height
  │         Analyze My Loan             │     bg: #2D7A3E, text: White 16sp Bold
  │                                     │
  └─────────────────────────────────────┘
  Loading state: button text → white spinner 24dp, disabled bg


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  RESULT CARD  (renders below CTA after tap)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ─ ─ ─ ─ ─  Result appears below  ─ ─ ─ ─

  ┌─────────────────────────────────────┐
  │                                     │
  │  [✅  आप पात्र हैं / Eligible  ]   │   ← STATUS BADGE — green pill
  │                                     │     bg: #E8F5EC, text: #2D7A3E
  │                                     │
  │   ₹ 1,20,000                        │   ← LOAN AMOUNT — Display 28sp
  │   तक का लोन / Loan up to amount     │     Color: #2D7A3E (Primary Green)
  │                                     │     Indian numbering format
  │  ──────────────────────────────────  │
  │                                     │
  │   Kisan Credit Card (KCC)           │   ← Scheme name — H3 16sp SemiBold
  │   7% प्रति वर्ष / 7% per annum      │   ← Interest rate — Body 16sp
  │   (2% Government Subsidy applied)   │   ← Sub-note — Caption 12sp
  │                                     │
  │  ──────────────────────────────────  │
  │                                     │
  │  ┌───────────────────────────────┐  │
  │  │ 📋  जरूरी दस्तावेज़       [▾] │  │   ← COLLAPSIBLE ACCORDION
  │  └───────────────────────────────┘  │     Chevron flips on tap
  │                                     │
  │  [EXPANDED STATE BELOW]             │
  │  ┌───────────────────────────────┐  │
  │  │  ✓  Aadhaar Card              │  │
  │  │  ✓  Land Records (7/12 Utara) │  │
  │  │  ✓  Bank Passbook (6 months)  │  │
  │  │  ✓  Passport Photos (×2)      │  │
  │  │  ✓  Crop Sowing Certificate   │  │
  │  │                               │  │
  │  │  [🖨 Print]  [📲 WhatsApp]    │  │   ← Checklist action row
  │  └───────────────────────────────┘  │
  │                                     │
  │  ──────────────────────────────────  │
  │                                     │
  │  [📤  Share Result on WhatsApp  ]   │   ← Secondary button, full width
  │  [💬  Ask Kisan AI a Question   ]   │   ← Tertiary link → AI tab
  │  [🖨  Print Summary             ]   │   ← Tertiary link (CSC/desktop)
  │                                     │
  └─────────────────────────────────────┘
       Card: bg White, border 1.5dp #DDE5D5
       radius 16dp, shadow 0 2px 12px rgba(0,0,0,0.08)
       padding 20dp


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EMPTY STATE  (before analysis runs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [Result zone is replaced by:]

  ┌─────────────────────────────────────┐
  │                                     │
  │     [  🌾  Field SVG illustration ] │   ← Simple green line art
  │                                     │
  │   अपनी जानकारी भरें                 │   ← Headline 18sp Bold
  │   Fill in your details              │
  │                                     │
  │   ऊपर फॉर्म भरकर अपनी लोन           │   ← Body 14sp, secondary color
  │   पात्रता जानें।                     │
  │   Fill the form to discover your    │
  │   loan eligibility.                 │
  │                                     │
  └─────────────────────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  FOOTER / BOTTOM NAVIGATION  64dp fixed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═════════════════════════════════════════╗
║                                         ║
║  [ 🌾 Loan  ]  [ 💬 Ask AI ]  [📊 Risk]║
║   Analyzer      Kisan AI     Simulator  ║
║                                         ║
╚═════════════════════════════════════════╝
   ^ ACTIVE TAB ^    Inactive     Inactive
   Green icon         Grey icon   Grey icon
   11sp Bold          11sp Reg    11sp Reg

   bg: White  |  top border: 1dp #E0E0E0
   Each tab: full 1/3 width, 64dp height
```

---

## Loan Analyzer — Desktop / CSC Layout  768px+

```
╔══════════════════════════════════════════════════════════════════╗
║  [🌱]  KisanCredit AI                          [Language ▾]     ║
╠═══════════╦══════════════════════════════════════════════════════╣
║           ║                                                      ║
║  🌾 Loan  ║   FORM PANEL  (left 40%)    RESULT PANEL (right 60%)║
║  Analyzer ║   ─────────────────────     ──────────────────────   ║
║  [ACTIVE] ║                             ┌────────────────────┐   ║
║           ║   [Crop Grid — 4 columns]   │ ✅ Eligible        │   ║
║  💬 Ask   ║                             │                    │   ║
║  Kisan AI ║   [Farm Size Picker]        │  ₹ 1,20,000        │   ║
║           ║                             │  KCC Scheme        │   ║
║  📊 Risk  ║   [State ▾] [District ▾]   │  7% p.a.           │   ║
║  Simulatr ║                             │                    │   ║
║           ║   (●) Owned  ( ) Leased     │  [📋 Documents ▾]  │   ║
║           ║                             │                    │   ║
║           ║   [₹ Income — Optional]     │  [📤 Share]        │   ║
║           ║                             │  [💬 Ask AI]       │   ║
║           ║   [🔍 Analyze My Loan]      │  [🖨  Print]       │   ║
║           ║                             └────────────────────┘   ║
╚═══════════╩══════════════════════════════════════════════════════╝
  Sidebar: 240px    Form 40%     Result card 60%, side by side
  No bottom nav     Crop grid: 4 columns on desktop
```

---
---

# PAGE 2 — ASK KISAN AI
## Mobile View  |  360px width

```
╔═════════════════════════════════════════╗
║              HEADER  56dp               ║
║                                         ║
║  [🌱]    KisanCredit AI    [हिं ▾]     ║
║                                         ║
╚═════════════════════════════════════════╝
   Header scrolls away on chat screen
   to maximise visible chat area


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  QUICK QUESTIONS STRIP  (horizontal scroll)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ─── जल्दी सवाल / Quick Questions ────

  ┌──────────────────┐┌──────────────┐┌──────────┐  →→ scroll
  │ KCC loan क्या है?││ Am I eligible││ Documents│
  └──────────────────┘└──────────────┘└──────────┘

  ┌─────────────────┐┌────────────────────────┐     →→ scroll
  │  Interest rate? ││  Govt subsidy kitni?   │
  └─────────────────┘└────────────────────────┘

  Chips: 36dp height, 18dp border-radius, pad 0 16dp
  bg: White, border: 1dp #DDE5D5, text: 13sp #4A5E4C
  Tap: fills input field with chip text
  No visible scrollbar


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CHAT AREA  (scrollable, grows upward)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────────────────────────────┐
  │ 🤖                                  │   ← AI WELCOME BUBBLE  (LEFT)
  │ ┌─────────────────────────────────┐ │     bg: #F5F7F2
  │ │ नमस्ते! मैं Kisan AI हूँ।        │ │     radius: 16 16 16 4 dp
  │ │ मैं आपके लोन से जुड़े किसी भी   │ │     max-width: 85% of container
  │ │ सवाल का जवाब दे सकता हूँ।       │ │     text: #1A2E1C, 16sp
  │ └─────────────────────────────────┘ │
  │   [Source: KCC Guidelines]          │   ← Source tag — 11sp italic
  └─────────────────────────────────────┘

  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  ┌─────────────────────────────────────┐
  │                                     │   ← USER MESSAGE  (RIGHT)
  │      ┌──────────────────────────┐   │     bg: #2D7A3E (Primary Green)
  │      │  KCC loan ke liye        │   │     text: White, 16sp
  │      │  kya chahiye?            │   │     radius: 16 16 4 16 dp
  │      └──────────────────────────┘   │     max-width: 75% of container
  │                              12:34  │   ← Timestamp 11sp, right-align
  └─────────────────────────────────────┘

  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  ┌─────────────────────────────────────┐
  │ 🤖                                  │   ← AI RESPONSE BUBBLE  (LEFT)
  │ ┌─────────────────────────────────┐ │
  │ │ KCC (Kisan Credit Card)         │ │
  │ │ ke liye aapko chahiye:          │ │
  │ │                                 │ │
  │ │  •  Aadhaar / Voter ID card     │ │
  │ │  •  Zameen ke kaagaz (7/12)     │ │
  │ │  •  Fasal ka praman-patra       │ │
  │ │  •  Bank passbook (6 months)    │ │
  │ │  •  Passport size photos ×2     │ │
  │ │                                 │ │
  │ │  Aur kuch poochna hai?          │ │
  │ └─────────────────────────────────┘ │
  │   [Source: RBI KCC Circular 2023]   │   ← Source tag below bubble
  └─────────────────────────────────────┘

  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  ┌─────────────────────────────────────┐
  │ 🤖                                  │   ← TYPING INDICATOR
  │  ┌───────┐                          │     Shown while AI generates
  │  │ ● ● ● │                          │     Three animated dots in bubble
  │  └───────┘                          │     Timeout: 30s → error msg
  └─────────────────────────────────────┘

  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CONTEXTUAL FOLLOW-UP CHIPS
  (appear ONLY after AI responds)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌───────────────────────────────────────┐
  │  ─── आगे पूछें / Suggested ───        │
  │  ┌────────────────────┐ ┌──────────┐  │
  │  │  Kitna loan milega?│ │Interest? │  │   ← Contextual to AI response
  │  └────────────────────┘ └──────────┘  │
  └───────────────────────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT BAR  (sticky above bottom nav)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═════════════════════════════════════════╗
║  ┌────────────────────────────────┐[🎤] ║
║  │  अपना सवाल लिखें...            │     ║   ← Text input, 48dp height
║  └────────────────────────────────┘[➤] ║   ← Send arrow button 48x48dp
╚═════════════════════════════════════════╝
   Input: flex grow, border 1.5dp, radius 10dp
   Mic [🎤]: 52×52dp circle, bg #2D7A3E, white icon
   Mic ACTIVE: red pulsing circle bg #C62828 + ripple
   Send [➤]: 48×48dp, bg #2D7A3E, white arrow


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  VOICE INPUT ACTIVE STATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═════════════════════════════════════════╗
║  ┌────────────────────────────────┐[🔴] ║
║  │  ~~~~ बोल रहे हैं... ~~~~      │     ║   ← Waveform in input area
║  └────────────────────────────────┘[■] ║   ← Stop button replaces send
╚═════════════════════════════════════════╝
   Stops on: second tap OR 3s silence
   Transcribed text then appears in field
   User can edit before tapping send


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  FOOTER / BOTTOM NAVIGATION  64dp fixed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═════════════════════════════════════════╗
║                                         ║
║  [ 🌾 Loan  ]  [💬 Ask AI ]  [📊 Risk] ║
║   Analyzer      Kisan AI    Simulator   ║
║                                         ║
╚═════════════════════════════════════════╝
                   ^ ACTIVE ^
                   Green icon, 11sp Bold
   Inactive: Grey icon, 11sp Regular
```

---

## Ask Kisan AI — Empty / No-Chat State

```
  ┌─────────────────────────────────────┐
  │                                     │
  │     [  🤖  Robot + speech bubble  ] │   ← Friendly illustration
  │         SVG, green accent           │
  │                                     │
  │   कुछ भी पूछिए                      │   ← Headline 18sp Bold
  │   Ask Anything                      │
  │                                     │
  │   KCC लोन, ब्याज दर, दस्तावेज़ —    │   ← Body 14sp, secondary color
  │   कोई भी सवाल।                      │
  │   KCC loans, rates, documents —     │
  │   any question.                     │
  │                                     │
  │  ┌────────────┐ ┌─────────────────┐ │
  │  │ What is    │ │  Am I eligible? │ │   ← Quick-start chips
  │  │   KCC?     │ │                 │ │
  │  └────────────┘ └─────────────────┘ │
  │  ┌──────────────────────┐           │
  │  │  Which documents?    │           │
  │  └──────────────────────┘           │
  │                                     │
  └─────────────────────────────────────┘
```

---

## Ask Kisan AI — Desktop Layout  768px+

```
╔══════════════════════════════════════════════════════════════════╗
║  [🌱]  KisanCredit AI                          [Language ▾]     ║
╠═══════════╦══════════════════════════════════════════════════════╣
║           ║                                                      ║
║  🌾 Loan  ║         CHAT AREA — centred, max 720px              ║
║  Analyzer ║  ┌──────────────────────────────────────────────┐   ║
║           ║  │  🤖 [AI Welcome bubble — left]               │   ║
║  💬 Ask   ║  │                                              │   ║
║  Kisan AI ║  │             [User message — right]           │   ║
║  [ACTIVE] ║  │  🤖 [AI response bubble — left]              │   ║
║           ║  │             [User message — right]           │   ║
║  📊 Risk  ║  │  🤖 [AI response bubble]                     │   ║
║  Simulatr ║  │  ● ● ● [typing indicator]                    │   ║
║           ║  └──────────────────────────────────────────────┘   ║
║ Popular   ║  ┌──────────────────────────────────────────────┐   ║
║ Questions ║  │  [Type your question...]          [🎤]  [➤]  │   ║
║ ──────────║  └──────────────────────────────────────────────┘   ║
║ [KCC?]    ║         Input pinned to bottom of chat container    ║
║ [Eligible]║                                                      ║
║ [Docs?]   ║  Suggested chips in left sidebar as Popular Qs      ║
╚═══════════╩══════════════════════════════════════════════════════╝
```

---
---

# PAGE 3 — RISK SIMULATOR
## Mobile View  |  360px width

```
╔═════════════════════════════════════════╗
║              HEADER  56dp               ║
║                                         ║
║  [🌱]    KisanCredit AI    [हिं ▾]     ║
║                                         ║
╚═════════════════════════════════════════╝
   Header: FIXED on Risk Simulator page


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PAGE TITLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📊 Risk Simulator                       ← H1, 22sp Bold, #1A2E1C
     Simulate loan risk scenarios         ← Subtitle, 14sp, #4A5E4C

  ──────────────────────────────────────


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 1 — GEOGRAPHY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ── Geography ─────────────────────────

  ┌──────────────────┐  ┌──────────────┐
  │   State      ▾   │  │ District  ▾  │   ← Two-column dropdowns
  └──────────────────┘  └──────────────┘   Each 56dp height, radius 10dp
                                            District locked until State set


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 2 — CROP & SEASON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ── Crop & Season ──────────────────────

  ┌──────────────────┐  ┌──────────────┐
  │  Crop Type   ▾   │  │  Season   ▾  │   ← Two-column dropdowns
  └──────────────────┘  └──────────────┘   Season: Kharif / Rabi / Zaid


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INPUT SECTION 3 — RISK VARIABLE SLIDERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ── Risk Variables ─────────────────────

  ┌─────────────────────────────────────┐
  │                                     │
  │  🌧  Rainfall Level                 │   ← Slider 1 label, 14sp
  │      Current:  Below Normal         │   ← Live value label, 14sp Bold
  │                                     │
  │  Very Low                  Very High│   ← Min/Max labels, 12sp
  │  ├────●────────────────────────┤    │   ← Track 6dp, filled: #2D7A3E
  │      ^                              │     Thumb: 24dp circle, white
  │  Value tooltip above thumb          │     Touch target: 48×48dp
  │                                     │
  └─────────────────────────────────────┘

  ┌─────────────────────────────────────┐
  │                                     │
  │  📈  Market Price Volatility        │   ← Slider 2
  │      Current:  Moderate             │
  │                                     │
  │  Stable                    Volatile │
  │  ├──────────────●──────────────┤    │   ← Thumb centered = Moderate
  │                                     │
  └─────────────────────────────────────┘

  ┌─────────────────────────────────────┐
  │                                     │
  │  🧪  Input Cost Pressure            │   ← Slider 3
  │      Current:  High                 │
  │                                     │
  │  Low                           High │
  │  ├────────────────────────●────┤    │   ← Thumb near right = High
  │                                     │
  └─────────────────────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PRIMARY CTA BUTTON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────────────────────────────┐
  │                                     │
  │    📊   Simulate Risk  →            │   ← Full width, 56dp, #2D7A3E bg
  │                                     │     Spinner when processing
  └─────────────────────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  RESULT CARD  (renders after Simulate tap)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ─ ─ ─ ─ ─  Risk Result  ─ ─ ─ ─ ─ ─

  ┌─────────────────────────────────────┐
  │                                     │
  │  RISK SCORE                         │   ← Label, 12sp SemiBold
  │                                     │
  │          🔴   72                    │   ← Score number: Display 28sp Bold
  │              HIGH                   │   ← Risk label: 16sp, #E64A19
  │                                     │     Color changes by score range:
  │                                     │     0-20   Deep Green #1B5E20
  │                                     │     21-40  Green      #388E3C
  │                                     │     41-60  Amber      #F9A825
  │                                     │     61-80  Orange     #E64A19
  │                                     │     81-100 Red        #B71C1C
  │                                     │
  │  ──────────────────────────────────  │
  │                                     │
  │  ── Risk Breakdown ──               │   ← Sub-section label
  │                                     │
  │       ╭──────────────╮              │   ← DONUT / RING CHART
  │     ╭─┤              ├─╮            │     3 colour bands:
  │     │ │  Score:  72  │ │            │     🔴 Outer ring = Weather
  │     │ │              │ │            │     🟡 Mid ring   = Market
  │     ╰─┤              ├─╯            │     🟠 Inner ring = Cost
  │       ╰──────────────╯              │     Rendered via st.plotly_chart
  │                                     │     or st.altair_chart
  │                                     │
  │  ──────────────────────────────────  │
  │                                     │
  │  🌧  Weather Risk                   │   ← BAR BREAKDOWN
  │      ████████████████░░░░░░   40%   │     Progress bars, color-coded
  │                                     │
  │  📈  Market Risk                    │
  │      ██████████░░░░░░░░░░░░   22%   │
  │                                     │
  │  💰  Cost Pressure                  │
  │      █████░░░░░░░░░░░░░░░░░   10%   │
  │                                     │
  │  ──────────────────────────────────  │
  │                                     │
  │  ── What This Means ──              │   ← Narrative label
  │                                     │
  │  Based on this scenario, the        │   ← Plain-language text, 14sp
  │  default probability is elevated.   │     #1A2E1C, max 66 chars/line
  │  Recommend shorter loan tenure or   │
  │  weather insurance cover.           │
  │                                     │
  │  ──────────────────────────────────  │
  │                                     │
  │  ┌─────────────────────────────┐    │
  │  │   📥   Export PDF Report    │    │   ← Secondary CTA, full width
  │  └─────────────────────────────┘    │     Outlined style (green border)
  │                                     │
  └─────────────────────────────────────┘
       Card: bg White, border 1.5dp #DDE5D5
       radius 16dp, shadow 0 2px 12px rgba(0,0,0,0.08)
       padding 20dp


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  EMPTY STATE  (before simulation runs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ┌─────────────────────────────────────┐
  │                                     │
  │    [  📊  Bar chart outline SVG  ]  │   ← Green illustrative art
  │                                     │
  │   एक परिदृश्य चुनें                  │   ← Headline 18sp Bold
  │   Choose a Scenario                 │
  │                                     │
  │   भूगोल और फसल चुनें, फिर           │   ← Body 14sp, secondary
  │   रिस्क कारक सेट करें।               │
  │   Select geography and crop,        │
  │   then set risk factors.            │
  │                                     │
  └─────────────────────────────────────┘


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  FOOTER / BOTTOM NAVIGATION  64dp fixed
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔═════════════════════════════════════════╗
║                                         ║
║  [ 🌾 Loan  ]  [💬 Ask AI]  [📊 Risk ] ║
║   Analyzer      Kisan AI    Simulator   ║
║                                         ║
╚═════════════════════════════════════════╝
                               ^ ACTIVE ^
                               Green icon, 11sp Bold
   Inactive: Grey icon, 11sp Regular
```

---

## Risk Simulator — Desktop Layout  768px+

```
╔══════════════════════════════════════════════════════════════════╗
║  [🌱]  KisanCredit AI                          [Language ▾]     ║
╠═══════════╦══════════════════════════════════════════════════════╣
║           ║                                                      ║
║  🌾 Loan  ║  INPUT PANEL (left 40%)   RESULT PANEL (right 60%)  ║
║  Analyzer ║  ─────────────────────    ──────────────────────     ║
║           ║  [State ▾][District ▾]    ┌───────────────────────┐  ║
║  💬 Ask   ║                           │  RISK SCORE           │  ║
║  Kisan AI ║  [Crop ▾][Season ▾]       │                       │  ║
║           ║                           │       🔴   72         │  ║
║  📊 Risk  ║  🌧 Rainfall              │           HIGH        │  ║
║  Simulatr ║  VLow──●──────VHigh       │                       │  ║
║  [ACTIVE] ║                           │  [Donut Chart 200px]  │  ║
║           ║  📈 Market Volatility      │                       │  ║
║           ║  Stbl──────●──Volat        │  🌧 Weather:  40%    │  ║
║           ║                           │  📈 Market:   22%    │  ║
║           ║  🧪 Input Cost Pressure   │  💰 Cost:     10%    │  ║
║           ║  Low────────────●High     │                       │  ║
║           ║                           │  Narrative text...    │  ║
║           ║  ← Sliders update result  │                       │  ║
║           ║    in real-time           │  [📥 Export PDF]      │  ║
║           ║    No Simulate btn on     └───────────────────────┘  ║
║           ║    desktop                Export always visible       ║
╚═══════════╩══════════════════════════════════════════════════════╝
  Donut chart: 200×200px on desktop (vs small on mobile)
  Sliders update results live — no separate CTA on desktop
```

---
---

# SHARED STATES & OVERLAYS

## Language Selection Modal — First Launch  (Full Screen)

```
╔═════════════════════════════════════════╗
║                                         ║
║                                         ║
║           🌱  KisanCredit AI            ║   ← Logo + App Name
║                                         ║
║       अपनी भाषा चुनें                   ║   ← H1, 22sp Bold
║       Choose your language              ║   ← Subtitle 14sp
║                                         ║
║   ┌──────────────┐   ┌──────────────┐   ║
║   │  हिंदी        │   │   English    │   ║   ← Language tiles, 2-col grid
║   │  [AUTO ✓]   │   │              │   ║     Auto-detected tile highlighted
║   └──────────────┘   └──────────────┘   ║     with green border
║   ┌──────────────┐   ┌──────────────┐   ║
║   │  मराठी       │   │   తెలుగు     │   ║
║   └──────────────┘   └──────────────┘   ║
║   ┌──────────────┐   ┌──────────────┐   ║
║   │   தமிழ்     │   │   ಕನ್ನಡ      │   ║
║   └──────────────┘   └──────────────┘   ║
║   ┌──────────────┐   ┌──────────────┐   ║
║   │   বাংলা     │   │  ગુજરાતી    │   ║
║   └──────────────┘   └──────────────┘   ║
║                                         ║
║   ┌─────────────────────────────────┐   ║
║   │  ✓  Confirm / जारी रखें         │   ║   ← Primary CTA button
║   └─────────────────────────────────┘   ║
║                                         ║
╚═════════════════════════════════════════╝
  Tile: 48dp min height, 12dp radius, 1.5dp border
  Selected: #2D7A3E border + #E8F5EC bg
  Stored in localStorage; persists across sessions
```

---

## Error State — Network Error  (Inline)

```
  ┌─────────────────────────────────────┐
  │                                     │
  │     [  📶✗  WiFi-off icon, amber ]  │
  │                                     │
  │   इंटरनेट कनेक्शन नहीं              │   ← Headline 18sp Bold
  │   No internet connection            │
  │                                     │
  │   कृपया अपना नेटवर्क जांचें और      │   ← Body 14sp secondary
  │   दोबारा कोशिश करें।                │
  │   Check your connection & retry.   │
  │                                     │
  │   ┌─────────────────────────────┐   │
  │   │   🔄  दोबारा / Retry        │   │   ← Primary CTA
  │   └─────────────────────────────┘   │
  │                                     │
  └─────────────────────────────────────┘
```

---

## Error State — Form Validation  (Inline Field)

```
  फसल / Crop                              ← Field label

  ┌─────────────────────────────────────┐
  │   [No crop selected]                │   ← Input border RED, 2dp
  └─────────────────────────────────────┘
  ⚠  कृपया एक फसल चुनें                  ← Error text 12sp, #C62828
     Please select a crop               ← Shown on blur, not just submit
```

---
---

# STREAMLIT COMPONENT MAPPING

```
  UI Element              Streamlit Widget / Approach
  ─────────────────────────────────────────────────────────────
  Header bar              st.markdown + custom CSS sticky header
  App title + logo        st.columns + st.image + st.markdown
  Language selector       st.selectbox in header col or sidebar
  Crop grid               st.columns(3) + st.button per crop
  Farm size picker        st.number_input (step=0.5, min=0.5)
  Unit tab switcher       st.radio (horizontal layout)
  State / District        st.selectbox (district disabled if no state)
  Land ownership radio    st.radio
  Annual income input     st.number_input (optional, numeric)
  Skip link               st.markdown hyperlink style
  Primary CTA button      st.button + custom CSS for full-width green
  Status badge            st.success / st.warning / st.error
  Loan amount display     st.metric  (large number display)
  Result card             st.container + st.columns inside
  Document checklist      st.expander (collapsible accordion)
  Share / Print buttons   st.columns + st.button
  Chat bubbles            st.chat_message("user") / ("assistant")
  Chat input bar          st.chat_input (Streamlit >= 1.25)
  Quick chips             st.button in st.columns (horizontal)
  Typing indicator        st.spinner or animated markdown
  Follow-up chips         st.button row below AI message
  Risk sliders            st.slider (with min, max, step, format)
  Slider value display    st.write / st.metric above each slider
  Donut / ring chart      st.plotly_chart (go.Pie with hole=0.6)
  Risk bar breakdown      st.progress + st.columns for label+pct
  Narrative text          st.info / st.markdown in result card
  Export PDF button       st.download_button
  Bottom navigation       CSS sticky footer via st.markdown HTML
  Language modal          st.dialog (Streamlit >= 1.29) or session state
  Network error toast     st.toast (Streamlit >= 1.27)
  Form validation error   st.error below relevant widget
  ─────────────────────────────────────────────────────────────
  Note: Bottom navigation sticky footer requires
        st.markdown(unsafe_allow_html=True) with custom CSS.
        All custom styling via st.markdown + <style> block.
```

---

*KisanCredit AI — Low-Fidelity Wireframes v1.0*
*Mobile-first · Farmer-first · Streamlit-compatible · No code*
