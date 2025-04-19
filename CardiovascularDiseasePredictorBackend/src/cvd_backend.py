import os.path

from flask import Flask, request
from sqlalchemy import sql, create_engine,Table, MetaData, Column, Integer, String, insert, select
from service.login_service import LoginService
from service.result_service import ResultService
from service.signup_service import SignUpService
from sqlalchemy.orm import sessionmaker




"""
Implements the application front end
"""

port = 8000

class CVDBackEnd:
    def __init__(self, db_path):
        self.APPT_NAME = 'CVDBackEnd'
        self.APPT_PORT = port
        self.DB_PATH =  db_path




    def  create_app(self):
        """
        set up the flask server
        Input: None
        Output: None
        """
        app = Flask(self.APPT_NAME)
        app.login = False
        app.currentProfilerId = None
        app.currentResultId = None
        engine = create_engine(f'sqlite:///{self.DB_PATH}')
        session = sessionmaker(bind=engine)()


        #controllers
        @app.route("/")
        def home():
            return "hello"

        @app.route("/login", methods=["POST"])
        def login():
            return LoginService().login(request.json, session)
        @app.route("/signup", methods=["POST"])
        def signup():
            return SignUpService().signup(request.json, engine)
        @app.route("/sample_form", methods=["POST", "GET"])
        def sample_form():
            return ResultService().get_results(request.json, engine, session)


        return app




if(__name__ == '__main__'):
    db_path = os.path.join(os.getcwd(), 'db/CardiovascularDiseasesDB.db')
    cvd_app = CVDBackEnd(db_path)
    app = cvd_app.create_app()
    app.run(port=cvd_app.APPT_PORT)