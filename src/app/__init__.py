from flask import Flask; 
from flask import request; 
from flask import Response; 
from service.messageService import MessageService;

app = Flask(__name__)
app.config.from_pyfile('config.py')

messageService = MessageService()

@app.route('/v1/ds/message', methods = ['POST'])
def handle_message():
    message = request.json.get("message")
    result = messageService.process_message(message)
    json_response = result.json()
    return Response(json_response, mimetype = 'application/json')

@app.route('/hello', methods = ['GET'])
def handle_get():
    return Response("Hello World...")

if __name__ == "__main__":
    app.run(host = "localhost", port = 8000, debug = True)

 