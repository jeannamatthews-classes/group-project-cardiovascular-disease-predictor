from sqlalchemy import Table, MetaData, Column, Integer, String

"""
Represents models for the DB objects
"""

class DbModel:

    def __init__(self):
        self.metadata = MetaData()

    def get_profiler(self):
        '''
        Returns the object representing profiler object
        Input: None
        Output: returns the profiler model
        '''
        profiler = Table('profiler', self.metadata,
                      Column('id', Integer, primary_key=True),
                      Column('firstname', String),
                      Column('lastname', String),
                      Column('username', String),
                      Column('company', String),
                      Column('password', String)
        )
        return profiler

    def get_sample(self):
        '''
        Returns the object representing sample object
        Input: None
        Output: returns the sample model
        '''
        sample = Table('sample', self.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('sample_content', String),
                         Column('record_added', String),
        )
        return sample

    def get_result(self):
        '''
        Returns the object representing result object
        Input: None
        Output: returns the result model
        '''
        result = Table('result', self.metadata,
                       Column('id', Integer, primary_key=True),
                       Column('profiler_id', Integer),
                       Column('sample_id', Integer),
                       Column('record_added', String),
                       Column('result', String),
        )
        return result