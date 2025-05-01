from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import spacy

app = FastAPI()

candidate_intents = ["order_status", "cancel_order", "return_order", "payment_help", "account_issue", "greetings"]
classifier = pipeline("zero-shot-classification")
nlp = spacy.load("en_core_web_sm")

class ChatRequest(BaseModel):
    message: str

def classify_intent(text):
    result = classifier(text, candidate_intents)
    return result["labels"][0]

def extract_entities(text):
    doc = nlp(text)
    return {ent.label_: ent.text for ent in doc.ents}

def generate_response(intent, entities):
    if intent == "order_status":
        return "I see you are asking about your order status. Could you please provide your order ID?"
    elif intent == "cancel_order":
        return "I can help with cancelling your order. Please share your order ID."
    elif intent == "greetings":
        return "Hello there! How can I help you today?"
    return "I'm not sure about that. Could you provide more details?"

@app.post("/chat")
def chat(chat_request: ChatRequest):
    intent = classify_intent(chat_request.message)
    entities = extract_entities(chat_request.message)
    response_message = generate_response(intent, entities)
    return {"intent": intent, "entities": entities, "response": response_message}
