# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
# import pickle
# import json

# app = Flask(__name__)

# # Load model + vectorizer
# vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))
# classifier = pickle.load(open("model/classifier.pkl", "rb"))

# # Load intents
# intents = json.load(open("intents.json", encoding="utf-8"))


# def get_response(tag):
#     for intent in intents["intents"]:
#         if intent["tag"] == tag:
#             return intent["responses"][0]
#     return "Sorry, I didn't understand that."

# @app.route("/whatsapp", methods=['POST'])
# def whatsapp_reply():
#     incoming_msg = request.form.get("Body").lower()

#     # NLP prediction
#     X = vectorizer.transform([incoming_msg])
#     tag = classifier.predict(X)[0]

#     bot_reply = get_response(tag)

#     # Send WhatsApp message
#     resp = MessagingResponse()
#     resp.message(bot_reply)
#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

# Initialize OpenAI
client = OpenAI(api_key="OPENAI_API_KEY")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body")

    # Ask ChatGPT
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI tutor. Explain answers clearly and simply."},
            {"role": "user", "content": incoming_msg}
        ]
    )

    reply_text = response.choices[0].message.content


    # Send to WhatsApp
    twilio_resp = MessagingResponse()
    twilio_resp.message(reply_text)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(debug=True)
