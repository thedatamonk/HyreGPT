import streamlit as st
import json
import os


st.title("Enter Job Details")

with st.form(key='job_details_form'):

    # Create text input for each detail you want to collect
    job_title = st.text_input(label='Job Title')
    company_name = st.text_input(label='Company Name')
    role_type = st.text_input(label='Role Type', placeholder="full-time/part-time/contract/internship")
    job_location = st.text_input(label='Job Location')

    compensation = st.text_input(label='Compensation')
    currency = st.selectbox('Currency', ['USD', 'EUR', 'GBP', 'INR', 'JPY', 'CAD'])  # You can extend this list as required

    job_purpose = st.text_area(label='Job Purpose')  # Using text_area for possibly longer input

    file_name = st.text_input(label='File name', placeholder="amazon_sde1.json")

    # Create a submit button
    submit_button = st.form_submit_button(label='Submit')



if submit_button:

    job_details = {
        "job_title": job_title,
        "company_name": company_name,
        "role_type": role_type,
        "job_location": job_location,
        "compensation": f"{compensation} {currency}",
        "job_purpose": job_purpose
    }
    
    
    # Save the dictionary to a JSON file

    with open(os.path.join("tests/job_descriptions/json", file_name), 'w') as f:
        json.dump(job_details, f)

    st.success("Job details saved successfully!")