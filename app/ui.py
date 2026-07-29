import streamlit as st
import tempfile
import os

from services.analyzer_service import analyze_resume_against_jd
from report.pdf_generator import generate_pdf_report

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
)

# -----------------------------
# Header
# -----------------------------

st.title("🤖 AI Resume Analyzer")
st.caption("Semantic Resume Matching • AI Suggestions • ATS Optimization")

st.divider()

# -----------------------------
# Upload Section
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"],
    )

with col2:
    jd_file = st.file_uploader(
        "📋 Upload Job Description",
        type=["pdf"],
    )

st.divider()

# -----------------------------
# Analyze Button
# -----------------------------

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True,
)

# -----------------------------
# Analysis
# -----------------------------

if analyze:

    if resume_file is None or jd_file is None:
        st.warning("Please upload both Resume and Job Description.")
        st.stop()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as resume_temp:
        resume_temp.write(resume_file.read())
        resume_path = resume_temp.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as jd_temp:
        jd_temp.write(jd_file.read())
        jd_path = jd_temp.name

    with st.spinner("Analyzing Resume..."):

        result = analyze_resume_against_jd(
            resume_path,
            jd_path,
        )

        pdf_path = generate_pdf_report(result)

    st.success("Analysis Completed Successfully!")

    st.divider()

    # ====================================
    # Dashboard
    # ====================================

    st.header("📊 Resume Analysis Dashboard")

    metric1, metric2, skill_col = st.columns([1, 1, 2])

    # -----------------------------
    # Semantic Match
    # -----------------------------

    with metric1:

        st.metric(
            label="Semantic Match",
            value=f"{result['semantic_match']:.2f}%",
        )

    # -----------------------------
    # ATS Score
    # -----------------------------

    with metric2:

        st.metric(
            label="ATS Score",
            value=f"{result['ats_score']:.2f}/100",
        )

    # -----------------------------
    # Missing Skills
    # -----------------------------

    with skill_col:

        st.subheader("❌ Missing Skills")

        if result["missing_skills"]:

            for skill in result["missing_skills"]:
                st.markdown(f"- **{skill}**")

        else:
            st.success("No Missing Skills 🎉")

    st.divider()

    # -----------------------------
    # AI Suggestions
    # -----------------------------

    st.subheader("💡 AI Suggestions")

    st.info(result["suggestions"])

    st.divider()

    # -----------------------------
    # Download Report
    # -----------------------------

    with open(pdf_path, "rb") as pdf:

        st.download_button(
            label="📥 Download Analysis Report",
            data=pdf,
            file_name="Resume_Analysis_Report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    os.remove(resume_path)
    os.remove(jd_path)
