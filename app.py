import streamlit as st
import time
from datetime import datetime

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Startup Builder",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
# GLOBAL CSS  –  dark theme · rich animations · highlighted text
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ── Reset ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: #060910;
    color: #e2e8f0;
}

/* ── Animated radial + grid background ── */
[data-testid="stAppViewContainer"] {
    background-color: #060910;
    background-image:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(99,102,241,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 110%, rgba(192,132,252,0.08) 0%, transparent 60%),
        linear-gradient(rgba(99,102,241,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,102,241,0.025) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
}
[data-testid="stHeader"]  { background: transparent; }
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0a0f1a 0%, #0d1525 100%);
    border-right: 1px solid rgba(99,102,241,0.18);
}

/* ════════════════════════════════
   HERO
════════════════════════════════ */
.hero-wrap { position: relative; padding: 1rem 0 0.5rem; }

.hero-eyebrow {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 99px; padding: 0.3rem 0.9rem;
    font-size: 0.72rem; font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.1em; text-transform: uppercase;
    color: #818cf8; margin-bottom: 0.9rem;
    animation: fade-in-up 0.6s ease both;
}
.hero-eyebrow .dot {
    width: 6px; height: 6px; background: #34d399; border-radius: 50%;
    animation: live-pulse 1.5s ease-in-out infinite;
}
@keyframes live-pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(52,211,153,0.6); }
    50%      { box-shadow: 0 0 0 5px rgba(52,211,153,0); }
}

