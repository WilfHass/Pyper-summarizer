from transformers import pipeline
import openai

class NLPSummarizer:
    
    available_models = {
            'Bart': 'facebook/bart-large-cnn',
            'Bart-Scientific': 'com3dian/Bart-large-paper2slides-summarizer',
            'T5': 't5-large',
            'Pegasus': 'google/pegasus-large',
            'GPT-3.5': 'gpt-3.5'
        }
    
    def __init__(self, model_name, api_key=''):
        self.model = None
        
        if model_name == 'GPT-3.5':
            if api_key:
                openai.api_key = api_key
                self.model = NLPSummarizer.available_models["GPT-3.5"]
            else:
                raise ValueError("OpenAI API key is required for GPT-3.5")

        else:
            self.load_model(model_name)
            
            
    def load_model(self, model_name):
        model_identifier = NLPSummarizer.available_models.get(model_name)
        if model_identifier:
            self.model = pipeline("summarization", model=model_identifier)
        else:
            raise ValueError("Unknown model selection")
        
        
    def generate_bullet_points(self, abstract, prompt_text):
        if not self.model:
            raise ValueError("Model not loaded.")

        if self.model == 'gpt-3':
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=f"{prompt_text} {abstract}",
                max_tokens=100
            )
            bullet_points = response.choices[0].text.strip()

        else:
            if prompt_text:
                prompt = f"{prompt_text} {abstract}"
            else:
                prompt = abstract

            summary = self.model(prompt, max_length=150, min_length=30, do_sample=False)
            bullet_points = summary[0]['summary_text']

        return bullet_points


def process_abstracts(abstracts, model_name='Bart-Scientific', prompt_text='Summarize 3 bullet points based on this article:', api_key=None):
    
    processor = NLPSummarizer(model_name=model_name, api_key=api_key)
    
    processed_abstracts = {}
    for title, abstract in abstracts.items():
        bullet_points = processor.generate_bullet_points(abstract, prompt_text=prompt_text)
        processed_abstracts[title] = bullet_points

    return processed_abstracts