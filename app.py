from flask import Flask

# App B runs on port 3000
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world_b():
    """Endpoint for App B (the callee)."""
    # This is the message App A will retrieve
    return 'The message from App B (Port 3000) is: este es el Hola Mundo2', 200

if __name__ == '__main__':
    # Running on 0.0.0.0 and port 3000
    app.run(host='0.0.0.0', port=3000)
