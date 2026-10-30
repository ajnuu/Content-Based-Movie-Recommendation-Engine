import time

import streamlit as st

from recommender import movies, recommend

st.set_page_config(
    page_title="CineSense AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    html, body {
        background: #050816;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(76, 104, 255, 0.25), transparent 27%),
            radial-gradient(circle at bottom right, rgba(255, 120, 90, 0.18), transparent 30%),
            linear-gradient(135deg, #020611 0%, #0b1120 28%, #111827 60%, #070b16 100%);
        color: #edf2ff;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background-image:
            radial-gradient(2px 2px at 20% 30%, rgba(255,255,255,0.8), transparent),
            radial-gradient(1.5px 1.5px at 70% 40%, rgba(159,173,255,0.8), transparent),
            radial-gradient(1.5px 1.5px at 80% 70%, rgba(255,255,255,0.8), transparent),
            radial-gradient(2px 2px at 35% 80%, rgba(125,211,252,0.75), transparent),
            radial-gradient(1.5px 1.5px at 55% 20%, rgba(255,255,255,0.8), transparent),
            radial-gradient(2px 2px at 90% 15%, rgba(255,255,255,0.7), transparent);
        background-repeat: repeat;
        background-size: 300px 300px;
        opacity: 0.9;
        pointer-events: none;
        z-index: 0;
    }

    .main .block-container {
        position: relative;
        z-index: 1;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .topbar {
        display: none;
    }

    .stSelectbox > div > div {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.25);
        border-radius: 14px;
        box-shadow: inset 0 0 18px rgba(96, 165, 250, 0.08);
    }

    .stButton > button {
        background: linear-gradient(135deg, #7c3aed 0%, #38bdf8 100%);
        color: white;
        border: none;
        border-radius: 14px;
        font-weight: 700;
        padding: 0.75rem 1.5rem;
        box-shadow: 0 10px 22px rgba(56, 189, 248, 0.28);
    }

    .stButton > button:hover {
        filter: brightness(1.08);
        transform: translateY(-1px);
    }

    .hero-panel {
        border: 1px solid rgba(148, 163, 184, 0.2);
        background: rgba(8, 12, 22, 0.68);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 1.2rem 1.5rem 1rem;
        box-shadow: 0 20px 40px rgba(2, 6, 23, 0.45);
        margin-bottom: 1.2rem;
    }

    .hero-title {
        text-align: center;
        font-size: clamp(2.5rem, 4vw, 4.5rem);
        font-weight: 800;
        letter-spacing: 0.06em;
        margin: 0;
        color: #f8fbff;
        text-shadow: 0 0 18px rgba(96, 165, 250, 0.45), 0 0 32px rgba(168, 85, 247, 0.22);
    }

    .hero-subtitle {
        text-align: center;
        margin-top: 0.6rem;
        color: #cbd5e1;
        font-size: 1.05rem;
        letter-spacing: 0.04em;
    }

    .feature-pill {
        display: inline-block;
        padding: 0.45rem 0.8rem;
        border-radius: 999px;
        background: rgba(59, 130, 246, 0.12);
        border: 1px solid rgba(96, 165, 250, 0.25);
        color: #dbeafe;
        font-size: 0.76rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .panel-tag {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(15, 118, 110, 0.12);
        color: #a7f3d0;
        border: 1px solid rgba(45, 212, 191, 0.2);
        border-radius: 999px;
        padding: 0.4rem 0.8rem;
        font-size: 0.72rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .movie-card {
        position: relative;
        border-radius: 20px;
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.9), rgba(8, 11, 20, 0.96));
        border: 1px solid rgba(148, 163, 184, 0.18);
        min-height: 230px;
        padding: 1rem 1rem 0.9rem;
        overflow: hidden;
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.42);
        margin-bottom: 0.9rem;
    }

    .movie-card::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(59,130,246,0.08), rgba(168,85,247,0.08));
        pointer-events: none;
    }

    .card-header {
        position: relative;
        z-index: 1;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.8rem;
    }

    .card-badge {
        background: rgba(14, 165, 233, 0.18);
        color: #dbeafe;
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 999px;
        padding: 0.28rem 0.62rem;
        font-size: 0.64rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .card-number {
        color: rgba(191, 219, 254, 0.75);
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
    }

    .movie-title {
        position: relative;
        z-index: 1;
        color: #f8fafc;
        font-size: 1.2rem;
        font-weight: 700;
        line-height: 1.35;
        margin: 0.2rem 0 0.55rem;
    }

    .movie-blurb {
        position: relative;
        z-index: 1;
        color: #dbe7ff;
        font-size: 0.82rem;
        line-height: 1.6;
        margin: 0;
    }

    .glow-line {
        position: absolute;
        bottom: 0;
        left: 0;
        height: 2px;
        width: 100%;
        background: linear-gradient(90deg, rgba(56, 189, 248, 0.8), rgba(168, 85, 247, 0.75), rgba(248, 113, 113, 0.7));
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

st.markdown(
    """
    <div class="hero-panel">
        <div class="panel-tag">✨ neural curiosity engine</div>
        <h1 class="hero-title">CineSense AI</h1>
        <div class="hero-subtitle">Discover the next cinematic obsession with a little cosmic intuition.</div>
        <div style="text-align:center; margin-top:1rem;">
            <span class="feature-pill">AI matching</span>
            <span class="feature-pill">Genre similarity</span>
            <span class="feature-pill">Curated picks</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

movie_name = st.selectbox("Select a movie", movies["title"].values)


def escape_html(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


if st.button("✨ Recommend"):
    try:
        with st.spinner("🚀 Scanning the galaxy for your next favorite movie..."):
            time.sleep(1)
            results = recommend(movie_name)

        st.markdown("<h3 style='color:#dbeafe; margin-top:1.2rem; margin-bottom:1rem;'>Recommended for you</h3>", unsafe_allow_html=True)

        columns = st.columns(5)
        for index, movie in enumerate(results):
            with columns[index % 5]:
                safe_movie = escape_html(movie)
                st.markdown(
                    f"""
                    <div class="movie-card">
                        <div class="card-header">
                            <span class="card-badge">Neural Match</span>
                            <span class="card-number">#{index + 1}</span>
                        </div>
                        <h3 class="movie-title">{safe_movie}</h3>
                        <p class="movie-blurb">This pick aligns with the same genre DNA and cinematic energy as your selection.</p>
                        <div class="glow-line"></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    except Exception as exc:
        st.error(exc)
