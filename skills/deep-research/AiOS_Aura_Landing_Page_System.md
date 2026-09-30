# AiOS — Aura Landing Page System & Gemini 3 Prompt Pack
## Kompletná adaptácia šablóny Aura Financial a 8-dielnej metodiky pre AiOS / RAVID AI

Tento dokument transformuje princípy tvorby špičkových landing pages (podľa benchmarku **aura-financial.aura.build**, Unicorn Studio a Gemini 3) priamo do architektúry, copywritingu a kódu projektu **AiOS / RAVID AI**.

---

## 1. Strategická transformácia obsahu (FinTech → B2B AI Infraštruktúra)

Predloha z **Aura Financial** stavia na autorite, presnosti a znížení kognitívneho zaťaženia. Pre **AiOS** ide o dokonalý náprotivok: namiesto správy finančného portfólia spravujeme **prevádzkovú inteligenciu, dopyty a procesy firmy**.

### 1.1 Porovnávacia matica obsahu

| Sekcia predlohy (Aura Financial) | Adaptácia pre AiOS (Slovenská verzia) | Adaptácia pre AiOS (Anglická verzia) |
| :--- | :--- | :--- |
| **Hero Badge / Eyebrow** | `AI INFRAŠTRUKTÚRA / PREVÁDZKOVÁ KONTROLA` | `AI INFRASTRUCTURE / OPERATIONAL CONTROL` |
| **Hero Headline** | **Navrhnite inteligenciu firmy s absolútnou presnosťou.** | **Architect your business intelligence with absolute precision.** |
| **Hero Subheadline** | Pokročilé AI protokoly prepojené s intuitívnym dizajnom. Dodávame infraštruktúru, ktorá eliminuje chaos a znásobuje výkon vašich ľudí. | Advanced AI operational protocols merged with intuitive design. We provide the infrastructure to eliminate chaos and compound your team's output. |
| **Hero CTA 1 (Primary)** | `Inicializovať protokol (Spustiť Audit)` | `Initialize Protocol (Start Audit)` |
| **Hero CTA 2 (Secondary)** | `Preskúmať ekosystém →` | `View Ecosystem →` |
| **Social Proof Ticker** | Modely a infraštruktúra: Anthropic Claude, OpenAI, Gemini 3, n8n, Supabase, PostgreSQL | Ecosystem: Anthropic Claude, OpenAI, Gemini 3, n8n, Supabase, PostgreSQL |
| **Social Proof Quote (Alex Sterling)** | **„Kedysi som riešil dopyty v e-maile, zákazky v tabuľkách a riziko nikde. AiOS to zjednodušil — vidím celý stav prevádzky bez kognitívneho zaťaženia.“**<br>*Marek Varga — Technický riaditeľ & Prevádzkovateľ servisov* | **"I used to track incoming leads in email, jobs in spreadsheets, and risk nowhere. AiOS keeps it simple — I see the full operational picture without the cognitive load."**<br>*Marcus Vance — Operations Director* |
| **Quote Headline** | Moderný majiteľ firmy sa netopí v operatíve — riadi, overuje a deleguje chytro. Tento systém bol stvorený pre neho. | The modern operator doesn't drown in busywork — they orchestrate, verify, and scale smart. This protocol was made for them. |
| **Feature Grid Headline** | **Podniková inteligencia bez námahy.** | **Enterprise intelligence made effortless.** |
| **Feature Grid Subheadline** | Zjednodušte tok vašich zákaziek pomocou AI protokolov navrhnutých na zjednodušenie, automatizáciu a zabezpečenie firemných dát. | Streamline your client pipeline with AI-driven protocols designed to simplify, automate, and enhance your operational architecture. |
| **Stĺpec 1 (Automated Execution)** | **Automatizovaná exekúcia**<br>Spracujte prichádzajúce dopyty, extrahujte dáta z fotiek a pripravte odpovede v milisekundách pomocou kontrolovaných AI algoritmov. | **Automated Execution**<br>Ingest complex leads, extract parameters from visual inputs, and prepare client quotes in milliseconds with our custodial AI algorithms. |
| **Stĺpec 2 (Smart Liquidity / Data Flow)** | **Plynulý dátový tok**<br>Prepojte WhatsApp, e-maily, formuláre a CRM do jedného živého toku dát bez manuálneho prepisovania a straty kontextu. | **Smart Liquidity & Data Flow**<br>Connect distributed communication channels into unified operational pipelines to ensure zero data-leakage across departments. |
| **Stĺpec 3 (Multi-Sig Governance)** | **Human-in-the-Loop Riadenie**<br>Spravujte prevádzku s inštitucionálnou bezpečnosťou. Nastavte používateľské roly, schvaľovanie človekom pri každom kľúčovom kroku a auditný log. | **Multi-Sig & Human Governance**<br>Manage agency operations with enterprise-grade guardrails. Set strict permissions, mandatory human sign-offs, and immutable audit logs. |
| **Riadiace centrum (Liquidate & Exchange)** | **Riadiace centrum a živý stav modulov**<br>Prehľad schválených zákaziek, aktívnych výnimiek, úspory hodín a zdravia infraštruktúry v reálnom čase. | **Control Room & Live Operations**<br>Real-time telemetry on processed tasks, human overrides, exception queues, and infrastructure health score. |

