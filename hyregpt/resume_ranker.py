import html2text
import textract
import os

def html_to_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0

    markdown_content = h.handle(html_content)

    return markdown_content


def pdf_to_text(file_path):
    return textract.process(file_path)


def compute_similarity_score(job_description_file_path, candidate_resumes):

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    

    # create vocab of job description
    job_description = html_to_text(job_description_file_path)
    vectorizer = CountVectorizer().fit([job_description])

    jd_vector = vectorizer.transform([job_description])

    scores = {}
    for resume_path in candidate_resumes:

        filename = os.path.basename(resume_path)

        resume = pdf_to_text(resume_path)
    
        # create count matrix for each document; each row is a doc and each column indicates a word in the vocab
        # TODO: this is a very naive way to convert words to numbers and will not capture any semantics. 
        # We should definitely use word embeddings to capture semantics

        resume_vector = vectorizer.transform([resume])


        similarity_score = cosine_similarity(jd_vector, resume_vector)[0][0] # for countvectorizer, the similarity score is in [0, 1] range
        similarity_score = round(similarity_score * 100, 2) # [0, 100]
        scores[filename] = similarity_score
    
    
    return scores    