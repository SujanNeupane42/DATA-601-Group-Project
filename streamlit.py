import streamlit as st

# Set the title of the app
st.title("University Admission Predictor")

# Input fields
gre_score = st.number_input("GRE Score", min_value=260, max_value=340, step=1)
toefl_score = st.number_input("TOEFL Score", min_value=0, max_value=120, step=1)
university_rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])
sop = st.number_input("SOP (Statement of Purpose Strength)", min_value=0.5, max_value=5.0, step=0.5)
lor = st.number_input("LOR (Letter of Recommendation Strength)", min_value=0.5, max_value=5.0, step=0.5)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
research = st.selectbox("Research Experience", ["No Research Experience (0)", "Some Research Experience (1)"])

# Convert research experience to binary
research_binary = 1 if research == "Some Research Experience (1)" else 0

# Button to submit the form
if st.button("Submit"):
    st.write("Your Input:")
    st.write(f"GRE Score: {gre_score}")
    st.write(f"TOEFL Score: {toefl_score}")
    st.write(f"University Rating: {university_rating}")
    st.write(f"SOP Strength: {sop}")
    st.write(f"LOR Strength: {lor}")
    st.write(f"CGPA: {cgpa}")
    st.write(f"Research Experience: {research_binary}")
