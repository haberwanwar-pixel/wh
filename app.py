from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running successfully!"

@app.route('/listener', methods=['POST', 'GET'])
def listener():
    data = request.data or request.form
    print(f"Received data: {data}")
    return "Data received", 200

if __name__ == '__main__':
    app.run()
