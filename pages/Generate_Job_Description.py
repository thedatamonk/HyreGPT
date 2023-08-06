import streamlit as st
from hyregpt.jd_utils import generate_job_description

st.title("Generate job description")

uploaded_file = st.file_uploader("Choose the job details file.", type="json")

# Check if a file is uploaded
if uploaded_file:
    # Read the uploaded file
    
    if st.button("Generate job description"):

        job_description = generate_job_description(
            jd_file_path=uploaded_file.name
        )
        
        st.markdown(job_description)