---

## 2. Aplikácia 8-dielnej metodiky na web AiOS

### Príspevok 1/8: Hero sekcia (50 % času a nastavenie vizuálnej DNA)
- **Rozloženie:** Floating pill navbar hore, decentný eyebrow s pulzujúcou bodkou, dominantný typografický nadpis s jemným dutým/obrysovým písmom (`-webkit-text-stroke`), dvojica tlačidiel, pod nimi sociálny dôkaz a v pozadí laserový mesh / beam vizuál.
- **DNA prvky:** Hlboká modro-čierna paleta (`#070A10`, `#0B1220`), akcent v neónovej kyano-modrej (`#25D9FF` až `#38BDF8`), mono font pre štítky (`DM Mono` / `Space Mono`) a geometrický grotesk pre nadpisy (`Space Grotesk` / `Sora`).

### Príspevok 2/8: Ikony a intro animácie
- **Ikony:** Namiesto štandardných Lucide použité sety z **Iconify** (napr. *Solar Linear*, *Phosphor Duotone*, *Iconoir*).
- **Animácie:** Kaskádový nástup prvkov (staggered intro) s kombináciou `fade-in`, `slide-in` a jemného `blur-in`:
```css
/* Intro Stagger s fill-mode: both a bez počiatočného tvrdého opacity: 0 v DOMe */
@keyframes heroIntro {
  0% {
    opacity: 0.01;
    transform: translateY(22px);
    filter: blur(8px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
  }
}

.animate-hero-eyebrow { animation: heroIntro 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.1s both; }
.animate-hero-title   { animation: heroIntro 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.25s both; }
.animate-hero-sub     { animation: heroIntro 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.4s both; }
.animate-hero-cta     { animation: heroIntro 0.85s cubic-bezier(0.16, 1, 0.3, 1) 0.55s both; }
.animate-hero-proof   { animation: heroIntro 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.7s both; }
```

### Príspevok 3/8: Beam Animation & Laser Background (Unicorn Studio štýl)
- **Noodle / Beam animácia:** Prepojenie vstupných uzlov (dáta, dopyt) svetelným lúčom, ktorý tečie priamo do cieľového kruhu ("Intelligence Core") so sonarom a radarovými kruhmi.
- **Pozadie:** Dynamický laserový glow efekt kombinujúci radiálne žiarenie a subtílnu mriežku:
```css
.laser-mesh-bg {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(ellipse 80% 50% at 50% -15%, rgba(37, 217, 255, 0.28), transparent 70%),
    radial-gradient(circle 400px at 75% 20%, rgba(56, 189, 248, 0.18), transparent 80%),
    linear-gradient(180deg, #070A10 0%, #0A0F18 100%);
  overflow: hidden;
}

.laser-grid-overlay {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(37, 217, 255, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(37, 217, 255, 0.05) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse 70% 60% at 50% 30%, black 20%, transparent 80%);
}
```

