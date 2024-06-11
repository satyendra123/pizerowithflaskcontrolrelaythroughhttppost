from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/esp32/boom/', methods=['GET'])
def handle_get():
    response = {
        "status": "success",
        "data": "LED should toggle"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

