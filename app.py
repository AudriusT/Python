from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/form-page")
def hello():
    return render_template("forms.html")


@app.route("/add-name/<name>")
def add_name(name):
    return f"Labas ir vardas {name}"


@app.route("/action-page, methods-_POST ")
def add_action():
    duomenys = dict(request.args)
    vardas = duomenys['vardas'][0]
    amzius_ = duomenys['amzius'][0]
    if amzius_.isdigit():
        amzius = int(amzius_)
        if 10 < amzius < 90:
            return jsonify({"vardas":vardas, "amzius":amzius})
        else:
            return jsonify({"error":"Blogai nurodytas amžius"}),403
    return jsonify({"error":"Įveskite tik skaičiūs į amžių."}),403


@app.route("/form-page")
def add_action_js():
    duomenys = request.form
    vardas = duomenys['vardas'][0]
    amzius_ = duomenys['amzius'][0]
    if amzius_.isdigit():
        amzius = int(amzius_)
        if 10 < amzius < 90:
            return jsonify({"vardas":vardas, "amzius":amzius})
        else:
            return jsonify({"error":"Blogai nurodytas amžius"}),403
    return jsonify({"error":"Įveskite tik skaičiūs į amžių."}),403


if __name__ == '__main__':
    app.run()