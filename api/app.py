import sys
from datetime import datetime,timedelta
from pathlib import Path
from flask import Flask

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from metrics.decentralizationMetrics import DecentralizationMetrics

app = Flask(__name__)

@app.route('/metrics')
def hello_world():
    date = datetime.now() - timedelta(days=1)
    date= date.strftime('%d%m%Y')
    print(date)
    result = DecentralizationMetrics.calculate_metrics(date)
    return result.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)