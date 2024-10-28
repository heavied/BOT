from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)
openai.api_key = os.getenv("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")

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
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
        print(f"OpenAI API error: {e}")  # Log the exact error message
        reply.body(f"Error: {str(e)}")  # Send back the exact error for debugging

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)

