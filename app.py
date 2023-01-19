from flask import Flask, request, render_template
from challenge.calculation import CalculationPaint

app = Flask(__name__)


@app.route("/", methods=('GET', 'POST'))
def home():
    dict, data_calculation, result, message, area = {}, {}, 0, None, 0

    if request.method == 'POST':

        for i in range(1, 5):

            dict['height'] = request.form.get('height_'+str(i))
            dict['width'] = request.form.get('width_' + str(i))
            dict['window'] = request.form.get('window_' + str(i))
            dict['door'] = request.form.get('door_' + str(i))

            data_calculation[i] = dict

        result, area, message = CalculationPaint().calculation_paint_cans(data_calculation)

    return render_template("home.html", result=result, area=area, message=message)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)