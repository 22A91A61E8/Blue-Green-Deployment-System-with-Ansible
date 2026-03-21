 
import requests
import json
import os

# Constants
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# Function to query Ollama
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model"

# Load prompt templates
with open("prompts/zero_shot_template.txt", encoding="utf-8") as f:
    zero_shot_template = f.read()
with open("prompts/one_shot_template.txt", encoding="utf-8") as f:
    one_shot_template = f.read()

# 20 adapted e-commerce queries
queries = [
    "How do I track my order?",
    "My discount code isn't working",
    "Can I change my shipping address after placing an order?",
    "How do I cancel an order?",
    "Do you offer gift wrapping?",
    "When will my order be delivered?",
    "How do I return a damaged product?",
    "Can I exchange an item for a different size?",
    "Do you have international shipping?",
    "How can I apply multiple promo codes?",
    "What payment methods do you accept?",
    "How do I update my account information?",
    "I received the wrong item. What should I do?",
    "Can I pre-order upcoming products?",
    "Do you restock sold-out items?",
    "How do I subscribe to your newsletter?",
    "Is my personal information safe?",
    "Can I request expedited shipping?",
    "How do I track my return refund?",
    "What is your warranty policy?"
]

# Open results file
os.makedirs("eval", exist_ok=True)
with open("eval/results.md", "w", encoding="utf-8") as f:
    f.write("|Query #|Customer Query|Prompting Method|Response|\n")
    f.write("|---|---|---|---|\n")
    for i, query in enumerate(queries, 1):
        # Zero-Shot
        prompt_zero = zero_shot_template.replace("(query)", query)
        response_zero = query_ollama(prompt_zero)
        f.write(f"|{i}|{query}|Zero-Shot|{response_zero}|\n")

        # One-Shot
        prompt_one = one_shot_template.replace("(query)", query)
        response_one = query_ollama(prompt_one)
        f.write(f"|{i}|{query}|One-Shot|{response_one}|\n")

print("Chatbot evaluation complete! Check eval/results.md")
