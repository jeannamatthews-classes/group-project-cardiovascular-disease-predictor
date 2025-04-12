from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv


def create_app():
    app = Flask(__name__)
    app.login = False
    app.currentProfilerId = None
    app.currentResultId = None

    # Initialize the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profiler.db'  # /instance/

    app.config['SQLALCHEMY_BINDS'] = {
        'sample': 'sqlite:///sample.db',
        'result': 'sqlite:///result.db'
    }

    db = SQLAlchemy(app)

    # Create database models
    class Profiler(db.Model):
        # No Bind Key - created in default (profiler)
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(200), nullable=False)
        last_name = db.Column(db.String(200), nullable=False)
        company = db.Column(db.String(200), nullable=False)
        username = db.Column(db.String(200), nullable=False)
        password = db.Column(db.String(200), nullable=False)

    class Sample(db.Model):
        __bind_key__ = 'sample'
        id = db.Column(db.Integer, primary_key=True)
        gender = db.Column(db.Integer, nullable=False)
        bmi = db.Column(db.Integer, nullable=False)
        age = db.Column(db.Integer, nullable=False)
        height = db.Column(db.Integer, nullable=False)
        smoker = db.Column(db.Integer, nullable=False)

    class Result(db.Model):
        __bind_key__ = 'result'
        id = db.Column(db.Integer, primary_key=True)
        profiler_id = db.Column(db.Integer, nullable=False)
        patient_id = db.Column(db.Integer, nullable=False)
        result_rundate = db.Column(db.DateTime, nullable=False)
        result_value = db.Column(db.String(200), nullable=False)

    # with app.app_context():
    #    db.create_all()

    # Home Page
    @app.route("/")  # URL
    def home():
        return render_template("index.html")

    # Signup Page
    @app.route("/signup", methods=["POST", "GET"])  # URL
    def signup():
        if request.method == "POST":
            new_first_name = request.form['firstName']
            new_last_name = request.form['firstName']
            new_company = request.form['company']
            new_username = request.form['username']
            new_password = request.form['password']
            new_profiler = Profiler(first_name=new_first_name, last_name=new_last_name, company=new_company,
                                    username=new_username, password=new_password)

            # Push to Database
            try:
                db.session.add(new_profiler)
                db.session.commit()
                return render_template("index.html")
            except:
                return "There was an error adding the account."
        else:
            return render_template("signup.html")

    # Login Page
    @app.route("/login", methods=["POST", "GET"])  # URL
    def login():
        error_message = None
        if request.method == "POST":
            entered_username = request.form['username']
            entered_password = request.form['password']

            matching_users = db.session.query(Profiler).filter(Profiler.username == entered_username)
            for matching_user in matching_users:
                if (matching_user.password == entered_password):
                    app.login = True
                    app.currentProfilerId = matching_user.id
                    return redirect(url_for("user_home"))
            error_message = "Invalid credentials."
            return render_template("login.html", message=error_message)

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
            # uploaded_file = request.files.get('')
            file = request.files['csv_file']
            stream = file.stream.read().decode("UTF-8").splitlines()
            reader = csv.reader(stream)
            for row in reader:
                new_gender = row[0]
                new_bmi = row[1]
                new_age = row[2]
                new_height = row[3]
                new_smoker = row[4]
                new_sample = Sample(gender=new_gender, bmi=new_bmi, age=new_age, height=new_height, smoker=new_smoker)

                # Push to Database
                try:
                    db.session.add(new_sample)
                    db.session.commit()
                except:
                    return "There was an error adding the sample."

                # CALCULATE THE RESULT
                new_profiler_id = app.currentProfilerId
                new_patient_id = new_sample.id
                new_result_rundate = datetime.now()
                new_result_value = 1  # CHANGE
                new_result = Result(profiler_id=new_profiler_id, patient_id=new_patient_id,
                                    result_rundate=new_result_rundate, result_value=new_result_value)

                # Push to Database
                try:
                    db.session.add(new_result)
                    db.session.commit()
                except:
                    return "There was an error adding the sample."

                app.currentResultId = new_result.id

            return redirect(url_for("results"))

        else:
            if app.login:
                return render_template("sample_form.html")
            else:
                return redirect(url_for("home"))

    # Results Page
    @app.route("/results")  # URL
    def results():
        if app.login:
            current_result = db.session.query(Result).filter(Result.id == app.currentResultId).one()
            current_result_value = current_result.result_value
            DM = HTN = CAD = CMP = CKD = None
            if (current_result_value == "1"):
                DM = "low"
                HTN = "low"
                CAD = "low"
                CMP = "low"
                CKD = "low"
            elif (current_result_value == "2"):
                DM = "low"
                HTN = "moderate"
                CAD = "low"
                CMP = "low"
                CKD = "low"
            elif (current_result_value == "3"):
                DM = "low"
                HTN = "low"
                CAD = "moderate"
                CMP = "low"
                CKD = "low"

            return render_template("results.html", DM_RISK=DM, HTN_RISK=HTN, CAD_RISK=CAD, CMP_RISK=CMP, CKD_RISK=CKD)

        else:
            return redirect(url_for("home"))

    return app