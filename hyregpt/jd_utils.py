import openai
import os
import json
import markdown
import webbrowser
from decouple import config

openai.api_key = config("OPENAI_API_KEY")


JOB_DESCRIPTION_TEMPLATE = """

### GOAL

Please act as a talent acquisition expert with knowledge of every title. The goal is to generate a comprehensive job description. This prompt will consist of two parts. 

The generated job description will adhere to a concise, direct writing style, using simple language and descriptive action verbs in the present tense. It will avoid abbreviations, acronyms, ambiguous terms, gender-specific language, and references to other employees’ names. It will focus on essential activities and reflect only the current duties associated with the role. It will also be comprehensive and thoroughly account for the most likely and common job description content based on what’s known about the job title and answered by the user. 

Below are specific details about the job - 

1. Job Title: {job_title} 

2. Company Name: {company_name}

3. Is the job full-time, part-time, or another arrangement? : {role_type}

4. Job Location; Is it remote, in-office, or a hybrid model? : {job_location}

5. Compensation: {compensation} 

6. Job Purpose: {job_purpose}


### OUTPUT FORMAT INSTRUCTIONS

Draft a job description adhering to the format and headers below for a web page. Please display the headers in Markdown, and answers in regular text. 

H2 Company Name
<company name>

H2 Job Title
<job tile>

H2 Role type 
<role type>

H2 Location
<location>

H2 Compensation
<compensation>

H2 Job Purpose

H2 Job Duties

H2 Required Qualifications 

H3 Education

H3 Experience

H3 Knowledge and Skills

H3 Preferred Qualifications

H2 Working Conditions

"""

def generate_job_description(jd_file_path):
    
    ROOT_PATH = "tests/job_descriptions/json/"
    full_path = os.path.join(ROOT_PATH, jd_file_path)

    with open(full_path, "r") as file:
        jd_configs = json.load(file)

    job_desc_prompt = JOB_DESCRIPTION_TEMPLATE.format(**jd_configs)

    # LLM call
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": job_desc_prompt}
        ]
    )


    job_description = response.choices[0].message.content

    basename = os.path.splitext(jd_file_path)[0]

    output_markdown_file_path = os.path.join("tests/job_descriptions/html/", basename+".html")

    with open(output_markdown_file_path, "w") as f:
        f.write(job_description)

    
    return job_description
    '''
    html = markdown.markdown(job_description)

    basename, _ = os.path.splitext(input_jd_file_name)

    html_file = f"tests/job_descriptions/html/{basename}.html"

    with open(html_file, "w") as f:
        f.write(html)
    webbrowser.open('file://' + os.path.abspath(html_file))
    '''