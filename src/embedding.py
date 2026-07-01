import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

def load_embedding_model(modal_name = "all-MiniLM-L6-v2"):
    modal = SentenceTransformer(modal_name)
    return modal

def generate_embedding(df,model):
    documents = (
        df["Title"].fillna("") +
        " " +
        df["Abstract"].fillna("")
    ).tolist()

    embeddings = model.encode(
        documents,
        show_progress_bar=True
    )

    return embeddings
