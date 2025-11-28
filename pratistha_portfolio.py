import streamlit as st
from pathlib import Path

# ================== BASIC CONFIG ==================
st.set_page_config(
    page_title="Pratistha Thapa | Portfolio",
    page_icon="📊",
    layout="wide",
)

# ================== PATHS & ASSETS ==================
ASSETS_DIR = Path("assets")
PROFILE_PIC_PATH = ASSETS_DIR / "PratisthaThapa.jpeg"
RESUME_PATH = ASSETS_DIR / "CV_PratisthaThapa.pdf"

RESUME_BYTES = None
if RESUME_PATH.exists():
    with open(RESUME_PATH, "rb") as f:
        RESUME_BYTES = f.read()

# ================== SIDEBAR ==================
with st.sidebar:
    st.title("👋 Bonjour!")

    # Profile picture (optional)
    if PROFILE_PIC_PATH.exists():
        st.image(str(PROFILE_PIC_PATH), use_container_width=True)

    st.markdown(
        """
        **Location:** Paris, France  
        **Email:** [prtsthapa99@gmail.com](mailto:prtsthapa99@gmail.com)  
        **Phone:** +33 6 16 16 23 89
        """
    )

    # Resume download (optional)
    if RESUME_BYTES is not None:
        st.download_button(
            label="📄 Download my CV",
            data=RESUME_BYTES,
            file_name="CV_PratisthaThapa.pdf",
            mime="application/pdf",
            key="download_resume_sidebar",
        )

   


    st.markdown("---")
    st.caption("Open to Data / Product Analytics roles (junior & graduate).")

