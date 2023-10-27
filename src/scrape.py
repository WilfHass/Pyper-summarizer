import arxiv
import re
from collections import defaultdict


def strip_abstract(text):
    
    text_stripped = re.sub(r"[$\\\"\`]", "", text)
    
    return text_stripped


def subject_search(arxiv_query):
    
    search = arxiv.Search(
        query = arxiv_query,
        max_results = 10,
        sort_by = arxiv.SortCriterion.SubmittedDate
        )
    
    results = arxiv.Client().results(search)
    
    return results