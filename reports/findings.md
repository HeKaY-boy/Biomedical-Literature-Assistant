Dataset Summary
---------------
• Total papers collected: 100
• Features extracted:
    - PMID
    - Title
    - Abstract
    - Year

Publication Year Analysis
-------------------------
• 99 papers were published in 2026.
• 1 paper was published in 2025.
• The dataset is heavily biased toward recent publications because PubMed returns the most recent matching articles first.

Abstract Length Analysis
------------------------
• Average abstract length: 245 words
• Median abstract length: 239 words
• Shortest abstract: 90 words
• Longest abstract: 783 words
• Standard deviation: 87 words

Key Observations
----------------
• Mean and median abstract lengths are very close (245 vs 239), indicating a fairly balanced distribution.
• Most abstracts fall within a moderate length range suitable for NLP processing.
• No extreme outliers were observed that would indicate extraction errors.
• The dataset appears clean and consistent for downstream tasks.

Implications for the Project
----------------------------
• Abstracts are sufficiently detailed for semantic search and retrieval.
• Most documents are short enough to be embedded directly without aggressive chunking.
• The dataset is suitable for generating embeddings using Sentence Transformers.
• The collected literature can serve as the knowledge base for the Biomedical Literature Assistant RAG pipeline.