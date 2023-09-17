import openai
import asyncio
import websockets


def GPTRequest_LaymansTerms(ComplicatedText):
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.8,
    max_tokens = 500,
    messages = [
        {"role": "system", "content": "You simplify complext text"},
        {"role": "user", "content": "Make this text as simple as possible as though a 5 year old can read it and make it shorter: " + ComplicatedText},
     ]
    )
    print("ChatGPT Call Successful")
    return completion.choices[0].message["content"]


async def echo(websocket, path):
    async for message in websocket:
        LaymanedTerm = GPTRequest_LaymansTerms(message)
        print(LaymanedTerm)
        await websocket.send(f"Simplified Text: {LaymanedTerm}")

start_server = websockets.serve(echo, "localhost", 5001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


"""
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1" # Set Server to VM 
port = 5001

server_socket.bind((host, port))


server_socket.listen(1)

print(f"Server listening on {host}:{port}")

#client_socket, client_address = server_socket.accept()

#print(f"Connected by {client_address}")


while True:
    client_socket, client_address = server_socket.accept()

    print(f"Connected by {client_address}")

    try:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from client: {data.decode()}")

        print(GPTRequest_LaymansTerms(data.decode()))
        response = "Sent a response"

        client_socket.send(response.encode())
    except:
        print("Connection Reset")

    client_socket.close()
"""
