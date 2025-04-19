from repository.db_model import DbModel
from sqlalchemy import sql, create_engine,insert, select




"""
Implements the logic for the login
"""

class LoginService:

    def login(self, user_info, session):
        '''
        Check whether the right username & password is provided
        Input:
            user_info: dictionary that has user info
            session : Db session
        Output: 0 for success, 1 for fail
        '''

        username = user_info['username']
        password = user_info['password']

        Profiler = DbModel().get_profiler()
        matching_users = select(Profiler)
        for matching_user in session.execute(matching_users):
            if (matching_user.username == username and
                    matching_user.password == password):
                return str(matching_user.id)
        return 'Error'







