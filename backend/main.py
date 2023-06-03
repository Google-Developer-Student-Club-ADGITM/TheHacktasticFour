from flask import Flask, request
import random
import string
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"status": "ok"}

@app.post("/api/query")
async def handleQuery():
    time.sleep(1)
    query = request.json
    # output = await generate_output_via_ML(query)
    output = ''.join((random.choice(string.ascii_lowercase) for x in range(10)))
    return {"status": "ok", "output": output}

if __name__ == "__main__":
    app.run(host="localhost", port=8080)