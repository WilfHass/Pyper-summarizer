import streamlit as st
import openai
from utils.arxiv_handler import fetch_arxiv_abstracts
from utils.nlp_processor import process_abstracts
from utils.nlp_processor import NLPSummarizer

def display_bullet_points(abstracts):
    for i, (title, bullet_points) in enumerate(abstracts.items()):
        st.subheader(f"Article {i+1}")
        st.markdown(f"**Title:** {title}")
        st.markdown(f"**Summary:**")
        
        bullet_points = bullet_points.split(". ")
        for bullet in bullet_points:
            st.markdown(f"- {bullet}")

def main():
    
    st.title('ArXiv Article Summaries Inbox')
    query = st.text_input('Enter your search query:')
    # prompt = st.text_input('Enter what you want to do with the articles')
    
    model_name = st.selectbox('Select NLP Model',
                              list(NLPSummarizer.available_models),
                              index=1)
    
    if model_name == "GPT-3":
        with open("../../openai_key.txt") as f:
            api_key = f.readline()
    else:
        api_key = None
    
    max_results = st.slider('Max Results', min_value=1, max_value=20, value=5)

    if st.button('Fetch Articles'):
        arxiv_abstracts = fetch_arxiv_abstracts(query=query, max_results=max_results)
        processed_abstracts = process_abstracts(arxiv_abstracts, model_name, api_key=api_key)
        display_bullet_points(processed_abstracts)


if __name__ == "__main__":
    main()