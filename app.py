from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
openai.api_key = 'sk-2DeorHiN1irhWpY2jnOy1SCzfEyvB7LxAuDmhSZ7g4T3BlbkFJQYBJbibQui5dn_YQRhLd8q8eHegYx2K9mIywq0PWsA'

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp():
    if request.method == 'GET':
        return "WhatsApp route is working!"  # Add this for testing

    # Rest of your code
    incoming_msg = request.values.get('Body', '').strip()
    response = MessagingResponse()
    reply = response.message()

    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",
            prompt=incoming_msg,
            max_tokens=150
        )
        reply.body(completion.choices[0].text.strip())
    except Exception as e:
        reply.body("Error connecting to ChatGPT. Try again later.")

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return "Hello, world! This is the home route."
