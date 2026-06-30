# KisanCredit AI — Frontend Product Requirements Document

**Version:** 1.0
**Document Type:** Frontend PRD / UX Specification
**Prepared by:** Senior Product Designer & UX Architect
**Audience:** Hackathon Design & Development Team
**Status:** Ready for Implementation

---

## Table of Contents

1. Executive Summary
2. Design Philosophy
3. User Personas
4. User Journeys
5. Information Architecture
6. Navigation Structure
7. Color System
8. Typography Guidelines
9. Component Library
10. Page-Wise Layout Specifications
    - 10.1 Loan Analyzer
    - 10.2 Ask Kisan AI
    - 10.3 Risk Simulator
11. Empty States
12. Error States
13. Multilingual Framework
14. Accessibility Considerations
15. Mobile Responsiveness
16. Interaction Principles

---

## 1. Executive Summary

KisanCredit AI is a multilingual farmer loan advisory platform designed to democratize access to agricultural credit information. The frontend must bridge a significant digital literacy gap — serving farmers who may be first-time smartphone users, CSC (Common Service Centre) operators who act as intermediaries, and agricultural stakeholders who need portfolio-level insights.

The three core pages — **Loan Analyzer**, **Ask Kisan AI**, and **Risk Simulator** — must each feel instantly usable without any onboarding, readable under direct sunlight on low-cost Android devices, and trustworthy enough for a farmer to make a significant financial decision.

---

## 2. Design Philosophy

### 2.1 Core Principles

**Farmer-First**
Every design decision is evaluated through the lens of a farmer standing in a field with a low-end Android phone and limited data. If a feature confuses them, it is redesigned, not explained.

**Mobile-First**
The primary viewport is 360–390px wide. Desktop is a secondary experience, primarily for CSC Operators. All layouts begin at 360px and scale up.

**Extremely Simple**
One primary action per screen. No nested menus. No jargon. No hidden features. Complexity is dissolved before it reaches the user.

**Recommendation-Focused**
The platform does not present raw data — it presents verdicts. "You are eligible for ₹1.2L" is shown before the breakdown. Conclusions lead; data follows.

**Large Readable UI**
Minimum body text: 16sp. Primary actions: 18–22sp. Touch targets: minimum 48×48dp. High-contrast text on all backgrounds.

**Multilingual**
UI is language-agnostic by design. Every text element uses a translation token. Language can switch at any time without layout breakage. Supported languages at launch: Hindi, English, Marathi, Telugu, Tamil, Kannada, Bengali, Gujarati.

---

## 3. User Personas

### Persona 1 — Ramesh, the Smallholder Farmer
**Age:** 42
**Location:** Vidarbha, Maharashtra
**Device:** Redmi 9A (4-inch screen, Android 10)
**Connectivity:** 2G/3G, intermittent
**Digital Literacy:** Uses WhatsApp and makes calls. Has never filled an online form alone.
**Primary Goal:** Find out if he qualifies for a Kisan Credit Card loan and how much he can get.
**Pain Points:** Bank officials speak in complex language. He doesn't know what documents are needed. He fears rejection.
**Key Behaviour:** Speaks in Marathi. Will abandon a task if it requires more than 3 taps to reach a meaningful answer.
**Success Looks Like:** He sees a clear number and a list of what to bring to the bank — in Marathi.

---

### Persona 2 — Priya, the CSC Operator
**Age:** 28
**Location:** Raipur, Chhattisgarh
**Device:** Samsung Galaxy A33 + 14-inch laptop (dual setup)
**Connectivity:** Broadband at CSC kiosk
**Digital Literacy:** Comfortable with government portals, digital forms, and basic spreadsheets.
**Primary Goal:** Help 10–20 farmers per day assess loan eligibility and generate printable summaries.
**Pain Points:** Farmers arrive with incomplete information. Each farmer interaction must be fast. She needs to guide without overwhelming the farmer sitting beside her.
**Key Behaviour:** Uses the platform in Hindi-English mix. Needs efficiency — quick input, instant output.
**Success Looks Like:** She completes a full loan assessment in under 4 minutes per farmer and can print or share the result via WhatsApp.

---

### Persona 3 — Arjun, the Agricultural Stakeholder
**Age:** 51
**Location:** Bengaluru (NABARD / Agri-lending institution)
**Device:** MacBook Pro + iPhone 14
**Connectivity:** High-speed broadband
**Digital Literacy:** Power user. Comfortable with dashboards and data.
**Primary Goal:** Understand risk patterns across farmer profiles and geographies to support credit policy decisions.
**Pain Points:** Existing reports are static PDFs. He wants interactive risk exploration.
**Key Behaviour:** Uses English. Needs dense information presented clearly.
**Success Looks Like:** He can simulate how a drought or crop failure scenario changes loan risk across a region.

---

## 4. User Journeys

### Journey 1 — Ramesh: First-Time Loan Assessment (Farmer)

