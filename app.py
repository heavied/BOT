from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse
import os
import logging

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    response = MessagingResponse()
    reply = response.message()

    logging.info(f"Received message: {incoming_msg}")
    logging.info("Attempting to connect to OpenAI API...")

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": incoming_msg}],
            max_tokens=150
        )
        response_text = completion['choices'][0]['message']['content'].strip()
        logging.info(f"OpenAI response: {response_text}")
        reply.body(response_text)
    except Exception as e:
        logging.error(f"Error connecting to OpenAI API: {e}", exc_info=True)
        reply.body("There was an error connecting to ChatGPT. Try again later.")

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
