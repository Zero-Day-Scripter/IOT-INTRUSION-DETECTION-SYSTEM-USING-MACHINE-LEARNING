import streamlit as st

def load_cyber_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ========== ROOT VARIABLES ========== */
    :root {
        --bg-page:       #0e1624;
        --bg-nav:        #111927;
        --bg-sidebar:    #131d2e;
        --bg-card:       #182235;
        --bg-input:      #1a2740;
        --bg-term:       #0a0f1a;
        --border:        #1e3050;
        --border-light:  #243a5e;
        --green:         #9fef00;
        --green-dim:     #6abf00;
        --green-bg:      rgba(159,239,0,0.08);
        --blue:          #4d9de0;
        --red:           #ff4d4d;
        --orange:        #f0883e;
        --text-h:        #ffffff;
        --text-body:     #cdd6f4;
        --text-muted:    #7a8fa6;
        --text-dim:      #3d5270;
        --font-ui:       'Inter', system-ui, sans-serif;
        --font-mono:     'JetBrains Mono', 'Courier New', monospace;
        --radius:        10px;
        --radius-sm:     6px;
    }

    /* ========== GLOBAL ========== */
    *, *::before, *::after {
        box-sizing: border-box !important;
    }

    html {
        font-size: 16px !important;
    }

    body, .stApp {
        background-color: var(--bg-page) !important;
        color: var(--text-body) !important;
        font-family: var(--font-ui) !important;
    }

    /* ========== HIDE STREAMLIT CHROME ========== */
    #MainMenu { visibility: hidden !important; }
    footer    { visibility: hidden !important; }

    /* ========== TOP NAV BAR (full width) ========== */
    header[data-testid="stHeader"] {
        background: transparent !important;
        border-bottom: none !important;
        height: 64px !important;
        min-height: 64px !important;
        display: flex !important;
        align-items: center !important;
        padding: 0 24px !important;
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        z-index: 10001 !important;
        pointer-events: none !important;
    }

    /* Sidebar toggle in header */
    button[data-testid="baseButton-header"] {
        position: relative !important;
        z-index: 10002 !important;
        pointer-events: auto !important;
        color: var(--text-muted) !important;
        background: transparent !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        font-size: 1rem !important;
        padding: 6px 10px !important;
        margin-right: 16px !important;
        transition: all 0.15s !important;
    }
    button[data-testid="baseButton-header"]:hover {
        border-color: var(--green) !important;
        color: var(--green) !important;
    }

    /* Push main content below fixed header */
    .main .block-container {
        padding-top: 80px !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 1400px !important;
    }

    /* ========== SIDEBAR ========== */
    section[data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border) !important;
        position: fixed !important;
        top: 64px !important;
        bottom: 0 !important;
        height: auto !important;
        padding: 24px 16px !important;
        min-width: 270px !important;
        max-width: 270px !important;
    }

    section[data-testid="stSidebar"] * {
        font-family: var(--font-ui) !important;
    }

    section[data-testid="stSidebar"] .material-symbols-rounded,
    section[data-testid="stSidebar"] [data-testid="stIconMaterial"] {
        font-family: "Material Symbols Rounded" !important;
    }

    /* Sidebar section headers */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        font-size: 0.68rem !important;
        font-weight: 700 !important;
        color: var(--green) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.12em !important;
        border-bottom: 1px solid var(--border) !important;
        padding-bottom: 10px !important;
        margin: 0 0 16px 0 !important;
    }

    /* Sidebar labels */
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] div[data-testid="stWidgetLabel"] * {
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        color: var(--text-muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
    }

    /* Radio options */
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        color: var(--text-body) !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
        padding: 10px 14px !important;
        margin: 4px 0 !important;
        border-radius: var(--radius-sm) !important;
        border: 1px solid transparent !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        transition: all 0.15s !important;
        cursor: pointer !important;
    }
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
        background: var(--bg-input) !important;
        border-color: var(--border-light) !important;
        color: var(--text-h) !important;
    }
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label[data-checked="true"] {
        background: var(--green-bg) !important;
        border-color: var(--green-dim) !important;
        color: var(--green) !important;
        font-weight: 600 !important;
    }

    /* Sidebar alerts / success */
    section[data-testid="stSidebar"] .stAlert {
        font-size: 0.85rem !important;
        padding: 10px 14px !important;
        border-radius: var(--radius-sm) !important;
        border: 1px solid var(--green-dim) !important;
        background: var(--green-bg) !important;
        color: var(--green) !important;
    }

    /* ========== HEADINGS (main area) ========== */
    h1 {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        color: var(--text-h) !important;
        font-family: var(--font-ui) !important;
        letter-spacing: -0.02em !important;
        margin-bottom: 6px !important;
    }
    h2 {
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        color: var(--text-h) !important;
        font-family: var(--font-ui) !important;
        margin-bottom: 4px !important;
    }
    h3 {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: var(--text-body) !important;
        font-family: var(--font-ui) !important;
    }
    h4 {
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        color: var(--text-muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        font-family: var(--font-ui) !important;
    }

    /* ========== PARAGRAPH / BODY ========== */
    p, .stMarkdown p {
        font-size: 1rem !important;
        color: var(--text-body) !important;
        line-height: 1.6 !important;
        font-family: var(--font-ui) !important;
    }

    /* ========== WIDGET LABELS (main area) ========== */
    label,
    div[data-testid="stWidgetLabel"],
    div[data-testid="stWidgetLabel"] *,
    div[data-testid="stBaseWidgetLabel"] * {
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        color: var(--text-muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        font-family: var(--font-ui) !important;
    }

    /* ========== TABS ========== */
    .stTabs [role="tablist"] {
        background: transparent !important;
        border-bottom: 1px solid var(--border) !important;
        gap: 0 !important;
        padding: 0 !important;
        margin-bottom: 28px !important;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        font-family: var(--font-ui) !important;
        color: var(--text-muted) !important;
        padding: 12px 24px !important;
        background: transparent !important;
        border-radius: 0 !important;
        border-bottom: 2px solid transparent !important;
        transition: all 0.15s !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-h) !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: var(--green) !important;
        border-bottom-color: var(--green) !important;
        font-weight: 600 !important;
    }

    /* ========== SELECTBOX ========== */
    .stSelectbox div[data-baseweb="select"] > div {
        background: var(--bg-input) !important;
        border: 1px solid var(--border-light) !important;
        border-radius: var(--radius-sm) !important;
        min-height: 48px !important;
        transition: border-color 0.15s !important;
    }
    .stSelectbox div[data-baseweb="select"] > div:hover {
        border-color: var(--green) !important;
    }
    .stSelectbox div[data-baseweb="select"] > div div {
        color: var(--text-h) !important;
        font-size: 0.95rem !important;
        font-family: var(--font-ui) !important;
        font-weight: 500 !important;
    }
    .stSelectbox div[data-baseweb="select"] input {
        color: var(--text-h) !important;
        font-size: 0.95rem !important;
        font-family: var(--font-ui) !important;
    }
    .stSelectbox div[data-baseweb="select"] svg {
        fill: var(--text-muted) !important;
    }

    /* Dropdown list */
    div[data-baseweb="popover"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border-light) !important;
        border-radius: var(--radius-sm) !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6) !important;
    }
    div[data-baseweb="popover"] li {
        font-size: 0.9rem !important;
        font-family: var(--font-ui) !important;
        color: var(--text-body) !important;
        background: transparent !important;
        padding: 10px 16px !important;
        border-bottom: 1px solid var(--border) !important;
        list-style: none !important;
        transition: all 0.12s !important;
    }
    div[data-baseweb="popover"] li:hover {
        background: var(--bg-input) !important;
        color: var(--text-h) !important;
    }
    div[data-baseweb="popover"] li[aria-selected="true"] {
        background: var(--green-bg) !important;
        color: var(--green) !important;
        font-weight: 600 !important;
    }

    /* ========== SLIDER ========== */
    .stSlider [data-testid="stTickBarMin"],
    .stSlider [data-testid="stTickBarMax"],
    .stSlider [data-testid="stThumbValue"],
    .stSlider [data-testid="stSliderThumbValue"] {
        font-size: 0.82rem !important;
        font-family: var(--font-mono) !important;
        color: var(--text-muted) !important;
    }
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background: var(--green) !important;
        border: 2px solid var(--bg-page) !important;
        width: 18px !important;
        height: 18px !important;
    }

    /* ========== BUTTONS ========== */
    .stButton > button {
        font-family: var(--font-ui) !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.01em !important;
        padding: 12px 28px !important;
        border-radius: var(--radius-sm) !important;
        background: #2563eb !important;
        color: #ffffff !important;
        border: none !important;
        transition: all 0.15s !important;
        cursor: pointer !important;
    }
    .stButton > button:hover {
        background: #1d4ed8 !important;
        box-shadow: 0 0 20px rgba(37,99,235,0.35) !important;
        transform: translateY(-1px) !important;
    }
    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* ========== METRIC CARDS ========== */
    [data-testid="stMetric"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        padding: 20px 24px !important;
        transition: border-color 0.15s !important;
    }
    [data-testid="stMetric"]:hover {
        border-color: var(--green-dim) !important;
    }
    [data-testid="stMetric"] label {
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 800 !important;
        color: var(--text-h) !important;
        font-family: var(--font-ui) !important;
    }

    /* ========== ALERTS ========== */
    .stAlert {
        font-size: 0.9rem !important;
        font-family: var(--font-ui) !important;
        border-radius: var(--radius-sm) !important;
        padding: 12px 18px !important;
    }

    /* ========== DATA FRAME ========== */
    [data-testid="stDataFrame"] {
        border-radius: var(--radius) !important;
        border: 1px solid var(--border) !important;
        overflow: hidden !important;
    }
    [data-testid="stDataFrame"] table {
        font-family: var(--font-mono) !important;
        font-size: 0.88rem !important;
    }
    [data-testid="stDataFrame"] thead th {
        background: var(--bg-card) !important;
        color: var(--text-muted) !important;
        font-size: 0.72rem !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        padding: 12px 16px !important;
        border-bottom: 1px solid var(--border-light) !important;
        font-family: var(--font-ui) !important;
    }
    [data-testid="stDataFrame"] tbody td {
        background: var(--bg-page) !important;
        color: var(--text-body) !important;
        font-size: 0.88rem !important;
        padding: 10px 16px !important;
        border-bottom: 1px solid var(--border) !important;
    }
    [data-testid="stDataFrame"] tbody tr:hover td {
        background: var(--bg-card) !important;
    }

    /* ========== FILE UPLOADER ========== */
    [data-testid="stFileUploader"] {
        border: 1px dashed var(--border-light) !important;
        border-radius: var(--radius) !important;
        padding: 32px !important;
        background: var(--bg-card) !important;
        transition: all 0.15s !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--green) !important;
        background: rgba(159,239,0,0.03) !important;
    }
    [data-testid="stFileUploader"] label {
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        color: var(--text-body) !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
    }

    /* ========== SPINNER ========== */
    .stSpinner > div {
        border-color: var(--green) transparent transparent !important;
    }

    /* ========== SCROLLBAR ========== */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-page); }
    ::-webkit-scrollbar-thumb {
        background: var(--border-light);
        border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--green-dim); }

    /* ========== CUSTOM COMPONENTS ========== */

    /* Top nav brand bar */
    .top-nav {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 64px;
        background: var(--bg-nav);
        border-bottom: 1px solid var(--border);
        display: flex;
        align-items: center;
        padding: 0 28px 0 76px;
        z-index: 10000;
        gap: 16px;
    }
    .top-nav-logo {
        display: flex;
        align-items: center;
        gap: 10px;
        text-decoration: none;
    }
    .top-nav-icon {
        width: 36px;
        height: 36px;
        background: var(--green);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
    }
    .top-nav-brand {
        font-family: var(--font-ui) !important;
        font-size: 1.05rem !important;
        font-weight: 800 !important;
        color: var(--text-h) !important;
        letter-spacing: -0.01em;
    }
    .top-nav-brand span {
        color: var(--green) !important;
    }
    .top-nav-divider {
        width: 1px;
        height: 28px;
        background: var(--border);
        margin: 0 8px;
    }
    .top-nav-subtitle {
        font-size: 0.82rem !important;
        color: var(--text-muted) !important;
        font-family: var(--font-ui) !important;
    }
    .top-nav-badge {
        margin-left: auto;
        font-size: 0.72rem;
        font-weight: 700;
        font-family: var(--font-mono) !important;
        color: var(--bg-page);
        background: var(--green);
        border-radius: 20px;
        padding: 4px 14px;
        letter-spacing: 0.05em;
    }

    /* Page section header */
    .section-header {
        margin: 0 0 24px 0;
    }
    .section-header h2 {
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        color: var(--text-h) !important;
        margin: 0 0 4px 0 !important;
    }
    .section-header p {
        font-size: 0.92rem !important;
        color: var(--text-muted) !important;
        margin: 0 !important;
    }

    /* Stat row cards */
    .stat-row {
        display: flex;
        gap: 14px;
        margin: 20px 0;
        flex-wrap: wrap;
    }
    .stat-card {
        flex: 1;
        min-width: 130px;
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 18px 20px;
        transition: border-color 0.15s;
    }
    .stat-card:hover { border-color: var(--border-light); }
    .stat-card-label {
        font-size: 0.68rem;
        font-weight: 700;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.12em;
        margin-bottom: 8px;
        font-family: var(--font-ui) !important;
    }
    .stat-card-value {
        font-size: 2rem;
        font-weight: 800;
        color: var(--text-h);
        font-family: var(--font-ui) !important;
        line-height: 1;
    }
    .stat-card-value.green { color: var(--green); }
    .stat-card-value.red   { color: var(--red);   }
    .stat-card-value.blue  { color: var(--blue);  }

    /* Terminal block */
    .term-block {
        background: var(--bg-term);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 18px 22px;
        margin: 16px 0;
        font-family: var(--font-mono) !important;
        font-size: 0.88rem;
        line-height: 1.8;
        overflow-x: auto;
    }
    .t-prompt { color: var(--text-dim); }
    .t-cmd    { color: var(--text-body); }
    .t-ok     { color: var(--green); }
    .t-warn   { color: var(--orange); }
    .t-err    { color: var(--red); }
    .t-dim    { color: var(--text-dim); }

    /* Divider */
    .divider {
        border: none;
        border-top: 1px solid var(--border);
        margin: 24px 0;
    }

    /* Sidebar info block */
    .info-block {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-sm);
        padding: 14px 16px;
        margin-top: 12px;
    }
    .info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0;
        border-bottom: 1px solid var(--border);
        font-size: 0.82rem;
        font-family: var(--font-ui) !important;
    }
    .info-row:last-child { border-bottom: none; }
    .info-row-key {
        color: var(--text-muted);
        font-weight: 600;
    }
    .info-row-val {
        color: var(--text-h);
        font-family: var(--font-mono) !important;
        font-size: 0.8rem;
    }
    </style>

    <!-- ====== FIXED TOP NAV BAR ====== -->
    <div class="top-nav">
        <div class="top-nav-logo">
            <div class="top-nav-icon">🛡</div>
            <span class="top-nav-brand">IoT&nbsp;<span>IDS</span></span>
        </div>
        <div class="top-nav-divider"></div>
        <span class="top-nav-subtitle">
            Real-time ML-based Network Intrusion Detection
        </span>
        <div class="top-nav-badge">● LIVE</div>
    </div>
    """, unsafe_allow_html=True)


# ========== HELPER RENDERERS ==========

def render_section_header(title: str, subtitle: str = ""):
    st.markdown(f"""
    <div class="section-header">
        <h2>{title}</h2>
        {"<p>" + subtitle + "</p>" if subtitle else ""}
    </div>
    """, unsafe_allow_html=True)


def render_stat_row(total, attacks, normals, packets=None):
    pkt_html = ""
    if packets is not None:
        pkt_html = (
            '<div class="stat-card">'
            '<div class="stat-card-label">Packets</div>'
            f'<div class="stat-card-value blue">{packets}</div>'
            '</div>'
        )

    threat_pct = f"{(attacks/total*100):.0f}%" if total > 0 else "0%"

    html = (
        '<div class="stat-row">'
        '<div class="stat-card">'
        '<div class="stat-card-label">Flows Analyzed</div>'
        f'<div class="stat-card-value">{total}</div>'
        '</div>'
        '<div class="stat-card">'
        '<div class="stat-card-label">Normal</div>'
        f'<div class="stat-card-value green">{normals}</div>'
        '</div>'
        '<div class="stat-card">'
        '<div class="stat-card-label">Attacks</div>'
        f'<div class="stat-card-value red">{attacks}</div>'
        '</div>'
        '<div class="stat-card">'
        '<div class="stat-card-label">Threat Rate</div>'
        f'<div class="stat-card-value {"red" if attacks > 0 else "green"}">'
        f'{threat_pct}</div>'
        '</div>'
        f'{pkt_html}'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


def render_term(lines: list):
    inner = ""
    for line in lines:
        t    = line.get("type", "ok")
        text = line.get("text", "")
        if t == "prompt":
            inner += (
                f'<span class="t-prompt">$ </span>'
                f'<span class="t-cmd">{text}</span><br>'
            )
        elif t == "ok":
            inner += f'<span class="t-ok">✓ {text}</span><br>'
        elif t == "warn":
            inner += f'<span class="t-warn">⚠ {text}</span><br>'
        elif t == "err":
            inner += f'<span class="t-err">✗ {text}</span><br>'
        else:
            inner += f'<span class="t-dim">{text}</span><br>'

    st.markdown(
        f'<div class="term-block">{inner}</div>',
        unsafe_allow_html=True
    )


def render_sidebar_info(meta: dict):
    rows = "".join(
        f'<div class="info-row">'
        f'<span class="info-row-key">{k}</span>'
        f'<span class="info-row-val">{v}</span>'
        f'</div>'
        for k, v in meta.items()
    )
    st.sidebar.markdown(
        f'<div class="info-block">{rows}</div>',
        unsafe_allow_html=True
    )