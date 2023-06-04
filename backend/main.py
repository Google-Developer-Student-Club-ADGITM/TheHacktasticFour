from flask import Flask, request
import random
import string
import time
from chatbot import evalQuery, inference_api, setup_auth

app = Flask(__name__)
setup_auth()
ChatBotInstance = inference_api()

@app.route("/")
def hello_world():
    return {"status": "ok"}

@app.post("/api/query")
async def handleQuery():
    query = request.json

    output = await evalQuery(query['query'], ChatBotInstance)
    
#    output = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
    return {"status": "ok", "output": output}

if __name__ == "__main__":
    app.run(host="localhost", port = 8080)