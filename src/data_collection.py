from Bio import Entrez
import pandas as pd

Entrez.email = "hekaybob5522@gmail.com"

def search_pubmed(search_term, retmax=100):
    
    handle = Entrez.esearch(
        db="pubmed",
        term=search_term,
        retmax=retmax
    )

    record = Entrez.read(handle)
    return record["IdList"], record['Count']


def fetch_papers(pmids):
    papers_data = []

    for pmid in pmids:
        try:
            handle = Entrez.efetch(
                db="pubmed",
                id=pmid,
                rettype="abstract",
                retmode="xml"
            )

            paper = Entrez.read(handle)
            article = paper["PubmedArticle"][0]

            year = None
            try:
                year = article["MedlineCitation"]["Article"]["ArticleDate"][0]["Year"]
            except:
                pass

            abstract = ""
            try:
                abstract_list = article["MedlineCitation"]["Article"]["Abstract"]["AbstractText"]
                abstract = " ".join(map(str, abstract_list))
            except:
                pass

            papers_data.append({
                "PMID": str(article["MedlineCitation"]["PMID"]),
                "Title": str(article["MedlineCitation"]["Article"]["ArticleTitle"]),
                "Abstract": abstract,
                "Year": year
            })

        except Exception as e:
            print(f"Failed pmid: {pmid} with exception: {e}")

    return pd.DataFrame(papers_data)

