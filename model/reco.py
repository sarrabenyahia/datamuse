import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel

SELECTION = 'title'

class Recommandation():


  def __init__(self, data, research):
    self.data = data
    self.research = research

  def inputer(self):

    df = pd.read_csv(self.data, sep=";")
    title = str(self.research).lower()

    #Replace NaN with an empty string
    df[SELECTION] = df[SELECTION].fillna('')
    #Create new observation for computation
    df.loc[len(df.index)] = ["99999", " ", title, " ", " ", " "," "," "," "," "," "," "," "," ", " "," "," "," "," "," "," "," "," "," "," "," ",
    " "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",]

    return df,title


  def compute_similarity(df, title):
    #----------------- def tfidf
    #Matrice TFID
    stopwords_list = stopwords.words('french')
    tfidf = TfidfVectorizer(stop_words=stopwords_list)
    tfidf_matrix = tfidf.fit_transform(df[SELECTION])

    # cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    #Construct a reverse map of indices and movie titles
    indices = pd.Series(df.index, index=df[SELECTION]).drop_duplicates()

    # Get the index of the event that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the events based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:4]

    # Get the event indices
    movie_indices = [i[0] for i in sim_scores]

    return movie_indices

  def results(df,movie_indices):
    # Return the top 10 most similar events
    return df[['title','lead_text','date_description','cover_url']].iloc[movie_indices]

def running(PATH, cherche):
    reco1 = Recommandation(PATH, cherche)
    df,title = reco1.inputer()
    mtrx = Recommandation.compute_similarity(df,title)
    output = Recommandation.results(df,mtrx)
    output = output.reset_index(drop=True)
    title = output.loc[0, ['title']]
    return title


