from flask import Flask, jsonify
from flask_cors import CORS
from filters import filter_projects

app = Flask(__name__)
CORS(app)

MOCK_DATA = [
    {
        "name": "Ethereum",
        "mcap": 250000000000,
        "fdv": 260000000000,
        "volume_24h": 12000000000,
        "preview_listing": True,
        "max_supply": 100,
        "total_supply": 100,
        "tvl": 5000000000
    },
    {
        "name": "SmallCapX",
        "mcap": 40000000,
        "fdv": 80000000,
        "volume_24h": 90000,
        "preview_listing": True,
        "max_supply": 1000,
        "total_supply": 1000,
        "tvl": 120000
    }
]

@app.route("/projects")
def projects():
    result = filter_projects(MOCK_DATA)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
