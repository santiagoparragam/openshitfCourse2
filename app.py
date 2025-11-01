# app_b.py
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
try:
    return 'Hola desde app B', 200
except Exception as e:
        # Catch any unexpected errors during the request handling
        print(f"An error occurred in hello_world: {e}", file=sys.stderr)
        
        # Return a standard HTTP 500 Internal Server Error response
        error_response = {
            "error": "Internal Server Error.......",
            "message": str(e)
        }
        return jsonify(error_response), 500
    # ---------------------------------

@app.route('/health', methods=['GET'])
def call_health():
    return 'OK', 200

@app.route('/startup', methods=['GET'])
def call_startup():
    return 'OK', 200
    
@app.route('/readiness', methods=['GET'])
def call_readiness():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