```
Entry: Opens link shared by CSC operator on WhatsApp
  ↓
Language Selection Modal (auto-detected, confirmable)
  ↓
Home / Loan Analyzer Page
  ↓
Enters farm size (number picker — no keyboard needed)
  ↓
Selects crop from visual grid (icons + labels)
  ↓
Selects state from dropdown
  ↓
Enters land ownership (radio buttons: Owned / Leased)
  ↓
[TAP: Analyze My Loan →]
  ↓
Result Card appears: Eligible Amount + Loan Type + Bank Recommendation
  ↓
Taps "What documents do I need?" → Document Checklist expands
  ↓
Taps Share → WhatsApp share intent opens
```

**Critical Drop-off Points:** Step 3 (crop selection confusion), Step 6 (result not being clear enough)
**Design Response:** Crop grid uses both icon and regional name. Result uses bold primary number at top.

---

### Journey 2 — Priya: Assisted Assessment (CSC Operator)

```
Entry: Opens app directly on laptop browser
  ↓
No language modal (defaults to Hindi, changeable in header)
  ↓
Loan Analyzer — enters farmer data in under 2 minutes
  ↓
Result page — reviews with farmer sitting beside her
  ↓
Switches to Ask Kisan AI — types farmer's specific question
  ↓
AI provides answer in farmer's selected language
  ↓
Taps Print Summary → Printer-optimised result card opens
  ↓
WhatsApp Share → sends to farmer's number
```

---

### Journey 3 — Arjun: Risk Simulation (Stakeholder)

```
Entry: Direct URL, desktop browser
  ↓
Risk Simulator page
  ↓
Selects geography (State → District)
  ↓
Sets crop type and season
  ↓
Adjusts risk sliders (rainfall, market price, input costs)
  ↓
Risk Score updates in real-time
  ↓
Reads Risk Breakdown (donut chart + narrative)
  ↓
Exports PDF summary of simulation
```

---

## 5. Information Architecture

```
KisanCredit AI
│
├── 🌾 Loan Analyzer          [Primary — All Personas]
│   ├── Input Form
│   │   ├── Farm Size Input
│   │   ├── Crop Selector (Visual Grid)
│   │   ├── State / District
│   │   ├── Land Ownership
│   │   └── Annual Income (optional)
│   ├── Analyze CTA
│   └── Result View
│       ├── Eligibility Card (Primary)
│       ├── Loan Amount Range
│       ├── Recommended Scheme
│       ├── Interest Rate
│       ├── Document Checklist (collapsible)
│       └── Action Bar (Share / Print / Ask AI)
│
├── 💬 Ask Kisan AI           [All Personas — Conversational]
│   ├── Chat Interface
│   │   ├── Message History
│   │   ├── AI Response Cards
│   │   └── Source Tags (scheme names)
│   ├── Input Area
│   │   ├── Text Input
│   │   └── Voice Input Button
│   └── Suggested Questions (Quick Chips)
│
└── 📊 Risk Simulator         [Stakeholders / CSC Operators]
    ├── Geography Selector
    ├── Scenario Inputs
    │   ├── Crop Type
    │   ├── Season
    │   ├── Rainfall Slider
    │   ├── Market Price Slider
    │   └── Input Cost Slider
    ├── Risk Score Display (Live)
    ├── Risk Breakdown Chart
    ├── Narrative Interpretation
    └── Export Action
```

---

## 6. Navigation Structure

### 6.1 Bottom Navigation Bar (Mobile — Primary)

The bottom navigation is the sole primary navigation surface on mobile. It is persistent across all three pages.

```
┌─────────────────────────────────────────┐
│  🌾 Loan       💬 Ask AI    📊 Risk     │
│  Analyzer      Kisan        Simulator   │
└─────────────────────────────────────────┘
```

