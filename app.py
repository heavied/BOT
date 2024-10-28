from flask import Flask, request
import openai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
openai.api_key = os.getenv("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")

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
    print(f"OpenAI API error: {e}")  # Log the exact error message
    reply.body(f"Error: {str(e)}")  # Send back the exact error for debugging

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
