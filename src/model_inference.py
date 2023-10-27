from transformers import pipeline


def load_model(model_name="com3dian/Bart-large-paper2slides-summarizer"):
    
    summarizer = pipeline("summarization", model=model_name)
    return summarizer
    
    
def inference(model, text):
    
    summary = model(text, max_length=50, min_length=30, do_sample=False)
    return summary

