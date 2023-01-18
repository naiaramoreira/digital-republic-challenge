from flask import Flask, request, render_template
from challenge.calculation import CalculationPaint

app = Flask(__name__)


@app.route("/")
def home():
    height = {}
    width = {}
    window = {}
    door = {}
    data_calculation = []

    for i in range(1, 5):
        height[i] = request.args.get('height_'+str(i))
        width[i] = request.args.get('width_' + str(i))
        window[i] = request.args.get('window_' + str(i))
        door[i] = request.args.get('door_' + str(i))

    data_calculation.append(height)
    data_calculation.append(width)
    data_calculation.append(window)
    data_calculation.append(door)
    result = CalculationPaint().calculoLatas()

    return render_template("home.html", result=result)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)