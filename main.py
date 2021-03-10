import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    home_html = """<div style="text-align: center">
    <h1>Simple DB on requests!</h1>
    <ul>
    <li>Get all records: [GET] link: localhost:5123/db</li>
    <li>Set all records: [POST] link: localhost:5123/db !!!All data must be in BODY!!!</li>
    </ul>
    <h5>FROM__DICH_WITH__LOVE</h5><div>"""
    return home_html, 200


@app.route('/db', methods=['GET', 'POST'])
def db():
    if request.method == 'GET':
        with open('db.json', 'r') as file:
            data_json = json.load(file)
        return jsonify(data_json), 200
    elif request.method == 'POST':
        try:
            data_json = json.loads(request.data)
        except json.JSONDecodeError:
            return 'Wrong JSON structure', 500
        with open('db.json', 'w') as file:
            json.dump(data_json, file)
        return 'OK', 200
    return 'Wrong request method', 405


@app.route('/table', methods=['GET'])
def table():
    return render_template('your_table.html')


app.run(port=5123, debug=True)