### Príspevok 4/8: Nekonečný Marquee ticker s alfa maskou
- Logá modelov a nástrojov (Claude, OpenAI, Gemini, n8n, Supabase, PostgreSQL) rotujúce v nekonečnej slučke s plynulým prechodom do stratena na okrajoch:
```css
.marquee-container {
  position: relative;
  overflow: hidden;
  width: 100%;
  mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, black 15%, black 85%, transparent);
}

.marquee-track {
  display: flex;
  width: max-content;
  gap: 48px;
  animation: marqueeScroll 28s linear infinite;
}

.marquee-track:hover {
  animation-play-state: paused;
}

@keyframes marqueeScroll {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

### Príspevok 5/8: "Lickable" CTA tlačidlá s 1px Border Beam animáciou
- Špičkové tlačidlo s rotujúcim svetelným lúčom po obvode (border beam) a jemným vnútorným skleným odleskom:
```css
.btn-border-beam {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 14px 28px;
  border-radius: 9999px;
  background: rgba(15, 23, 38, 0.85);
  backdrop-filter: blur(12px);
  color: #F4F7FA;
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 0 20px rgba(37, 217, 255, 0.15);
}

.btn-border-beam::before {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: 9999px;
  padding: 2px;
  background: conic-gradient(
    from 0deg,
    transparent 0deg,
    transparent 280deg,
    #25D9FF 340deg,
    #FFFFFF 360deg
  );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: rotateBeam 3.5s linear infinite;
}

.btn-border-beam:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 32px rgba(37, 217, 255, 0.35);
  border-color: rgba(37, 217, 255, 0.5);
}

