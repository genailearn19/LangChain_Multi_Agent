
import streamlit as st
from datetime import datetime

from src.pipeline.pipeline import run_research_pipeline


# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Eswara AI Research Studio",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM CSS - MODERN LIGHT THEME
# =========================================================
st.markdown("""
<style>
/* Main application background */
.stApp {
    background: #F1F5FB;
    color: #172033;
    font-family: "Segoe UI", Arial, sans-serif;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

/* Global text visibility */
.stApp p,
.stApp label,
.stApp li,
.stApp .stMarkdown,
.stApp [data-testid="stCaptionContainer"] {
    color: #26354A;
}

h1, h2, h3, h4 {
    color: #152747 !important;
    font-weight: 750 !important;
}

/* LEFT SIDEBAR */
[data-testid="stSidebar"] {
    background: #142440;
    border-right: 1px solid #263B5B;
}

[data-testid="stSidebar"] > div:first-child {
    background: #142440;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #F1F5FF !important;
}

[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #C0D0E8 !important;
    font-size: 14px;
}

[data-testid="stSidebar"] hr {
    border-color: #3A4D6B;
}

/* Sidebar information box */
[data-testid="stSidebar"] [data-testid="stAlert"] {
    background: #223858;
    border: 1px solid #47638B;
    border-radius: 12px;
}

[data-testid="stSidebar"] [data-testid="stAlert"] p {
    color: #F1F6FF !important;
}

/* Sidebar buttons */
[data-testid="stSidebar"] .stButton > button {
    background: #E45454;
    color: #FFFFFF !important;
    border: 1px solid #F07878;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #C93B45;
    border-color: #FFFFFF;
}

/* HERO BANNER */
.hero {
    padding: 36px;
    border-radius: 22px;
    background: linear-gradient(120deg, #155EEF 0%, #365FEA 50%, #7048D8 100%);
    color: #FFFFFF;
    margin-bottom: 28px;
    box-shadow: 0 12px 30px rgba(36, 82, 180, 0.18);
    border: 1px solid rgba(255, 255, 255, 0.25);
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: clamp(30px, 3vw, 42px);
    line-height: 1.2;
    margin: 0 0 14px 0;
}

.hero p {
    color: #F1F5FF !important;
    font-size: 17px;
    line-height: 1.8;
    margin: 0;
    max-width: 900px;
}

/* SECTION HEADINGS */
.section-title {
    color: #173C78;
    font-size: 25px;
    font-weight: 800;
    margin: 28px 0 18px 0;
    padding-bottom: 10px;
    border-bottom: 2px solid #D8E4F4;
}

/* WORKFLOW CARDS */
.stage {
    padding: 22px 18px;
    border-radius: 17px;
    background: #FFFFFF;
    border: 1px solid #DFE8F5;
    border-top: 4px solid #3976E8;
    min-height: 155px;
    box-shadow: 0 5px 16px rgba(31, 55, 90, 0.06);
    transition: transform 0.2s, box-shadow 0.2s;
}

.stage:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(31, 55, 90, 0.12);
}

.stage-icon {
    font-size: 32px;
}

.stage-title {
    font-size: 17px;
    font-weight: 800;
    color: #183B70;
    margin-top: 12px;
}

.stage-desc {
    color: #52647C;
    font-size: 14px;
    line-height: 1.6;
    margin-top: 8px;
}

/* INPUT FIELDS */
.stTextArea textarea,
.stTextInput input {
    background: #FFFFFF !important;
    color: #172033 !important;
    -webkit-text-fill-color: #172033 !important;
    border: 1px solid #BCCDE2 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
}

.stTextArea textarea::placeholder,
.stTextInput input::placeholder {
    color: #667991 !important;
    -webkit-text-fill-color: #667991 !important;
    opacity: 1 !important;
}

.stTextArea textarea:focus,
.stTextInput input:focus {
    border: 2px solid #3976E8 !important;
    box-shadow: 0 0 0 3px rgba(57, 118, 232, 0.12) !important;
}

/* MAIN BUTTONS */
.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button {
    background: linear-gradient(100deg, #1D5FE8, #5149D9);
    color: #FFFFFF !important;
    border: 1px solid #1D5FE8;
    border-radius: 11px;
    font-size: 15px;
    font-weight: 750;
    min-height: 46px;
    transition: all 0.2s ease;
}

.stButton > button p,
.stFormSubmitButton > button p,
.stDownloadButton > button p {
    color: #FFFFFF !important;
    font-weight: 750;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover {
    filter: brightness(0.90);
    border-color: #153FA0;
    box-shadow: 0 5px 15px rgba(29, 95, 232, 0.2);
}

/* METRIC CARDS */
[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #DFE8F5;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 5px 15px rgba(31, 55, 90, 0.05);
}

[data-testid="stMetricLabel"] {
    color: #536781 !important;
    font-size: 14px !important;
    font-weight: 650 !important;
}

[data-testid="stMetricValue"] {
    color: #174EA6 !important;
    font-weight: 800 !important;
}

/* EXPANDERS */
[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #DCE6F2;
    border-radius: 13px;
    overflow: hidden;
}

[data-testid="stExpander"] summary {
    color: #173C78 !important;
    font-weight: 750;
}

[data-testid="stExpander"] summary p {
    color: #173C78 !important;
    font-size: 15px;
    font-weight: 750;
}

/* REPORT CARDS */
.result-card {
    padding: 24px;
    background: #FFFFFF;
    border: 1px solid #DFE8F5;
    border-left: 5px solid #3976E8;
    border-radius: 14px;
    margin-bottom: 18px;
    box-shadow: 0 5px 16px rgba(31, 55, 90, 0.05);
    color: #26354A;
    line-height: 1.8;
}

.report-content {
    background: #FFFFFF;
    color: #26354A;
    padding: 24px;
    border: 1px solid #DCE6F2;
    border-radius: 14px;
    line-height: 1.85;
}

/* ALERTS */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* DIVIDERS */
hr {
    border-color: #DCE6F2;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #657790;
    font-size: 13px;
    padding: 32px 0 12px 0;
    border-top: 1px solid #DCE6F2;
    margin-top: 40px;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .hero {
        padding: 24px;
    }

    .hero p {
        font-size: 15px;
    }

    .section-title {
        font-size: 22px;
    }

    .stage {
        min-height: 120px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================
if "research_data" not in st.session_state:
    st.session_state.research_data = None

if "research_topic" not in st.session_state:
    st.session_state.research_topic = ""

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.markdown("## 🔬 Eswara AI Research Studio")
    st.caption("MULTI-AGENT RESEARCH WORKSPACE")

    st.divider()

    st.markdown("### ⚙️ Research Pipeline")

    pipeline_steps = [
        ("🔎", "01", "Search Agent", "Find relevant sources"),
        ("📚", "02", "Reader Agent", "Analyze source content"),
        ("✍️", "03", "Writer Agent", "Generate the report"),
        ("🛡️", "04", "Critic Agent", "Review report quality"),
    ]

    for icon, number, title, description in pipeline_steps:
        st.markdown(
            f"""
            <div style="
                background:#203655;
                border:1px solid #3B5273;
                border-radius:12px;
                padding:12px;
                margin:10px 0;
            ">
                <div style="font-size:15px;font-weight:800;color:#FFFFFF;">
                    {icon} &nbsp; {number} &nbsp; {title}
                </div>
                <div style="
                    font-size:13px;
                    color:#D0DDF0;
                    margin-top:6px;
                    line-height:1.5;
                ">
                    {description}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("### 💡 Research Tips")
    st.info(
        "Use a specific research question. Include the technology, "
        "use case, time period, or business problem for more focused results."
    )

    if st.button("🗑️ Clear Results", use_container_width=True):
        st.session_state.research_data = None
        st.session_state.research_topic = ""
        st.rerun()

    st.divider()
    st.caption("Powered by Streamlit + LangChain")


# =========================================================
# HERO HEADER
# =========================================================
st.markdown("""
<div class="hero">
    <h1>🔬 Eswara AI Research Studio</h1>
    <p>
        Your intelligent research workspace.
        Discover reliable sources, analyze content, generate
        structured reports, and review the results with
        an autonomous multi-agent AI pipeline.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# WORKFLOW OVERVIEW
# =========================================================
st.markdown(
    '<div class="section-title">🚀 Your Research Workflow</div>',
    unsafe_allow_html=True,
)

columns = st.columns(4, gap="medium")

stages = [
    ("🔎", "Search Agent", "Discover relevant information and sources."),
    ("📚", "Reader Agent", "Extract key facts and insights from content."),
    ("✍️", "Writer Agent", "Prepare a clear, structured research report."),
    ("🛡️", "Critic Agent", "Evaluate the report and provide feedback."),
]

for col, (emoji, title, description) in zip(columns, stages):
    with col:
        st.markdown(
            f"""
            <div class="stage">
                <div class="stage-icon">{emoji}</div>
                <div class="stage-title">{title}</div>
                <div class="stage-desc">{description}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# RESEARCH INPUT
# =========================================================
st.markdown(
    '<div class="section-title">🎯 Start Your Research</div>',
    unsafe_allow_html=True,
)

st.markdown(
    "Enter a research question below. Your AI agents will "
    "search, analyze, write, and review the findings."
)

with st.form("research_form"):
    topic = st.text_area(
        "Research topic",
        value=st.session_state.research_topic,
        placeholder=(
            "Example: Latest advancements in Agentic AI, "
            "RAG architectures, multi-agent systems, and "
            "their enterprise applications"
        ),
        height=125,
    )

    submitted = st.form_submit_button(
        "🚀 Start AI Research",
        use_container_width=True,
    )


# =========================================================
# RUN RESEARCH PIPELINE
# =========================================================
if submitted:
    if not topic.strip():
        st.warning("Please enter a research topic before continuing.")
    else:
        st.session_state.research_data = None
        st.session_state.research_topic = topic.strip()

        try:
            with st.status(
                "🤖 AI agents are researching your topic...",
                expanded=True,
            ) as status:
                st.write("🔎 Searching for relevant information...")
                st.write("📚 Reading and analyzing source content...")
                st.write("✍️ Preparing the research report...")
                st.write("🛡️ Reviewing the report...")

                result = run_research_pipeline(topic.strip())

                st.session_state.research_data = result

                status.update(
                    label="✅ Research completed successfully!",
                    state="complete",
                    expanded=False,
                )

            st.success("Your research report is ready!")

        except Exception as exc:
            st.error(f"Research failed: {exc}")
            st.exception(exc)


# =========================================================
# DISPLAY RESEARCH RESULTS
# =========================================================
data = st.session_state.research_data

if data:
    st.divider()

    st.markdown(
        '<div class="section-title">📊 Research Dashboard</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"**Research Topic:** {st.session_state.research_topic}"
    )

    st.caption(
        "Generated on "
        + datetime.now().strftime("%d %b %Y, %I:%M %p")
    )

    # Result overview
    c1, c2, c3, c4 = st.columns(4, gap="medium")

    with c1:
        st.metric("Workflow Stages", "4")

    with c2:
        st.metric(
            "Search Results",
            "Available" if data.get("search_results") else "Empty",
        )

    with c3:
        st.metric(
            "Scraped Content",
            "Available" if data.get("scraped_content") else "Empty",
        )

    with c4:
        st.metric(
            "Final Report",
            "Ready" if data.get("report") else "Empty",
        )

    # Search results
    with st.expander("🔎 Step 1 — Search Agent Results"):
        st.markdown(
            data.get("search_results") or "No search results available."
        )

    # Scraped content
    with st.expander("📚 Step 2 — Reader Agent Content"):
        st.markdown(
            data.get("scraped_content")
            or "No scraped content available."
        )

    # Final report
    st.markdown(
        '<div class="section-title">📄 Final Research Report</div>',
        unsafe_allow_html=True,
    )

    report = data.get("report") or "No report generated."

    st.markdown('<div class="report-content">', unsafe_allow_html=True)
    st.markdown(report)
    st.markdown('</div>', unsafe_allow_html=True)

    st.download_button(
        label="⬇️ Download Research Report",
        data=str(report),
        file_name="ai_research_report.md",
        mime="text/markdown",
        use_container_width=True,
    )

    # Critic feedback
    st.markdown(
        '<div class="section-title">🛡️ Critic Review & Feedback</div>',
        unsafe_allow_html=True,
    )

    feedback = data.get("feedback") or "No critic feedback available."

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(feedback)
    st.markdown('</div>', unsafe_allow_html=True)

    st.download_button(
        label="⬇️ Download Critic Feedback",
        data=str(feedback),
        file_name="critic_feedback.md",
        mime="text/markdown",
        use_container_width=True,
    )

else:
    st.markdown("---")

    st.info(
        "👋 Welcome to AI Research Studio! Enter a topic above "
        "and select **Start AI Research** to generate your first report."
    )


# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">
    AI Research Studio · Intelligent Multi-Agent Research Pipeline
</div>
""", unsafe_allow_html=True)
