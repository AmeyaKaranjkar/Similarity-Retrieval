import numpy as np
import pandas as pd
import math
import io
import nltk
from nltk.tokenize import word_tokenize
import pickle
from sentence_transformers import SentenceTransformer

sample_data= pd.read_csv('prepared_data.csv')
sample_duplicates= pd.read_csv('prepared_duplicates.csv')
sample_limit= len(sample_data)
# Taking the first sample_limit number of sample questions
sample_data= sample_data[:sample_limit]

# importing the saved sbert_model
filename= 'sbert_model.sav'
sbert_model= pickle.load(open(filename, 'rb'))

# importing the sbert_embedding
with open('sbert_embedding.data','rb') as filehandle:
    sbert_embedding= pickle.load(filehandle)

def cosine(u, v):
    ''' this function returns the cosine similarity b/w two vectors'''
    return np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

# finding the similarity scores for each query with all the questions in corpus- We have used three similarity measures
sbert_cosine_simscores=[]

test_questions= list(sample_duplicates['preparedtitle'])

for i in range(len(test_questions)):
    query= test_questions[i]
    query_vec = sbert_model.encode([query])[0]

    cosine_simscore=[] # list of similarity scores with all the questions for this current query.

    for s in sbert_embedding:
        cosine_sim= cosine(query_vec, s)

        cosine_simscore.append(cosine_sim)

    # now we have the similarity scores with all the questions for this current query.
    sbert_cosine_simscores.append(cosine_simscore)

sbert_cosine_simscores= np.array(sbert_cosine_simscores)

# saving the sbert_cosine_simscores
with open('sbert_cosine_simscores.data', 'wb') as filehandle:
    pickle.dump(sbert_cosine_simscores, filehandle)