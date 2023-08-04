def resumes_to_embeddings(path):
    # load resumes from path

    # divide resumes(docs) into chunks

    # compute embeddings of each chunk

    # store embeddings along with original text in vector DB like chroma

    pass

def get_relevant_resumes(vectordb_path, job_description):
    # convert job description into a embeddings

    # similarity search between embeddings of the JD and the resume embeddings

    # retrieve the resummes and their embeddings which are closest to the JD embedding

    pass

def rank_resumes(candidate_resumes, job_description):
    # given JD and candidate resumes, rank them in order of relevance/suitability for the role etc

    pass


def improve_job_description(job_description):
    # this function will interact with the HR representative to improve the JD

    # the function will recommend some improvements and HR repr will review and incorporate 1 or more of those changes

    # the function will again review the JD and give some more suggestions. This will keep on happening until the job description has reached "perfection" stage

    pass


def generate_screening_questions(job_description):

    # this function will generate relevant questions for the screening round

    # the HR representative may provide feedback, edit the questions directly

    # finally a set of questions will be generated
    
    pass


def conduct_screening_round(job_description, candidate_resume, screening_questions):

    # conduct screening round

    # ask screening questions and answer follow-up questions from the candidates

    pass


def evaluate_candidate(job_description, candidate_question_responses):

    # evaluate and give feedback to a candidate based on his responses

    pass