.hero-title {
    font-size: 3.6rem; font-weight: 800; letter-spacing: -0.04em;
    line-height: 1.05; margin-bottom: 0.5rem;
    animation: fade-in-up 0.7s 0.1s ease both;
}
.hero-title .word-ai     { color: #818cf8; }
.hero-title .word-startup {
    background: linear-gradient(135deg, #c084fc 0%, #818cf8 60%, #38bdf8 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; background-size: 200% 200%;
    animation: gradient-shift 4s ease infinite;
}
.hero-title .word-builder { color: #e2e8f0; }

@keyframes gradient-shift {
    0%,100% { background-position: 0% 50%; }
    50%      { background-position: 100% 50%; }
}
.hero-sub {
    font-size: 1.05rem; color: #64748b;
    font-family: 'JetBrains Mono', monospace;
    animation: fade-in-up 0.7s 0.2s ease both;
}
.hero-sub .hl-crew  { color: #c084fc; font-weight: 600; }
.hero-sub .hl-model { color: #38bdf8; font-weight: 600; }

@keyframes fade-in-up {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ════════════════════════════════
   CHIPS & KEYWORD HIGHLIGHTS
════════════════════════════════ */
.chip {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 0.18rem 0.65rem; border-radius: 6px;
    font-size: 0.8rem; font-weight: 700;
    font-family: 'JetBrains Mono', monospace; letter-spacing: 0.04em;
    transition: all 0.2s; border: 1px solid;
}
.chip-violet { background: rgba(129,140,248,0.15); color: #a5b4fc; border-color: rgba(129,140,248,0.25); }
.chip-cyan   { background: rgba(56,189,248,0.12);  color: #7dd3fc; border-color: rgba(56,189,248,0.22); }
.chip-green  { background: rgba(52,211,153,0.12);  color: #6ee7b7; border-color: rgba(52,211,153,0.22); }
.chip-amber  { background: rgba(251,191,36,0.12);  color: #fcd34d; border-color: rgba(251,191,36,0.22); }
.chip-rose   { background: rgba(251,113,133,0.12); color: #fca5a5; border-color: rgba(251,113,133,0.22); }
.chip:hover  { transform: translateY(-1px) scale(1.04); filter: brightness(1.2); cursor: default; }

.kw   { font-weight: 700; font-family: 'JetBrains Mono', monospace; }
.kw-v { color: #a5b4fc; }
.kw-c { color: #67e8f9; }
.kw-g { color: #6ee7b7; }
.kw-a { color: #fcd34d; }

/* ════════════════════════════════
   INPUT & BUTTON
════════════════════════════════ */
[data-testid="stTextInput"] input {
    background: rgba(10,15,26,0.95) !important;
    border: 1px solid rgba(99,102,241,0.28) !important;
    border-radius: 14px !important; color: #e2e8f0 !important;
    font-family: 'Syne', sans-serif !important; font-size: 1rem !important;
    padding: 0.9rem 1.1rem !important;
    transition: border-color 0.25s, box-shadow 0.25s, background 0.25s;
}
[data-testid="stTextInput"] input:focus {
    border-color: #818cf8 !important;
    background: rgba(15,22,40,0.98) !important;
    box-shadow: 0 0 0 3px rgba(129,140,248,0.18), 0 0 28px rgba(129,140,248,0.1) !important;
    outline: none !important;
}

[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #5f5fcf 0%, #7c3aed 100%) !important;
    color: white !important; border: none !important; border-radius: 13px !important;
    font-family: 'Syne', sans-serif !important; font-weight: 700 !important;
    font-size: 0.97rem !important; padding: 0.8rem 2rem !important;
    letter-spacing: 0.05em !important; cursor: pointer !important;
    transition: all 0.22s ease !important;
    box-shadow: 0 4px 28px rgba(99,102,241,0.4) !important;
    position: relative; overflow: hidden;
}
[data-testid="stButton"] > button::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, transparent 60%);
    border-radius: 13px;
}
[data-testid="stButton"] > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 10px 36px rgba(99,102,241,0.55), 0 0 0 3px rgba(129,140,248,0.18) !important;
}
[data-testid="stButton"] > button:active { transform: translateY(0) scale(0.99) !important; }

/* ════════════════════════════════
   PIPELINE BANNER
════════════════════════════════ */
.pipeline-banner {
    background: linear-gradient(90deg, rgba(10,15,26,0.9) 0%, rgba(30,20,60,0.7) 50%, rgba(10,15,26,0.9) 100%);
    border: 1px solid rgba(99,102,241,0.2); border-radius: 14px;
    padding: 0.85rem 1.4rem; display: flex; align-items: center; gap: 1rem;
    margin-bottom: 1rem; animation: fade-in-up 0.5s ease both;
}
.pipeline-title {
    font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: #818cf8; font-family: 'JetBrains Mono', monospace;
}
.pipeline-desc { font-size: 0.78rem; color: #475569; font-family: 'JetBrains Mono', monospace; }

/* ════════════════════════════════
   AGENT CARDS
════════════════════════════════ */
.agent-card {
    background: linear-gradient(135deg, rgba(12,18,32,0.95) 0%, rgba(16,24,44,0.98) 100%);
    border: 1px solid rgba(99,102,241,0.1); border-radius: 18px;
    padding: 1.2rem 1.1rem 1rem; display: flex; flex-direction: column;
    align-items: center; text-align: center; gap: 0.45rem;
    transition: border-color 0.35s, box-shadow 0.35s, transform 0.25s;
    position: relative; overflow: hidden; min-height: 135px;
}
.agent-card::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(99,102,241,0.04) 0%, transparent 70%);
    pointer-events: none;
}
.agent-card.idle  { opacity: 0.5; }
.agent-card.active {
    border-color: rgba(129,140,248,0.6); opacity: 1;
    transform: translateY(-5px) scale(1.03);
    animation: active-glow 2s ease-in-out infinite;
}
@keyframes active-glow {
    0%,100% { box-shadow: 0 0 0 1px rgba(129,140,248,0.2), 0 0 30px rgba(99,102,241,0.2); }
    50%      { box-shadow: 0 0 0 2px rgba(129,140,248,0.4), 0 0 55px rgba(99,102,241,0.38); }
}
.agent-card.active::after {
    content: ''; position: absolute; top: 0; left: -60%; width: 40%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
    animation: shimmer 2.4s ease-in-out infinite;
}
@keyframes shimmer { to { left: 130%; } }

.agent-card.done {
    border-color: rgba(52,211,153,0.35); opacity: 1;
    box-shadow: 0 0 22px rgba(52,211,153,0.08);
    animation: done-pop 0.4s cubic-bezier(0.34,1.56,0.64,1);
}
@keyframes done-pop {
    0%   { transform: scale(0.94); }
    60%  { transform: scale(1.05); }
    100% { transform: scale(1); }
}
.agent-card.done::before {
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(52,211,153,0.06) 0%, transparent 70%);
}

.agent-icon { font-size: 2rem; line-height: 1; margin-bottom: 0.1rem; }
.agent-card.active .agent-icon { animation: icon-float 2s ease-in-out infinite; }
@keyframes icon-float {
    0%,100% { transform: translateY(0); }
    50%      { transform: translateY(-6px); }
}
.agent-name  { font-weight: 700; font-size: 0.78rem; color: #c7d2fe; line-height: 1.3; }
.agent-step  { font-size: 0.62rem; font-family: 'JetBrains Mono', monospace; color: #334155; letter-spacing: 0.08em; text-transform: uppercase; }
.agent-status-line { font-size: 0.7rem; font-family: 'JetBrains Mono', monospace; margin-top: 0.1rem; }
.agent-status-line.idle    { color: #334155; }
.agent-status-line.running { color: #818cf8; animation: blink 1.4s ease-in-out infinite; }
.agent-status-line.done    { color: #34d399; }
@keyframes blink { 0%,100% { opacity:1; } 50% { opacity:0.4; } }

/* ════════════════════════════════
   DOT SPINNER
════════════════════════════════ */
.dot-spinner { display: inline-flex; gap: 3px; align-items: center; margin-left: 6px; }
.dot-spinner span {
    width: 4px; height: 4px; background: #818cf8; border-radius: 50%;
    animation: dot-bounce 1.2s ease-in-out infinite;
}
.dot-spinner span:nth-child(2) { animation-delay: 0.18s; }
.dot-spinner span:nth-child(3) { animation-delay: 0.36s; }
@keyframes dot-bounce {
    0%,80%,100% { transform: translateY(0); opacity: 0.35; }
    40%          { transform: translateY(-6px); opacity: 1; }
}

/* ════════════════════════════════
   PROGRESS BAR
════════════════════════════════ */
[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #c084fc, #38bdf8) !important;
    background-size: 200% 100% !important; border-radius: 99px !important;
    transition: width 0.6s cubic-bezier(0.4,0,0.2,1) !important;
    box-shadow: 0 0 16px rgba(129,140,248,0.5);
    animation: bar-shimmer 2s linear infinite;
}
@keyframes bar-shimmer {
    0%   { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
[data-testid="stProgress"] > div > div > div {
    background: rgba(10,15,26,0.9) !important; border-radius: 99px !important;
    border: 1px solid rgba(99,102,241,0.18) !important;
}

/* ════════════════════════════════
   METRICS STRIP
════════════════════════════════ */
.metric-strip { display: flex; gap: 0.85rem; margin: 1.25rem 0; }
.metric-box {
    flex: 1; background: rgba(10,15,26,0.7);
    border: 1px solid rgba(99,102,241,0.1); border-radius: 14px;
    padding: 0.9rem 1rem; text-align: center;
    transition: border-color 0.3s, box-shadow 0.3s; position: relative; overflow: hidden;
}
.metric-box::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.4), transparent);
}
.metric-box.highlight { border-color: rgba(129,140,248,0.35); box-shadow: 0 0 20px rgba(99,102,241,0.1); }
.metric-value {
    font-size: 1.9rem; font-weight: 800;
    background: linear-gradient(135deg, #818cf8, #c084fc);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    line-height: 1; animation: count-in 0.4s ease both;
}
@keyframes count-in { from { opacity:0; transform:scale(0.7); } to { opacity:1; transform:scale(1); } }
.metric-label {
    font-size: 0.67rem; color: #475569; text-transform: uppercase;
    letter-spacing: 0.1em; font-family: 'JetBrains Mono', monospace; margin-top: 0.3rem;
}
.metric-badge {
    font-size: 0.6rem; padding: 0.1rem 0.45rem; border-radius: 99px;
    font-family: 'JetBrains Mono', monospace; font-weight: 600;
    display: inline-block; margin-top: 0.3rem;
}
.metric-badge.good    { background: rgba(52,211,153,0.15); color: #34d399; }
.metric-badge.running { background: rgba(99,102,241,0.15); color: #818cf8; }

/* ════════════════════════════════
   STATUS BADGE
════════════════════════════════ */
.status-badge {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 0.4rem 1rem; border-radius: 99px;
    font-size: 0.78rem; font-weight: 700;
    font-family: 'JetBrains Mono', monospace; letter-spacing: 0.06em;
}
.status-badge.idle    { background: rgba(71,85,105,0.15); color: #475569; border: 1px solid rgba(71,85,105,0.25); }
.status-badge.running { background: rgba(99,102,241,0.12); color: #818cf8; border: 1px solid rgba(99,102,241,0.3); animation: badge-pulse 2s ease-in-out infinite; }
@keyframes badge-pulse {
    0%,100% { box-shadow: 0 0 0 0 rgba(99,102,241,0.3); }
    50%      { box-shadow: 0 0 0 6px rgba(99,102,241,0); }
}
.status-badge.done { background: rgba(52,211,153,0.1); color: #34d399; border: 1px solid rgba(52,211,153,0.28); }

/* ════════════════════════════════
   RESULT CARDS
════════════════════════════════ */
.result-wrap { animation: fade-in-up 0.5s ease both; }
.result-header {
    display: flex; align-items: center; gap: 0.75rem;
    margin-bottom: 1rem; padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(99,102,241,0.1);
}
.result-header-icon { font-size: 1.6rem; }
.result-header-title { font-size: 1.15rem; font-weight: 800; color: #e2e8f0; }
.result-header-sub { font-size: 0.72rem; font-family: 'JetBrains Mono', monospace; color: #475569; margin-top: 0.1rem; }

.result-card {
    background: linear-gradient(160deg, rgba(10,15,26,0.95) 0%, rgba(16,22,38,0.98) 100%);
    border: 1px solid rgba(99,102,241,0.14); border-radius: 18px;
    padding: 1.75rem 2rem; margin-top: 0.5rem; line-height: 1.85;
    font-size: 0.92rem; color: #94a3b8; white-space: pre-wrap;
    font-family: 'JetBrains Mono', monospace;
    position: relative; overflow: hidden;
}
.result-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, #6366f1, #c084fc, #38bdf8);
    background-size: 200% 100%; animation: gradient-shift 4s ease infinite;
}
.result-card::after {
    content: ''; position: absolute; top: 0; left: 0; bottom: 0;
    width: 3px; background: linear-gradient(180deg, #6366f1, #c084fc, transparent); opacity: 0.45;
}

.result-label {
    font-size: 0.67rem; font-weight: 700; letter-spacing: 0.14em;
    text-transform: uppercase; color: #334155;
    font-family: 'JetBrains Mono', monospace; margin-bottom: 0.5rem;
}
.section-tag {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 0.25rem 0.75rem; border-radius: 8px; font-size: 0.73rem;
    font-weight: 700; font-family: 'JetBrains Mono', monospace; letter-spacing: 0.05em;
    margin: 0 4px 8px 0; border: 1px solid; animation: fade-in-up 0.4s ease both;
    cursor: default; transition: all 0.2s;
}
.section-tag:hover { transform: translateY(-2px); filter: brightness(1.15); }

/* ════════════════════════════════
   TABS
════════════════════════════════ */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    background: rgba(10,15,26,0.6); border-radius: 14px; padding: 5px; gap: 4px;
    border: 1px solid rgba(99,102,241,0.1);
}
[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important; color: #334155 !important;
    border-radius: 9px !important; font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important; font-size: 0.8rem !important;
    padding: 0.5rem 1rem !important; border: none !important;
    transition: all 0.22s !important; letter-spacing: 0.02em;
}
[data-testid="stTabs"] [data-baseweb="tab"]:hover {
    color: #818cf8 !important; background: rgba(99,102,241,0.08) !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(99,102,241,0.22) 0%, rgba(139,92,246,0.16) 100%) !important;
    color: #c7d2fe !important; box-shadow: 0 2px 10px rgba(99,102,241,0.18) !important;
}
[data-testid="stTabs"] [data-baseweb="tab-highlight"] { display: none; }

/* ════════════════════════════════
   SIDEBAR
════════════════════════════════ */
.sidebar-header {
    font-size: 0.65rem; font-weight: 700; letter-spacing: 0.16em;
    text-transform: uppercase; color: #334155;
    font-family: 'JetBrains Mono', monospace; margin-bottom: 0.85rem;
    padding-bottom: 0.5rem; border-bottom: 1px solid rgba(99,102,241,0.1);
}
.sidebar-agent {
    display: flex; align-items: flex-start; gap: 0.7rem; padding: 0.8rem;
    border-radius: 11px; margin-bottom: 0.45rem;
    background: rgba(99,102,241,0.04); border: 1px solid rgba(99,102,241,0.07);
    transition: all 0.22s; cursor: default;
}
.sidebar-agent:hover { background: rgba(99,102,241,0.1); border-color: rgba(99,102,241,0.2); transform: translateX(3px); }
.sidebar-agent-icon { font-size: 1.3rem; min-width: 1.5rem; margin-top: 1px; }
.sidebar-agent-name { font-weight: 700; font-size: 0.82rem; color: #a5b4fc; }
.sidebar-agent-desc { font-size: 0.73rem; color: #475569; margin-top: 0.12rem; line-height: 1.45; }

.step-item {
    display: flex; align-items: flex-start; gap: 0.6rem; padding: 0.4rem 0;
    border-left: 2px solid rgba(99,102,241,0.15);
    padding-left: 0.7rem; margin-left: 0.5rem; margin-bottom: 0.3rem;
}
.step-num {
    font-size: 0.65rem; font-weight: 700;
    font-family: 'JetBrains Mono', monospace; color: #6366f1;
    background: rgba(99,102,241,0.12); border-radius: 4px;
    padding: 0.1rem 0.35rem; flex-shrink: 0;
}
.step-text { font-size: 0.76rem; color: #475569; font-family: 'JetBrains Mono', monospace; line-height: 1.4; }

/* ════════════════════════════════
   IDLE PLACEHOLDER
════════════════════════════════ */
.idle-placeholder {
    margin-top: 2.5rem; text-align: center; padding: 3.5rem 2rem;
    border: 1px dashed rgba(99,102,241,0.15); border-radius: 24px;
    background: radial-gradient(ellipse 60% 50% at 50% 50%, rgba(99,102,241,0.04) 0%, transparent 70%);
    animation: fade-in-up 0.6s ease both;
}
.idle-rocket {
    font-size: 3.5rem; display: block; margin-bottom: 1.2rem;
    animation: rocket-hover 3s ease-in-out infinite;
}
@keyframes rocket-hover {
    0%,100% { transform: translateY(0) rotate(-5deg); }
    50%      { transform: translateY(-12px) rotate(5deg); }
}
.idle-title { font-size: 1.15rem; font-weight: 800; color: #1e293b; margin-bottom: 0.5rem; }
.idle-sub   { font-size: 0.82rem; color: #1e293b; font-family: 'JetBrains Mono', monospace; margin-bottom: 1.5rem; }
.idle-chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.4rem; }

/* ════════════════════════════════
   SUCCESS BANNER
════════════════════════════════ */
.success-banner {
    background: linear-gradient(90deg, rgba(52,211,153,0.08) 0%, rgba(56,189,248,0.06) 100%);
    border: 1px solid rgba(52,211,153,0.22); border-radius: 14px;
    padding: 1rem 1.5rem; display: flex; align-items: center; gap: 1rem;
    margin: 1rem 0; animation: fade-in-up 0.5s ease both;
}
.success-banner-text  { font-size: 0.88rem; font-weight: 700; color: #6ee7b7; font-family: 'JetBrains Mono', monospace; }
.success-banner-sub   { font-size: 0.75rem; color: #334155; font-family: 'JetBrains Mono', monospace; margin-top: 0.15rem; }

/* ════════════════════════════════
   DOWNLOAD
════════════════════════════════ */
[data-testid="stDownloadButton"] > button {
    background: linear-gradient(135deg, rgba(10,15,26,0.95) 0%, rgba(20,28,46,0.98) 100%) !important;
    color: #818cf8 !important; border: 1px solid rgba(99,102,241,0.35) !important;
    border-radius: 12px !important; font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important; font-size: 0.88rem !important; letter-spacing: 0.04em !important;
    transition: all 0.22s !important;
}
[data-testid="stDownloadButton"] > button:hover {
    background: linear-gradient(135deg, rgba(99,102,241,0.18) 0%, rgba(139,92,246,0.12) 100%) !important;
    border-color: rgba(99,102,241,0.6) !important;
    transform: translateY(-2px) !important; box-shadow: 0 6px 20px rgba(99,102,241,0.22) !important;
}

/* ════════════════════════════════
   MISC
════════════════════════════════ */
hr { border-color: rgba(99,102,241,0.08) !important; }
[data-testid="stAlert"] {
    background: rgba(52,211,153,0.07) !important; border: 1px solid rgba(52,211,153,0.2) !important;
    border-radius: 12px !important; color: #34d399 !important;
}
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.25); border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: rgba(99,102,241,0.45); }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# AGENT METADATA
# ══════════════════════════════════════════════════════════════════════════════
AGENTS = [
    {
        "key": "ceo",      "icon": "🧠", "step": "Step 01",
        "name": "Startup CEO",
        "tab": "💡 Startup Idea",
        "desc": "Serial entrepreneur who generates innovative startup ideas based on market gaps.",
        "chip_color": "chip-violet", "tag": "IDEATION",
        "section_tags": ["Problem Statement","Core Solution","Target Users","Value Proposition"],
        "tag_colors":   ["chip-violet","chip-cyan","chip-green","chip-amber"],
    },
    {
        "key": "market",   "icon": "📊", "step": "Step 02",
        "name": "Market Research Analyst",
        "tab": "📊 Market Research",
        "desc": "Deep-dives into market size, competitors, and growth opportunities.",
        "chip_color": "chip-cyan", "tag": "RESEARCH",
        "section_tags": ["Market Size","Key Competitors","Growth Trends","Opportunities"],
        "tag_colors":   ["chip-cyan","chip-rose","chip-amber","chip-green"],
    },
    {
        "key": "product",  "icon": "🗂️", "step": "Step 03",
        "name": "Product Manager",
        "tab": "🗂️ Product Plan",
        "desc": "Defines the MVP, feature set, and product roadmap.",
        "chip_color": "chip-amber", "tag": "PRODUCT",
        "section_tags": ["Core Features","MVP Scope","Roadmap","User Stories"],
        "tag_colors":   ["chip-amber","chip-violet","chip-cyan","chip-green"],
    },
    {
        "key": "cto",      "icon": "⚙️", "step": "Step 04",
        "name": "CTO",
        "tab": "⚙️ Tech Stack",
        "desc": "Architects the system design and recommends the ideal tech stack.",
        "chip_color": "chip-rose", "tag": "ARCHITECTURE",
        "section_tags": ["Tech Stack","System Design","Infrastructure","APIs & Integrations"],
        "tag_colors":   ["chip-rose","chip-cyan","chip-violet","chip-amber"],
    },
    {
        "key": "engineer", "icon": "🖥️", "step": "Step 05",
        "name": "Software Engineer",
        "tab": "🖥️ Landing Page",
        "desc": "Builds the landing page HTML structure for the startup.",
        "chip_color": "chip-green", "tag": "FRONTEND",
        "section_tags": ["Hero Section","Features","CTA","Footer"],
        "tag_colors":   ["chip-green","chip-amber","chip-violet","chip-cyan"],
    },
    {
        "key": "pitch",    "icon": "💰", "step": "Step 06",
        "name": "Pitch Writer",
        "tab": "💰 Investor Pitch",
        "desc": "Crafts a compelling pitch deck narrative for fundraising.",
        "chip_color": "chip-amber", "tag": "FUNDRAISING",
        "section_tags": ["The Hook","Problem & Solution","Traction","The Ask"],
        "tag_colors":   ["chip-amber","chip-rose","chip-green","chip-violet"],
    },
]

# ── Session state ──────────────────────────────────────────────────────────────
for key, default in [
    ("results", {}), ("agent_statuses", {}), ("running", False),
    ("done", False), ("start_time", None), ("elapsed", 0), ("industry_used", ""),
]:
    if key not in st.session_state:
        st.session_state[key] = default

if not st.session_state.agent_statuses:
    st.session_state.agent_statuses = {a["key"]: "idle" for a in AGENTS}

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="margin-bottom:1.5rem">
        <div style="font-size:1.3rem;font-weight:800;color:#e2e8f0;letter-spacing:-0.02em">
            🚀 <span style="background:linear-gradient(135deg,#818cf8,#c084fc);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">
            Startup Builder</span>
        </div>
        <div style="font-size:0.7rem;color:#334155;font-family:JetBrains Mono,monospace;
        margin-top:0.3rem;letter-spacing:0.08em">AI-POWERED · 6 AGENTS · CREWAI</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-header">🤖 Agent Crew</div>', unsafe_allow_html=True)
    for agent in AGENTS:
        st.markdown(f"""
        <div class="sidebar-agent">
            <div class="sidebar-agent-icon">{agent['icon']}</div>
            <div>
                <div class="sidebar-agent-name">
                    {agent['name']}
                    <span class="chip {agent['chip_color']}" style="margin-left:6px;font-size:0.58rem;padding:0.05rem 0.4rem">{agent['tag']}</span>
                </div>
                <div class="sidebar-agent-desc">{agent['desc']}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="sidebar-header">📋 How It Works</div>', unsafe_allow_html=True)
    steps_info = [
        ("01","Enter your target industry"),
        ("02","Click Launch Crew"),
        ("03","6 AI agents collaborate in sequence"),
        ("04","Review each agent's output in tabs"),
        ("05","Download your full startup report"),
    ]
    for num, text in steps_info:
        st.markdown(f"""
        <div class="step-item">
            <span class="step-num">{num}</span>
            <span class="step-text">{text}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center;display:flex;flex-wrap:wrap;gap:0.35rem;justify-content:center">
        <span class="chip chip-violet">CrewAI</span>
        <span class="chip chip-cyan">LLaMA 3</span>
        <span class="chip chip-green">Multi-Agent</span>
        <span class="chip chip-amber">RAG-Ready</span>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN — HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
    <div class="hero-eyebrow">
        <span class="dot"></span>
        Multi-Agent AI Platform &nbsp;·&nbsp; 6 Specialized Agents
    </div>
    <div class="hero-title">
        <span class="word-ai">AI</span>&nbsp;<span class="word-startup">Startup</span>&nbsp;<span class="word-builder">Builder</span>
    </div>
    <div class="hero-sub">
        Powered by <span class="hl-crew">CrewAI</span> agents &amp;
        <span class="hl-model">Meta LLaMA 3</span> &mdash;
        from idea to investor pitch in seconds
    </div>
</div>
""", unsafe_allow_html=True)

# Animated feature chip row
st.markdown("""
<div style="margin:0.75rem 0 1.5rem;display:flex;flex-wrap:wrap;gap:0.4rem;align-items:center">
    <span class="chip chip-violet">💡 Idea Generation</span>
    <span class="chip chip-cyan">📊 Market Research</span>
    <span class="chip chip-amber">🗂️ Product Planning</span>
    <span class="chip chip-rose">⚙️ Tech Architecture</span>
    <span class="chip chip-green">🖥️ Landing Page</span>
    <span class="chip chip-amber">💰 Investor Pitch</span>
</div>
""", unsafe_allow_html=True)

# ── Input row ──────────────────────────────────────────────────────────────────
col_input, col_btn = st.columns([4, 1])
with col_input:
    industry = st.text_input(
        "Industry Input", placeholder="Enter your target industry  e.g. HealthTech · FinTech · EdTech · CleanEnergy · SaaS…",
        label_visibility="collapsed"
    )
with col_btn:
    launch = st.button("🚀 Launch Crew", use_container_width=True)

# Pipeline banner
st.markdown("""
<div class="pipeline-banner">
    <div>
        <div class="pipeline-title">⬡ Agent Execution Pipeline</div>
        <div class="pipeline-desc">Sequential · Context-sharing · Collaborative output</div>
    </div>
    <div style="margin-left:auto;display:flex;gap:0.35rem;flex-wrap:wrap;align-items:center">
        <span class="chip chip-violet" style="font-size:0.66rem">🧠 CEO</span>
        <span style="color:#334155">→</span>
        <span class="chip chip-cyan" style="font-size:0.66rem">📊 Market</span>
        <span style="color:#334155">→</span>
        <span class="chip chip-amber" style="font-size:0.66rem">🗂️ Product</span>
        <span style="color:#334155">→</span>
        <span class="chip chip-rose" style="font-size:0.66rem">⚙️ CTO</span>
        <span style="color:#334155">→</span>
        <span class="chip chip-green" style="font-size:0.66rem">🖥️ Engineer</span>
        <span style="color:#334155">→</span>
        <span class="chip chip-amber" style="font-size:0.66rem">💰 Pitch</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Agent cards ────────────────────────────────────────────────────────────────
prog_placeholder   = st.empty()
status_placeholder = st.empty()
agent_cols         = st.columns(6)
agent_placeholders = [c.empty() for c in agent_cols]

def render_agent_cards(statuses):
    for i, agent in enumerate(AGENTS):
        s        = statuses.get(agent["key"], "idle")
        card_cls = "active" if s == "running" else ("done" if s == "done" else "idle")
        spinner  = '<div class="dot-spinner"><span></span><span></span><span></span></div>' if s == "running" else ""
        s_text   = {"idle": "⬡ Waiting", "running": "Running…", "done": "✓ Complete"}.get(s, "Waiting")
        s_cls    = {"idle": "idle", "running": "running", "done": "done"}.get(s, "idle")
        chip     = f'<span class="chip {agent["chip_color"]}" style="font-size:0.58rem;padding:0.05rem 0.38rem">{agent["tag"]}</span>'
        agent_placeholders[i].markdown(f"""
        <div class="agent-card {card_cls}">
            <div class="agent-step">{agent['step']}</div>
            <div class="agent-icon">{agent['icon']}</div>
            <div class="agent-name">{agent['name']}</div>
            {chip}
            <div class="agent-status-line {s_cls}">{s_text}{spinner}</div>
        </div>""", unsafe_allow_html=True)

render_agent_cards(st.session_state.agent_statuses)

# ── Metrics ────────────────────────────────────────────────────────────────────
metrics_placeholder = st.empty()

def render_metrics(completed, elapsed, is_running=False):
    pct = int((completed / 6) * 100)
    hl  = lambda n: "highlight" if n else ""
    b_done    = '<span class="metric-badge good">ALL DONE</span>' if completed == 6 else ""
    b_running = '<span class="metric-badge running">ACTIVE</span>' if is_running else ""
    metrics_placeholder.markdown(f"""
    <div class="metric-strip">
        <div class="metric-box {hl(completed > 0)}">
            <div class="metric-value">{completed}</div>
            <div class="metric-label">Agents Done</div>{b_done}
        </div>
        <div class="metric-box">
            <div class="metric-value" style="background:linear-gradient(135deg,#f472b6,#fb923c);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">
            {6 - completed}</div>
            <div class="metric-label">Remaining</div>
        </div>
        <div class="metric-box {hl(is_running)}">
            <div class="metric-value" style="background:linear-gradient(135deg,#38bdf8,#818cf8);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">
            {elapsed}s</div>
            <div class="metric-label">Elapsed</div>{b_running}
        </div>
        <div class="metric-box {hl(pct > 0)}">
            <div class="metric-value">{pct}%</div>
            <div class="metric-label">Progress</div>
        </div>
    </div>""", unsafe_allow_html=True)

render_metrics(
    sum(1 for v in st.session_state.agent_statuses.values() if v == "done"),
    st.session_state.elapsed or 0
)

# ══════════════════════════════════════════════════════════════════════════════
# DIAGRAMS  — Flowchart + Architecture + Feature Map
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)

DIAGRAM_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: transparent;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    color: #e2e8f0;
    overflow-x: hidden;
  }

  /* ── Tab bar ── */
  .tab-bar {
    display: flex; gap: 6px; margin-bottom: 20px;
    background: rgba(10,15,26,0.8);
    border: 1px solid rgba(99,102,241,0.18);
    border-radius: 12px; padding: 5px;
  }
  .tab-btn {
    flex: 1; padding: 8px 12px; border-radius: 8px; border: none;
    background: transparent; color: #475569;
    font-family: inherit; font-size: 11px; font-weight: 700;
    letter-spacing: 0.06em; text-transform: uppercase; cursor: pointer;
    transition: all 0.2s;
  }
  .tab-btn:hover  { background: rgba(99,102,241,0.1); color: #818cf8; }
  .tab-btn.active {
    background: linear-gradient(135deg, rgba(99,102,241,0.25), rgba(139,92,246,0.18));
    color: #c7d2fe;
    box-shadow: 0 2px 10px rgba(99,102,241,0.2);
  }
  .diagram-panel { display: none; animation: fadeUp 0.4s ease; }
  .diagram-panel.active { display: block; }
  @keyframes fadeUp {
    from { opacity:0; transform:translateY(12px); }
    to   { opacity:1; transform:translateY(0); }
  }

  /* ══════════════════════════════
     PANEL 1 — AGENT FLOWCHART
  ══════════════════════════════ */
  .flow-wrap {
    display: flex; align-items: center; justify-content: center;
    gap: 0; padding: 16px 8px; flex-wrap: nowrap; overflow-x: auto;
  }
  .flow-node {
    display: flex; flex-direction: column; align-items: center;
    background: linear-gradient(160deg, rgba(15,22,40,0.98), rgba(20,30,55,0.95));
    border: 1px solid rgba(99,102,241,0.2); border-radius: 16px;
    padding: 14px 10px 12px; min-width: 110px; max-width: 118px;
    text-align: center; cursor: pointer; position: relative;
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
    flex-shrink: 0;
  }
  .flow-node::before {
    content: ''; position: absolute; inset: 0; border-radius: 16px;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(99,102,241,0.06) 0%, transparent 70%);
    pointer-events: none;
  }
  .flow-node:hover {
    transform: translateY(-6px) scale(1.04);
    border-color: rgba(129,140,248,0.6);
    box-shadow: 0 8px 32px rgba(99,102,241,0.25), 0 0 0 1px rgba(129,140,248,0.2);
  }
  .flow-node .fn-step {
    font-size: 9px; font-weight: 700; letter-spacing: 0.1em;
    text-transform: uppercase; color: #334155; margin-bottom: 6px;
  }
  .flow-node .fn-icon { font-size: 26px; margin-bottom: 6px; }
  .flow-node .fn-name {
    font-size: 10px; font-weight: 700; color: #c7d2fe;
    line-height: 1.3; margin-bottom: 5px;
  }
  .flow-node .fn-tag {
    font-size: 9px; padding: 2px 7px; border-radius: 5px;
    font-weight: 700; border: 1px solid; margin-bottom: 6px;
  }
  .flow-node .fn-desc {
    font-size: 9px; color: #475569; line-height: 1.5;
    font-family: 'JetBrains Mono', monospace;
  }
  .flow-node .fn-output {
    margin-top: 7px; padding: 4px 7px; border-radius: 6px;
    font-size: 8px; font-weight: 700; letter-spacing: 0.06em;
    background: rgba(99,102,241,0.1); color: #818cf8;
    border: 1px solid rgba(99,102,241,0.2); width: 100%;
  }

  /* tooltip */
  .fn-tooltip {
    position: absolute; bottom: calc(100% + 10px); left: 50%;
    transform: translateX(-50%);
    background: rgba(10,15,26,0.97); border: 1px solid rgba(99,102,241,0.35);
    border-radius: 10px; padding: 10px 13px; width: 180px;
    font-size: 10px; color: #cbd5e1; line-height: 1.6;
    pointer-events: none; opacity: 0;
    transition: opacity 0.2s; z-index: 99;
    box-shadow: 0 8px 24px rgba(0,0,0,0.5);
  }
  .fn-tooltip::after {
    content: ''; position: absolute; top: 100%; left: 50%;
    transform: translateX(-50%); border: 6px solid transparent;
    border-top-color: rgba(99,102,241,0.35);
  }
  .flow-node:hover .fn-tooltip { opacity: 1; }

  /* animated arrow connector */
  .flow-arrow {
    display: flex; align-items: center; flex-direction: column;
    padding: 0 2px; flex-shrink: 0; gap: 2px; position: relative;
  }
  .arrow-line {
    width: 28px; height: 2px; position: relative; overflow: visible;
  }
  .arrow-track { width: 100%; height: 2px; background: rgba(99,102,241,0.12); border-radius: 99px; }
  .arrow-dot {
    position: absolute; top: -3px; width: 8px; height: 8px;
    background: #818cf8; border-radius: 50%;
    animation: travel 2s linear infinite;
    box-shadow: 0 0 6px #818cf8;
  }
  @keyframes travel { from { left: -8px; opacity:0.2; } 40% { opacity:1; } to { left: 28px; opacity:0.2; } }
  .arrow-head { color: rgba(99,102,241,0.5); font-size: 14px; margin-top: -4px; }
  .arrow-label { font-size: 8px; color: #334155; letter-spacing: 0.06em; text-transform: uppercase; }

  /* color variants */
  .tag-v { background: rgba(129,140,248,0.12); color: #a5b4fc; border-color: rgba(129,140,248,0.25); }
  .tag-c { background: rgba(56,189,248,0.12);  color: #7dd3fc; border-color: rgba(56,189,248,0.22); }
  .tag-a { background: rgba(251,191,36,0.12);  color: #fcd34d; border-color: rgba(251,191,36,0.22); }
  .tag-r { background: rgba(251,113,133,0.12); color: #fca5a5; border-color: rgba(251,113,133,0.22); }
  .tag-g { background: rgba(52,211,153,0.12);  color: #6ee7b7; border-color: rgba(52,211,153,0.22); }
  .border-v { border-color: rgba(129,140,248,0.35) !important; }
  .border-c { border-color: rgba(56,189,248,0.3) !important; }
  .border-a { border-color: rgba(251,191,36,0.3) !important; }
  .border-r { border-color: rgba(251,113,133,0.3) !important; }
  .border-g { border-color: rgba(52,211,153,0.3) !important; }

  /* input + output nodes */
  .io-node {
    display: flex; flex-direction: column; align-items: center;
    background: rgba(10,15,26,0.6); border: 1px dashed rgba(99,102,241,0.25);
    border-radius: 14px; padding: 12px 10px; min-width: 90px; text-align: center;
    flex-shrink: 0;
  }
  .io-node .io-icon { font-size: 20px; margin-bottom: 5px; }
  .io-node .io-label { font-size: 9px; color: #475569; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }
  .io-node .io-val   { font-size: 10px; color: #818cf8; font-weight: 700; margin-top: 3px; }

  /* ══════════════════════════════
     PANEL 2 — ARCHITECTURE
  ══════════════════════════════ */
  .arch-wrap { padding: 10px 4px; }
  .arch-title {
    font-size: 10px; font-weight: 700; letter-spacing: 0.12em;
    text-transform: uppercase; color: #334155; margin-bottom: 14px;
    display: flex; align-items: center; gap: 8px;
  }
  .arch-title::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(99,102,241,0.2), transparent);
  }

  .arch-layer {
    background: rgba(10,15,26,0.6);
    border: 1px solid rgba(99,102,241,0.12); border-radius: 14px;
    margin-bottom: 10px; overflow: hidden; position: relative;
    transition: border-color 0.25s;
  }
  .arch-layer:hover { border-color: rgba(99,102,241,0.3); }
  .arch-layer-header {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 16px 8px;
    border-bottom: 1px solid rgba(99,102,241,0.08);
    background: rgba(99,102,241,0.04);
  }
  .arch-layer-icon { font-size: 18px; }
  .arch-layer-name { font-size: 11px; font-weight: 700; color: #c7d2fe; }
  .arch-layer-sub  { font-size: 9px; color: #475569; margin-top: 1px; }
  .arch-layer-body {
    display: flex; flex-wrap: wrap; gap: 8px;
    padding: 12px 16px;
  }
  .arch-block {
    background: rgba(15,22,40,0.8); border: 1px solid rgba(99,102,241,0.12);
    border-radius: 9px; padding: 7px 11px; font-size: 10px;
    color: #94a3b8; font-weight: 600; cursor: default;
    transition: all 0.2s; display: flex; align-items: center; gap: 5px;
  }
  .arch-block:hover {
    background: rgba(99,102,241,0.1); color: #c7d2fe;
    border-color: rgba(99,102,241,0.3); transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(99,102,241,0.12);
  }
  .arch-block .ab-dot {
    width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0;
  }
  .arch-connect {
    display: flex; justify-content: center; align-items: center;
    gap: 6px; margin: -4px 0; position: relative; z-index: 1;
  }
  .arch-connect-line {
    width: 1px; height: 18px;
    background: linear-gradient(180deg, rgba(99,102,241,0.4), rgba(99,102,241,0.1));
  }
  .arch-connect-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: #6366f1; box-shadow: 0 0 8px rgba(99,102,241,0.6);
    animation: arch-pulse 1.8s ease-in-out infinite;
  }
  @keyframes arch-pulse {
    0%,100% { box-shadow: 0 0 4px rgba(99,102,241,0.4); transform: scale(1); }
    50%      { box-shadow: 0 0 14px rgba(99,102,241,0.7); transform: scale(1.3); }
  }

  /* ══════════════════════════════
     PANEL 3 — FEATURE MAP
  ══════════════════════════════ */
  .feat-wrap { padding: 8px 4px; }
  .feat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .feat-card {
    background: rgba(10,15,26,0.7); border: 1px solid rgba(99,102,241,0.12);
    border-radius: 14px; padding: 14px; cursor: default;
    transition: all 0.25s; position: relative; overflow: hidden;
  }
  .feat-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    opacity: 0; transition: opacity 0.25s;
  }
  .feat-card:hover {
    transform: translateY(-4px);
    border-color: rgba(99,102,241,0.35);
    box-shadow: 0 8px 24px rgba(99,102,241,0.12);
  }
  .feat-card:hover::before { opacity: 1; }
  .feat-card.fc-v::before { background: linear-gradient(90deg, #6366f1, #8b5cf6); }
  .feat-card.fc-c::before { background: linear-gradient(90deg, #0ea5e9, #38bdf8); }
  .feat-card.fc-a::before { background: linear-gradient(90deg, #d97706, #fbbf24); }
  .feat-card.fc-r::before { background: linear-gradient(90deg, #e11d48, #fb7185); }
  .feat-card.fc-g::before { background: linear-gradient(90deg, #059669, #34d399); }
  .feat-card.fc-p::before { background: linear-gradient(90deg, #7c3aed, #a78bfa); }

  .fc-header { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
  .fc-icon   { font-size: 20px; }
  .fc-name   { font-size: 11px; font-weight: 700; color: #c7d2fe; }
  .fc-tag    { font-size: 9px; padding: 2px 7px; border-radius: 5px; font-weight: 700; border: 1px solid; margin-top: 1px; }
  .fc-desc   { font-size: 9.5px; color: #475569; line-height: 1.6; margin-bottom: 8px; }
  .fc-bullets { list-style: none; padding: 0; }
  .fc-bullets li {
    font-size: 9px; color: #64748b; padding: 2px 0;
    display: flex; align-items: flex-start; gap: 5px; line-height: 1.5;
  }
  .fc-bullets li::before { content: '▸'; color: #6366f1; flex-shrink: 0; margin-top: 1px; }

  /* ══════════════════════════════
     PANEL 4 — DATA FLOW
  ══════════════════════════════ */
  .dflow-wrap { padding: 8px 4px; }
  .dflow-row  {
    display: flex; align-items: stretch; gap: 0;
    margin-bottom: 8px; position: relative;
  }
  .dflow-agent {
    background: rgba(10,15,26,0.85); border: 1px solid rgba(99,102,241,0.15);
    border-radius: 12px 0 0 12px; padding: 10px 14px;
    min-width: 130px; display: flex; align-items: center; gap: 8px;
    transition: border-color 0.2s;
  }
  .dflow-agent:hover { border-color: rgba(99,102,241,0.4); }
  .dflow-agent .da-icon { font-size: 18px; flex-shrink: 0; }
  .dflow-agent .da-name { font-size: 10px; font-weight: 700; color: #c7d2fe; line-height: 1.3; }
  .dflow-agent .da-role { font-size: 8px; color: #475569; margin-top: 1px; font-weight: 600; }

  .dflow-pipe {
    display: flex; align-items: center; padding: 0 4px;
    background: rgba(10,15,26,0.5); border-top: 1px solid rgba(99,102,241,0.1);
    border-bottom: 1px solid rgba(99,102,241,0.1); min-width: 40px;
    position: relative; overflow: hidden;
  }
  .dflow-pipe-inner {
    width: 100%; height: 3px; background: rgba(99,102,241,0.1);
    position: relative; overflow: hidden; border-radius: 99px;
  }
  .dflow-pipe-anim {
    position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(99,102,241,0.7), transparent);
    animation: pipe-flow 2s linear infinite;
  }
  @keyframes pipe-flow { to { left: 100%; } }

  .dflow-output {
    flex: 1; background: rgba(10,15,26,0.7); border: 1px solid rgba(99,102,241,0.1);
    border-radius: 0 12px 12px 0; padding: 10px 14px;
    display: flex; align-items: center; flex-wrap: wrap; gap: 5px;
    border-left: none;
  }
  .dflow-output .do-label {
    font-size: 9px; font-weight: 700; letter-spacing: 0.08em;
    text-transform: uppercase; color: #334155; margin-right: 4px;
  }
  .dflow-badge {
    font-size: 9px; padding: 2px 8px; border-radius: 5px;
    font-weight: 700; border: 1px solid;
  }

  .dflow-vconnect {
    display: flex; justify-content: flex-start; padding-left: 64px;
    align-items: center; height: 8px;
  }
  .dflow-vline {
    width: 1px; height: 8px;
    background: linear-gradient(180deg, rgba(99,102,241,0.3), rgba(99,102,241,0.1));
  }
</style>
</head>
<body>

<!-- Tab bar -->
<div class="tab-bar">
  <button class="tab-btn active" onclick="showTab('flow')">🔄 Agent Flowchart</button>
  <button class="tab-btn" onclick="showTab('arch')">🏗️ Architecture</button>
  <button class="tab-btn" onclick="showTab('feat')">✦ Feature Map</button>
  <button class="tab-btn" onclick="showTab('dflow')">⟶ Data Flow</button>
</div>

<!-- ══ PANEL 1: AGENT FLOWCHART ══ -->
<div id="tab-flow" class="diagram-panel active">
  <div class="flow-wrap">

    <!-- Input -->
    <div class="io-node">
      <div class="io-icon">⌨️</div>
      <div class="io-label">Input</div>
      <div class="io-val">Industry</div>
    </div>

    <!-- Arrow 0→1 -->
    <div class="flow-arrow">
      <div class="arrow-line"><div class="arrow-track"></div><div class="arrow-dot" style="animation-delay:0s"></div></div>
      <div class="arrow-head">▶</div>
      <div class="arrow-label">kickoff</div>
    </div>

    <!-- Node 1: CEO -->
    <div class="flow-node border-v">
      <div class="fn-step">Step 01</div>
      <div class="fn-icon">🧠</div>
      <div class="fn-name">Startup CEO</div>
      <div class="fn-tag tag-v">IDEATION</div>
      <div class="fn-desc">Generates the core startup concept</div>
      <div class="fn-output">💡 Startup Idea</div>
      <div class="fn-tooltip">
        <strong style="color:#a5b4fc">Startup CEO</strong><br>
        Analyzes the industry input and generates:<br>
        • Problem statement<br>• Core solution<br>• Target audience<br>• Value proposition
      </div>
    </div>

    <!-- Arrow 1→2 -->
    <div class="flow-arrow">
      <div class="arrow-line"><div class="arrow-track"></div><div class="arrow-dot" style="animation-delay:0.33s"></div></div>
      <div class="arrow-head">▶</div>
      <div class="arrow-label">context</div>
    </div>

    <!-- Node 2: Market -->
    <div class="flow-node border-c">
      <div class="fn-step">Step 02</div>
      <div class="fn-icon">📊</div>
      <div class="fn-name">Market Analyst</div>
      <div class="fn-tag tag-c">RESEARCH</div>
      <div class="fn-desc">Researches market & competitors</div>
      <div class="fn-output">📊 Market Report</div>
      <div class="fn-tooltip">
        <strong style="color:#7dd3fc">Market Analyst</strong><br>
        Reads the startup idea and produces:<br>
        • Market size (TAM/SAM/SOM)<br>• Competitor landscape<br>• Growth opportunities
      </div>
    </div>

    <!-- Arrow 2→3 -->
    <div class="flow-arrow">
      <div class="arrow-line"><div class="arrow-track"></div><div class="arrow-dot" style="animation-delay:0.66s"></div></div>
      <div class="arrow-head">▶</div>
      <div class="arrow-label">context</div>
    </div>

    <!-- Node 3: PM -->
    <div class="flow-node border-a">
      <div class="fn-step">Step 03</div>
      <div class="fn-icon">🗂️</div>
      <div class="fn-name">Product Manager</div>
      <div class="fn-tag tag-a">PRODUCT</div>
      <div class="fn-desc">Defines MVP & feature roadmap</div>
      <div class="fn-output">🗺️ Product Plan</div>
      <div class="fn-tooltip">
        <strong style="color:#fcd34d">Product Manager</strong><br>
        Leverages market research to define:<br>
        • Core features list<br>• MVP scope<br>• Sprint roadmap<br>• User stories
      </div>
    </div>

    <!-- Arrow 3→4 -->
    <div class="flow-arrow">
      <div class="arrow-line"><div class="arrow-track"></div><div class="arrow-dot" style="animation-delay:1s"></div></div>
      <div class="arrow-head">▶</div>
      <div class="arrow-label">context</div>
    </div>

    <!-- Node 4: CTO -->
    <div class="flow-node border-r">
      <div class="fn-step">Step 04</div>
      <div class="fn-icon">⚙️</div>
      <div class="fn-name">CTO</div>
      <div class="fn-tag tag-r">ARCHITECT</div>
      <div class="fn-desc">Designs tech stack & system</div>
      <div class="fn-output">⚙️ Tech Blueprint</div>
      <div class="fn-tooltip">
        <strong style="color:#fca5a5">Chief Technology Officer</strong><br>
        Uses product plan to architect:<br>
        • Technology stack<br>• System architecture<br>• Infra & APIs<br>• Scalability plan
      </div>
    </div>

    <!-- Arrow 4→5 -->
    <div class="flow-arrow">
      <div class="arrow-line"><div class="arrow-track"></div><div class="arrow-dot" style="animation-delay:1.33s"></div></div>
      <div class="arrow-head">▶</div>
      <div class="arrow-label">context</div>
    </div>

    <!-- Node 5: Engineer -->
    <div class="flow-node border-g">
      <div class="fn-step">Step 05</div>
      <div class="fn-icon">🖥️</div>
      <div class="fn-name">Engineer</div>
      <div class="fn-tag tag-g">FRONTEND</div>
      <div class="fn-desc">Builds landing page HTML</div>
      <div class="fn-output">🌐 HTML Page</div>
      <div class="fn-tooltip">
        <strong style="color:#6ee7b7">Software Engineer</strong><br>
        Generates a fully structured:<br>
        • Hero section<br>• Features section<br>• CTA buttons<br>• Responsive layout
      </div>
    </div>

    <!-- Arrow 5→6 -->
    <div class="flow-arrow">
      <div class="arrow-line"><div class="arrow-track"></div><div class="arrow-dot" style="animation-delay:1.66s"></div></div>
      <div class="arrow-head">▶</div>
      <div class="arrow-label">context</div>
    </div>

    <!-- Node 6: Pitch -->
    <div class="flow-node border-a">
      <div class="fn-step">Step 06</div>
      <div class="fn-icon">💰</div>
      <div class="fn-name">Pitch Writer</div>
      <div class="fn-tag tag-a">FUNDRAISE</div>
      <div class="fn-desc">Writes investor pitch deck</div>
      <div class="fn-output">📄 Pitch Deck</div>
      <div class="fn-tooltip">
        <strong style="color:#fcd34d">Pitch Writer</strong><br>
        Synthesizes all context to craft:<br>
        • Investor hook<br>• Problem / solution narrative<br>• Market opportunity<br>• The Ask
      </div>
    </div>

    <!-- Arrow 6→Output -->
    <div class="flow-arrow">
      <div class="arrow-line"><div class="arrow-track"></div><div class="arrow-dot" style="animation-delay:2s"></div></div>
      <div class="arrow-head">▶</div>
      <div class="arrow-label">output</div>
    </div>

    <!-- Final output -->
    <div class="io-node" style="border-color:rgba(52,211,153,0.3);background:rgba(52,211,153,0.04)">
      <div class="io-icon">📥</div>
      <div class="io-label" style="color:#34d399">Output</div>
      <div class="io-val" style="color:#34d399">Full Report</div>
    </div>

  </div>
  <div style="text-align:center;font-size:9px;color:#334155;margin-top:4px;letter-spacing:0.06em">
    HOVER OVER EACH AGENT NODE FOR DETAILS &nbsp;·&nbsp; ANIMATED DOTS SHOW DATA FLOW DIRECTION
  </div>
</div>

<!-- ══ PANEL 2: ARCHITECTURE ══ -->
<div id="tab-arch" class="diagram-panel">
  <div class="arch-wrap">

    <div class="arch-title">System Architecture Overview</div>

    <!-- Layer 1: UI -->
    <div class="arch-layer">
      <div class="arch-layer-header">
        <div class="arch-layer-icon">🖥️</div>
        <div>
          <div class="arch-layer-name">Presentation Layer — Streamlit UI</div>
          <div class="arch-layer-sub">Dark-themed dashboard · Real-time updates · Interactive tabs</div>
        </div>
        <span style="margin-left:auto;font-size:9px;padding:3px 9px;border-radius:6px;background:rgba(99,102,241,0.12);color:#818cf8;border:1px solid rgba(99,102,241,0.25);font-weight:700">FRONTEND</span>
      </div>
      <div class="arch-layer-body">
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>Hero + Input Form</div>
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>Agent Progress Cards</div>
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>Live Metrics Strip</div>
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>Progress Bar</div>
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>Result Tabs (×6)</div>
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>HTML Live Preview</div>
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>Diagram Viewer</div>
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>Download Report</div>
      </div>
    </div>

    <div class="arch-connect"><div class="arch-connect-line"></div><div class="arch-connect-dot"></div><div class="arch-connect-line"></div></div>

    <!-- Layer 2: Orchestration -->
    <div class="arch-layer">
      <div class="arch-layer-header">
        <div class="arch-layer-icon">🎛️</div>
        <div>
          <div class="arch-layer-name">Orchestration Layer — CrewAI</div>
          <div class="arch-layer-sub">Task routing · Context sharing · Sequential agent pipeline</div>
        </div>
        <span style="margin-left:auto;font-size:9px;padding:3px 9px;border-radius:6px;background:rgba(192,132,252,0.12);color:#c084fc;border:1px solid rgba(192,132,252,0.25);font-weight:700">CREWAI</span>
      </div>
      <div class="arch-layer-body">
        <div class="arch-block"><span class="ab-dot" style="background:#c084fc"></span>startup_crew.kickoff()</div>
        <div class="arch-block"><span class="ab-dot" style="background:#c084fc"></span>Task Queue Manager</div>
        <div class="arch-block"><span class="ab-dot" style="background:#c084fc"></span>Context Propagation</div>
        <div class="arch-block"><span class="ab-dot" style="background:#c084fc"></span>Output Aggregation</div>
        <div class="arch-block"><span class="ab-dot" style="background:#c084fc"></span>Error Handling</div>
        <div class="arch-block"><span class="ab-dot" style="background:#c084fc"></span>tasks_output Parser</div>
      </div>
    </div>

    <div class="arch-connect"><div class="arch-connect-line"></div><div class="arch-connect-dot"></div><div class="arch-connect-line"></div></div>

    <!-- Layer 3: Agents -->
    <div class="arch-layer">
      <div class="arch-layer-header">
        <div class="arch-layer-icon">🤖</div>
        <div>
          <div class="arch-layer-name">Agent Layer — 6 Specialized AI Agents</div>
          <div class="arch-layer-sub">Role-specific prompts · Shared memory · Sequential execution</div>
        </div>
        <span style="margin-left:auto;font-size:9px;padding:3px 9px;border-radius:6px;background:rgba(56,189,248,0.12);color:#38bdf8;border:1px solid rgba(56,189,248,0.25);font-weight:700">AGENTS</span>
      </div>
      <div class="arch-layer-body">
        <div class="arch-block"><span class="ab-dot" style="background:#818cf8"></span>🧠 Startup CEO</div>
        <div class="arch-block"><span class="ab-dot" style="background:#38bdf8"></span>📊 Market Analyst</div>
        <div class="arch-block"><span class="ab-dot" style="background:#fcd34d"></span>🗂️ Product Manager</div>
        <div class="arch-block"><span class="ab-dot" style="background:#fca5a5"></span>⚙️ CTO</div>
        <div class="arch-block"><span class="ab-dot" style="background:#6ee7b7"></span>🖥️ Engineer</div>
        <div class="arch-block"><span class="ab-dot" style="background:#fcd34d"></span>💰 Pitch Writer</div>
      </div>
    </div>

    <div class="arch-connect"><div class="arch-connect-line"></div><div class="arch-connect-dot"></div><div class="arch-connect-line"></div></div>

    <!-- Layer 4: LLM -->
    <div class="arch-layer">
      <div class="arch-layer-header">
        <div class="arch-layer-icon">🧬</div>
        <div>
          <div class="arch-layer-name">Model Layer — Meta LLaMA 3 via HuggingFace</div>
          <div class="arch-layer-sub">8B parameter model · Instruction-tuned · HuggingFace inference</div>
        </div>
        <span style="margin-left:auto;font-size:9px;padding:3px 9px;border-radius:6px;background:rgba(52,211,153,0.12);color:#34d399;border:1px solid rgba(52,211,153,0.25);font-weight:700">LLM</span>
      </div>
      <div class="arch-layer-body">
        <div class="arch-block"><span class="ab-dot" style="background:#34d399"></span>Meta-Llama-3-8B-Instruct</div>
        <div class="arch-block"><span class="ab-dot" style="background:#34d399"></span>HuggingFace API</div>
        <div class="arch-block"><span class="ab-dot" style="background:#34d399"></span>Prompt Templates</div>
        <div class="arch-block"><span class="ab-dot" style="background:#34d399"></span>Token Management</div>
        <div class="arch-block"><span class="ab-dot" style="background:#34d399"></span>Response Parsing</div>
      </div>
    </div>

  </div>
</div>

<!-- ══ PANEL 3: FEATURE MAP ══ -->
<div id="tab-feat" class="diagram-panel">
  <div class="feat-wrap">
    <div class="feat-grid">

      <div class="feat-card fc-v">
        <div class="fc-header">
          <div class="fc-icon">💡</div>
          <div><div class="fc-name">Startup Ideation</div><div class="fc-tag tag-v">CEO AGENT</div></div>
        </div>
        <div class="fc-desc">Generates a complete startup concept from a single industry keyword using the Startup CEO agent.</div>
        <ul class="fc-bullets">
          <li>Problem statement generation</li>
          <li>Core solution design</li>
          <li>Target user identification</li>
          <li>Unique value proposition</li>
        </ul>
      </div>

      <div class="feat-card fc-c">
        <div class="fc-header">
          <div class="fc-icon">📊</div>
          <div><div class="fc-name">Market Research</div><div class="fc-tag tag-c">ANALYST AGENT</div></div>
        </div>
        <div class="fc-desc">Analyses market landscape, sizing the opportunity and mapping the competitive environment.</div>
        <ul class="fc-bullets">
          <li>TAM / SAM / SOM sizing</li>
          <li>Competitor identification</li>
          <li>Market growth trends</li>
          <li>Strategic opportunities</li>
        </ul>
      </div>

      <div class="feat-card fc-a">
        <div class="fc-header">
          <div class="fc-icon">🗂️</div>
          <div><div class="fc-name">Product Planning</div><div class="fc-tag tag-a">PM AGENT</div></div>
        </div>
        <div class="fc-desc">Translates market insights into an actionable product roadmap with clearly defined MVP scope.</div>
        <ul class="fc-bullets">
          <li>Feature list prioritisation</li>
          <li>MVP scope definition</li>
          <li>Sprint roadmap planning</li>
          <li>User story generation</li>
        </ul>
      </div>

      <div class="feat-card fc-r">
        <div class="fc-header">
          <div class="fc-icon">⚙️</div>
          <div><div class="fc-name">Tech Architecture</div><div class="fc-tag tag-r">CTO AGENT</div></div>
        </div>
        <div class="fc-desc">Designs a scalable system architecture and recommends the optimal tech stack for the product.</div>
        <ul class="fc-bullets">
          <li>Technology stack selection</li>
          <li>System design diagram</li>
          <li>Infrastructure planning</li>
          <li>API & integration map</li>
        </ul>
      </div>

      <div class="feat-card fc-g">
        <div class="fc-header">
          <div class="fc-icon">🖥️</div>
          <div><div class="fc-name">Landing Page</div><div class="fc-tag tag-g">ENGINEER AGENT</div></div>
        </div>
        <div class="fc-desc">Auto-generates a complete HTML landing page structure with live in-browser preview.</div>
        <ul class="fc-bullets">
          <li>Hero + headline copy</li>
          <li>Feature highlight sections</li>
          <li>CTA button layout</li>
          <li>Live preview renderer</li>
        </ul>
      </div>

      <div class="feat-card fc-p">
        <div class="fc-header">
          <div class="fc-icon">💰</div>
          <div><div class="fc-name">Investor Pitch</div><div class="fc-tag tag-v">PITCH AGENT</div></div>
        </div>
        <div class="fc-desc">Synthesises all prior context to produce a compelling, structured investor pitch narrative.</div>
        <ul class="fc-bullets">
          <li>Attention-grabbing hook</li>
          <li>Problem / solution story</li>
          <li>Traction & metrics slide</li>
          <li>Funding ask & use of funds</li>
        </ul>
      </div>

    </div>
  </div>
</div>

<!-- ══ PANEL 4: DATA FLOW ══ -->
<div id="tab-dflow" class="diagram-panel">
  <div class="dflow-wrap">

    <!-- Row 1 -->
    <div class="dflow-row">
      <div class="dflow-agent">
        <div class="da-icon">⌨️</div>
        <div><div class="da-name">User Input</div><div class="da-role">Industry Keyword</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:0s"></div></div></div>
      <div class="dflow-output">
        <div class="do-label">Payload →</div>
        <div class="dflow-badge tag-v">inputs.industry</div>
        <div class="dflow-badge tag-c">kickoff()</div>
      </div>
    </div>
    <div class="dflow-vconnect"><div class="dflow-vline"></div></div>

    <!-- Row 2 -->
    <div class="dflow-row">
      <div class="dflow-agent" style="border-color:rgba(129,140,248,0.3)">
        <div class="da-icon">🧠</div>
        <div><div class="da-name">Startup CEO</div><div class="da-role">idea_task</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:0.4s"></div></div></div>
      <div class="dflow-output">
        <div class="do-label">Produces →</div>
        <div class="dflow-badge tag-v">Problem Statement</div>
        <div class="dflow-badge tag-v">Solution</div>
        <div class="dflow-badge tag-v">Target Users</div>
        <div class="dflow-badge" style="background:rgba(99,102,241,0.08);color:#818cf8;border-color:rgba(99,102,241,0.2)">→ passed to all subsequent agents</div>
      </div>
    </div>
    <div class="dflow-vconnect"><div class="dflow-vline"></div></div>

    <!-- Row 3 -->
    <div class="dflow-row">
      <div class="dflow-agent" style="border-color:rgba(56,189,248,0.3)">
        <div class="da-icon">📊</div>
        <div><div class="da-name">Market Analyst</div><div class="da-role">market_task</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:0.8s"></div></div></div>
      <div class="dflow-output">
        <div class="do-label">Produces →</div>
        <div class="dflow-badge tag-c">Market Size</div>
        <div class="dflow-badge tag-c">Competitors</div>
        <div class="dflow-badge tag-c">Opportunities</div>
        <div class="dflow-badge" style="background:rgba(56,189,248,0.08);color:#38bdf8;border-color:rgba(56,189,248,0.2)">→ passed downstream</div>
      </div>
    </div>
    <div class="dflow-vconnect"><div class="dflow-vline"></div></div>

    <!-- Row 4 -->
    <div class="dflow-row">
      <div class="dflow-agent" style="border-color:rgba(251,191,36,0.3)">
        <div class="da-icon">🗂️</div>
        <div><div class="da-name">Product Manager</div><div class="da-role">product_task</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:1.2s"></div></div></div>
      <div class="dflow-output">
        <div class="do-label">Produces →</div>
        <div class="dflow-badge tag-a">Feature List</div>
        <div class="dflow-badge tag-a">MVP Plan</div>
        <div class="dflow-badge tag-a">Roadmap</div>
      </div>
    </div>
    <div class="dflow-vconnect"><div class="dflow-vline"></div></div>

    <!-- Row 5 -->
    <div class="dflow-row">
      <div class="dflow-agent" style="border-color:rgba(251,113,133,0.3)">
        <div class="da-icon">⚙️</div>
        <div><div class="da-name">CTO</div><div class="da-role">tech_task</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:1.6s"></div></div></div>
      <div class="dflow-output">
        <div class="do-label">Produces →</div>
        <div class="dflow-badge tag-r">Tech Stack</div>
        <div class="dflow-badge tag-r">Architecture</div>
        <div class="dflow-badge tag-r">Infra Plan</div>
      </div>
    </div>
    <div class="dflow-vconnect"><div class="dflow-vline"></div></div>

    <!-- Row 6 -->
    <div class="dflow-row">
      <div class="dflow-agent" style="border-color:rgba(52,211,153,0.3)">
        <div class="da-icon">🖥️</div>
        <div><div class="da-name">Engineer</div><div class="da-role">landing_task</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:2s"></div></div></div>
      <div class="dflow-output">
        <div class="do-label">Produces →</div>
        <div class="dflow-badge tag-g">HTML Structure</div>
        <div class="dflow-badge tag-g">Live Preview</div>
      </div>
    </div>
    <div class="dflow-vconnect"><div class="dflow-vline"></div></div>

    <!-- Row 7 -->
    <div class="dflow-row">
      <div class="dflow-agent" style="border-color:rgba(251,191,36,0.3)">
        <div class="da-icon">💰</div>
        <div><div class="da-name">Pitch Writer</div><div class="da-role">pitch_task</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:2.4s"></div></div></div>
      <div class="dflow-output">
        <div class="do-label">Produces →</div>
        <div class="dflow-badge tag-a">Investor Pitch</div>
        <div class="dflow-badge tag-a">Funding Ask</div>
      </div>
    </div>
    <div class="dflow-vconnect"><div class="dflow-vline"></div></div>

    <!-- Final -->
    <div class="dflow-row">
      <div class="dflow-agent" style="border-color:rgba(52,211,153,0.4);background:rgba(52,211,153,0.04)">
        <div class="da-icon">📥</div>
        <div><div class="da-name" style="color:#6ee7b7">Full Report</div><div class="da-role">tasks_output[0..5]</div></div>
      </div>
      <div class="dflow-pipe"><div class="dflow-pipe-inner"><div class="dflow-pipe-anim" style="animation-delay:2.8s;background:linear-gradient(90deg,transparent,rgba(52,211,153,0.7),transparent)"></div></div></div>
      <div class="dflow-output" style="border-color:rgba(52,211,153,0.15)">
        <div class="do-label">Exports →</div>
        <div class="dflow-badge tag-g">6-Tab Dashboard</div>
        <div class="dflow-badge tag-g">Markdown Download</div>
        <div class="dflow-badge tag-g">HTML Preview</div>
      </div>
    </div>

  </div>
</div>

<script>
function showTab(name) {
  document.querySelectorAll('.diagram-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + name).classList.add('active');
  event.target.classList.add('active');
}
</script>
</body>
</html>
"""

with st.expander("📐  System Diagrams — Flowchart · Architecture · Feature Map · Data Flow", expanded=True):
    st.components.v1.html(DIAGRAM_HTML, height=560, scrolling=True)

st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# LAUNCH LOGIC
# ══════════════════════════════════════════════════════════════════════════════
if launch:
    if not industry.strip():
        st.warning("⚠️  Please enter an industry to continue.")
    else:
        st.session_state.results        = {}
        st.session_state.agent_statuses = {a["key"]: "idle" for a in AGENTS}
        st.session_state.running        = True
        st.session_state.done           = False
        st.session_state.start_time     = time.time()
        st.session_state.industry_used  = industry.strip()

        try:
            from crew import startup_crew
        except ImportError:
            st.error("⚠️  Could not import `crew.py`. Make sure it lives alongside `app.py`.")
            st.stop()

        task_keys = ["ceo", "market", "product", "cto", "engineer", "pitch"]

        for i, key in enumerate(task_keys):
            st.session_state.agent_statuses[key] = "running"
            render_agent_cards(st.session_state.agent_statuses)
            elapsed = int(time.time() - st.session_state.start_time)
            prog_placeholder.progress(i / 6, text=f"{AGENTS[i]['icon']}  Agent {i+1}/6 — {AGENTS[i]['name']} is working…")
            render_metrics(i, elapsed, is_running=True)
            status_placeholder.markdown(
                f'<div class="status-badge running">'
                f'{AGENTS[i]["icon"]} {AGENTS[i]["name"]} is thinking…'
                f'<div class="dot-spinner"><span></span><span></span><span></span></div></div>',
                unsafe_allow_html=True
            )

        with st.spinner(""):
            try:
                result = startup_crew.kickoff(inputs={"industry": industry.strip()})
            except Exception as e:
                st.error(f"CrewAI execution error: {e}")
                st.stop()

        try:
            task_outputs = result.tasks_output
            for i, key in enumerate(task_keys):
                st.session_state.results[key] = str(task_outputs[i].raw) if i < len(task_outputs) else ""
                st.session_state.agent_statuses[key] = "done"
        except Exception:
            raw = str(result)
            for key in task_keys:
                st.session_state.results[key] = raw
                st.session_state.agent_statuses[key] = "done"

        st.session_state.running = False
        st.session_state.done    = True
        elapsed = int(time.time() - st.session_state.start_time)
        st.session_state.elapsed = elapsed

        prog_placeholder.progress(1.0, text="✅  All 6 agents completed — scroll down to explore your startup plan!")
        render_agent_cards(st.session_state.agent_statuses)
        render_metrics(6, elapsed, is_running=False)
        status_placeholder.markdown(
            '<div class="status-badge done">✅ Startup plan generated — scroll down to explore results</div>',
            unsafe_allow_html=True
        )
        st.rerun()

# ══════════════════════════════════════════════════════════════════════════════
# RESULTS
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.done and st.session_state.results:
    elapsed = st.session_state.elapsed or 0
    ind     = st.session_state.industry_used or industry

    st.markdown(f"""
    <div class="success-banner">
        <div style="font-size:2rem">🎉</div>
        <div>
            <div class="success-banner-text">
                Startup plan for
                <span style="color:#38bdf8;font-weight:800">{ind}</span> is ready!
            </div>
            <div class="success-banner-sub">
                <span class="kw kw-g">6 agents completed</span> ·
                <span class="kw kw-a">{elapsed}s total runtime</span> ·
                <span class="chip chip-green" style="font-size:0.6rem">All tasks done</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    tab_labels = [a["tab"] for a in AGENTS]
    tabs = st.tabs(tab_labels)

    for i, agent in enumerate(AGENTS):
        with tabs[i]:
            content = st.session_state.results.get(agent["key"], "")

            tags_html = "".join([
                f'<span class="section-tag {agent["tag_colors"][j]}">{t}</span>'
                for j, t in enumerate(agent["section_tags"])
            ])

            st.markdown(f"""
            <div class="result-wrap">
                <div class="result-header">
                    <div class="result-header-icon">{agent['icon']}</div>
                    <div>
                        <div class="result-header-title">{agent['name']}</div>
                        <div class="result-header-sub">
                            {agent['tab']} &nbsp;·&nbsp;
                            <span class="chip {agent['chip_color']}" style="font-size:0.63rem">{agent['tag']}</span>
                            &nbsp;·&nbsp; Industry:
                            <span class="kw kw-c">{ind}</span>
                        </div>
                    </div>
                </div>
                <div style="margin-bottom:1rem;display:flex;flex-wrap:wrap">{tags_html}</div>
            </div>
            """, unsafe_allow_html=True)

            if not content:
                st.markdown('<div class="result-card"><span style="color:#334155">No output captured for this agent.</span></div>', unsafe_allow_html=True)
                continue

            if agent["key"] == "engineer":
                st.markdown('<div class="result-label">▸ Generated HTML Source</div>', unsafe_allow_html=True)
                html_content = content
                import re

                # remove markdown code block fences that break rendering
                html_content = re.sub(r"```html", "", html_content)
                html_content = re.sub(r"```", "", html_content)

                # trim whitespace
                html_content = html_content.strip()

                st.markdown(f'<div class="result-card">{content}</div>', unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("""
                <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.5rem">
                    <span class="result-label" style="margin:0">▸ Live Browser Preview</span>
                    <span class="chip chip-green" style="font-size:0.6rem">RENDERED</span>
                </div>
                """, unsafe_allow_html=True)

                preview_html = f"""
                <html>
                <head>
                <style>
                    body {{
                        margin:0;
                        padding:20px;
                        background:#ffffff;
                        font-family:Arial, sans-serif;
                    }}
                </style>
                </head>
                <body>
                {html_content}
                </body>
                </html>
                """

                st.components.v1.html(preview_html, height=700, scrolling=True)
            else:
                st.markdown(f'<div class="result-label">▸ {agent["name"]} Output — <span class="kw kw-v">{ind}</span></div>', unsafe_allow_html=True)
                st.markdown(f'<div class="result-card">{content}</div>', unsafe_allow_html=True)

    # ── Download ───────────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.75rem">
        <span style="font-size:1.1rem;font-weight:800;color:#e2e8f0">📥 Export Your Report</span>
        <span class="chip chip-cyan" style="font-size:0.68rem">Markdown Format</span>
        <span class="chip chip-green" style="font-size:0.68rem">All 6 Sections</span>
    </div>
    """, unsafe_allow_html=True)

    now    = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = (
        f"# 🚀 AI Startup Builder Report\n\n"
        f"**Generated:** {now}  \n**Industry:** {ind}  \n**Agents:** 6  \n**Total Time:** {elapsed}s\n\n---\n\n"
    )
    report += "\n\n---\n\n".join([
        f"## {a['icon']} {a['tab']}\n\n{st.session_state.results.get(a['key'], '')}"
        for a in AGENTS
    ])

    col_dl, col_info, _ = st.columns([2, 3, 2])
    with col_dl:
        st.download_button(
            label="⬇  Download Full Report (.md)",
            data=report.encode("utf-8"),
            file_name=f"startup_plan_{ind.lower().replace(' ','_')}.md",
            mime="text/markdown",
            use_container_width=True,
        )
    with col_info:
        st.markdown(f"""
        <div style="padding:0.6rem 1rem;background:rgba(10,15,26,0.7);
        border:1px solid rgba(99,102,241,0.12);border-radius:10px;
        font-size:0.75rem;font-family:JetBrains Mono,monospace;color:#475569;line-height:1.6">
            Includes <span class="kw kw-v">6 complete sections</span> ·
            ~{len(report)//1000}KB ·
            <span class="kw kw-g">Ready to share</span>
        </div>""", unsafe_allow_html=True)

elif not st.session_state.running:
    example_industries = ["HealthTech","FinTech","EdTech","CleanEnergy","SaaS","AgriTech","LegalTech","PropTech"]
    chip_cycle = ["chip-violet","chip-cyan","chip-amber","chip-rose","chip-green","chip-violet","chip-cyan","chip-amber"]
    chips = "".join([
        f'<span class="chip {chip_cycle[i]}">{e}</span>'
        for i, e in enumerate(example_industries)
    ])
    st.markdown(f"""
    <div class="idle-placeholder">
        <span class="idle-rocket">🚀</span>
        <div class="idle-title">Your AI crew is standing by</div>
        <div class="idle-sub">
            Enter an industry above and hit
            <span class="kw kw-v">Launch Crew</span> to begin
        </div>
        <div class="idle-chips">{chips}</div>
        <div style="margin-top:1.5rem;font-size:0.72rem;color:#1e293b;
        font-family:JetBrains Mono,monospace;display:flex;flex-wrap:wrap;
        justify-content:center;gap:0.5rem">
            <span class="kw kw-c">6 agents</span>
            <span style="color:#1e293b">·</span>
            <span class="kw kw-g">sequential execution</span>
            <span style="color:#1e293b">·</span>
            <span class="kw kw-a">real-time progress</span>
            <span style="color:#1e293b">·</span>
            <span class="kw kw-v">full report download</span>
        </div>
    </div>
    """, unsafe_allow_html=True)