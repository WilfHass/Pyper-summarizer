# Pyper-summarizer

The purpose of this repository is to create an easier way to skim through new Arxiv postings in order to speed up the research for relevant articles.

Pyper Summarizer is a Streamlit app that scrapes the most recent Arxiv papers, summarizes them using [a fine-tuned model](https://huggingface.co/com3dian/Bart-large-paper2slides-summarizer) (TBD on the model yet), then shows the summary to the user. The user will then have the option to read the full paper (or check if the summary is correct) and can be further tuned using this new data.
