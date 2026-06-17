Biomedical Literature Assistant - Quick Memory Notes

Goal:
Build a system that can search biomedical research papers and answer questions using those papers.

---I converted research papers into embeddings,
searched them using cosine similarity,
retrieved the most relevant papers,
and gave those papers to an LLM to generate an answer.---


Step 1: Collect Data

* Used PubMed API (Entrez)
* Retrieved papers related to lung cancer
* Stored:

  * PMID
  * Title
  * Abstract
  * Year
* Created a pandas DataFrame

Output:
Dataset of biomedical papers

---

Step 2: Explore Data (EDA)

* Counted papers
* Checked missing values
* Analyzed publication years
* Measured abstract lengths

Output:
Understanding of dataset quality

---

Step 3: Create Embeddings

* Used Hugging Face SentenceTransformer
* Model: all-MiniLM-L6-v2
* Converted each abstract into a 384-dimensional vector

Idea:
Text → Numbers

Output:
Embeddings matrix of shape (100, 384)

---

Step 4: Semantic Search

* User enters a query
* Query converted into an embedding
* Used cosine similarity to compare query embedding with all paper embeddings
* Retrieved most relevant papers

Idea:
Meaning-based search, not keyword search

Output:
Top-K relevant papers

---

Step 5: Build Context

* Took retrieved papers
* Combined Title + Abstract into one large context string

Output:
Context ready for LLM

---

Step 6: RAG (Retrieval Augmented Generation)

* Loaded FLAN-T5 from Hugging Face
* Sent:
  Question + Retrieved Context
* Model generated an answer

Pipeline:

User Question
↓
Embedding
↓
Similarity Search
↓
Top-K Papers
↓
Context Builder
↓
FLAN-T5
↓
Generated Answer

---

Key Concepts Learned

Embedding:
A numerical representation of text.

384-Dimensional Vector:
Each abstract becomes 384 numbers representing its meaning.

Cosine Similarity:
Measures semantic similarity between two embeddings.

Retriever:
Finds relevant papers.

Generator:
Reads retrieved papers and generates an answer.

RAG:
Retriever + Generator

---

Current Status
* PubMed Data Collection
* EDA
* Embeddings
* Semantic Search
* Top-K Retrieval
* Context Builder
* FLAN-T5 Integration
* First End-to-End RAG Pipeline


Next Improvements

* Better prompts
* Better LLM
* Streamlit UI
* Refactor into src/
* Add citations and references
