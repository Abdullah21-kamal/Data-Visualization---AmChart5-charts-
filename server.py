from flask import Flask, jsonify, render_template
import pandas as pd


df = pd.read_csv("Orders.csv")
df['Order Date'] = df['Order Date'].sort_values()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-datachart')
def get_datachart():
    classes = df["Ship Mode"].value_counts().index
    values = df["Ship Mode"].value_counts().values

    data = []

    for i in range(len(classes)):
        data.append({"class": classes[i], "value":int(values[i])})

    return jsonify(data)


@app.route('/get-datatable')
def get_datatable():
    classes = df["Segment"].value_counts().index
    values = df["Segment"].value_counts().values

    data = []

    for i in range(len(classes)):
        data.append({"class": classes[i], "value":int(values[i])})

    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)