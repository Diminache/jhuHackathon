import openai
import asyncio
import websockets


def GPTRequest_LaymansTerms(ComplicatedText):
    openai.api_key = "GetYourOwnKey"

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

