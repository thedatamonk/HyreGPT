import streamlit as st
import os
from hyregpt.resume_ranker import compute_similarity_score
import pandas as pd


st.title("Resume ranking")


def score_resumes():

    if 'selected_jd' not in st.session_state.keys():
        st.error("No job description file found. Please upload a valid job description file from your local file storage.")
    
    if not st.session_state['selected_jd'].endswith('.html'):
        st.error("Job description file should be of HTML type.")

    if 'selected_resumes' not in st.session_state.keys():
        st.error("No resumes are selected. Please select atleast one valid resume.")

    if not all(file_path.endswith(".pdf") for file_path in st.session_state['selected_resumes']):
        st.error("One or more resume files are not of pdf type.")


    resume_scores = compute_similarity_score(
        job_description_file_path=st.session_state['selected_jd'],
        candidate_resumes=st.session_state['selected_resumes']
    )


    resume_scores_table = pd.DataFrame({
        "Resume": list(resume_scores.keys()),
        "Score": list(resume_scores.values())
    })

    st.table(resume_scores_table)
    

def list_resumes(dir_path="tests/resumes"):
    try:
        all_resumes = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.pdf')]
        selected_resumes = st.multiselect('Select one or more resumes for processing:', all_resumes)

        st.session_state['selected_resumes'] = [os.path.join(st.secrets['filepaths']['resume_directory'], f) for f in selected_resumes]

        if st.button('Analyse and score resumes'):
            score_resumes()
    except Exception as e:
        st.write("Error occurred while selecting resumes: ", e)


def select_job_description(dir_path="tests/job_descriptions/html"):
    try:
        all_jds = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.html')]

        placeholder_option = "Select a job description file..."
        all_jds =  [placeholder_option] + all_jds

        selected_jd = st.selectbox('Select a job description from your local storage:', all_jds)

        if selected_jd != placeholder_option:
            st.session_state['selected_jd'] = os.path.join(st.secrets['filepaths']['job_description_directory'], selected_jd)

    except Exception as e:
        st.write("Error occurred while selecting job description file: ", e)


st.markdown("""## Job Description""")
select_job_description()


st.markdown("""## Resumes""")
list_resumes()

