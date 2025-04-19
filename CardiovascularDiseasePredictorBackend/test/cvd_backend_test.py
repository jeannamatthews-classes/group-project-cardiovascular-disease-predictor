import unittest
from cvd_backend import CVDBackEnd
import os

DB_PATH = os.path.join(os.getcwd(), 'test/db/CardiovascularDiseasesDB_test.db')


class AppTest(unittest.TestCase):

    def test_home(self):
        """Test the home page."""
        cvd_app = CVDBackEnd(DB_PATH)
        app = cvd_app.create_app()
        with app.test_client() as client:
            response = client.get('/')
            assert response.status_code == 200
            assert response.text == 'hello'

    def test_login_success(self):
        """Test the login page."""
        cvd_app = CVDBackEnd(DB_PATH)
        app = cvd_app.create_app()
        request_param = {'username':'test', 'password':'s3cr3t'}
        with app.test_client() as client:
            response = client.post('/login', json=request_param)
            assert response.status_code == 200
            assert response.text != 'Error'

    def test_login_fail(self):
        """Test the login page."""
        cvd_app = CVDBackEnd(DB_PATH)
        app = cvd_app.create_app()
        request_param = {'username':'test', 'password':'s3cr3ts'}
        with app.test_client() as client:
            response = client.post('/login', json=request_param)
            assert response.status_code == 200
            assert response.text == 'Error'

    def test_singup_success(self):
        """Test the signup page."""
        cvd_app = CVDBackEnd(DB_PATH)
        app = cvd_app.create_app()
        request_param = {'firstName': 'S1', 'lastName':'L1', 'username':'test',
                         'company':'C1', 'password':'P1'}
        with app.test_client() as client:
            response = client.post('/signup', json=request_param)
            assert response.status_code == 200
            assert response.text == '0'

    def test_model1(self):
        """Test the signup page."""
        cvd_app = CVDBackEnd(DB_PATH)
        app = cvd_app.create_app()
        test_sample_path = os.path.join(os.getcwd(), 'resource/test_data.csv')
        sample_list = open(test_sample_path, 'r').readlines()
        sample = "".join(sample_list)
        request_param = {'csv_file': sample, 'prediction_type':'1', 'profiler_id': '1'}
        with app.test_client() as client:
            response = client.post('/sample_form', json=request_param)
            assert response.status_code == 200
            assert response.text == 'The presence of cardiovascular disease was detected in the sample.'

    def test_model2(self):
        """Test the signup page."""
        cvd_app = CVDBackEnd(DB_PATH)
        app = cvd_app.create_app()
        test_sample_path = os.path.join(os.getcwd(), 'resource/test_data.csv')
        sample_list = open(test_sample_path, 'r').readlines()
        sample = "".join(sample_list)
        request_param = {'csv_file': sample, 'prediction_type':'2', 'profiler_id': '1'}
        with app.test_client() as client:
            response = client.post('/sample_form', json=request_param)
            assert response.status_code == 200
            assert response.text == 'The presence of CONGENITAL HEART DISEASE was detected in the sample.'



if __name__ == '__main__':
    unittest.main()