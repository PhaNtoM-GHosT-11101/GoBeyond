# GoBeyond — Candidate Authenticity Engine

> *A resume is a claim. A GitHub profile is evidence. An adaptive MCQ test is live proof. GoBeyond combines all three to give recruiters a single, trustworthy Authenticity Score for every candidate.*

<div align="center">

![GoBeyond Banner](https://img.shields.io/badge/GoBeyond-Candidate%20Authenticity%20Engine-6C63FF?style=for-the-badge)
![Built With Claude](https://img.shields.io/badge/Powered%20by-Claude%20AI-orange?style=for-the-badge&logo=anthropic)
![Hackathon](https://img.shields.io/badge/AI%20Product%20Hackathon-2026-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [The Problem](#-the-problem)
- [How It Works](#-how-it-works)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [API Prompts](#-api-prompts)
- [Authenticity Score Formula](#-authenticity-score-formula)
- [Score Bands](#-score-bands)
- [Job Market Intelligence](#-job-market-intelligence)
- [Demo](#-demo)
- [Built At](#-built-at)
- [Author](#-author)

---

## 🔍 Overview

**GoBeyond** is a multi-signal candidate authenticity platform that goes far beyond the standard resume screener. It is a full **Candidate Authenticity Engine** that combines three independent verification signals to determine whether a candidate is genuinely qualified — or fraudulently misrepresenting themselves.

Built for the **AI Product Hackathon 2026** at GL Bajaj Institute of Management and Research, GoBeyond was conceived from a real problem observed first-hand as a Placement Coordinator at NIT Agartala, where shortlisted candidates frequently could not answer basic questions about skills they had claimed on their resumes.

---

## 🚨 The Problem

### The Stated Problem
Hiring teams review dozens of resumes per role, but many candidates do not match the required skills or experience. Traditional screening is:

- ⏱️ **Manual and time-intensive** — recruiters spend ~23 hours/week on resume screening *(LinkedIn, 2023)*
- 🎯 **Keyword-based and gameable** — candidates optimise for ATS keywords, not actual skill
- 🔍 **Single-signal** — the resume is the only input, with zero verification

### The Deeper Problem
Beyond efficiency, there is a **trust crisis** in hiring:

- 📊 ~40% of resumes contain at least one significant exaggeration *(HireRight Employment Screening Benchmark Report)*
- 🎓 Tier-2/3 college students face harsher scrutiny yet greater pressure to inflate credentials
- ❌ Recruiters have no systematic way to verify claims before investing in an interview

> **Why this matters for India:** India graduates 1.5 million engineering students per year. An estimated 80% enter the job market through campus placements at Tier-2/3 institutions, with no standardised, scalable verification layer in place.

---

## ⚙️ How It Works

GoBeyond operates as a **fully agentic pipeline**. Once a candidate uploads their resume, every subsequent step is automated without recruiter intervention:

```
Resume Upload
      │
      ▼
AI Skill Extraction (Claude)
      │
      ▼
Dynamic MCQ Generation (tailored to resume)
      │
      ▼
Adaptive Difficulty Loop (observes performance → adjusts in real time)
      │
      ▼
Speed Anomaly Detection (JS timer per question)
      │
      ▼
GitHub API Scan + LinkedIn Paste Analysis
      │
      ▼
Mismatch Detection (Claude cross-references claims vs. evidence)
      │
      ▼
Authenticity Score Computation
      │
      ▼
Trust Passport Generation (recruiter-facing card)
```

---

## ✨ Features

### 1. 🧠 MCQ Authentication Engine
A dynamic, resume-specific test generated fresh for every candidate — not a static question bank.

| Feature | Description |
|---|---|
| Resume Upload + Parsing | PDF or plain-text input; Claude extracts skills, technologies, years of experience, and role history |
| Dynamic Question Generation | Claude generates 15–50 MCQs specifically targeting the skills on *this* candidate's resume |
| Adaptive Difficulty Loop | If a candidate answers 5/5 correctly, Claude generates harder follow-up questions in real time |
| Timed Quiz UI | Each question has a countdown timer; JS tracks `time_per_answer` for anomaly detection |
| Speed Anomaly Detection | Answers taking over 60 seconds are flagged as potential external lookup |

> **Why adaptive difficulty matters:** A static MCQ generator is not agentic. GoBeyond's system observes performance mid-test and makes real-time decisions about what to ask next — this is genuine agentic behaviour.

---

### 2. 🔗 GitHub + LinkedIn Proof-of-Work Scanner
Retrieves verifiable, multi-year records of actual work output that cannot be manufactured on short notice.

| Feature | Description |
|---|---|
| GitHub API Integration | No key needed. Fetches repo names, descriptions, languages, creation dates, commit counts, stars |
| GitHub Fraud Pattern Detection | Flags: account age < 3 months, > 70% forked repos, zero original commits, no contribution history |
| Claude Proof-of-Work Summary | Claude summarises real work output and flags where resume claims diverge from evidence |
| LinkedIn Experience Import | Candidate pastes their LinkedIn About + Experience section into a text area |
| Streaming AI Output | Anthropic streaming API lets recruiters watch Claude generate analysis token by token |

---

### 3. 🚩 Mismatch Detection — The Killer Feature

| Standard Resume Screener | GoBeyond |
|---|---|
| Matches resume keywords to job description | Catches where resume claims *contradict* actual evidence |
| Scores fit against a job description | Scores the *authenticity* of the candidate's identity |
| Can be fooled by keyword stuffing | Cannot be fooled without years of real work history |

**Example mismatch flags Claude generates:**
- *"Claims 4 years of React experience but GitHub shows first React repo was created 8 months ago"*
- *"Resume lists 3 machine learning projects but all GitHub repos are forked with zero original commits"*
- *"Account created 11 days ago with 18 repos — pattern consistent with profile fabrication"*
- *"LinkedIn role at Company X (2020–2022) but GitHub activity shows a 2-year gap in that period"*

---

### 4. 📊 Job Market Intelligence Dashboard
Transforms GoBeyond from a recruiter tool into a **career guidance platform for students**.

Shows the growth rate of job demand by field over time, giving students data-driven context for career decisions — powered by NASSCOM India Tech Hiring Report 2024 and LinkedIn Economic Graph data.

| Field | 2020–2024 Growth | Status |
|---|---|---|
| AI / ML Engineering | +180% | 🟢 Booming |
| Cloud / DevOps | +110% | 🟢 Booming |
| Data Engineering | +95% | 🟢 Booming |
| Cybersecurity | +85% | 🟢 Booming |
| Full Stack (React/Node) | +30% | 🟡 Stable |
| Java Backend | +5% | 🟡 Stable |
| Manual QA Testing | -25% | 🔴 Declining |
| PHP Development | -35% | 🔴 Declining |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Vanilla HTML + CSS + JavaScript (single file, zero build step) |
| AI Engine | [Anthropic Claude API](https://www.anthropic.com) (streaming + structured JSON output) |
| PDF Parsing | [pdf.js](https://mozilla.github.io/pdf.js/) via CDN |
| Data Visualisation | [Chart.js](https://www.chartjs.org/) via CDN |
| GitHub Data | [GitHub Public REST API](https://docs.github.com/en/rest) (no authentication required) |
| Deployment | GitHub Pages (zero configuration) |

> **Why a single HTML file?** No build step, no Webpack, no environment variables that break at demo time. Judges can download the file and open it instantly in any browser.

---

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Edge, Safari)
- An [Anthropic API key](https://console.anthropic.com/) (Claude Sonnet)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/gobeyond.git

# Navigate into the project directory
cd gobeyond
```

### Running the App

Since GoBeyond is a single HTML file with no build step:

```bash
# Option 1: Open directly in browser
open index.html

# Option 2: Serve locally (recommended for PDF.js compatibility)
npx serve .
# or
python -m http.server 8000
```

Then visit `http://localhost:8000` in your browser.

### Setting Your API Key

When prompted in the UI, enter your Anthropic API key. It is stored only in browser memory and never sent to any server other than Anthropic's API endpoint.

---

## 📁 Project Structure

```
gobeyond/
├── index.html          # Entire application — single file
├── README.md           # This file
└── assets/             # (Optional) Screenshots and demo GIFs
    ├── trust-passport.png
    └── demo.gif
```

---

## 🔑 API Prompts

### MCQ Generation Prompt

```
SYSTEM: You are a strict technical interviewer. Given a resume, generate MCQ questions
that test whether the candidate actually knows what they claim. Be adversarial.

Return ONLY valid JSON. No preamble. Format:
[{"question":"...","options":["A","B","C","D"],"correct":0,"difficulty":"easy|medium|hard"}]

Generate 15 questions targeting these skills: {skills_list}
```

### Mismatch Detection Prompt

```
SYSTEM: You are a background verification specialist. Compare the resume claims
against the GitHub evidence and LinkedIn history. Be honest and direct.

Return JSON:
{"pow_score":0-100,"summary":"...","mismatches":["..."],"fraud_flags":["..."]}

RESUME: {resume_text}
GITHUB DATA: {github_summary} | LINKEDIN: {linkedin_paste}
```

---

## 📐 Authenticity Score Formula

```
Authenticity Score = (MCQ Score × 0.40) + (Proof-of-Work Score × 0.60)
```

GitHub commit history and LinkedIn work history are multi-year records that cannot be fabricated overnight. The 60/40 split reflects this asymmetric trust value — MCQ receives a lower weight because a determined candidate can still prepare using external resources during the test.

---

## 🏅 Score Bands

| Score | Tier | Recruiter Action |
|---|---|---|
| **85 – 100** | ✅ Verified | Shortlist immediately |
| **65 – 84** | 🟢 Likely Authentic | Proceed to interview with confidence |
| **45 – 64** | 🟡 Needs Review | Some discrepancies detected — probe during interview |
| **0 – 44** | 🔴 Flagged | Significant mismatch between claims and evidence |

---

## 📈 Job Market Intelligence

The dashboard renders as a filterable Chart.js line chart with four filter categories:

- **All Fields** — full overview
- **Booming** — fastest-growing demand sectors
- **Stable** — consistent but moderate growth
- **Declining** — fields facing automation or market contraction

Each filter updates the chart and displays a plain-English insight panel below it.

---

## 🎬 Demo

> *Demo GIF / screenshots coming soon*

**Three contrasting test personas used in the demo:**

1. **Legitimate candidate** — Resume claims match GitHub history → High Authenticity Score
2. **Inflated resume** — Claims 4 years of React; GitHub shows 8 months → Mismatch flagged
3. **Fabricated profile** — Account created weeks ago, 70%+ forked repos, zero commits → Fraud flags triggered

---

## 🏫 Built At

**AI Product Hackathon 2026**
GL Bajaj Institute of Management and Research
Problem Statement 2: *Recruiters Spend Too Much Time Screening Candidates*

---

## 👤 Author

Built by a **Placement Coordinator at NIT Agartala** who has personally witnessed resume fraud affecting real students and real recruiters.

- **LinkedIn:** [Your LinkedIn Profile](https://linkedin.com/in/YOUR_HANDLE)
- **GitHub:** [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**GoBeyond** — *Don't just screen. Verify.*

</div>
