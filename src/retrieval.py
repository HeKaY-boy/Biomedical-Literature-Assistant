import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def search_paper(query, top_k, df, embeddings, model):
    
    """
    Retrieve the top-k most relevant biomedical papers
    using semantic search based on cosine similarity.

    Parameters:
        query (str): User search query
        df (pd.DataFrame): Paper metadata and abstracts
        embeddings (np.ndarray): Precomputed paper embeddings
        model: SentenceTransformer model
        top_k (int): Number of papers to retrieve

    Returns:
        list[dict]: Retrieved papers with similarity scores
    """

    embedding_query = model.encode(query)
    similarities = cosine_similarity([embedding_query], embeddings)
    top_k_indx = np.argsort(similarities[0])[-top_k:][::-1]
    results= []
    
    for idx in top_k_indx:
        pmid = int(df.iloc[idx]['PMID'])
        title = df.iloc[idx]['Title']
        abstract = df.iloc[idx]['Abstract']
        sim = float(similarities[0][idx])

        results.append({
            'PMID':pmid,
            'Title':title,
            'Abstract':abstract,
            'Similarity':sim
            })
          
    return(results)