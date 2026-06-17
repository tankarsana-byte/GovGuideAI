import streamlit as st
from streamlit_option_menu import option_menu
from backend import navigate_query

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="GovGuide AI",
    page_icon="🏛️",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

[data-testid="stSidebar"] {
    background-color: #0f172a;
}

[data-testid="stSidebar"] * {
    color: orange;
}

.big-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 18px;
    margin-bottom: 30px;
}

.service-card {
    background: #f8fafc;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
    text-align: center;
    font-weight: bold;
}

.response-box {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    margin-top: 20px;
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# SIDEBAR
# ==================================

with st.sidebar:

    st.title("🏛️ GovGuide AI")

    selected = option_menu(
        "Quick Services",
        [
            "Home",
            "Food Business",
            "Scholarships",
            "MSME Registration",
            "Farmer Schemes",
            "Certificates"
        ],
        icons=[
            "house",
            "shop",
            "mortarboard",
            "building",
            "tree",
            "file-earmark-text"
        ],
        menu_icon="robot",
        default_index=0
    )

    st.divider()

    state = st.selectbox(
        "📍 Select State",
        [
            "Maharashtra",
            "Gujarat",
            "Karnataka",
            "Delhi"
        ]
    )

    language = st.selectbox(
        "🌐 Language",
        [
            "English",
            "Hindi",
            "Marathi"
        ]
    )

# ==================================
# HEADER
# ==================================

st.markdown(
    '<div class="big-title">🏛️ GovGuide AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Government Service Navigator</div>',
    unsafe_allow_html=True
)

# ==================================
# QUICK SERVICE BUTTONS
# ==================================

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🧁 Start Food Business"):
        st.session_state["query"] = "I want to start a bakery in Maharashtra"

with col2:
    if st.button("🎓 Find Scholarships"):
        st.session_state["query"] = "Scholarships for engineering students"

with col3:
    if st.button("🏢 MSME Registration"):
        st.session_state["query"] = "How can I register my MSME business"

st.write("")

# ==================================
# CHAT INPUT
# ==================================

default_query = st.session_state.get("query", "")

query = st.text_area(
    "💬 Describe your requirement",
    value=default_query,
    height=300,
    placeholder="""
Examples:

• I want to start a bakery in Maharashtra

• I am a female engineering student looking for scholarships

• I want to register my business under MSME

• Tell me schemes available for women entrepreneurs

• Government schemes for farmers
"""
)

# ==================================
# ANALYZE BUTTON
# ==================================

if st.button("🚀 Analyze Request"):

    if query.strip() == "":
        st.warning("Please enter your query.")

    else:

        try:

            with st.spinner("🤖 GovGuide AI is analyzing your request..."):

                answer = navigate_query(query)

            st.success("Analysis Complete")

            st.markdown("## 🤖 AI Recommendation")

            st.markdown("---")

            st.markdown(answer)

        except Exception as e:

            st.error(f"Error: {str(e)}")

# ==================================
# FOOTER
# ==================================

st.write("")
st.write("")
st.divider()

st.caption("Built with ❤️ using Streamlit | GovGuide AI | BuildFest 2026")
