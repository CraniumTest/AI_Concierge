from transformers import pipeline

# Initialize a pipeline for language processing (simplifying with sentiment-analysis for demonstration)
language_model = pipeline("sentiment-analysis")

def process_input(text):
    response = language_model(text)
    return response[0]['label']
