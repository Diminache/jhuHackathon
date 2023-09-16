from flask import Flask, request, jsonify

app = Flask(__name__)

chat_log = []

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_log.append(data)
    data = request.json
    user_message = data['queryResult']['queryText']
    print("User's Message:", user_message)
    return jsonify({"message": "Message received"})


if __name__ == '__main__':
    app.run(debug=True)




