import openai


RESUME_RANKER_TEMPLATE = """


"""

def rank_resumes(resumes):

    resume_ranker_prompt = RESUME_RANKER_TEMPLATE.format(resumes=resumes)

    # LLM call
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": resume_ranker_prompt}
        ]
    )

    ranked_resumes = response.choices[0].message.content

    # processed ranked_resumes and convert it into a list and then store this info somewhere

    return ranked_resumes
    