@keyframes rotateBeam {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

### Príspevok 6/8: Moduly šité na 8 segmentov AiOS
Každý segment využíva rovnakú trojvrstvovú štruktúru (Vstup dát → AI syntéza → Ľudské schválenie):
1. **ServiceOS (Autoservisy):** Fotografia techničáku/dielu → AI kalkulácia normohodín a dielov → Schválenie prijímacím technikom.
2. **RealtyOS (Reality):** Dopyt z portálu → Kvalifikácia bonity a preferencií → Odporúčanie maklérovi na osobný kontakt.
3. **GuestOS (Penzióny):** Otázka na Booking/WhatsApp → AI draft v kontexte pravidiel penziónu → 1-klikové potvrdenie recepčnou.
4. **LegalDesk (Právnici):** Nahratie 40-stranového spisu → Extrakcia rizík a lehôt → Odborný posudok advokáta.
5. **FurnitureOS (Nábytok):** Foto interiéru + rozmery → AI konfigurátor a párovanie produktov → Obchodná ponuka.
6. **StudioOS (Fotoateliéry):** Dopyt na termín a štýl → Automatická ponuka balíkov a príprava zmluvy → Schválenie fotografom.
7. **VisualOS (Dekorácie):** Fotografia priestoru → Vizuálny placement dekorácie → Cenová kalkulácia pre klienta.
8. **RestoreOS (Renovácie):** Foto poškodeného kusu nábytku → Odhad spotreby materiálu a hodín → Schválenie majstrom dielne.

---

## 3. Presný Prompt Pack pre Gemini 3 (Generovanie a iterácia sekcií)

### Master Prompt pre generovanie Hero sekcie v štýle Aura Financial
```text
Role: Senior Staff Frontend Engineer and Design Technologist specialized in ultra-premium dark-mode web experiences (Unicorn Studio / Aura.build / Linear aesthetics).

Task: Create a hero section for "AiOS" (Enterprise AI Operating System & Infrastructure).

Style reference: aura-financial.aura.build
Visual aesthetics:
- Deep obsidian & midnight navy background (#070A10, #0B1220) with cyan laser glow accents (#25D9FF, #38BDF8)
- Glowing laser mesh/grid waves in the background using CSS gradients and SVG
- Floating glassmorphism pill navigation bar with status indicator
- Monospace tags and badges (DM Mono) combined with sharp typography (Space Grotesk)
- Pill-shaped "lickable" primary CTA button with a rotating 1px border beam animation
- Secondary ghost button with hover arrow transform
- Infinite marquee logo carousel with duplicated items and CSS alpha mask (transparent at edges)
- Subdued social proof metrics with subtle borders

Headline: "Architect your business intelligence with absolute precision."
Subheadline: "Advanced AI operational protocols merged with intuitive design. We provide the infrastructure to eliminate chaos and compound your team's output."
CTAs: "Initialize Protocol" (primary) and "View Ecosystem >" (secondary)

Intro animation instructions:
Animate fade in, slide in, blur in, element by element. Use 'both' instead of 'forwards'. Don't use permanent opacity 0.
```

### Prompt pre Feature Grid ("Banking intelligence made effortless" → "Podniková inteligencia")
```text
Create the feature architecture section for AiOS directly below the hero marquee.
Section Headline: "Podniková inteligencia bez námahy." / "Enterprise intelligence made effortless."
Section Subtitle: "Zjednodušte tok vašich zákaziek pomocou AI protokolov navrhnutých na zjednodušenie, automatizáciu a zabezpečenie firemných dát."

Layout: 3-column institutional card grid on dark glass background with subtle hover borders (1px cyan border highlight on hover).
Column 1:
- Icon: Iconify solar:bolt-circle-linear
- Title: "Automatizovaná exekúcia"
- Description: "Spracujte prichádzajúce dopyty, extrahujte dáta z fotiek a pripravte odpovede v milisekundách pomocou kontrolovaných AI algoritmov."
Column 2:
- Icon: Iconify solar:smart-home-angle-linear
- Title: "Plynulý dátový tok"
- Description: "Prepojte WhatsApp, e-maily, formuláre a CRM do jedného živého toku dát bez manuálneho prepisovania a straty kontextu."
Column 3:
- Icon: Iconify solar:shield-keyhole-minimalistic-linear
- Title: "Human-in-the-Loop Riadenie"
- Description: "Spravujte prevádzku s inštitucionálnou bezpečnosťou. Nastavte používateľské roly, schvaľovanie človekom pri každom kľúčovom kroku a auditný log."
```

### Prompt pre sekciu Sociálneho dôkazu & Citátu (Alex Sterling ekvivalent)
```text
Create a high-credibility testimonial and manifesto section inspired by the right-hand column of aura-financial.aura.build.
Headline: "Moderný majiteľ firmy sa netopí v operatíve — riadi, overuje a deleguje chytro. Tento operačný systém bol stvorený pre neho."
Visual: High-contrast black and white portrait photo of an operations leader with subtle cyan vignette.
Quote text: "Kedysi som riešil dopyty v e-maile, zákazky v tabuľkách a riziko nikde. AiOS to zjednodušil — vidím celý stav prevádzky bez kognitívneho zaťaženia."
Author: "Marek Varga — Technický riaditeľ & Prevádzkovateľ servisov"
Style: Dark card with inset border glow, crisp typography, and institutional badge.
```

---

## 4. Odporúčaný akčný plán implementácie do `aios-brand-site (2)`

1. **Vložiť CSS tokeny a animácie** do `client/src/index.css`:
   - `.btn-border-beam` (rotujúci kužeľový lúč tlačidiel),
   - `.laser-mesh-bg` a `.laser-grid-overlay` (pozadie Unicorn Studio štýlu),
   - `.marquee-container` a `.marquee-track` (plynulý ticker partnerov),
   - `@keyframes heroIntro` (staggered blur-in animácie).
2. **Aktualizovať Hero sekciu v `client/src/pages/Home.tsx`**:
   - Pridať horný plávajúci pill navbar,
   - Vložiť adaptované headliney a novú sekciu nekonečného marquee tickeru,
   - Nahradiť štandardné tlačidlá za "lickable" border-beam tlačidlá.
3. **Doplniť sekciu 3 stĺpcov & Citát stratéga**:
   - Umiestniť pod marquee sekciu „Podniková inteligencia bez námahy“ a profilovú kartu sociálneho dôkazu podľa predlohy z obrázka.
