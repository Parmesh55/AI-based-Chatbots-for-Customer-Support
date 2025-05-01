from transformers import pipeline
import datetime

# Initialize the text-generation pipeline using GPT-2.
generator = pipeline("text-generation", model="gpt2")

def generate_response(user_message):
    # Convert the message to lower case for easier matching.
    msg_lower = user_message.lower()

    # Special case: if the user asks for the date
    if "date" in msg_lower:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}."
    # Special case: if the user asks for the meaning of "Parmesh"
    elif "meaning" in msg_lower and "parmesh" in msg_lower:
        # You can adjust the wording as you like.
        return "The name 'Parmesh' is often derived from 'Parameshwar', meaning 'Supreme Lord' or 'God'."
    
    # Otherwise, use GPT-2 to generate a response.
    prompt = f"User: {user_message}\nBot:"
    print("Prompt:", prompt)  # Debug: print the prompt to the server console
    # Increase max_length if needed.
    generated = generator(prompt, max_length=150, num_return_sequences=1)
    generated_text = generated[0]["generated_text"]
    print("Generated text:", generated_text)  # Debug: print the generated text

    # Remove the prompt from the generated text to extract only the response.
    response = generated_text[len(prompt):].strip()
    return response
