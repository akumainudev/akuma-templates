# Simple API Template (Flask Placeholder)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Simple API Template!"})

@app.route('/health')
def health_check():
    return jsonify({"status": "ok"})

# Add more routes as needed for the template

if __name__ == '__main__':
    # Note: For production, use a proper WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=8080, debug=True) # Debug=True for template development

