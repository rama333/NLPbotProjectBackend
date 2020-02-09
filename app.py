from flask import Flask, jsonify, request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
@app.route("/api/upload_csv", methods=['POST'])
def upload_csv():
    # work with csv
    return jsonify({
        "type": "ok"
    })

if __name__ == '__main__':
    app.run()
    print("Server listening on port 5000")