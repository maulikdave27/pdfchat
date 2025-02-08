import os
from embedchain import App

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = ""

config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.2',
      'top_p': 0.5,
      'temperature': 1.0,  
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  }
}
ai = App.from_config(config=config)
ai.add('The-Hidden-Hindu.pdf')
print(ai.query("Give me a detailed summary of the story and how it ended"))