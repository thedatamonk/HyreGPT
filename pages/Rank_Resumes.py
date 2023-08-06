import streamlit as st
import os

def process_selected_files(selected_files):
    for file in selected_files:
        st.write(f"You selected {file}")

# Display files in the given directory
def list_files_in_directory(dir_path="."):
    try:
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        selected_files = st.multiselect('Select one or more files for processing:', files)
        if st.button('Process Selected Files'):
            process_selected_files(selected_files)
    except Exception as e:
        st.write("An error occurred:", e)

dir_path = "tests/job_descriptions/html"

list_files_in_directory(dir_path)
