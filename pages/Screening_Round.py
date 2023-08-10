import streamlit as st

st.title("Screening interview")
st.sidebar.header("Candidate details")

if "candidate_details_submitted" not in st.session_state:
    st.session_state.candidate_details_submitted = False

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

if "candidate_resume" not in st.session_state:
    st.session_state.candidate_resume = None

if "job_description" not in st.session_state:
    st.session_state.job_description = None

candidate_name = st.sidebar.text_input("Candidate Name")
candidate_resume = st.sidebar.file_uploader("Resume", type='pdf')
job_desc = st.sidebar.file_uploader("Job Description", type='html')

start_interview_button = st.sidebar.button(label="Start interview")

if start_interview_button:
    st.session_state.candidate_details_submitted = True
    st.session_state.candidate_name = candidate_name
    st.session_state.candidate_resume = candidate_resume
    st.session_state.job_desc = job_desc

    st.markdown(f"Hi {st.session_state.candidate_name}!")
    st.chat_input()


if st.sidebar.button("Reset"):
    del st.session_state.candidate_details_submitted
    del st.session_state.interview_started
    del st.session_state.candidate_name
