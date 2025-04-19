import requests
from flask import Flask, render_template, redirect, request, url_for



BACKEND_URL = 'http://127.0.0.1:8000'

"""
Frontend logic of the app
"""
def create_app():
    app = Flask(__name__)
    app.login = False
    app.currentProfilerId = None
    app.currentResultId = None



    # Home Page
    @app.route("/")  # URL
    def home():
        return render_template("index.html")

    # Signup Page
    @app.route("/signup", methods=["POST", "GET"])  # URL
    def signup():
        if request.method == "POST":
            response = requests.post(f'{BACKEND_URL}/signup', json=request.form)
            if(response.text == '0'):
                return render_template("index.html")
            else:
                return "There was an error adding the account."
        else:
            return render_template("signup.html")

    # Login Page
    @app.route("/login", methods=["POST", "GET"])  # URL
    def login():
        error_message = None
        if request.method == "POST":
            response = requests.post(f'{BACKEND_URL}/login', json=request.form)
            if(response.text != 'Error'):
                app.login = True
                app.currentProfilerId = response.text
                return redirect(url_for("user_home"))
            else:
                return render_template("login.html", message='"Invalid credentials."')

        else:
            return render_template("login.html")

    # User Home Page
    @app.route("/user_home")  # URL
    def user_home():
        if app.login:
            return render_template("user_home.html")
        else:
            return redirect(url_for("home"))

    # Sample Form Page
    @app.route("/sample_form", methods=["POST", "GET"])  # URL
    def sample_form():
         if request.method == "POST":
             file = request.files['csv_file']
             stream = file.stream.read().decode("UTF-8")
             sample_json = {'csv_file': stream,
                            'prediction_type': request.form['prediction_type'],
                            'profiler_id': app.currentProfilerId}
             response = requests.post(f'{BACKEND_URL}/sample_form', json=sample_json)
             if(response.text.startswith("T")):
                 result = response.text
                 return render_template("results.html", result=result)
         else:
            if app.login:
                return render_template("sample_form.html")
            else:
                return redirect(url_for("home"))

    return app


if (__name__ == '__main__'):
    app = create_app()
    app.run()