# ================== CUSTOM CSS ==================
st.markdown(
    """
    <style>
     /* Layout tweaks: let Streamlit decide width, just add comfortable padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2.5rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }

    /* Titles – smaller & more responsive */
    .big-title {
        font-size: 2.4rem !important;   /* ~38px on normal screens, scales better */
        line-height: 1.15;
        font-weight: 700 !important;
        margin-bottom: 0.1rem;
        word-wrap: break-word;
    } */

    /* Section titles */
    .section-header {
        font-size: 26px !important;
        font-weight: 600 !important;
        margin-top: 0.5rem;
        margin-bottom: 0.8rem;
    }

    /* Tags / pills */
    .tag-pill {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 999px;
        border: 1px solid #e5e7eb;
        margin-right: 6px;
        margin-bottom: 4px;
        font-size: 11px;
        background-color: #f9fafb;
    }
     /* Section headings like "About me", "Experience", etc. */
    h3 {
        font-size: 1.4rem !important;   /* bigger than body */
        font-weight: 700 !important;    /* bold */
        margin-top: 0.3rem;
        margin-bottom: 0.7rem;
    }

    /* Tabs styling */
    .stTabs [role="tablist"] {
        gap: 0.5rem;
        margin-bottom: 0.8rem;  /* 👈 add space below the tabs */
    }
    .stTabs [role="tab"] {
        padding: 0.4rem 0.9rem;
        border-radius: 999px;
        background-color: #f9fafb;
        color: #6b7280;
        border: 1px solid #e5e7eb;
        font-size: 14px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1, #ec4899);
        color: #ffffff !important;
        border: none;
        font-weight: 700;
    }
    /* Remove red underline under active tab */
    div[data-baseweb="tab-highlight"] {
        background-color: transparent !important;
    }
    /* Make all buttons smaller & tighter */
    .stButton > button, .stLinkButton > button {
        padding: 0.15rem 0.7rem;      /* smaller height & width */
        font-size: 13px;              /* smaller text */
        border-radius: 999px;
        margin-top: 0.2rem;           /* less vertical gap */
        margin-bottom: 0.2rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ================== HEADER / HERO ==================
st.title("Pratistha Thapa")
st.markdown(
    '<p class="sub-title">Data & Product Analytics · Python · SQL · Dashboards · Product Innovation</p>',
    unsafe_allow_html=True,
)

st.write(
    """
    I am a strategic Data Analyst working at the intersection of **data, product, and business**.  
    I use Python, SQL, and BI tools to transform large-scale data into **clear, actionable insights** 
    and to help teams optimise digital experiences through robust dashboards, experimentation, 
    and user journey analysis.

    When I’m not working with data, you’ll likely find me cycling around Paris 🚲🇫🇷, 
    vlogging my rides 🎥, and enjoying a great hot coffee ☕.
    """
)

# Small, close buttons
btn_col1, btn_col2, btn_col3 = st.columns([0.25, 0.25, 0.25])
with btn_col1:
    if RESUME_BYTES is not None:
        st.download_button(
            label="📄 Resume",
            data=RESUME_BYTES,
            file_name="CV_PratisthaThapa.pdf",
            mime="application/pdf",
            key="download_resume_main",
        )
with btn_col2:
    st.link_button("🐙 GitHub", "https://github.com/Pratistha-99")
with btn_col3:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/pratisthapa")

st.write("")  # a tiny spacer before tabs


# ================== TABS ==================
tab_about, tab_experience, tab_projects, tab_skills, tab_education = st.tabs(
    ["👤 About", "🧑‍💼 Experience", "📂 Projects", "🛠 Skills", "🎓 Education"]
)

# ================== ABOUT TAB ==================
with tab_about:
    # st.markdown('<p class="section-header">About me</p>', unsafe_allow_html=True)
    st.subheader("About me")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.write(
            """
            I’m a **data professional** operating at the intersection of **analytics, product ownership,
            requirement gathering, and stakeholder engagement**.

            My work has included:
            - Building and automating **data pipelines and ETL workflows**  
            - Designing **dashboards and monitoring frameworks** for business stakeholders  
            - Analysing **user behaviour, payment journeys, and loan portfolios**  
            - Supporting product strategy through **requirement gathering and roadmap management** within Scrum practices  

            I’m particularly interested in:
            - Product analytics and experimentation  
            - Data engineering, quality & governance  
            """
        )

    with col2:
        st.subheader("Snapshot")
        st.write("- 📍 Based in: Paris, France")
        st.write("- 🧭 Focus: Data Analytics & Product Management")
        st.write("- 🧪 Domains: Digital lending, e-wallets, payments, insurance")
        st.write("- 🤝 Roles: Data Analyst, Business Analyst, Product Owner")

# ================== EXPERIENCE TAB ==================
with tab_experience:
    # st.markdown('<p class="section-header">Experience</p>', unsafe_allow_html=True)
    st.subheader("Experience")

    # Allianz Trade
    with st.container(border=True):
        st.markdown("#### Data Analyst Intern — Allianz Trade (Euler Hermes)")
        st.caption("Jan 2025 – June 2025 · Paris, France")
        st.write(
            """
            - Built and automated **data pipelines / ETL workflows** in Python and Informatica,  
              with Strategy BI dashboard automation and **rule-based validations** across 3 layers
              and 4 insurance policy datasets, helping establish a **data governance framework**.
            - Partnered with the **Surety** team to define data requirements, write advanced SQL
              queries, and design an **intelligent data cube** powering a predictive insights
              dashboard for premiums, eliminating manual Excel workflows and improving accuracy
              and timeliness.
            - Published **monitoring dashboards** using VBA macros for PMO budgeting KPIs and
              timesheets, improving steering committee visibility.
            """
        )
        st.markdown(
            """
            <span class="tag-pill">Python</span>
            <span class="tag-pill">Snowflake</span>
            <span class="tag-pill">Informatica Data Integration</span>
            <span class="tag-pill">Strategy BI</span>
            <span class="tag-pill">Data Governance</span>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # Vanilla Transtechnor
    with st.container(border=True):
        st.markdown("#### Business Analyst / Product Owner — Vanilla Transtechnor Pvt. Ltd.")
        st.caption("June 2023 – July 2024 · Nepal")
        st.write(
            """
            - Led the **revamp of a digital wallet** across technical and UX tracks, running
              requirement gathering and authoring PRDs, user stories, and acceptance criteria.
            - Managed a backlog of **18 modules** and prioritised 5 high-impact features, 
              improving feature performance by **25%** and aligning with marketing and adoption goals.
            - Redesigned wallet **business logic** and standardized **UI/UX flows** for onboarding,
              authentication, and payment journeys; coordinated with engineering to deliver
              milestones **2 weeks ahead of schedule**, increasing throughput by **13%**.
            """
        )
        st.markdown(
            """
            <span class="tag-pill">Requirement Gathering</span>
            <span class="tag-pill">Product Ownership</span>
            <span class="tag-pill">Digital Wallet</span>
            <span class="tag-pill">User Journeys</span>
            <span class="tag-pill">Scrum</span>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # GTA
    with st.container(border=True):
        st.markdown("#### Graduate Teaching Assistant — Westcliff University")
        st.caption("May 2023 – June 2024 · Nepal")
        st.write(
            """
            - Supported courses such as **Information Systems** and **Principles of Data Management**
              with an average class size of ~20 students.
            - Facilitated class discussions, assisted with assignments, and provided feedback to
              help students understand core data and systems concepts.
            """
        )
        st.markdown(
            """
            <span class="tag-pill">Teaching</span>
            <span class="tag-pill">Information Systems</span>
            <span class="tag-pill">Data Management</span>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # eXtensoData
    with st.container(border=True):
        st.markdown("#### Business Analyst — eXtensoData Pvt. Ltd.")
        st.caption("June 2021 – May 2023 · Nepal")
        st.write(
            """
            - Onboarded **4 commercial banks** to a digital lending platform, generating a
              **USD 4.24M loan portfolio** across 46,000 loans and increasing revenue growth
              channel by **37%** over 10 months.
            - Defined KPIs and delivered an **automated monthly dashboard** analysing loan
              behaviour for 65k eligible users across 7 partner banks, enabling stakeholders to
              track **risk underwriting trends**.
            - Analysed digital payment user behaviour across channels, producing **80+ monthly**
              performance reports on user KPIs and campaign engagement, accelerating decisions by
              **53%** for partner banks and executives.
            - Collaborated with business development and operations teams to translate reporting
              requirements into **in-house BI solutions**, reducing manual data processing efforts
              by **370 hours per week**.
            """
        )
        st.markdown(
            """
            <span class="tag-pill">Digital Lending</span>
            <span class="tag-pill">KPI Design & Dashboards</span>
            <span class="tag-pill">Banking Analytics</span>
            <span class="tag-pill">Requirement Gathering</span>
            """,
            unsafe_allow_html=True,
        )

# ================== PROJECTS TAB ==================
with tab_projects:
    # st.markdown('<p class="section-header">Projects</p>', unsafe_allow_html=True)
    st.subheader("Projects")
    # ---------- PROJECT 1 ----------
    with st.container(border=True):
        # Title is a clickable link
        st.markdown("### 🧪 A/B Test Experiment Simulator")
        
        st.write(
            """
            Built an **A/B testing simulator** with user-level event generation and analytics
            to help product teams explore how changes in conversion impact overall performance.
            """
        )
        st.markdown(
            """
            **What it does:**
            - Simulates user-level events for **control** and **treatment** variants.  
            - Computes CTR, CVR, and lift between variants.  
            - Runs a **two-proportion Z-test** to evaluate statistical significance.  
            - Provides an interactive **Streamlit UI** so non-technical users can explore
              experiment scenarios.  
            """
        )
        st.markdown(
            """
            **Tech stack:** `Python` · `Streamlit` · `Pandas` · `NumPy`
            """,
        )

        col1, col2 = st.columns(2)
        with col1:
            st.link_button(
                "📂 View on GitHub",
                "https://github.com/Pratistha-99/ab-test-simulator",
            )
        with col2:
            st.link_button(
                "🚀 Open Live App",
                "https://ab-test-simulator-c5i9e4wlucgeexgeh4zagm.streamlit.app/",
            )

        st.markdown(
            """
            <span class="tag-pill">Experimentation</span>
            <span class="tag-pill">A/B Testing</span>
            <span class="tag-pill">Streamlit</span>
            """,
            unsafe_allow_html=True,
        )

# ================== SKILLS TAB ==================
with tab_skills:
    # st.markdown('<p class="section-header">Skills & Tools</p>', unsafe_allow_html=True)
    st.subheader("Skills & Tools")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Languages & Tools")
        st.write(
            """
            - Python (pandas, numpy, matplotlib, scipy)  
            - SQL (Presto / Snowflake)  
            - Informatica Data Integration  
            - Tableau  
            - Strategy BI (MicroStrategy), Power BI  
            """
        )

    with col2:
        st.subheader("Data & Product")
        st.write(
            """
            - Data pipelines & ETL  
            - KPI definition & monitoring  
            - Dashboarding & reporting  
            - Experimentation & user behaviour analysis  
            - Requirements gathering, PRDs, user stories  
            """
        )

    with col3:
        st.subheader("Other")
        st.write(
            """
            - Git  
            - Postman, Swagger  
            - Jira, Confluence  
            - Advanced Excel, VBA  
            - Figma, Canva, n8n, Lovable  
            """
        )

    st.markdown("---")

    st.subheader("Certifications")
    st.write(
        """
        - Registered Product Owner — Scrum Inc.  
        - Registered Scrum Master — Scrum Inc.
        """
    )

    st.markdown("---")

    st.subheader("Languages")
    st.write(
        """
        - English (C1)  
        - Nepali (C2)  
        - Hindi (C1)  
        - French (A2)  
        """
    )

# ================== EDUCATION TAB ==================
with tab_education:
    # st.markdown('<p class="section-header">Education</p>', unsafe_allow_html=True)
    st.subheader("Education")
    with st.container(border=True):
        st.markdown("#### MSc Data Science & Network Intelligence")
        st.caption("Institut Polytechnique de Paris, France · Sept 2024 – July 2025")
        st.write(
            """
            Focus on data science, networks, and intelligent systems, with emphasis on
            analytics, modelling, and scalable data processing.
            """
        )

    st.markdown("")

    with st.container(border=True):
        st.markdown("#### Master of Business Administration — Technology & Innovation")
        st.caption("Westcliff University, Nepal · 2021 – 2023")
        st.write(
            """
            Combined business education with a technology and innovation focus, bridging
            product, strategy, and data-driven decision-making.
            """
        )

    st.markdown("")

    with st.container(border=True):
        st.markdown("#### Bachelor of Computer Application")
        st.caption("Bangalore University, India · 2016 – 2019")
        st.write(
            """
            Built foundations in computer science, programming, and information systems.
            """
        )

# ================== FOOTER ==================
st.markdown("---")
st.caption(
    "Built with ❤️ in Streamlit · Last updated 28/11/2025 · "
    "For opportunities or collaborations, feel free to reach out via email."
)
