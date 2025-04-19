from repository.db_model import DbModel
from sqlalchemy import sql, create_engine,insert, select

"""
Implements the logic for the user sign up
"""

class SignUpService:

    def signup(self, user_info, engine):
        '''
        Add new user
        Input:
            user_info: dictionary that has user info
            engine : Db engine
        Output: 0 for success, 1 for fail
        '''
        firstname = user_info['firstName']
        lastname = user_info['lastName']
        company = user_info['company']
        username = user_info['username']
        password = user_info['password']

        Profiler = DbModel().get_profiler()
        query = insert(Profiler).values(firstname=firstname, lastname=lastname, company=company,
                                        username=username, password=password)

        try:
            with engine.connect() as connection:
                connection.execute(query)
                connection.commit()
            return '0'
        except:
            return '1'








