import arxiv
import re

def strip_abstract(text):
    
    text_stripped = re.sub(r"[$\\\"\`]", " ", text)
    return text_stripped

def fetch_arxiv_abstracts(query, max_results=5):
    
    search = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
        )
    
    results = arxiv.Client().results(search)
    abstracts = {result.title: strip_abstract(result.summary) for result in results}
    
    return abstracts