**Specifications:**
- Height: 64dp
- Background: White (#FFFFFF) with top border 1dp / #E0E0E0
- Active tab: Primary Green icon + label
- Inactive tab: Medium Grey icon + label
- Touch target per tab: Full third of bar width
- Label: Always visible (never icon-only)
- Font: 11sp Bold for active, 11sp Regular for inactive

### 6.2 Header Bar (Mobile)

```
┌─────────────────────────────────────────┐
│  [🌱 Logo]  KisanCredit AI    [हिं ▼]  │
└─────────────────────────────────────────┘
```

**Specifications:**
- Height: 56dp
- Background: Primary Green (#2D7A3E)
- Logo: 32×32dp, left-aligned with 16dp padding
- App name: 18sp Bold, White, centered
- Language Selector: Right-aligned, pill button, 14sp, White border

### 6.3 Desktop Navigation (Sidebar — CSC / Stakeholder)

On screens ≥ 768px, navigation shifts to a left sidebar, 240px wide.

```
┌──────────────────────────────────────────────────────┐
│ [Logo] KisanCredit AI              [Language ▾]      │
├──────────┬───────────────────────────────────────────│
│ 🌾 Loan  │                                           │
│ Analyzer │          Page Content                     │
│          │                                           │
│ 💬 Ask   │                                           │
│ Kisan AI │                                           │
│          │                                           │
│ 📊 Risk  │                                           │
│ Simulator│                                           │
└──────────┴───────────────────────────────────────────┘
```

---

## 7. Color System

### 7.1 Brand Palette

| Token                | Hex       | Usage                                                  |
|----------------------|-----------|--------------------------------------------------------|
| `--color-primary`    | `#2D7A3E` | Header, active nav, primary CTAs, key icons            |
| `--color-primary-lt` | `#E8F5EC` | Card backgrounds, selected states, light highlights    |
| `--color-secondary`  | `#F9A825` | Warnings, risk indicators (medium risk)                |
| `--color-danger`     | `#C62828` | High risk, errors, destructive actions                 |
| `--color-success`    | `#388E3C` | Eligibility confirmed, positive results                |
| `--color-surface`    | `#FFFFFF` | All card and page backgrounds                          |
| `--color-bg`         | `#F5F7F2` | Page-level background (off-white with green warmth)    |
| `--color-border`     | `#DDE5D5` | Card borders, dividers, input borders                  |

### 7.2 Text Colors

| Token                   | Hex       | Usage                                                  |
|-------------------------|-----------|--------------------------------------------------------|
| `--text-primary`        | `#1A2E1C` | All body copy, headlines                               |
| `--text-secondary`      | `#4A5E4C` | Supporting labels, captions, helper text               |
| `--text-disabled`       | `#9E9E9E` | Inactive elements, placeholder text                    |
| `--text-on-primary`     | `#FFFFFF` | Text on green backgrounds (header, primary buttons)    |
| `--text-link`           | `#1565C0` | Inline links, tappable secondary actions               |

### 7.3 Risk Color Scale (Risk Simulator)

| Risk Level   | Color     | Hex       |
|--------------|-----------|-----------|
| Very Low     | Deep Green| `#1B5E20` |
| Low          | Green     | `#388E3C` |
| Moderate     | Amber     | `#F9A825` |
| High         | Orange    | `#E64A19` |
| Very High    | Red       | `#B71C1C` |

### 7.4 Color Usage Rules

- Primary Green is never used for body text (accessibility)
- Never use red for decorative purposes; red signals danger only
- Amber/Yellow is used only for warnings, never for CTAs
- Background #F5F7F2 ensures cards on white read as distinct surfaces

---

## 8. Typography Guidelines

### 8.1 Font Stack

**Primary Font:** Noto Sans (supports all 8 target languages with consistent metrics)
**Fallback Stack:** `'Noto Sans', 'Hind', 'Mukta', system-ui, sans-serif`

Rationale: Noto Sans has complete coverage for Devanagari (Hindi/Marathi), Telugu, Tamil, Kannada, Bengali, and Gujarati scripts, ensuring consistent layout across language switches.

### 8.2 Type Scale

| Level          | Size  | Weight  | Line Height | Usage                                        |
|----------------|-------|---------|-------------|----------------------------------------------|
| Display        | 28sp  | 700     | 36px        | Loan amount result (primary number)          |
| Heading 1      | 22sp  | 700     | 30px        | Page titles, section headers                 |
| Heading 2      | 18sp  | 600     | 26px        | Card titles, result section labels           |
| Heading 3      | 16sp  | 600     | 24px        | Sub-section labels, input group labels       |
| Body Large     | 16sp  | 400     | 24px        | Primary body text, descriptions              |
| Body Regular   | 14sp  | 400     | 22px        | Supporting information, list items           |
| Caption        | 12sp  | 400     | 18px        | Footnotes, source attribution, timestamps    |
| Button Primary | 16sp  | 700     | —           | Primary CTA labels                           |
| Button Secondary| 14sp | 600     | —           | Secondary action labels                      |
| Label          | 12sp  | 600     | 18px        | Form field labels, tags, status badges       |

### 8.3 Typography Rules

- Minimum body text: 16sp (never smaller for primary content)
- Maximum line length: 66 characters for readability
- Text alignment: Left-aligned always; never justified (breaks Devanagari script)
- Do not use italic for UI elements (poor legibility in Indian scripts)
- Numerals: Always use locale-appropriate numeral system when localising (e.g., Devanagari numerals for Hindi if required by user testing)
- Loan amounts: Always display in Indian numbering system (₹1,20,000 not ₹120,000)

---

## 9. Component Library

### 9.1 Primary CTA Button

**Purpose:** The single main action on any screen (Analyze, Send, Simulate)

```
Specifications:
- Height: 56dp
- Width: Full-width (16dp margin on each side) on mobile
- Border radius: 12dp
- Background: --color-primary (#2D7A3E)
- Text: --text-on-primary, 16sp Bold, centered
- Icon: Optional leading icon, 24dp, left of label
- Touch feedback: Ripple effect, slightly darkened background (#245F32)
- Loading state: Text replaced by spinner (24dp, white)
- Disabled state: Background #BDBDBD, text #757575
```

### 9.2 Input Field

**Purpose:** All text/numeric data entry

```
Specifications:
- Height: 56dp
- Border: 1.5dp, --color-border
- Border radius: 10dp
- Background: White
- Label: Above field, 12sp SemiBold, --text-secondary
- Placeholder: --text-disabled, 16sp Regular
- Active/focus border: 2dp, --color-primary
- Error border: 2dp, --color-danger
- Error message: Below field, 12sp, --color-danger
- Padding: 16dp horizontal
```

### 9.3 Crop Selector Grid

**Purpose:** Farmer-friendly crop selection without typing

```
Specifications:
- Grid: 3 columns, auto rows
- Each tile: 100dp × 100dp
- Tile background: --color-surface
- Tile border: 1dp, --color-border, radius 12dp
- Icon: 40×40dp emoji or SVG illustration, centered
- Label: Below icon, 12sp SemiBold, --text-primary, centered
- Selected state: Border 2.5dp --color-primary, background --color-primary-lt
- Max visible: 9 crops (3×3), "Show More" option if additional
```

Crops to include in initial grid (sorted by national prevalence):
Paddy / Wheat / Cotton / Sugarcane / Maize / Soybean / Groundnut / Vegetables / Pulses

### 9.4 Result Card

**Purpose:** Primary output display after analysis

```
Specifications:
- Background: White
- Border: 1.5dp, --color-border
- Border radius: 16dp
- Shadow: 0 2px 12px rgba(0,0,0,0.08)
- Padding: 20dp
- Structure (top to bottom):
  1. Status Badge (Eligible / Not Eligible / Partially Eligible)
  2. Loan Amount (Display size, --color-primary)
  3. Scheme Name (Heading 3)
  4. Interest Rate (Body Large)
  5. Divider
  6. Action Buttons (Share / Document Checklist)
```

### 9.5 Status Badge

```
Eligible:        Green pill  (#E8F5EC bg, #2D7A3E text, ✓ icon)
Not Eligible:    Red pill    (#FFEBEE bg, #C62828 text, ✗ icon)
Partially:       Amber pill  (#FFF8E1 bg, #F9A825 text, ! icon)
Processing:      Grey pill   (#FAFAFA bg, #757575 text, spinner)
```

### 9.6 Slider Component (Risk Simulator)

```
Specifications:
- Track height: 6dp
- Track background: #E0E0E0
- Filled track: --color-primary
- Thumb: 24dp circle, white, 2dp primary border, 4dp shadow
- Labels: Min/Max displayed below track ends, 12sp
- Current value: Displayed above thumb in tooltip, 14sp Bold
- Step: Configurable per slider
- Touch target: 48×48dp centred on thumb
```

### 9.7 Chat Bubble — Ask Kisan AI

**User Message:**
```
- Background: --color-primary (#2D7A3E)
- Text: White
- Alignment: Right
- Border radius: 16dp 16dp 4dp 16dp
- Max width: 75% of container
- Padding: 12dp 16dp
```

**AI Response:**
```
- Background: #F5F7F2
- Text: --text-primary
- Alignment: Left
- Border radius: 16dp 16dp 16dp 4dp
- Max width: 85% of container
- Padding: 12dp 16dp
- Source tag: Below bubble, 11sp, italic, --text-secondary
```

### 9.8 Voice Input Button

```
- Size: 52×52dp circle
- Background: --color-primary
- Icon: Microphone (24dp, white)
- Active/Recording state: Pulsing red background (#C62828) with ripple animation
- Tooltip: "बोलें / Speak" on long press
```

### 9.9 Quick Suggestion Chips

```
- Height: 36dp
- Padding: 0 16dp
- Border: 1dp, --color-border
- Border radius: 18dp (fully rounded)
- Background: White
- Text: 13sp, --text-secondary
- On tap: Fills input field with chip text
- Scrollable row (horizontal scroll, no scrollbar visible)
```

### 9.10 Number Picker (Farm Size Input)

```
- Replaces free-text keyboard input for farm size
- Large minus (−) and plus (+) buttons flanking central value
- Button size: 56×56dp
- Central value: 24sp Bold
- Unit label below: "Acres" / "Bigha" / "Hectares" (selectable)
- Minimum: 0.5, Maximum: 500, Step: 0.5
```

---

## 10. Page-Wise Layout Specifications

### 10.1 Page: Loan Analyzer

**Purpose:** Help farmers determine loan eligibility and amount in under 3 minutes.

**Mobile Layout (360px):**

```
┌─────────────────────────────────┐
│ [Header: KisanCredit AI / Lang] │  ← 56dp
├─────────────────────────────────┤
│                                 │
│  🌾 अपनी फसल चुनें             │  ← Page title, H1, 22sp
│  Select Your Crop               │  ← Subtitle in secondary language
│                                 │
│  ┌───────┬───────┬───────┐      │
│  │  🌾   │  🌿   │  🌱   │      │  ← Crop Grid Row 1
│  │ Paddy │ Wheat │Cotton │      │
│  ├───────┼───────┼───────┤      │
│  │  🎋   │  🌽   │  🫘   │      │  ← Crop Grid Row 2
│  │Sugrc. │ Maize │ Soya  │      │
│  ├───────┼───────┼───────┤      │
│  │  🥜   │  🥦   │  🫛   │      │  ← Crop Grid Row 3
│  │Ground.│ Veg.  │Pulses │      │
│  └───────┴───────┴───────┘      │
│                                 │
│  जमीन का आकार / Farm Size       │  ← Section label
│  [  −  ]  [ 2.5 Acres ]  [ + ] │  ← Number Picker
│  [Acres ▾] [Bigha ▾] [Hectare]  │  ← Unit Tabs
│                                 │
│  राज्य / State                   │
│  [Select your state        ▾]   │  ← Dropdown
│                                 │
│  जिला / District                 │
│  [Select district          ▾]   │  ← Dropdown (enabled after state)
│                                 │
│  भूमि स्वामित्व / Land Ownership  │
│  ◉ Owned (Khud Ki)              │  ← Radio, large tap area
│  ○ Leased (Kiraye Ki)           │
│                                 │
│  सालाना आय / Annual Income      │
│  [Optional — enter amount]      │  ← Text input, keyboard = numeric
│  [Skip this step →]             │  ← Secondary action link
│                                 │
│  ┌─────────────────────────┐    │
│  │  🔍 लोन विश्लेषण करें   │    │  ← Primary CTA Button
│  │     Analyze My Loan     │    │     Full width, 56dp
│  └─────────────────────────┘    │
│                                 │
│    ─── Result appears below ─── │
│                                 │
│  ┌──────────────────────────┐   │
│  │  ✅ आप पात्र हैं          │   │  ← Status Badge
│  │  You are Eligible        │   │
│  │                          │   │
│  │  ₹ 1,20,000              │   │  ← Display size, primary green
│  │  तक का लोन               │   │  ← "up to this loan amount"
│  │                          │   │
│  │  Kisan Credit Card (KCC) │   │  ← Scheme name
│  │  7% प्रति वर्ष           │   │  ← Interest rate
│  │  (2% Govt. Subsidy)      │   │
│  │                          │   │
│  │  ─────────────────────   │   │
│  │                          │   │
│  │  [📋 Documents Needed]   │   │  ← Expandable chevron
│  │  [📤 Share Result]       │   │  ← WhatsApp share
│  │  [💬 Ask Kisan AI]       │   │  ← Navigates to AI chat
│  └──────────────────────────┘   │
│                                 │
├─────────────────────────────────┤
│ [🌾 Loan] [💬 Ask AI] [📊 Risk] │  ← Bottom nav, 64dp
└─────────────────────────────────┘
```

**Document Checklist Expansion (in-page accordion):**

```
┌──────────────────────────────────────┐
│  📋 जरूरी दस्तावेज़ / Documents      │
│  ─────────────────────────────────   │
│  ✓ Aadhaar Card                      │
│  ✓ Land Records (7/12 Utara)         │
│  ✓ Bank Passbook (last 6 months)     │
│  ✓ Passport-size Photographs (2)     │
│  ✓ Crop Sowing Certificate           │
│  ─────────────────────────────────   │
│  [Print Checklist]  [Share on WhatsApp]│
└──────────────────────────────────────┘
```

**Desktop Layout Notes (768px+):**
- Form and result display side by side in a 2-column grid
- Form on left (40%), Result card on right (60%)
- Crop grid expands to 4 columns
- No bottom nav; left sidebar navigation is used

---

### 10.2 Page: Ask Kisan AI

**Purpose:** Conversational AI interface for any agricultural loan question, in any supported language.

**Mobile Layout:**

```
┌─────────────────────────────────┐
│ [Header: KisanCredit AI / Lang] │
├─────────────────────────────────┤
│                                 │
│  ─── Quick Questions ───        │  ← Section label, 12sp
│  [KCC loan kya hai?] [Eligibi..]│  ← Horizontal scrollable chips
│  [Documents needed] [Interest?] │
│                                 │
├─────────────────────────────────┤
│                                 │
│  ┌──────────────────────────┐   │  ← AI Welcome Message
│  │  🤖                      │   │
│  │  नमस्ते! मैं Kisan AI हूँ।   │
│  │  मैं आपके लोन से जुड़े    │
│  │  किसी भी सवाल का जवाब    │
│  │  दे सकता हूँ।            │
│  │                          │
│  │  [Source: KCC Guidelines]│   │  ← Source tag
│  └──────────────────────────┘   │
│                                 │
│         ┌────────────────────┐  │
│         │ KCC loan ke liye   │  │  ← User message (right-aligned)
│         │ kya chahiye?       │  │
│         └────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐   │  ← AI Response
│  │  🤖                      │   │
│  │  KCC (Kisan Credit Card) │   │
│  │  ke liye aapko chahiye:  │   │
│  │                          │   │
│  │  • Aadhaar / Voter ID    │   │
│  │  • Zameen ke kaagaz      │   │
│  │  • Fasal ka praman       │   │
│  │  • Bank passbook         │   │
│  │                          │   │
│  │  Aur kuch poochna hai?   │   │
│  │  [Source: RBI KCC Circ.] │   │
│  └──────────────────────────┘   │
│                                 │
│  [ ... typing indicator ... ]   │  ← Shows when AI is generating
│                                 │
│  ┌─────────────────────────────┐│
│  │ ─────────────────────────  ││  ← SUGGESTED FOLLOW-UPS
│  │ [Kitna loan milega?]       ││  ← Contextual suggestions
│  │ [Interest rate kya hai?]   ││     appear after AI responds
│  └─────────────────────────────┘│
│                                 │
├─────────────────────────────────┤
│ ┌──────────────────────────┐[🎤]│  ← Input row (sticky bottom)
│ │ अपना सवाल लिखें...       │    │
│ └──────────────────────────┘[➤] │
├─────────────────────────────────┤
│ [🌾 Loan] [💬 Ask AI] [📊 Risk] │
└─────────────────────────────────┘
```

**Typing Indicator:**
```
Three animated dots in an AI bubble
Duration before timeout: 30 seconds
Timeout state → "AI is taking longer. Please wait..."
```

**Voice Input Flow:**
1. User taps microphone button
2. Button turns red, pulsing ring animation begins
3. Waveform animation shows in text input area
4. User speaks
5. Tap again or 3-second silence → stops recording
6. Transcribed text appears in input field
7. User can edit before sending

**Desktop Layout Notes:**
- Chat area is centred, max width 720px
- Input is pinned to bottom of chat container
- Quick chips appear in left sidebar as "Popular Questions"
- Option to see conversation history in left sidebar

---

### 10.3 Page: Risk Simulator

**Purpose:** Allow CSC operators and stakeholders to simulate loan risk scenarios by adjusting crop/weather/economic variables.

**Mobile Layout:**

```
┌─────────────────────────────────┐
│ [Header: KisanCredit AI / Lang] │
├─────────────────────────────────┤
│                                 │
│  📊 Risk Simulator              │  ← H1
│  Simulate loan risk scenarios   │  ← Subtitle
│                                 │
│  ── Geography ──────────────── │
│  [State          ▾] [District ▾]│  ← Two-column dropdowns
│                                 │
│  ── Crop & Season ─────────── │
│  [Crop Type      ▾] [Season   ▾]│
│                                 │
│  ─── Risk Variables ─────────  │
│                                 │
│  🌧 Rainfall Level              │  ← Slider Group 1
│  Below Normal      [●──────]    │
│  Very Low   ←─────────→  Very High│
│                                 │
│  📈 Market Price Volatility     │  ← Slider Group 2
│  Moderate          [───●───]    │
│  Stable   ←──────────→ Volatile │
│                                 │
│  🧪 Input Cost Pressure         │  ← Slider Group 3
│  High              [──────●]    │
│  Low     ←─────────────→  High │
│                                 │
│  ┌─────────────────────────┐   │
│  │  📊 Simulate Risk →     │   │  ← Primary CTA
│  └─────────────────────────┘   │
│                                 │
│  ── Risk Result ─────────────  │
│                                 │
│  ┌──────────────────────────┐  │
│  │   RISK SCORE             │  │
│  │                          │  │
│  │      🔴  72              │  │  ← Large score (Display size)
│  │        HIGH              │  │  ← Risk label
│  │                          │  │
│  │  ── Risk Breakdown ──    │  │
│  │  [Donut Chart: 3 bands]  │  │  ← Simple donut / ring chart
│  │  🌧 Weather Risk   : 40% │  │
│  │  📈 Market Risk    : 22% │  │
│  │  💰 Cost Pressure  : 10% │  │
│  │                          │  │
│  │  ── What This Means ──   │  │
│  │  Based on this scenario, │  │  ← Plain-language narrative
│  │  default probability is  │  │
│  │  elevated. Recommend     │  │
│  │  shorter loan tenure or  │  │
│  │  weather insurance.      │  │
│  │                          │  │
│  │  [📥 Export PDF Report]  │  │
│  └──────────────────────────┘  │
│                                 │
├─────────────────────────────────┤
│ [🌾 Loan] [💬 Ask AI] [📊 Risk] │
└─────────────────────────────────┘
```

**Risk Score Color Thresholds:**

| Score Range | Colour     | Label     |
|-------------|------------|-----------|
| 0 – 20      | Deep Green | Very Low  |
| 21 – 40     | Green      | Low       |
| 41 – 60     | Amber      | Moderate  |
| 61 – 80     | Orange     | High      |
| 81 – 100    | Red        | Very High |

**Desktop Layout Notes:**
- Inputs panel on left 40%, results on right 60%
- Sliders update results in real-time (no separate simulate button on desktop)
- Donut chart is larger (200×200px) on desktop
- Export button is always visible on desktop (not below fold)

---

## 11. Empty States

Empty states should never feel like errors. They are warm, helpful, and action-oriented.

### 11.1 Loan Analyzer — Pre-Analysis State

```
Illustration: Simple green field illustration (SVG, non-photographic)
Headline: "अपनी जानकारी भरें" / "Fill in your details"
Body: "ऊपर दिए फॉर्म को भरकर अपनी लोन पात्रता जानें।"
      "Fill the form above to discover your loan eligibility."
CTA: None (form is above, this state occupies result area)
```

### 11.2 Ask Kisan AI — No Conversation Yet

```
Illustration: Friendly robot/AI icon with speech bubble
Headline: "कुछ भी पूछिए / Ask anything"
Body: "KCC लोन, ब्याज दर, जरूरी दस्तावेज़ — कोई भी सवाल।"
      "KCC loans, interest rates, documents — any question."
Quick chips: [What is KCC?] [Am I eligible?] [Which documents?]
```

### 11.3 Risk Simulator — No Simulation Run Yet

```
Illustration: Simple bar chart outline (green, illustrative)
Headline: "एक परिदृश्य चुनें / Choose a scenario"
Body: "भूगोल और फसल चुनें, फिर रिस्क कारक सेट करें।"
      "Select a geography and crop, then set risk factors."
CTA: None (form is above)
```

---

## 12. Error States

Error states must be specific, never generic ("Something went wrong" is forbidden).

### 12.1 Network Error

```
Icon: WiFi off icon, amber colour
Headline: "इंटरनेट कनेक्शन नहीं"
         "No internet connection"
Body: "कृपया अपना नेटवर्क जांचें और दोबारा कोशिश करें।"
     "Please check your connection and try again."
CTA Button: "🔄 दोबारा कोशिश करें / Retry"
```

### 12.2 AI Response Timeout (Ask Kisan AI)

```
Icon: Clock icon, amber
Headline: "AI जवाब देने में देर हो रही है"
         "AI is taking longer than expected"
Body: "सर्वर व्यस्त है। थोड़ी देर बाद पूछें।"
     "Server is busy. Please try again shortly."
CTA: "🔄 Try Again"
Secondary: "📞 Helpline: 1800-XXX-XXXX" (national agri helpline)
```

### 12.3 Form Validation Errors

- Error message appears inline below each field immediately on blur (not only on submit)
- Error text: 12sp, --color-danger, with ⚠ icon
- Field border turns --color-danger

```
Examples:
- Farm size: "कृपया 0.5 से 500 एकड़ के बीच दर्ज करें"
- State: "कृपया अपना राज्य चुनें"
- Crop: "कृपया एक फसल चुनें"
```

### 12.4 No Eligibility Result

```
Icon: Information circle, neutral blue
Headline: "हम पात्रता निर्धारित नहीं कर सके"
         "We could not determine eligibility"
Body: "आपकी जानकारी के आधार पर परिणाम उपलब्ध नहीं है।
      नजदीकी CSC या बैंक से संपर्क करें।"
     "Based on your details, results are unavailable.
      Contact your nearest CSC or bank branch."
CTA: "💬 Ask Kisan AI for guidance"
Secondary Link: "📍 Find Nearest CSC"
```

### 12.5 Language Load Failure

```
Silent fallback to English.
Toast notification (bottom, 3 seconds):
"हिंदी लोड नहीं हुई। English में दिख रहा है।"
"Hindi failed to load. Showing in English."
```

---

## 13. Multilingual Framework

### 13.1 Language Selector Behaviour

- First launch: Language selection modal appears full-screen
- Auto-detects device locale and pre-selects matching language
- User confirms or changes selection
- Language stored in local storage; persists across sessions
- Language can be changed at any time via header pill
- Language change applies instantly without page reload

### 13.2 Language Selection Modal (First Launch)

```
┌─────────────────────────────────────┐
│                                     │
│    🌱 KisanCredit AI                │
│                                     │
│    अपनी भाषा चुनें                 │
│    Choose your language             │
│                                     │
│  ┌──────────┐  ┌──────────┐        │
│  │ हिंदी    │  │ English  │        │
│  └──────────┘  └──────────┘        │
│  ┌──────────┐  ┌──────────┐        │
│  │मराठी    │  │ తెలుగు   │        │
│  └──────────┘  └──────────┘        │
│  ┌──────────┐  ┌──────────┐        │
│  │ தமிழ்   │  │ ಕನ್ನಡ    │        │
│  └──────────┘  └──────────┘        │
│  ┌──────────┐  ┌──────────┐        │
│  │ বাংলা   │  │ ગુજરાતી  │        │
│  └──────────┘  └──────────┘        │
│                                     │
└─────────────────────────────────────┘
```

### 13.3 Text Rendering Considerations

- All UI strings use translation token keys (e.g., `loan_analyzer.cta.primary`)
- No hard-coded text in components
- Devanagari script: line height must be 1.6× (not 1.4×) to accommodate vowel marks above characters
- Tamil and Telugu scripts require slightly larger default font-size (17sp minimum)
- Numbers: use `Intl.NumberFormat` with locale for currency and numeral display
- RTL not required for current language set (all LTR scripts)

---

## 14. Accessibility Considerations

### 14.1 Contrast Ratios

All colour combinations must meet WCAG 2.1 AA minimum (4.5:1 for body text, 3:1 for large text).

| Combination                   | Ratio  | Standard |
|-------------------------------|--------|----------|
| White text on Primary Green   | 7.2:1  | AAA ✓   |
| Primary text on White bg      | 16.1:1 | AAA ✓   |
| Primary text on Light Green bg| 12.4:1 | AAA ✓   |
| Danger text on white          | 5.1:1  | AA ✓    |
| Disabled text on white        | 3.2:1  | AA ✓ (large text only — never used for body)  |

### 14.2 Touch Target Sizes

- All interactive elements: minimum 48×48dp
- Primary CTA: 56dp height, full width
- Bottom navigation tabs: Full 1/3 width × 64dp
- Crop grid tiles: 100×100dp
- Slider thumb: 24dp visual, 48×48dp touch target

### 14.3 Screen Reader Support

- All images and icons have descriptive `aria-label` attributes
- Form inputs have associated `<label>` elements (not placeholder-only)
- Result cards have structured heading hierarchy (h2 > h3)
- Status badges include text, not colour alone
- Voice input has `aria-live` region for transcription feedback

### 14.4 Keyboard Navigation (Desktop/CSC)

- Full tab order follows visual reading order
- Focus indicator: 3dp primary green outline, clearly visible
- Dropdowns and modals trap focus when open
- Escape key closes modals and dropdowns
- Enter/Space activates buttons and crop tiles

### 14.5 Reduced Motion

- Respect `prefers-reduced-motion` media query
- Animations such as the loading spinner and voice pulse reduce to static states when this is set
- Transition durations cut to 0ms when reduced motion is preferred

### 14.6 Offline / Low Connectivity

- Core loan analyzer form works without internet (uses cached scheme data)
- Ask Kisan AI shows a friendly offline message (cannot function offline)
- Network status indicator in header when offline

---

## 15. Mobile Responsiveness

### 15.1 Breakpoints

| Breakpoint | Width      | Device Category                     | Layout Mode    |
|------------|------------|-------------------------------------|----------------|
| xs         | 320–359px  | Very small Android (edge case)       | Compressed mobile |
| sm         | 360–767px  | Primary: Low-cost Android           | Full mobile    |
| md         | 768–1023px | Tablet / CSC Kiosk tablet           | Hybrid         |
| lg         | 1024–1279px| Laptop (CSC / Stakeholder)          | Desktop        |
| xl         | 1280px+    | Wide desktop (Stakeholder)          | Wide desktop   |

### 15.2 Responsive Behaviour Per Component

**Crop Grid:**
- xs/sm: 3 columns
- md: 4 columns
- lg+: 5 columns

**Navigation:**
- xs/sm/md: Bottom tab bar
- lg+: Left sidebar

**Result Card:**
- xs/sm: Full-width card, stacked
- md+: Card with two-column interior (amount + details side by side)

**Sliders (Risk Simulator):**
- xs/sm: Full-width, stacked vertically
- md+: Two columns of sliders

**Chat Interface:**
- xs/sm: Full-width, edge-to-edge
- md+: Centred, max 600px, with padding

### 15.3 Scrolling Behaviour

- Page-level scroll: Vertical only
- Bottom navigation: Fixed (does not scroll away)
- Header: Fixed on Loan Analyzer and Risk Simulator; scrolls away on chat screen (maximises chat area)
- Crop grid: Does not scroll; "Show More" expands in-place

### 15.4 Safe Area Handling

- Bottom navigation has `padding-bottom: env(safe-area-inset-bottom)` for iPhone notch/home bar compatibility
- Header has `padding-top: env(safe-area-inset-top)` to clear status bar

---

## 16. Interaction Principles

### 16.1 Loading Feedback

Every async action must show feedback within 200ms:
- Button tap: Immediate spinner + disabled state
- AI response: "AI सोच रहा है..." typing indicator (three dot animation)
- Page load: Skeleton loaders (not blank white screens)

### 16.2 Progressive Disclosure

- Loan Analyzer: Document checklist hidden by default; revealed on tap
- Risk Simulator: Risk breakdown narrative hidden until simulation completes
- Ask Kisan AI: Follow-up chips appear only after AI responds

### 16.3 Haptic Feedback

- Primary CTA tap: Light impact haptic (where supported)
- Successful result: Medium haptic
- Error/Not eligible: Double-tap haptic pattern

### 16.4 Transitions

- Page transitions: Slide left (forward), slide right (back) — 200ms ease-out
- Modal open: Slide up from bottom — 250ms ease-out
- Result card reveal: Fade + scale up from 0.95 — 300ms
- All transitions respect `prefers-reduced-motion`

### 16.5 Share & Print

**WhatsApp Share (Mobile):**
Shares a pre-formatted text message containing:
- Farmer name (if entered)
- Eligible amount and scheme
- Key documents list
- KisanCredit AI attribution line

**Print (Desktop/CSC):**
- Dedicated print stylesheet
- Hides navigation, headers, input form
- Shows: Logo + Result Card + Document Checklist in A4 print layout
- Font size increases to 14pt minimum for print readability

---

*End of KisanCredit AI Frontend PRD v1.0*

---

**Document Owner:** Product Design
**Next Review:** Post-hackathon, before production sprint
**Design System Status:** v1.0 — baseline defined, iteration expected after user testing