import streamlit as st

# page configuration
st.set_page_config(page_title="University Admission Predictor", page_icon="🎓", layout="wide")

# Custom CSS for our design
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f5;
    }
    .header {
        font-size: 36px;
        color: #3f51b5;
        font-weight: bold;
    }
    .subheader {
        font-size: 20px;
        color: #555;
    }
    .stButton>button {
        background-color: #3f51b5;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        height: 40px;
        width: 150px;
        margin-top: 10px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .success {
        background-color: #d4edda;
        color: #155724;
    }
    .warning {
        background-color: #fff3cd;
        color: #856404;
    }
    .error {
        background-color: #f8d7da;
        color: #721c24;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and subheader
st.markdown("<div class='header'>University Admission Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Enter your details below to predict your chances of admission!</div>", unsafe_allow_html=True)


with st.form("admission_form"):
    # Academic Information Section
    # each column will allow us to enter differnet categories of information
    st.markdown("### 📚 Academic Information")
    academic_col1, academic_col2 = st.columns(2)

    with academic_col1:
        gre_score = st.number_input("GRE Score", min_value=260, max_value=340, step=1)
        toefl_score = st.number_input("TOEFL Score", min_value=0, max_value=120, step=1)
        cgpa = st.number_input("CGPA (0.0 - 10.0)", min_value=0.0, max_value=10.0, step=0.1)

    with academic_col2:
        sop = st.number_input("SOP Strength (0.5 - 5.0)", min_value=0.5, max_value=5.0, step=0.5)
        lor = st.number_input("LOR Strength (0.5 - 5.0)", min_value=0.5, max_value=5.0, step=0.5)

    # University Information Section
    st.markdown("### 🏫 University Information")
    university_col1, university_col2 = st.columns(2)

    with university_col1:
        university_rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])

    with university_col2:
        research = st.selectbox("Research Experience", ["No Research Experience (0)", "Some Research Experience (1)"])

    # Submit button
    submitted = st.form_submit_button("🔍 Predict Admission Chance")

    # Convert research experience to binary
    research_binary = 1 if research == "Some Research Experience (1)" else 0

# Display the results after form submission (only works after sumbmit button is pressed.)
if submitted:
    # Predict admission chance based on GRE score
    if gre_score > 320:
        st.success("🎉 Your chance of admission: **99%**", icon="✅")
    else:
        st.warning("❗ Your chance of admission: **9%**", icon="⚠️")

    # Additional message based on other factors
    if university_rating >= 4 and research_binary == 1:
        st.info("You have a strong application profile! Consider applying to top-tier universities.", icon="💼")
    elif university_rating <= 2 and gre_score < 300:
        st.error("You may want to strengthen your profile before applying.", icon="🚫")

# Footer
st.markdown("---")
st.markdown("© 2024 UMBC DATA 601 Group 4")
