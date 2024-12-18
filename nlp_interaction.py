import transformers

class NLPInteraction:
    def __init__(self):
        self.model = transformers.pipeline('text2text-generation', model='t5-base')

    def process_request(self, request: str) -> str:
        # Here we would process the bi-directional dialog using NLP
        return self.model(f"Translate English to formal English: {request}")[0]['generated_text']
