import streamlit as st
from hyregpt.screening_round import conversation_chain
from ui.screening_interview_ui import message_func


def append_chat_history(question, answer):
    st.session_state["history"].append((question, answer))

def append_message(content, role="recruiter", display=False):
    message = {"role": role, "content": content}
    message_func(content, False, display)
    st.session_state.messages.append(message)
    append_chat_history(st.session_state.messages[-2]["content"], content)


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
    st.session_state.interview_started = True




if st.session_state.interview_started:
    INITIAL_MESSAGE = [
        {"role": "recruiter", "content": f"""Hi {st.session_state.candidate_name}! Welcome to AlphaMind's screening interview!\n Are you ready for the interview?"""}
    ]

    if "messages" not in st.session_state.keys():
        st.session_state['messages'] = INITIAL_MESSAGE

    if "history" not in st.session_state.keys():
        st.session_state["history"] = []


    if user_input := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": user_input})

    for message in st.session_state.messages:
        message_func(
            message["content"],
            True if message["role"] == "user" else False,
            True if message["role"] == "data" else False,
        )
    

    if st.session_state.messages[-1]["role"] != "recruiter":
        content = st.session_state.messages[-1]["content"]
        if isinstance(content, str):
            result = conversation_chain({"input": content})["response"]

            append_message(result)
    

if st.sidebar.button("Reset"):
    del st.session_state.candidate_details_submitted
    del st.session_state.interview_started
    del st.session_state.candidate_name
    del st.session_state.candidate_resume
    del st.session_state.job_desc
    del st.session_state.messages
    del st.session_state.history

    st.session_state["messages"] = INITIAL_MESSAGE
    st.session_state["history"] = []