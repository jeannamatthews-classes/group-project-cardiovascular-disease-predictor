from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import sql, create_engine,Table, MetaData, Column, Integer, String, insert, select
from sqlalchemy.orm import sessionmaker
import sys


#import backend component : TODO: To be decoupled
sys.path.insert(1, '../../CardiovascularDiseasePredictorBackend/src/service/')
from result_service import ResultService


from datetime import datetime
import csv


def create_app():
    app = Flask(__name__)
    app.login = False
    app.currentProfilerId = None
    app.currentResultId = None

    engine = create_engine('sqlite:///../db/CardiovascularDiseasesDB.db')
    metadata = MetaData()

    # Create database models
    Profiler = Table('profiler', metadata,
              Column('id', Integer, primary_key=True),
              Column('firstname', String),
              Column('lastname', String),
              Column('username', String),
              Column('company', String),
              Column('password', String)
    )
    Sample = Table('sample', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('sample_content', String),
                     Column('record_added', String),
    )
    Result = Table('result', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('profiler_id', Integer),
                   Column('sample_id', Integer),
                   Column('record_added', String),
                   Column('result', String),

    )





    def insert_query(query):
        with engine.connect() as connection:
            connection.execute(query)
            connection.commit()

    # Home Page
    @app.route("/")  # URL
    def home():
        return render_template("index.html")

    # Signup Page
    @app.route("/signup", methods=["POST", "GET"])  # URL
    def signup():
        if request.method == "POST":
            new_first_name = request.form['firstName']
            new_last_name = request.form['lastName']
            new_company = request.form['company']
            new_username = request.form['username']
            new_password = request.form['password']


            # Push to Database
            try:
                query = insert(Profiler).values(firstname=new_first_name, lastname=new_last_name, company=new_company,
                                                    username=new_username, password=new_password)
                insert_query(query)
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

            session = sessionmaker(bind=engine)()

            matching_users = select(Profiler)  #.where(Profiler.username==entered_username)
            for matching_user in session.execute(matching_users):
                if (matching_user.username == entered_username and
                        matching_user.password == entered_password):
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
            prediction_type = request.form['prediction_type']
            stream = file.stream.read().decode("UTF-8")
            current_timestamp = str(datetime.now())

            # Push to Database
            try:
                query = insert(Sample).values(sample_content=stream, record_added=current_timestamp)
                insert_query(query)
            except:
                return "There was an error adding the sample."


            # CALCULATE THE RESULT
            new_result_rundate = datetime.now()
            result_service = ResultService()
            new_result_value = result_service.get_results(prediction_type, stream)
            new_profiler_id = app.currentProfilerId
            sample_id_query = select(Sample.c.id).where(Sample.c.record_added==current_timestamp)
            session = sessionmaker(bind=engine)()
            new_sample_id = session.execute(sample_id_query).first()[0]


            # Push to Database
            try:
                query = insert(Result).values(profiler_id=new_profiler_id, sample_id=new_sample_id,
                                             record_added=new_result_rundate, result=new_result_value)
                insert_query(query)
            except:
                return "There was an error adding the Result."
            return render_template("results.html", result=new_result_value)


        else:
            if app.login:
                return render_template("sample_form.html")
            else:
                return redirect(url_for("home"))



    return app

if(__name__ == '__main__'):
    app = create_app()
    app.run()