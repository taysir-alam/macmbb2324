from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# Sample data for teams and metrics (replace with your data)
teams = ["MOHAWK", "MEMORIAL", "CONCORDIA"]
metrics = ["ANGLE %", "AWAY %", "SWING %", "TRANSITION %", "FREE PLAY %", "BLOB %", "SLOB %", "CONTEST %", "SOUL %"]

# Sample data for metrics per team (replace with your data)
team_metrics = {
    "MOHAWK": [26, 29, 0, 39, 25, 50, 40, 48, 54],
    "MEMORIAL": [0.68, 0.75, 0.60, 0.64, 0.78, 0.70, 0.75, 0.61, 0.66],
    "CONCORDIA": [0.72, 0.79, 0.65, 0.69, 0.82, 0.74, 0.79, 0.65, 0.70],
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_team = request.form.get("team")

    if selected_team:
        metrics_data = team_metrics.get(selected_team, [])
        metrics_and_values = zip(metrics, metrics_data)
    else:
        metrics_and_values = []

    return render_template("index.html", teams=teams, selected_team=selected_team, metrics_and_values=metrics_and_values)

if __name__ == "__main__":
    app.run(debug=True)
