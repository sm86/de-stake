import sys
from datetime import datetime,timedelta
from pathlib import Path
from flask import Flask, jsonify
from flask_cors import CORS

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from metrics.decentralizationMetrics import DecentralizationMetrics

app = Flask(__name__)
CORS(app)

@app.route('/metrics/<date>')
def metrics(date):
    result = DecentralizationMetrics.calculate_metrics(date)

    # Check if result is empty
    if result.empty:
        today = datetime.now().strftime('%d-%m-%Y')
        return jsonify({
            "error": "No data available for the selected date. Please select a date between 24-10-2023 and " + today
        }), 400

    return result.to_json(orient='records')


if __name__ == "__main__":
    app.run(debug=True)