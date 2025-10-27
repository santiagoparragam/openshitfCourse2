from flask import Flask

# App B runs on port 3000
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world_b():
    """Endpoint for App B (the callee)."""
    # This is the message App A will retrieve
    return 'The message from App B (Port 3000) is: este es el Hola Mundo2', 200

@app.route('/health', methods=['GET'])
def call_app_b():
    try:
        # Llamamos a la app B, que está en localhost:3001
        return 'OK', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500
@app.route('/startup', methods=['GET'])
def call_app_b():
    try:
        # Llamamos a la app B, que está en localhost:3001
        return 'OK', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500
@app.route('/readiness', methods=['GET'])
def call_app_b():
    try:
        # Llamamos a la app B, que está en localhost:3001
        return 'OK', response.status_code
    except requests.exceptions.ConnectionError:
        return 'Error: no se pudo conectar con app B', 500



if __name__ == '__main__':
    # Running on 0.0.0.0 and port 3000
    app.run(host='0.0.0.0', port=3000)
