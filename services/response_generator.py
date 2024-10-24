from transformers import pipeline

# Carregar o modelo GPT-2
generator = pipeline('text-generation', model='gpt2')

def responder_humanizado(command):
    response = generator(command, max_length=50, num_return_sequences=1)
    print(response[0]['generated_text'])
