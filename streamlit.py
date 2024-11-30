import pickle
import pandas as pd
import streamlit as st

# these are our fields
features = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA', 'Research']

# the page configuration; it will auto-load when opening the page
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

# Header and subheader design forr our webpage
st.markdown("<div class='header'>University Admission Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Enter your details below to predict your chances of admission!</div>", unsafe_allow_html=True)


# Load the pipeline from the file for prediction
with open('poly_regression_pipeline.pkl', 'rb') as f:
    loaded_pipeline = pickle.load(f)

# our form developed using using streamlit
with st.form("admission_form"):

    # Academic Information Section
    st.markdown("### 📚 Academic Information")
    academic_col1, academic_col2 = st.columns(2)

    # first column
    with academic_col1:
        gre_score = st.number_input("GRE Score", min_value=260, max_value=340, step=1)
        toefl_score = st.number_input("TOEFL Score", min_value=0, max_value=120, step=1)
        cgpa = st.number_input("CGPA (0.0 - 10.0)", min_value=0.0, max_value=10.0, step=0.1)

    # second column
    with academic_col2:
        sop = st.number_input("SOP Strength (0.5 - 5.0)", min_value=0.5, max_value=5.0, step=0.5)
        lor = st.number_input("LOR Strength (0.5 - 5.0)", min_value=0.5, max_value=5.0, step=0.5)
        research = st.selectbox("Research Experience", ["No Research Experience", "Some Research Experience"])

    # University Information Section
    st.markdown("### 🏫 University Information")
    university_col1, university_col2 = st.columns(2)

    with university_col1:
        university_rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])        

    # Submit button
    submitted = st.form_submit_button("🔍 Predict Admission Chance")

    # Convert research experience to binary (0/1)
    research_binary = 1 if research == "Some Research Experience" else 0

# Display the results after form submission (it will only work after pressing the buttonn)
if submitted:

    # our threshold to determine if an application is strong or not
    threshold = 0.75
    data = pd.DataFrame([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research_binary]], columns=features)
    prediction = loaded_pipeline.predict(data)[0]

    # essentially capping prediction between 0 and 1
    prediction = max(0, min(1, prediction))
    
    # Predict admission chance 
    if prediction >= threshold:
        st.success(f"🎉 Your chance of admission: **{round(prediction*100, 2)}%**", icon="✅")
    else:
        st.warning(f"❗ Your chance of admission: **{round(prediction*100, 2)}%**", icon="⚠️")

    # Additional message based on the threshold
    if prediction >= threshold:
        st.info("You have a strong application profile! Consider applying to top-tier universities.", icon="💼")
    else:
        st.error("You may want to strengthen your profile before applying.", icon="🚫")