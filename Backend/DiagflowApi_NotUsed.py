from flask import Flask, request, jsonify
import socket
import openai

app = Flask(__name__)

openai.api_key = "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"

def RequestGPT(Diagnosis):

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

chat_log = []

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_log.append(data)
    data = request.json
    user_message = data['queryResult']['queryText']
    print("User's Message:", user_message)
    RequestGPT(user_message)
    return jsonify({"message": "Message received"})


if __name__ == '__main__':
    app.run(debug=True)












