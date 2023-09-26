from flask import Flask, request, jsonify
import socket
import openai
import websockets
import asyncio

app = Flask(__name__)

openai.api_key = "GetYourOwnKey"

CurrentMessage = ""


def RequestGPT(Diagnosis):
    print("Requesting GPT")
    completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.8,
    max_tokens = 500,
    messages = [
        {"role": "system", "content": "You are responsible for diagnosing health issue with the client"},
        {"role": "user", "content": Diagnosis},
    ]
    )
    
    print(completion.choices[0].message)
    return completion.choices[0].message["content"]

chat_log = []

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_log.append(data)
    data = request.json
    CurrentMessage = data['queryResult']['queryText']
    print("User's Message:", CurrentMessage)
    DiagnosticI = RequestGPT(CurrentMessage)
    print(DiagnosticI)
    return jsonify({"message": "Message received"})


if __name__ == '__main__':
    app.run(debug=True)












